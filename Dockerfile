FROM python:3.13-slim
WORKDIR /spc
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn","app.main:app"]