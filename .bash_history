python manage.py jenkins --enable-coverage --settings=portfolio.settings.ci
python manage.py test --settings=portfolio.settings.ci
python manage.py makemigrations --settings=portfolio.settings.local
python manage.py migrate --settings=portfolio.settings.local
python manage.py shell --settings=portfolio.settings.local
python manage.py collectstatic --settings=portfolio.settings.local
python manage.py runserver 0.0.0.0:8200 --settings=portfolio.settings.local
