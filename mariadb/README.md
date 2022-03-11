# MariaDB

https://hub.docker.com/repository/docker/tot0ro/mariadb-neo

내부포트 3306

```bash
$ docker run -d --name mariadb \
 --network intra-net \                      # Server(Nginx)와 Web App(Django)과 연결
 -v db-data:/var/lib/mysql \                # DB 데이터 volume 연결
 -e MARIADB_USER=<DB_USER> \                # maria db user account id (생략가능)
 -e MARIADB_PASSWORD=<DB_PASS> \            # user account pw (생략가능)
 -e MARIADB_ROOT_PASSWORD=<DB_ROOT_PASS> \  # root pw
 tot0ro/mariadb-neo
```

최초 DB 실행 시 아래 수행

```bash
$ docker exec -it mariadb bash                           # Container 접속
$ mysql -p                                               # MariaDB root 로그인(DB_ROOT_PASS)
> create database <DB_NAME>;                             # DB 생성
> grant all privileges on <DB_NAME>.* to <DB_USER>@'%';  # DB 사용 권한 인계
> Ctrl-c                                                 # MariaDB 종료
$ Ctrl-d                                                 # Container 종료
```


### v0.1.0 latest

mariadb 기본적으로 동작

### v0.2.0 latest

User contents를 mount하여 사용할 수 있는 volume 추가
