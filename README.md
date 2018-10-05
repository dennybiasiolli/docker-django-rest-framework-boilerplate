# docker-django-rest-framework-boilerplate


#### Run development server

You can run development server from command line or from a docker-compose system.


##### command line method

```bash
cd src
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_dev.txt
python manage.py runserver
```


##### docker-compose method

Launch docker-compose system with `docker-compose up` and open http://127.0.0.1:8000