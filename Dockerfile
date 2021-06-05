FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY bot bot
COPY swagger_client swagger_client

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/bot:/usr/src/app"
WORKDIR /usr/src/app/bot
CMD [ "python", "main.py" ]