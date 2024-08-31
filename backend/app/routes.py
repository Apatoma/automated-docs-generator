from flask import jsonify, request
from app import app, db
from app.models import Documentation
from app.doc_generator import generate_docs_from_code

@app.route('/generate', methods=['POST'])
def generate_documentation():
    data = request.get_json()
    code = data.get('code')
    filename = data.get('filename')

    if not code or not filename:
        return jsonify({"error": "Code and filename are required."}), 400

    documentation_content = generate_docs_from_code(code, filename)
    documentation = Documentation(filename=filename, content=documentation_content)
    db.session.add(documentation)
    db.session.commit()

    return jsonify(documentation.to_dict())

@app.route('/docs', methods=['GET'])
def get_documentations():
    docs = Documentation.query.all()
    return jsonify([doc.to_dict() for doc in docs])

@app.route('/docs/<int:id>', methods=['GET'])
def get_documentation(id):
    doc = Documentation.query.get_or_404(id)
    return jsonify(doc.to_dict())
