import sqlite3

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect('ferramentas.db')

# Função para criar as tabelas
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    
    # Criação da tabela de Ferramentas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ferramentas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        estado TEXT,
        disponivel BOOLEAN DEFAULT 1
    )
    ''')

    # Criação da tabela de Empréstimos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS emprestimos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ferramenta_id INTEGER,
        apartamento_id TEXT,
        data_emprestimo DATE,
        data_devolucao DATE,
        data_devolvida DATE,
        FOREIGN KEY (ferramenta_id) REFERENCES ferramentas (id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Tabelas criadas com sucesso!")

# Executa a função de criação das tabelas
if __name__ == '__main__':
    criar_tabelas()
