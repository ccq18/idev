#!/usr/bin/env bash
# fastdfs laravel java elasticsearch nginxphp
# 一键启动所有容器，php,java等应用容器不会启动
for projectname in  mongo mysql apollo xxljob elk nacos  kafka    postgres redis rocketmq  ;
do
(
cd $projectname;
docker-compose up -d;
)
done


