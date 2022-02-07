#!/usr/bin/env bash

for projectname in apollo elasticsearch elk fastdfs java kafka laravel mongo mysql nacos nginxphp postgres redis rocketmq storage xxljob;
do
(
cd $projectname;
docker-compose up -d;
)
done