#/bin/bash
# @ ! lixiangheng
set -e

read -r -p "请确认上传的目录与文件名为/opt/package/dist.zip? [Y/n] " input

case $input in
    [yY][eE][sS]|[yY])
        # 备份
        WORKDIR=/data/h5/
        cd ${WORKDIR}
        DATE=`date +"%Y%m%d%H%M"`
        tar -czvf /opt/package/h5bak/h5-${DATE}.tar.gz dist/

        
        if [ ! -f "/opt/package/dist.zip" ];then
           echo "上传的文件名与目录可能不对，讲退出!"
           exit 1
        fi      
        rm -rf ${WORKDIR}/dist/*
        unzip -oq /opt/package/dist.zip -d ${WORKDIR}
        chown -R www: ${WORKDIR}/dist

        if [ $? == 0 ]; then
              echo "更新成功"
              rm -f /opt/package/dist.zip
        fi
        ;;

    [nN][oO]|[nN])
        exit 1
        ;;

    *)
        echo "无效输入..."
        exit 1
        ;;
esac
