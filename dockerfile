
FROM python:3.5

WORKDIR /app

COPY . /app

RUN pip install flask

EXPOSE 5000

# CMD python ./main.py

CMD [ "python", "./main.py" ]