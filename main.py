from flask import Flask, render_template, redirect, request, abort

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    pass