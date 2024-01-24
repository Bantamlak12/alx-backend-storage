# Project: 0x02. Redis basic

## Resources

#### Read or watch:

- [Redis commands](https://redis.io/commands/)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998&ab_channel=TraversyMedia)

## Learning Objectives

- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache

## Install Redis on Ubuntu 18.04

```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Use Redis in a container

Redis server is stopped by default - when you are starting a container, you should start it with: `service redis-server start`

## Tasks

| Task                                               | File                         |
| -------------------------------------------------- | ---------------------------- |
| 0. Writing strings to Redis                        | [exercise.py](./exercise.py) |
| 1. Reading from Redis and recovering original type | [exercise.py](./exercise.py) |
| 2. Incrementing values                             | [exercise.py](./exercise.py) |
| 3. Storing lists                                   | [exercise.py](./exercise.py) |
| 4. Retrieving lists                                | [exercise.py](./exercise.py) |
| 5. Implementing an expiring web cache and tracker  | [web.py](./web.py)           |
