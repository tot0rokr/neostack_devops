# Neostack devops project

## Jenkins

https://hub.docker.com/repository/docker/tot0ro/jenkins-blueocean-neo

```bash
$ docker network create net-jenkins
$ docker run --name jenkins -d --privileged --network net-jenkins --network-alias docker \
 --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client \
 --volume jenkins-data:/var/jenkins_home --publish 2376:2376 docker:dind --storage-driver \
 overlay2
$ docker run --name jenkins-blueocean -d --network net-jenkins --env DOCKER_HOST=tcp://docker:2376 \
 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 -p <PORT>:8080 -p 50000:50000 \
 --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro \
 tot0ro/jenkins-blueocean-neo
```

- PORT: Host machine port number

### v0.1.0 latest

Nordic nRF Mesh SDK를 컴파일 하기 위한 cmake compile 환경 세팅



## MariaDB

https://hub.docker.com/repository/docker/tot0ro/mariadb-neo

내부포트 3306

`/sql_query`를 마운트 해야함.

```bash
$ docker run -d --name mariadb -v <THIS REPO>/mariadb/sql_query:/sql_query \
 -e MARIADB_USER=<USER_ID> -e MARIADB_PASSWORD=<USER_PW> -e MARIADB_ROOT_PASSWORD=<ROOT_PW> \
 tot0ro/mariadb-neo
```

- USER\_ID: user id
- USER\_PW: user password
- ROOT\_PW: root password

직접 정하면 된다.

### v0.1.0 latest

mariadb 기본적으로 동작

## Django

https://hub.docker.com/repository/docker/tot0ro/django-neo

```bash
$ docker run --name intra -d -v <THIS REPO>/intra-django/app:/app \
 -e DJANGO_SECRET_KEY=<SECRET_KEY> \
 tot0ro/django-neo
```

- SECRET\_KEY: django key이다. [여기서](https://miniwebtool.com/django-secret-key-generator/) 새 key를 생성할 수 있다.


### intra-v0.1.0

django 프로젝트 생성


### intra-v0.2.0 latest

wcgi를 통해 nginx와 연동. nginx-neo v0.2.0과 호환



## Nginx

https://hub.docker.com/repository/docker/tot0ro/nginx-neo

내부 포트 8000

conf와 www 디렉토리를 마운트 해야함

```bash
$ docker run --name nginx -d -v <THIS REPO>/nginx/conf.d:/etc/nginx/conf.d \
 -v <THIS REPO>/nginx/www:/usr/share/nginx/www -p 80:8000 \
 tot0ro/nginx-neo
```

### v0.1.0

nginx 서버 기본적으로 동작.

### v0.2.0 latest

wcgi를 통해 django와 연동




## 네트워크 연결

```bash
$ docker network create intra-net
$ docker network connect intra-net mariadb
$ docker network connect intra-net intra
$ docker network connect intra-net nginx
```
