#!/usr/bin/env bash
# fastdfs laravel java elasticsearch nginxphp
# 一键启动所有容器，php,java等应用容器不会启动
for projectname in apollo  elk  kafka  mongo mysql nacos  postgres redis rocketmq  xxljob;
do
(
cd $projectname;
docker-compose up -d;
)
done