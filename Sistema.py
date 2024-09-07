import sqlite3
from datetime import date
import tkinter as tk
from tkinter import messagebox

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect('ferramentas.db')

# Função para adicionar uma nova ferramenta
def adicionar_ferramenta(nome, descricao, estado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO ferramentas (nome, descricao, estado, disponivel)
    VALUES (?, ?, ?, 1)
    ''', (nome, descricao, estado))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Ferramenta adicionada com sucesso!")

# Função para registrar um novo empréstimo
def registrar_emprestimo(ferramenta_id, apartamento_id, data_emprestimo, data_devolucao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO emprestimos (ferramenta_id, apartamento_id, data_emprestimo, data_devolucao)
    VALUES (?, ?, ?, ?)
    ''', (ferramenta_id, apartamento_id, data_emprestimo, data_devolucao))
    cursor.execute('''
    UPDATE ferramentas
    SET disponivel = 0
    WHERE id = ?
    ''', (ferramenta_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Empréstimo registrado com sucesso!")

# Função para registrar a devolução de uma ferramenta
def registrar_devolucao(emprestimo_id, data_devolvida):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE emprestimos
    SET data_devolvida = ?
    WHERE id = ?
    ''', (data_devolvida, emprestimo_id))
    cursor.execute('''
    UPDATE ferramentas
    SET disponivel = 1
    WHERE id = (SELECT ferramenta_id FROM emprestimos WHERE id = ?)
    ''', (emprestimo_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Devolução registrada com sucesso!")

# Função para listar todas as ferramentas
def listar_ferramentas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, descricao, estado, CASE WHEN disponivel = 1 THEN "Disponível" ELSE "Indisponível" END AS status FROM ferramentas')
    ferramentas = cursor.fetchall()
    conn.close()
    return ferramentas

# Função para listar todos os empréstimos
def listar_emprestimos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT e.id, e.apartamento_id, e.data_emprestimo, e.data_devolucao, f.nome FROM emprestimos e LEFT JOIN ferramentas f ON e.ferramenta_id = f.id')
    emprestimos = cursor.fetchall()
    conn.close()
    return emprestimos

# Função para criar a interface gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Sistema de Empréstimos de Ferramentas")

    # Frame para adicionar ferramenta
    frame_ferramenta = tk.Frame(root)
    frame_ferramenta.pack(pady=10)

    tk.Label(frame_ferramenta, text="Nome:").grid(row=0, column=0)
    nome_entry = tk.Entry(frame_ferramenta)
    nome_entry.grid(row=0, column=1)

    tk.Label(frame_ferramenta, text="Descrição:").grid(row=1, column=0)
    descricao_entry = tk.Entry(frame_ferramenta)
    descricao_entry.grid(row=1, column=1)

    tk.Label(frame_ferramenta, text="Estado:").grid(row=2, column=0)
    estado_entry = tk.Entry(frame_ferramenta)
    estado_entry.grid(row=2, column=1)

    def adicionar_ferramenta_callback():
        nome = nome_entry.get()
        descricao = descricao_entry.get()
        estado = estado_entry.get()
        adicionar_ferramenta(nome, descricao, estado)

    def limpar_formulario_ferramenta_callback():
        nome_entry.delete(0, tk.END)
        descricao_entry.delete(0, tk.END)
        estado_entry.delete(0, tk.END)

    tk.Button(frame_ferramenta, text="Adicionar Ferramenta", command=adicionar_ferramenta_callback).grid(row=3, column=0, pady=5)
    tk.Button(frame_ferramenta, text="Limpar Formulário", command=limpar_formulario_ferramenta_callback).grid(row=3, column=1, pady=5)

    # Frame para registrar empréstimo
    frame_emprestimo = tk.Frame(root)
    frame_emprestimo.pack(pady=10)

    tk.Label(frame_emprestimo, text="Nº da Ferramenta:").grid(row=0, column=0)
    ferramenta_id_entry = tk.Entry(frame_emprestimo)
    ferramenta_id_entry.grid(row=0, column=1)

    tk.Label(frame_emprestimo, text="Nº do Apartamento:").grid(row=1, column=0)
    apartamento_id_entry = tk.Entry(frame_emprestimo)
    apartamento_id_entry.grid(row=1, column=1)

    tk.Label(frame_emprestimo, text="Data de Empréstimo (YYYY-MM-DD):").grid(row=2, column=0)
    data_emprestimo_entry = tk.Entry(frame_emprestimo)
    data_emprestimo_entry.grid(row=2, column=1)

    tk.Label(frame_emprestimo, text="Data de Devolução (YYYY-MM-DD):").grid(row=3, column=0)
    data_devolucao_entry = tk.Entry(frame_emprestimo)
    data_devolucao_entry.grid(row=3, column=1)

    def registrar_emprestimo_callback():
        ferramenta_id = int(ferramenta_id_entry.get())
        apartamento_id = int(apartamento_id_entry.get())
        data_emprestimo = data_emprestimo_entry.get()
        data_devolucao = data_devolucao_entry.get()
        registrar_emprestimo(ferramenta_id, apartamento_id, data_emprestimo, data_devolucao)

    def limpar_formulario_emprestimo_callback():
        ferramenta_id_entry.delete(0, tk.END)
        apartamento_id_entry.delete(0, tk.END)
        data_emprestimo_entry.delete(0, tk.END)
        data_devolucao_entry.delete(0, tk.END)

    tk.Button(frame_emprestimo, text="Registrar Empréstimo", command=registrar_emprestimo_callback).grid(row=4, column=0, pady=5)
    tk.Button(frame_emprestimo, text="Limpar Formulário", command=limpar_formulario_emprestimo_callback).grid(row=4, column=1, pady=5)

    # Frame para registrar devolução
    frame_devolucao = tk.Frame(root)
    frame_devolucao.pack(pady=10)

    tk.Label(frame_devolucao, text="Nº do Empréstimo:").grid(row=0, column=0)
    emprestimo_id_entry = tk.Entry(frame_devolucao)
    emprestimo_id_entry.grid(row=0, column=1)

    tk.Label(frame_devolucao, text="Data de Devolução (YYYY-MM-DD):").grid(row=1, column=0)
    data_devolvida_entry = tk.Entry(frame_devolucao)
    data_devolvida_entry.grid(row=1, column=1)

    def registrar_devolucao_callback():
        emprestimo_id = int(emprestimo_id_entry.get())
        data_devolvida = data_devolvida_entry.get()
        registrar_devolucao(emprestimo_id, data_devolvida)

    def limpar_formulario_devolucao_callback():
        emprestimo_id_entry.delete(0, tk.END)
        data_devolvida_entry.delete(0, tk.END)

    tk.Button(frame_devolucao, text="Registrar Devolução", command=registrar_devolucao_callback).grid(row=2, column=0, pady=5)
    tk.Button(frame_devolucao, text="Limpar Formulário", command=limpar_formulario_devolucao_callback).grid(row=2, column=1, pady=5)

    # Frame para listar ferramentas
    frame_listar_ferramentas = tk.Frame(root)
    frame_listar_ferramentas.pack(pady=10)

    def listar_ferramentas_callback():
        ferramentas = listar_ferramentas()
        messagebox.showinfo("Ferramentas", "\n".join([str(f) for f in ferramentas]))

    tk.Button(frame_listar_ferramentas, text="Listar Ferramentas", command=listar_ferramentas_callback).pack()

    # Frame para listar empréstimos
    frame_listar_emprestimos = tk.Frame(root)
    frame_listar_emprestimos.pack(pady=10)

    def listar_emprestimos_callback():
        emprestimos = listar_emprestimos()
        messagebox.showinfo("Empréstimos", "\n".join([str(e) for e in emprestimos]))

    tk.Button(frame_listar_emprestimos, text="Listar Empréstimos", command=listar_emprestimos_callback).pack()


    root.mainloop()

# Executa a função de criação da interface gráfica
if __name__ == '__main__':
    criar_interface()
    