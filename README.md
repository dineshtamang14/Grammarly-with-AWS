# Grammarly-with-AWS
Grammarly like feature website created using flask with using aws services in backend.


### To Run server on local developement environment
```sh
python3 main.py
```


### To Run WSGI server on production environment on default port 8000
```sh
gunicorn wsgi:app
```

### To Run WSGI server on production level in port 80
```sh
sudo gunicorn --bind 0.0.0.0:80 wsgi:app
```
