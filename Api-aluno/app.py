from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Isso permite que a API seja acessada de qualquer domínio

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar se a API está funcionando"""
    return jsonify({
        "status": "success",
        "message": "API funcionando corretamente"
    })

@app.route('/me', methods=['GET'])
def get_student_info():
    """Endpoint para retornar informações do aluno"""
    student_info = {
        "nome": "Roberto Pereira de Sousa",
        "email": "Otaltorob@hotmail.com",
        "curso": "Sistemas de Informação",
        "GitHub": "https://github.com/rpsroberto",
        "cidade": "Juazeiro do Norte - CE",
        "interesses": ["programação", "tecnologia", "Backend", "APIs", "Flask", "Python"]
    }
    return jsonify(student_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)