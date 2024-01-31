from flask import Flask, Response
import json
import random
import newrelic.agent

app = Flask(__name__)

newrelic.agent.initialize("newrelic.ini")


@newrelic.agent.wsgi_application()
@app.route('/', methods=['GET', 'POST'])
def index():
    return Response(
        response=json.dumps({"welcome": "to ozone onboarding", 'value': "ozone-python-hello-world application"}),
        mimetype='application/json'
    )


@newrelic.agent.wsgi_application()
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    print("success")
    return Response(
        response=json.dumps(
            {"route": "/hello", "response": "hello world main branch"}),
        mimetype='application/json'
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int("3000"), debug=True)
