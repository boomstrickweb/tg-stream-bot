FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyrofork tgcrypto py-tgcalls

COPY . .

CMD ["python", "bot.py"]
