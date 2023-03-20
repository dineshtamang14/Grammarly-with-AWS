FROM python:3.9.5-buster
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV AWS_ACCESS_KEY_ID=your_access_key \
    AWS_SECRET_ACCESS_KEY=your_secret_key \
    AWS_DEFAULT_REGION=us-west-2
EXPOSE 5000   
CMD ["python", "main.py"]