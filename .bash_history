python manage.py jenkins --enable-coverage --settings=portfolio.settings.ci
python manage.py test --settings=portfolio.settings.ci
python manage.py makemigrations
python manage.py migrate
python manage.py shell
python manage.py collectstatic
python manage.py runserver 0.0.0.0:8200
