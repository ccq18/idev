# 介绍
这是个docker compose 的集合，简化本地各种环境配置部署。支持
db:kafka mysql redis postgres 
elk:elasticsearch, elk
apachephp:apache +php
nginxphp:nginx +php
根据以往经验，存储的依赖其实是可以多个项目共享的，比如：kafka mysql redis postgres，xxljob,apollo,注册中心等。
因此本项目将应用的运行环境和存储分开，只需要一个环境准备个公用的存储就好了，应用直接通过本地王霖端口访问存储，应用的执行环境可以很干净，可以做到和生产的一致。
# 基本操作
```
docker-compose up -d  //相当于pull+build+start
docker-compose build
docker-compose pull
docker-compose start
docker-compose stop
docker-compose rm -f
docker-compose ps
```
# 初始化
- 在以下版本正常工作
```
Docker version 20.10.8, build 3967b7d
docker-compose version 1.29.2, build 5becea4c
为解决不同环境下host.docker.internal  兼容问题
需要 设置HOST_IP
mac/weindows 下
export HOST_IP=host.docker.internal
linux下 为ip addr show docker0 对应的ip
/etc/bash.bashrc 
export HOST_IP=

为了避免权限问题 先初始化权限
chmod -R 777 ./
```
- 安装docker-compose
```
ubuntu:
snap install docker
sudo curl -L https://get.daocloud.io/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/bin/docker-compose
sudo chmod +x /usr/bin/docker-compose

macos：
下载app 安装docker 
sudo curl -L https://get.daocloud.io/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/bin/docker-compose
sudo chmod +x /usr/bin/docker-compose

windows：
下载app 安装docker 
https://github.com/docker/compose/releases
```
```
cd db
docker-compose up -d 
打开db工具导入xxljob/xxljob.sql apollo/apolloconfigdb.sql
```
# server
## phpmyadmin
http://localhost:9901/  
username: root  
password: tiger
## redis admin
http://localhost:9902/
## elk
http://127.0.0.1:5601/
user => "elastic"
password => "changeme"
## apache php
http://localhost:80
## nginx php
http://localhost:801

## xxljob
http://127.0.0.1:8099/xxl-job-admin/toLogin
admin 123456

# install ping
brew install telnet

apt update
apt install iputils-ping
apt install telnet
# 调试辅助命令（忽略）

ps -ef|grep mysqld
lsof -i tcp:3306  
brew services stop mysql
telnet 192.168.0.100 3306
docker ps -a --no-trunc
docker exec -it  idev-phpredisadmin /bin/sh
docker exec -it  idev-phpmyadmin /bin/sh
docker exec -it apollo-portal /bin/sh
docker exec -it idev-mysql57 /bin/sh
docker logs -f apollo-portal
docker exec -it mysql8.0 /bin/sh
mysql -h0.0.0.0 -u root -p
mysql -h0.0.0.0 -u nacos -p 
mysql -udocker -pdocker -h0.0.0.0 -P 3307  
