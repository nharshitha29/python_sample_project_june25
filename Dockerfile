FROM python:3.14-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --target=/deps -r requirements.txt

COPY . /app


FROM cgr.dev/chainguard/python:latest

WORKDIR /app

COPY --from=builder /deps /deps
COPY --from=builder /app /app

ENV PYTHONPATH=/deps

EXPOSE 8000

CMD ["app/main.py"]
                   