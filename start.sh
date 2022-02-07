#!/usr/bin/env bash
# fastdfs laravel java
for projectname in apollo elasticsearch elk  kafka  mongo mysql nacos nginxphp postgres redis rocketmq  xxljob;
do
(
cd $projectname;
docker-compose up -d;
)
done