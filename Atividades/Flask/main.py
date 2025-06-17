from flask import Flask, make_response, jsonify
from bd import saudacoes_personalizadas, calculo

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/saudacao_soma', methods= ['GET'])
def get_saudacao_soma():
    return make_response(
        jsonify(
            dados = list(saudacoes_personalizadas)
        )

    )

@app.route('/saudacao_soma', methods= ['POST'])
def post_saudacao_soma():
    return make_response(
        jsonify(
            resultado = calculo
        )

    )


if __name__ == '__main__':
    app.run()

