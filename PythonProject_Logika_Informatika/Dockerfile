FROM python:3.12

WORKDIR /PythonProject_Logika_Informatika

COPY . .
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



CMD ["gunicorn", "-b", "0.0.0.0:5001", "app:app"]

EXPOSE 5001

