from flask import Flask, request, jsonify
import Services.NotaGsmServices as services
import Model.NotaGsm as NotaGsm


app = Flask(__name__)

@app.route("/findAll", methods=['GET'])
def CadastrarfindAll():
    retorno = services.findAll()
    return retorno


@app.route("/CadastrarNotaGsm", methods=['POST'])
def CadastrarNotaGsm():
    notaGsmjson = request.get_json()
    notaGsm = NotaGsm.NotaGsm(**notaGsmjson)
    retorno = services.CadastrarNotaGsm(notaGsm)

    if retorno == "200":
        return  "Objeto inserido com sucesso - 200"
    else:
        return "Erro ao inserir objeto na base de dados - 500"
    


app.run(host='0.0.0.0', debug=True)
