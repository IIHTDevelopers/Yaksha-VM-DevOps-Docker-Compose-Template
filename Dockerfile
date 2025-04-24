FROM python:3.11-slim
WORKDIR /app
COPY tests/ .
RUN pip install pytest requests docker
CMD ["pytest", "test_nginx.py"]
