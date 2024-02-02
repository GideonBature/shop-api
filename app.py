from flask import Flask

app = Flask(__name__)
print(app)

@app.route('/')
def hello_world():
    return '<h1>Gideon Bature<h1>'

if __name__ == '__main__':
    app.run(debug=True)