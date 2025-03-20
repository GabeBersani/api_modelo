from flask import Flask
app = Flask(__name__)
# @app.route('/<informacao_texto>')
# def index(informacao_texto):
#   return f'Hello, World, {informacao_texto} !'

@app.route('/soma/<num1>+<num2>')
def soma (num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return str(num1 + num2)
    except ValueError:
        return "Apenas numeros inteiros"

@app.route('/sub/<num1>-<num2>')
def subtracao (num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return str(num1 - num2)
    except ValueError:
        return "Apenas numeros inteiros"

@app.route('/multiplicacao/<num1>*<num2>')
def multiplicacao (num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return str(num1 * num2)
    except ValueError:
        return "Apenas numeros inteiros"

@app.route('/divisao/<num1>/<num2>')
def divisao (num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return str(num1 / num2)
    except ValueError:
        return "Apenas numeros inteiros"

@app.route('/verficar/<num1>')
def verficar (num1):
    try:
        num1 = int(num1)
        if num1 % 2 == 0:
            return f'O número {num1} é par'
        elif num1 % 2 == 1:
            return f'O número {num1}, é impar'
    except ValueError:
        return "Apenas numeros inteiros"


if __name__ == '__main__':
    app.run(debug=True)

