# Fastapi Toy Project

간단한 blog backend 구현해보기
배포된 클라우드는 https://15ycx3.deta.dev/

## Requirements

```
pip install fastapi
pip install uvicorn
```

## Execution

app directory 들어가서

```
uvicorn main:app --reload
```

### Blog Execution

```
uvicorn blog.main:app --reload
```

or

```
python main.py
```

## Deploy

[Deta](https://www.deta.sh/) 에 배포

### Install the CLI

```
curl -fsSL https://get.deta.dev/cli.sh | sh
```

### Login with the CLI

```
$ deta login
Please, log in from the web page. Waiting...
https://web.deta.sh/cli/52520
Logged in successfully.
```

### Deploying with Deta

```
$ deta new
Successfully created a new micro
{
        "name": "app",
        "id": 생략,
        "project": "c0ubefzq",
        "runtime": "python3.9",
        "endpoint": "https://15ycx3.deta.dev",
        "region": "ap-southeast-1",
        "visor": "disabled",
        "http_auth": "disabled"
}
```

이후는

```
$ deta deploy
```
