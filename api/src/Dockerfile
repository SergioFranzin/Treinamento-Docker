FROM python:3

WORKDIR /src

COPY ./api/src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python3 ./api/src/app.py