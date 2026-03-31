FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir pyrofork tgcrypto py-tgcalls

COPY . .

CMD ["python", "bot.py"]
