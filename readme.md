# 介绍
当前为测试版，你可以在测试环境下使用，但后续升级可能会导致测试数据丢失  
idev是测试环境设计快速开发设计的环境集合，简化本地各种环境配置部署。目前以下所有功能都是为单机设计的，生产环境请谨慎使用。。  
支持
- mysql
- redis
- postgres sql
- mongodb
- apollo
- xxljob
- elk
- rocketmq
- kafka
- elasticsearch
- php

根据以往经验，存储的依赖其实是可以多个项目共享的，比如：kafka mysql redis postgres，xxljob,apollo,注册中心等。  
你的应用环境可以使用本机的，也可以使用idev中的应用环境。数据库和消息等使用idev中的配置就好 

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

- 环境参数
```
为解决不同环境下host.docker.internal  兼容问题
需要 设置HOST_IP
mac/weindows 下
export HOST_IP=host.docker.internal
linux下 为ip addr show docker0 对应的ip(以下命令在ubuntu 20.4有效，无效可以手动设置)
/etc/bash.bashrc 
export HOST_IP=$(ifconfig|grep -A 5 docker0|grep netmask|awk '{print $2}')
为了避免权限问题 先初始化权限
chmod -R 777 ./
```
- 配置项目下的.env,目前每个模块下都准备了sample.env 重命名为.env即可使用
- 启动
```
cd storage
docker-compose up -d 
打开db工具导入xxljob/xxljob1.sql apollo/apolloconfigdb.sql,apollo/apolloportaldb.sql
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


# 调试辅助命令（忽略） 
## 停止所有容器
docker stop $(docker ps -a -q)
删除所有已经停止的容器：
docker rm $(docker ps -a -q)
查看占用
docker system df
清理所有
docker system prune -a
## install ping
```
brew install telnet
apt update
apt install iputils-ping
apt install telnet
```

```
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
```