# UNE

## Content

- Docker Mongo
- Python project
- Links

## Docker Mongo

```
$ docker run -e MONGO_INITDB_ROOT_USERNAME='admin' -e MONGO_INITDB_ROOT_PASSWORD='123' --publish=27017:27017 --name mongodb mongo
```

## Python project

```
$ python3 -m venv venv
```

```
$ source ./venv/bin/activate
```

```
$ pip install -r requirements.txt
```

## Links

- [Mongodb Compass](https://www.mongodb.com/products/compass)
- [Virtual Environments](https://docs.python.org/3/tutorial/venv.html)