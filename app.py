from flask import Flask, request

app = Flask(__name__)


alunos = [
    {"id": 1, "nome": "Anerson"},
    {"id": 2, "nome": "Gabriel"},
    {"id": 3, "nome": "Brendon"}
]

#endpoint: buscar aluno com id
@app.route('/buscaraluno/<int:id>', methods=['GET'])
def buscar_alunos(id):
    for aluno  in alunos:
        if aluno ["id"] == id:
            return aluno
    return "Aluno não localizado"    
    



    #endpoint: deletar aluno com id
@app.route('/deletaraluno/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    for i,  aluno in enumerate (alunos):
        if aluno ["id"] == id:
            alunos.pop(i)
            return alunos
    return "Aluno não localizado"    
    

#endpoint: buscar todos os alunos
@app.route('/listaralunos', methods=['GET'])
def listar_alunos():

    return alunos

# endpoint: adicionar aluno query params
@app.route('/adicionaraluno', methods=['POST']) 
def adicionar_aluno():
    id = request.args.get('id')  
    nome = request.args.get('nome')
    novo = {"id": id , "nome": nome}
    novo["id"] = len(alunos)+1
    alunos.append(novo)

    return alunos


#endpoint: adicionar json aluno
@app.route('/adicionaralunojson', methods=['POST']) 
def adicionar_aluno_json():
    novo = request.get_json()
    novo["id"] = len(alunos)+1
    alunos.append(novo)
    return alunos



if __name__== "__main__":
    app.run(debug=True)

