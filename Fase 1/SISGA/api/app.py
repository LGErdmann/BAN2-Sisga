import psycopg2
from connection import get_conn
from flask import Flask, request, jsonify

conn = get_conn()
app = Flask(__name__)

########################################Alunos####################################################
@app.route('/alunos', methods=['GET'])
def get_alunos():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.alunos;")
    alunos = cursor.fetchall()
    cursor.close()
    return jsonify(alunos)

@app.route('/alunos/<int:cod_aluno>', methods=['GET'])
def get_aluno(cod_aluno):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.alunos WHERE cod_aluno = %s;", (cod_aluno,))
    aluno = cursor.fetchone()
    cursor.close()
    if aluno:
        return jsonify(aluno)
    return jsonify({'error': 'Aluno not found'}), 404

@app.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.json
    cursor = conn.cursor()
    cursor.execute("INSERT INTO public.alunos (cpf) VALUES (%s) RETURNING cod_aluno;", (data['cpf'],))
    cod_aluno = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    return jsonify({'cod_aluno': cod_aluno}), 201

@app.route('/alunos/<int:cod_aluno>', methods=['PUT'])
def update_aluno(cod_aluno):
    data = request.json
    cursor = conn.cursor()
    cursor.execute("UPDATE public.alunos SET cpf = %s WHERE cod_aluno = %s;", (data['cpf'], cod_aluno))
    conn.commit()
    cursor.close()
    return jsonify({'message': 'Aluno updated successfully'})

@app.route('/alunos/<int:cod_aluno>', methods=['DELETE'])
def delete_aluno(cod_aluno):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM public.alunos WHERE cod_aluno = %s;", (cod_aluno,))
    conn.commit()
    cursor.close()
    return jsonify({'message': 'Aluno deleted successfully'})

@app.route('/', methods=['GET'])
def health_check():
    return "healthy"

############################Coordenadores#######################################
@app.route('/coordenadores', methods=['GET'])
def get_coordenadores():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.coordenadores;")
    coordenadores = cursor.fetchall()
    cursor.close()
    return jsonify(coordenadores)

@app.route('/coordenadores/<int:cod_coordenador>', methods=['GET'])
def get_coordenador(cod_coordenador):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.coordenadores WHERE cod_coordenador = %s;", (cod_coordenador,))
    coordenador = cursor.fetchone()
    cursor.close()
    if coordenador:
        return jsonify(coordenador)
    return jsonify({'error': 'Coordenador not found'}), 404

@app.route('/coordenadores', methods=['POST'])
def create_coordenador():
    data = request.json
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO public.coordenadores (cpf, salario) VALUES (%s, %s) RETURNING cod_coordenador;",
        (data['cpf'], data['salario'])
    )
    cod_coordenador = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    return jsonify({'cod_coordenador': cod_coordenador}), 201

@app.route('/coordenadores/<int:cod_coordenador>', methods=['PUT'])
def update_coordenador(cod_coordenador):
    data = request.json
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE public.coordenadores SET cpf = %s, salario = %s WHERE cod_coordenador = %s;",
        (data['cpf'], data['salario'], cod_coordenador)
    )
    conn.commit()
    cursor.close()
    return jsonify({'message': 'Coordenador updated successfully'})

@app.route('/coordenadores/<int:cod_coordenador>', methods=['DELETE'])
def delete_coordenador(cod_coordenador):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM public.coordenadores WHERE cod_coordenador = %s;", (cod_coordenador,))
    conn.commit()
    cursor.close()
    return jsonify({'message': 'Coordenador deleted successfully'})

############################Professores#######################################
@app.route('/professores', methods=['GET'])
def get_professores():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.professores;")
    professores = cursor.fetchall()
    cursor.close()
    return jsonify(professores)

@app.route('/professores/<int:cod_professor>', methods=['GET'])
def get_professor(cod_professor):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.professores WHERE cod_professor = %s;", (cod_professor,))
    professor = cursor.fetchone()
    cursor.close()
    if professor:
        return jsonify(professor)
    return jsonify({'error': 'Professor not found'}), 404

