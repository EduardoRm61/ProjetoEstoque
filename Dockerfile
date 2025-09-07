FROM python:3.12-slim

WORKDIR /app

COPY requiremensts.txt .
RUN pip install --user -r requiremensts.txt

COPY . .

EXPOSE 5002

CMD ["python", "apps/app.py"]
