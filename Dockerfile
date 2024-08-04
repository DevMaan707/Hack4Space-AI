FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 uninstall -y torch
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip3 install gunicorn

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
