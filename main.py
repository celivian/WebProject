from flask import Flask, render_template, redirect, request, abort

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')