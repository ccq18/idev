# 宕机测试
## 内容
目前所有存储服务已经通过volumes将数据存储在实体机硬盘。
为了测试数据存储的可靠性，测试会将原有容器停止后删除容器数据，只保留实体机硬盘数据，
然后重新开启新的容器实例，观察数据是否有丢失。
# mysql
通过
数据存储在 app/mysql57/data目录
# redis
通过
数据存储在 app/redis/data目录
# postgres sql
通过
数据存储在 app/postgres/data目录
# apollo
通过
数据存储在对应数据库中
# xxljob
通过
数据存储在对应数据库中
# elk
# rocketmq
# kafka
