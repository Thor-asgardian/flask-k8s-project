FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app2.py .
CMD ["gunicorn", "-b", "0.0.0.0:6000", "app2:app"]
