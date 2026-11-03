FROM python:3.11-slim
WORKDIR /app
COPY wk8main.py .
COPY inventory.json .
CMD ["python", "wk8main.py"]