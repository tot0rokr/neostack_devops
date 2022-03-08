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

## Nginx

https://hub.docker.com/repository/docker/tot0ro/nginx-neo

내부 포트 8000 

conf와 www 디렉토리를 마운트 해야함

```bash
$ docker run --name nginx -d -v <THIS REPO>/nginx/conf.d:/etc/nginx/conf.d \
 -v <THIS REPO>/nginx/www:/usr/share/nginx/www -p 80:8000 tot0ro/nginx-neo
```

### v0.1.0 latest

nginx 서버 기본적으로 동작.

## Django
