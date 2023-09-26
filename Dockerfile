FROM python:3.12-rc-bookworm

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install -r requirements.txt

COPY . .

CMD python app.py