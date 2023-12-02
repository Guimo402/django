#!/bin/bash

sudo redis-server /etc/redis/redis.conf
service ssh start
/etc/init.d/nginx start