@app.route('/professores', methods=['POST'])
def create_professor():
    data = request.json
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO public.professores (cpf, salario, formacao) VALUES (%s, %s, %s) RETURNING cod_professor;",
        (data['cpf'], data['salario'], data.get('formacao'))
    )
    cod_professor = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    return jsonify({'cod_professor': cod_professor}), 201

@app.route('/professores/<int:cod_professor>', methods=['PUT'])
def update_professor(cod_professor):
    data = request.json
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE public.professores SET cpf = %s, salario = %s, formacao = %s WHERE cod_professor = %s;",
        (data['cpf'], data['salario'], data.get('formacao'), cod_professor)
    )
    conn.commit()
    cursor.close()
    return jsonify({'message': 'Professor updated successfully'})

@app.route('/professores/<int:cod_professor>', methods=['DELETE'])
def delete_professor(cod_professor):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM public.professores WHERE cod_professor = %s;", (cod_professor,))
    conn.commit()
    cursor.close()
    return jsonify({'message': 'Professor deleted successfully'})

#Relatorios
@app.route('/relatorios', methods=['GET'])
def get_relatórios():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT r.cod_relatorio, a.cod_aluno, array_agg(d.nome) AS disciplinas, r.notas, r.faltas
        FROM public.relatorios r
        JOIN public.alunos a ON r.cod_aluno = a.cod_aluno
        JOIN public.historicos h ON h.cod_aluno = a.cod_aluno
        JOIN public.disciplinas d ON h.cod_disciplina = d.cod_disciplina
        GROUP BY r.cod_relatorio, a.cod_aluno, r.notas, r.faltas;
    """)
    relatorios = cursor.fetchall()
    cursor.close()
    return jsonify(relatorios)

@app.route('/historico/<int:cod_aluno>', methods=['GET'])
def get_historico(cod_aluno):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT d.nome, h.nota_geral, h.frequencia_geral, h.aprovacao_final
        FROM public.historicos h
        JOIN public.disciplinas d ON h.cod_disciplina = d.cod_disciplina
        WHERE h.cod_aluno = %s;
    """, (cod_aluno,))
    historico = cursor.fetchall()
    cursor.close()
    return jsonify(historico)

#intercessão
@app.route('/alunos_disciplinas', methods=['GET'])
def get_alunos_disciplinas():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.cod_aluno, p.nome AS aluno_nome, d.nome AS disciplina_nome
        FROM public.alunos a
        JOIN public.historicos h ON a.cod_aluno = h.cod_aluno
        JOIN public.disciplinas d ON h.cod_disciplina = d.cod_disciplina
        JOIN public.pessoas p ON a.cpf = p.cpf;
    """)
    alunos_disciplinas = cursor.fetchall()
    cursor.close()
    return jsonify(alunos_disciplinas)

@app.route('/coordenadores_cursos', methods=['GET'])
def get_coordenadores_cursos():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.cod_coordenador, p.nome AS coordenador_nome, cu.nome AS curso_nome
        FROM public.coordenadores c
        JOIN public.cursos cu ON c.cod_coordenador = cu.cod_coordenador
        JOIN public.pessoas p ON c.cpf = p.cpf;
    """)
    coordenadores_cursos = cursor.fetchall()
    cursor.close()
    return jsonify(coordenadores_cursos)

@app.route('/professores_disciplinas', methods=['GET'])
def get_professores_disciplinas():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT pr.cod_professor, p.nome AS professor_nome, d.nome AS disciplina_nome
        FROM public.professores pr
        JOIN public.turmas t ON pr.cod_professor = t.cod_professor
        JOIN public.disciplinas d ON t.cod_disciplina = d.cod_disciplina
        JOIN public.pessoas p ON pr.cpf = p.cpf;
    """)
    professores_disciplinas = cursor.fetchall()
    cursor.close()
    return jsonify(professores_disciplinas)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002)