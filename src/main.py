from flask import Flask

app = Flask('Everything is fine')


@app.get('/health/')
def return_ok():
    return {"status": "OK"}, 200


if __name__ == "__main__":
    app.run()
