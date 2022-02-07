#!/usr/bin/env bash
# fastdfs laravel java elasticsearch
for projectname in apollo  elk  kafka  mongo mysql nacos nginxphp postgres redis rocketmq  xxljob;
do
(
cd $projectname;
docker-compose up -d;
)
done