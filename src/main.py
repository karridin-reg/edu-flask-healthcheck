from flask import Flask

app = Flask('Everything is fine')


@app.get('/health/')
def return_ok():
    return {"status": "OK"}, 200


@app.get('/liveness/')
def liveness():
    return {"liveness": "OK"}, 200


@app.get('/readiness/')
def readiness():
    return {"readiness": "OK"}, 200


if __name__ == "__main__":
    app.run(debug=True)
