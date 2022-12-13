# nginx api gateway

#### Usage:
```bash
$ docker-compose up
```

#### To deploy new nginx configuration:
```bash
$ docker compose build api-gateway
$ docker compose up --no-deps -d api-gateway
```

#### To renew certbot certificate:
```bash
$ docker compose run --rm certbot renew
```

#### API gateway high overview:

![illustration](apigateway.png)
