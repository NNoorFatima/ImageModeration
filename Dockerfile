FROM python:3.10-slim

WORKDIR /app

COPY . .

#dependencies installed
RUN pip install --no-cache-dir --upgrade -r backend/requirements.txt

#running port
EXPOSE 7000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "7000"]
