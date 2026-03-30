FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
```

**`requirements.txt`** bu olsun:
```
pyrogram==2.0.106
tgcrypto==1.2.5
py-tgcalls==0.9.0
