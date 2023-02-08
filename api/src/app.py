# coding: utf8
 
from flask import Flask, request, jsonify, json, Response
import pymysql
from flask_cors import CORS
import os, signal

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/stopServer', methods=['GET'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({ "success": True, "message": "Server is shutting down..." })

@app.route('/products')
def products():

    try:
        conn = pymysql.connect(
            # host = '0.0.0.0', # acessando o container pelo local host (tem que expor a porta na construção do mysql-container, assim: -p 3306:3306), se estiver utilizando linux é só usar o IP do mysql-container.
            host='mysql-container', # acessando o container utilizando a tag --link.
            # host='172.17.0.2', # acessando o container direto pelo endereço IP do mysql-container na mesma rede.
            database='solution',
            user='root',
            password='solution',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        rows = cursor.fetchall()
        resp = json.dumps(rows, ensure_ascii=False, indent=4, sort_keys=True).encode('utf-8')
        print(resp)
        response = Response(resp, content_type="application/json; charset=utf-8")
        print(response)
        response.status_code = 200
        # resp = jsonify(rows)
        # resp.status_code = 200
        return response
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/favicon.ico')
def favicon():
    return 'dummy', 200

if __name__ == "__main__":
    app.run(port=9001, host='0.0.0.0')