release: bash ./release-tasks.sh
web: bin/start-nginx bin/start-pgbouncer gunicorn -c config/gunicorn.conf portfolio.wsgi:application