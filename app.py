from flask import Flask, request

app = Flask(__name__)

#endpoint: buscar todos os alunos
@app.route('buscaralunos', methods=['GET'])
def buscar_alunos():
    return "todos alunos listados"

if __name__== "__main__":
    app.run(debug=True)

