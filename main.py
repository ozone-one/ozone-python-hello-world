from flask import Flask, Response
import json
import newrelic.agent

app = Flask(__name__)

newrelic.agent.initialize("newrelic.ini")


@newrelic.agent.wsgi_application()
@app.route('/', methods=['GET', 'POST'])
def index():
    # Simulating an unhandled exception occurring with every request
    raise Exception("Unhandled exception occurred")
    return Response(
        response=json.dumps({'value': 11}),
        mimetype='application/json'
    )


@newrelic.agent.wsgi_application()
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    n = random.random()
    if n > 0.98:
        raise Exception("unknown exception occured")
        print("unknown exception occured")
        newrelic.agent.notice_error()
        return Response(
            response=json.dumps({'error': "unknown exception happened"}),
            mimetype='application/json',
            status=500
        )
    else:
        print("success")
        return Response(
            response=json.dumps(
                {"route": "/hello", "response": "hello world main branch"}),
            mimetype='application/json'
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int("3000"), debug=True)
