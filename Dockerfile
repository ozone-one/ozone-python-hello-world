FROM blrdbharbor.ozonecloud.ai/ozone-public-registry/ozoneprod/python:3.8-slim-buster
WORKDIR /app
COPY . .
RUN pip3 install -U pip
RUN pwd
RUN ls
RUN pip3 install -r requirements.txt
EXPOSE 3000
CMD NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python main.py
