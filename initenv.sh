#!/usr/bin/env bash
for projectname in apollo elasticsearch elk fastdfs java kafka laravel mongo mysql nacos nginxphp postgres redis rocketmq  xxljob;
do
(
cp -rf $projectname/sample.env  $projectname/.env ;
)
done