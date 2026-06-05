FROM python:3.13-slim
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn
EXPOSE 8000
CMD ["python", "app/main.py"]