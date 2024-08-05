from flask import Flask, request, jsonify
import Services.NotaGsmServices as services
import Model.NotaGsm as NotaGsm

app = Flask(__name__)

@app.route("/findAll", methods=['GET'])
def CadastrarNotaGsm():
    retorno = services.findAll()
    return retorno.toJSON()

@app.route("/CadastrarNotaGsm", methods=['POST'])
def CadastrarNotaGsm():
    notaGsm = request.get_json()
    retorno = services.CadastrarNotaGsm(notaGsm)
    return jsonify(retorno)







app.run(host='0.0.0.0')