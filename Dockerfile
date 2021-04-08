FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY stu.py /app/stu.py

ENTRYPOINT ["python", "/app/stu.py"]
