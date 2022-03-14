# Neostack Jenkins Server

각 컴포넌트는 각각 README에서 확인하실 수 있습니다.

## How to Use

### Jenkins

http://\<HOSTNAME\>:8080

### Intra Net

http://\<HOSTNAME\>


## How to up the containers

설치: https://docs.docker.com/compose/install/

최소 실행 시, MariaDB README에서 MariaDB 최초 실행 시 수행해야하는 명령을 따라주세요.

```bash
$ cat > .env                             # 환경 변수 파일 생성
DB_NAME='...'                            # Mariadb에서 생성한 DB 이름
DB_USER='...'                            # DB에 접근 가능한 계정
DB_PASS='...'                            # 계정 비밀번호
DB_ROOT_PASS='...'                       # DB root 비밀번호
DJANGO_SECRET_KEY='<SECRET_KEY>'         # django secret key
DJANGO_ALLOWED_HOSTS='<HOSTS>'           # django allowed hosts
DEBUG='<DEBUG>'                          # whether to debug or not
<Ctrl-c>
$ docker-compose --env-file .env up [-d] # -d: Daemon으로 실행

# 오류 시 아래 명령으로, docker compose 환경 확인
$ docker-compose --env-file .env config  # docker-compose config 확인
```

- ...을 채워주세요.
- SECRET\_KEY: django key이다. [여기서](https://miniwebtool.com/django-secret-key-generator/) 새 key를 생성할 수 있습니다.
- HOSTS: 접속가능한 Host URL. 공백으로 구분된 리스트(콤마 아님). (ex, `.mywebsite.com`)
  - 자세한 내용은 [여기서](https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts) 살펴보실 수 있습니다.
- DEBUG: Debug 모드 여부입니다. Debug 상태에서는 공개되면 안되는 데이터가 표시되므로, 주의해주세요.
  - `1` - Debug mode.
  - `0` - Release mode.
- 환경 변수 파일은 repository에 push하지 마십시오. (기본적으로 .env는 gitignore의 대상임)

## Server Migrations

다른 Host 머신으로 migration할 때, 다음 volume 이 저장된 디렉토리를 함께 이동하십시오.

- db-data
- jenkins-data
- jenkins-docker-certs

```bash
# 기존 Host 머신
$ docker volume ls                 # volume 목록
$ docker volume inspect <VOLUME>   # <VOLUME>의 상태 정보 (데이터 저장 위치)
Mountpoint 디렉토리를 복사

# 새로운 Host 머신
$ docker volume create <VOLUME>
Mountpoint 디렉토리에 붙여넣기
```
