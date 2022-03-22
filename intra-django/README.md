# Django

https://hub.docker.com/repository/docker/tot0ro/django-neo

```bash
$ docker run -d --name intra \
 --network intra-net \                   # DataBase(MariaDB)와 Server(Nginx)와 연결
 -v <THIS REPO>/intra-django/app:/app \  # Django Code volume 연결
 -e DJANGO_SECRET_KEY=<SECRET_KEY> \
 -e DB_NAME=<DB_NAME> \
 -e DB_USER=<DB_USER> \
 -e DB_PASS=<DB_PASS> \
 tot0ro/django-neo
```

- Nginx 보다 먼저 동작하여야 함.
- NginX 및 MariaDB와 같은 네트워크에 소속되어야 함
- SECRET\_KEY: django key이다. [여기서](https://miniwebtool.com/django-secret-key-generator/) 새 key를 생성할 수 있다.
- DB\_NAME: DB 이름. 해당 사이트에서 사용할 DB 이름이다.
- DB\_USER: 유저 계정 id. DB\_NAME을 사용할 권한이 있어야 한다.
- DB\_PASS: DB\_USER의 password.

### 최소 실행 시 아래 작업 수행

1. Admin 계정 생성
  ```bash
  $ docker exec intra python manage.py createsuperuser
  ```
1. REST API 접근 계정 생성.
  - Username: `<RESTAPI_USER>`
  - Password: `<RESTAPI_PASS>`
1. Permission 설정.
  ```
  fw_storage | nordic | Can add nordic
  fw_storage | nordic | Can change nordic
  fw_storage | nordic | Can delete nordic
  fw_storage | nordic | Can view nordic
  ```

## Environments

환경 변수의 경우, 점점 많아질 수 있다.
이 경우, 매번 `-e <KEY>=<VALUE>` 옵션으로 넣기 힘들다.
대신 `--env-file=<ENV FILE>` 옵션을 사용한다.

```bash
$ cat > <ENV FILE>
<KEY>=<VALUE>
<KEY>=<VALUE>
<KEY>=<VALUE>
...
Ctrl+c
$ docker ...축약... --env-file=<ENV FILE>
```

개발 환경에서도 동일한 환경변수를 사용하고 싶을 경우, 다음 명령으로 export 할 수 있다.

```bash
$ export $(cat <ENV FILE> | xargs -0)
```


## Requirements

Django application을 개발할 때 필요한 패키지이다.
어플리케이션을 동작시키는 것은 docker이므로, **"개발환경"**에 필요한 패키지만을 저장하고 있다.
개발할 때, 추가적인 패키지가 요구된다면,

```bash
$ pip freeze > requirements.txt
```

새로운 개발환경 혹은 필요한 패키지가 설치되어있지 않다면,

```bash
$ pip install -r requirements.txt
```

### intra-v0.1.0

django 프로젝트 생성


### intra-v0.2.0

wcgi를 통해 nginx와 연동. nginx-neo v0.2.0과 호환

### intra-v0.3.0 latest

MariaDB와 연동. 사용할 db 및 user가 생성되어 있어야 함

- DB: intradb
- USER: intradb\_user
- PASS: intradb\_user


### intra-v0.4.0 latest

Django Rest Framework 적용
