# 进度
## 已完成
## 已可用
kafka
redis
elasticsearch
logstash
php
apache
mysql
## 未完成
# nginx         
# rocketmq  nacos  apollo xxljob
# 启动
https://www.runoob.com/docker/docker-compose.html

docker-compose up -d  //相当于pull+build+start
docker-compose build
docker-compose pull
docker-compose start
docker-compose stop
docker-compose rm -f
docker-compose ps

# 常用命令
https://www.runoob.com/docker/docker-command-manual.html
## 容器
docker stats
使用镜列出所有容器
docker ps

使用镜像 nginx:latest，以后台模式启动一个容器,将容器的 80 端口映射到主机的 80 端口,主机的目录 /data 映射到容器的 /data。
docker run -p 80:80 -v /data:/data -d nginx:latest

在容器 mynginx 中以交互模式执行容器内 /root/runoob.sh 脚本:
docker exec -it mynginx /bin/sh /root/runoob.sh

删除容器
docker rm -f db01

删除容器 nginx01, 并删除容器挂载的数据卷
docker rm -v nginx01

启动已被停止的容器myrunoob
docker start myrunoob

停止运行中的容器myrunoob
docker stop myrunoob

重启容器myrunoob
docker restart myrunoob


容器查看命令 元数据、端口、日志、top进程信息
docker inspect mysql:5.6
docker port mymysql
docker logs -f mynginx
docker top mymysql

## images
docker images
docker rmi -f runoob/ubuntu:v4

docker build -t runoob/ubuntu:v1 . 
docker tag ubuntu:15.10 runoob/ubuntu:v3
docker save -o my_ubuntu_v3.tar runoob/ubuntu:v3
docker load < busybox.tar.gz
docker import  my_ubuntu_v3.tar runoob/ubuntu:v4  

查看本地镜像runoob/ubuntu:v3的创建历史。
docker history runoob/ubuntu:v3
# 仓库
docker login -u 用户名 -p 密码
docker pull java
docker push myapache:v1
docker search  java

## 清理
删除所有已经停止的容器：
docker rm $(docker ps -a -q)
查看占用
docker system df
清理所有
docker system prune -a