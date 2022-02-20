# 介绍
idev是一个docker-compose 集合，支持apollo  elk  kafka  mongo mysql nacos  postgres redis rocketmq  xxljob，php,java的一键部署。  
专门为测试环境快速开发设计，简化本地各种环境配置部署。   
我将容器环境分为应用运行环境和外部依赖两个部分。 
外部依赖如redis,mysql等这些通常一个环境公用一个就好了，不需要每个应用单独起一个，这样可以简化新项目起环境的配置。  
应用运行环境专为应用定制，如php,java等，你可以拷贝应用环境到自己的应用中按需修改。  
# 脚本
allenv 全局配置文件
initenvbyall.py 基于全局配置文件和sample.env 初始化配置
initenv.sh  基于 sample.env 初始化配置
start.sh 启动全部实例
delall.sh 删除全部实例
# 使用
0.由于总所周知的原因，你在国内使用docker很可能会遇到网络问题，因此我建议你在开始一切之前先设置镜像加速。    
如果你遇到问题，以下链接可能可以帮助到你。  
镜像加速：[https://www.runoob.com/docker/docker-mirror-acceleration.html](https://www.runoob.com/docker/docker-mirror-acceleration.html)  
docker 问题解决：
- [https://yeasy.gitbook.io/docker_practice/appendix/faq](https://yeasy.gitbook.io/docker_practice/appendix/faq)
- [https://walkingsun.github.io/WindBlog/2019/01/18/docker_question/#bash-ps-command-not-found](https://walkingsun.github.io/WindBlog/2019/01/18/docker_question/#bash-ps-command-not-found)
git clone git@github.com:ccq18/idev.git
2. 安装docker-compose
```
ubuntu:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

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
2. 环境参数
```
为解决不同环境下host.docker.internal  兼容问题需要添加一个名为HOST_IP的环境变量
mac/weindows 下
export HOST_IP=host.docker.internal
linux下 为ip addr show docker0 对应的ip(以下命令在ubuntu 20.4有效，无效可以手动设置)
/etc/bash.bashrc 
export HOST_IP=$(ifconfig|grep -A 5 docker0|grep netmask|awk '{print $2}')

```
3. 配置项目下的.env,目前每个模块下都准备了sample.env 重命名为.env即可使用 以下脚本可以一键复制sample.env 为.env文件
```
sh initenv.sh
```
4. 启动  可以去各个目录下执行 docker-compose up -d，也可以使用以下脚本一键启动所有容器（除应用环境容器java，php等），建议根据自己需要修改
```
为了避免权限问题 先初始化权限
chmod -R 777 ./
sh start.sh
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

## apollo
http://localhost:9170
meta:http://localhost:9180
用户名：apollo
密码：admin
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