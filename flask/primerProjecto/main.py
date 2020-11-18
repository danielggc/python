from flask import Flask,Markup,make_response,request
app = Flask(__name__)
@app.route("/")
def show_user():
    return 'hola retrasado lento'
@app.route("/salir/")
def saliendo():
    return "vas a asd"

@app.route("/dato/")
def hello():
    return  Markup("<h1>Hello World!</h1>")
@app.route("/json/")
def jSon():
    heders ={"Content-Type": "application/json"}
    return make_response('esto es un trabajo',200,heders)

@app.route("/get/")
def Get():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    headers = {"Content-Type": "application/json"}
    return make_response('it worked!', 1000, headers)