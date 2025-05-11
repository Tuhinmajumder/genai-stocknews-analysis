FROM python:3.12-slim
<<<<<<< HEAD
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app:create_app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:create_app()"]
=======

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
ENV FLASK_APP=app:create_app
CMD ["gunicorn","-b","0.0.0.0:8080","app:create_app()"]
>>>>>>> 8cf0c21 (updated codebase)
