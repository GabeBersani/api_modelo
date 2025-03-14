from flask import Flask
app = Flask(__name__)
# @app.route('/<informacao_texto>')
# def index(informacao_texto):
#   return f'Hello, World, {informacao_texto} !'

@app.route('/soma/<int:num1>+<float:num2>')
def soma (num1, num2):
    return f'{num1} + {num2} = {num1 + num2}'

@app.route('/sub/<int:num1>-<int:num2>')
def subtracao (num1, num2):
    return f'{num1} - {num2} = {num1 - num2}'

@app.route('/multiplicacao/<int:num1>*<int:num2>')
def multiplicacao (num1, num2):
    return f'{num1} * {num2} = {num1 * num2}'

@app.route('/divisao/<int:num1>/<int:num2>')
def divisao (num1, num2):
    return f'{num1} / {num2} = {num1 / num2}'

@app.route('/verficar/<int:num1>')
def verficar (num1):
    if num1 % 2 == 0:
        return f'O número {num1} é par'
    elif num1 % 2 == 1:
        return f'O número {num1}, é impar'
    else:
        print("algo deu errado")





if __name__ == '__main__':
    app.run(debug=True)

