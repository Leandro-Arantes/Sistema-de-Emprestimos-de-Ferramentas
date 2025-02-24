import sqlite3


def conectar():
    """Conecta ao banco de dados SQLite."""
    return sqlite3.connect('ferramentas.db')


def criar_tabelas():
    """Cria as tabelas no banco de dados."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ferramentas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            estado TEXT,
            disponivel BOOLEAN DEFAULT 1
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS emprestimos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ferramenta_id INTEGER,
            apartamento_id TEXT,
            data_emprestimo DATE,
            data_devolucao DATE,
            data_devolvida DATE,
            FOREIGN KEY (ferramenta_id) REFERENCES ferramentas (id)
        )
        """
    )

    conn.commit()
    conn.close()
    print('Tabelas criadas com sucesso!')
