FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --no-cache-dir fastapi uvicorn
RUN pip install --no-cache-dir pydantic
RUN pip install --no-cache-dir subprocess.run
RUN pip install --no-cache-dir mysql.connector
RUN pip install --no-cache-dir kafka-python

VOLUME /app

COPY ./app /app

CMD /start-reload.sh

