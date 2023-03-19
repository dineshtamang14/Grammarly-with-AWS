FROM python:3.9.5-buster
WORKDIR /app 
COPY requirements .
RUN pip3 install -r --no-cache-dir requirements.txt
COPY . .
EXPOSE 8000   
CMD ["gunicorn", "wsgi:app"]