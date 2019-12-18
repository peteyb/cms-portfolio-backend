# cms-portfolio-backend

Headless CMS powered by Wagtail 2.7 LTS enabling GraphQL requests from frontend

## Getting Started

```bash
docker network create portfolio_network --subnet=172.30.0.0/16 --gateway 172.30.0.1
echo "127.0.0.1   portfolio.dev.local" | sudo tee --append /etc/hosts
```
