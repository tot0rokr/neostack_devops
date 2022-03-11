# Jenkins

https://hub.docker.com/repository/docker/tot0ro/jenkins-blueocean-neo

```bash
$ docker network create jenkins-net                # Jenkins network 생성

$ docker run -d --name jenkins-docker \            # docker in docker container. jenkins 내부에서 docker를 실행하기 위해 사용
 --privileged \                                    # 이를 위해 root 권한인 privileged 권한이 필요함. 보안에 취약.
 --network jenkins-net \
 --network-alias docker \
 --env DOCKER_TLS_CERTDIR=/certs \
 --volume jenkins-docker-certs:/certs/client \     # client certifications volume
 --volume jenkins-data:/var/jenkins_home \         # Data volume
 --publish 2376:2376 \
 docker:dind \
 --storage-driver overlay2

$ docker run -d --name jenkins-blueocean \         # Jenkins application container
 --network jenkins-net \
 --env DOCKER_HOST=tcp://docker:2376 \
 --env DOCKER_CERT_PATH=/certs/client \
 --env DOCKER_TLS_VERIFY=1 \
 -p 8080:8080 -p 50000:50000 \                     # Export port 8080
 --volume jenkins-data:/var/jenkins_home \         # Data volume
 --volume jenkins-docker-certs:/certs/client:ro \  # client certifications volume
 tot0ro/jenkins-blueocean-neo
```

- 외부에서 http://HOST명:8080으로 접속
- DB도 연결하려면 network간 연결이 필요함. (위에 언급 없음)


### v0.1.0 latest

Nordic nRF Mesh SDK를 컴파일 하기 위한 cmake compile 환경 세팅
