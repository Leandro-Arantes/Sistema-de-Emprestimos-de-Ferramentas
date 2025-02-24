from .database import conectar


def adicionar_ferramenta(nome, descricao, estado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO ferramentas (nome, descricao, estado, disponivel) VALUES (?, ?, ?, 1)',
        (nome, descricao, estado),
    )
    conn.commit()
    conn.close()


def listar_ferramentas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome, descricao, estado, CASE WHEN disponivel = 1 THEN 'Disponível' ELSE 'Indisponível' END AS status FROM ferramentas"
    )
    ferramentas = cursor.fetchall()
    conn.close()
    return ferramentas
