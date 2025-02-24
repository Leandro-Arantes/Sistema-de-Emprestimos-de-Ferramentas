from .database import conectar


def registrar_emprestimo(
    ferramenta_id, apartamento_id, data_emprestimo, data_devolucao
):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO emprestimos (ferramenta_id, apartamento_id, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)',
        (ferramenta_id, apartamento_id, data_emprestimo, data_devolucao),
    )
    cursor.execute(
        'UPDATE ferramentas SET disponivel = 0 WHERE id = ?',
        (ferramenta_id,),
    )
    conn.commit()
    conn.close()


def registrar_devolucao(emprestimo_id, data_devolvida):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE emprestimos SET data_devolvida = ? WHERE id = ?',
        (data_devolvida, emprestimo_id),
    )
    cursor.execute(
        'UPDATE ferramentas SET disponivel = 1 WHERE id = (SELECT ferramenta_id FROM emprestimos WHERE id = ?)',
        (emprestimo_id,),
    )
    conn.commit()
    conn.close()


def listar_emprestimos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT e.id, e.apartamento_id, e.data_emprestimo, e.data_devolucao, f.nome FROM emprestimos e LEFT JOIN ferramentas f ON e.ferramenta_id = f.id'
    )
    emprestimos = cursor.fetchall()
    conn.close()
    return emprestimos
