from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hola Mundo!!"

@app.route("/hola")
def hola():
    return "Hola mis amigos!!"

@app.route("/elegante")
def hola_mundo_elegante():
    return """
        <html>
            <body>
                <h1>SALUDOS!!</h1>
                <p>HOLA MUNDO!!</p>
            </body>
        </html>
        """

if __name__=="__main__":
    app.run(debug=True)