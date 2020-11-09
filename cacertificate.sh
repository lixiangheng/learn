# /bin/bash
#@ lxh
# date: 20201107
# cfssl install
echo "etcd-config -------"
cat > ca-config.json <<\EOF
{
    "signing": {
        "default": {
            "expiry": "87600h"
        },
        "profiles": {        
            "kubernetes": {
                "expiry": "87600h",
                "usages": [
                    "signing",
                    "key encipherment",
                    "server auth",
                    "client auth"
                ]
            }
        }
    }
}
EOF
cat > etcd-ca-csr.json <<\EOF
{
    "CN": "etcd-ca",
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "L": "HUNAN",
            "ST": "CHANGSHA",
            "O": "etcd",
            "OU": "etcd system"
        }
    ]
}
EOF
# etcd-csr.json
cat > etcd-csr.json <<\EOF
{
    "CN": "etcd",
    "hosts": [
        "127.0.0.1",
        "master01",
        "master02",
        "master03",
        "10.20.100.20",
        "10.20.100.21",
        "10.20.100.22"
    ],
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "L": "HUNAN",
            "ST": "CHANGSHA",
            "O": "etcd",
            "OU": "etcd security"
        }
    ]
}
EOF
cfssl gencert -initca etcd-ca-csr.json | cfssljson -bare etcd-ca
cfssl gencert -ca=etcd-ca.pem -ca-key=etcd-ca-key.pem -config=ca-config.json -profile=kubernetes etcd-csr.json | cfssljson -bare etcd
echo "etcd-config end-------"
# ca-csr.json
echo "kubernetes-config start-------"
cat > ca-csr.json <<\EOF
{
    "CN": "kubernetes",
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "L": "HUNAN",
            "ST": "CHANGSHA",
            "O": "k8s",
            "OU": "k8s system"
        }
    ]
}
EOF
# admin-csr.json
cat > admin-csr.json <<\EOF
{
    "CN": "admin",
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "L": "HUNAN",
            "ST": "CHANGSHA",
            "O": "system:masters",
            "OU": "k8s system"
        }
    ]
}
EOF
# apiserver 
cat > apiserver-csr.json <<\EOF
{
    "CN": "kube-apiserver",
    "hosts": [
        "127.0.0.1",
        "10.96.0.1",
        "10.96.0.1",
        "kubernetes",
        "kubernetes.default",
        "kubernetes.default.svc",
        "kubernetes.default.svc.cluster",
        "kubernetes.default.svc.cluster.local",
        "master01",
        "master02",
        "master03",
        "10.20.100.20",
        "10.20.100.21",
        "10.20.100.22",
        "10.20.100.88"
    ],
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "L": "HUNAN",
            "ST": "CHANGSHA",
            "O": "k8s",
            "OU": "k8s system"
        }
    ]
}
EOF
# controller-manager.csr
cat > controller-manager.csr <<\EOF
{
    "CN": "system:kube-controller-manager",
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "L": "HUNAN",
            "ST": "CHANGSHA",
            "O": "system:kube-controller-manager",
            "OU": "system"
        }
    ]
}
EOF
# scheduler.csr
cat > scheduler.csr <<\EOF
{
    "CN": "system:kube-scheduler",
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "L": "HUNAN",
            "ST": "CHANGSHA",
            "O": "system:kube-scheduler",
            "OU": "system"
        }
    ]
}
EOF
#cfssl gencert -initca ca-csr.json | cfssljson -bare ca
#cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes  admin-csr.json | cfssljson -bare admin
cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes  apiserver-csr.json | cfssljson -bare kube-apiserver
#cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes  controller-manager.csr | cfssljson -bare manager
#cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes  scheduler.csr | cfssljson -bare scheduler

# proxy-client
echo "kubernetes-config end-------"
echo "front-config start-------"
cat > front-ca-csr.json <<EOF
{
    "CN": "kubernetes",
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "L": "HUNAN",
            "ST": "CHANGSHA",
            "O": "front",
            "OU": "front system"
        }
    ]
}
EOF
cat > proxyclient-csr.json <<\EOF
{
    "CN": "proxy-client",
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "L": "HUNAN",
            "ST": "CHANGSHA",
            "O": "proxy",
            "OU": "system"
        }
    ]
}
EOF
cfssl gencert -initca front-ca-csr.json | cfssljson -bare front-ca
cfssl gencert -ca=front-ca.pem -ca-key=front-ca-key.pem -config=ca-config.json -profile=kubernetes  proxyclient-csr.json | cfssljson -bare proxy-client
