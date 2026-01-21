FROM python:3.12

WORKDIR /PythonProject_Logika_Informatika

COPY . .
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

EXPOSE 8080

