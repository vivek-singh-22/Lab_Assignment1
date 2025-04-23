FROM python:3.9-slim

WORKDIR /Lab_Assignment1
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]