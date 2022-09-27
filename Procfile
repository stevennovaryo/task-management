release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json initial_watchlist_data.json testing_todolist_data.json'
web: gunicorn project_django.wsgi --log-file -