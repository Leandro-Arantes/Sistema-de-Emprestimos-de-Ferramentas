import tkinter as tk
from tkinter import messagebox

from src.models.emprestimos import (
    listar_emprestimos,
    registrar_devolucao,
    registrar_emprestimo,
)
from src.models.ferramentas import adicionar_ferramenta, listar_ferramentas


def criar_interface():
    root = tk.Tk()
    root.title('Sistema de Empréstimos de Ferramentas')

    # Frame para adicionar ferramenta
    frame_ferramenta = tk.Frame(root)
    frame_ferramenta.pack(pady=10)

    tk.Label(frame_ferramenta, text='Nome:').grid(row=0, column=0)
    nome_entry = tk.Entry(frame_ferramenta)
    nome_entry.grid(row=0, column=1)

    tk.Label(frame_ferramenta, text='Descrição:').grid(row=1, column=0)
    descricao_entry = tk.Entry(frame_ferramenta)
    descricao_entry.grid(row=1, column=1)

    tk.Label(frame_ferramenta, text='Estado:').grid(row=2, column=0)
    estado_entry = tk.Entry(frame_ferramenta)
    estado_entry.grid(row=2, column=1)

    def adicionar_ferramenta_callback():
        nome = nome_entry.get()
        descricao = descricao_entry.get()
        estado = estado_entry.get()
        adicionar_ferramenta(nome, descricao, estado)
        messagebox.showinfo('Sucesso', 'Ferramenta adicionada com sucesso!')

    tk.Button(
        frame_ferramenta,
        text='Adicionar Ferramenta',
        command=adicionar_ferramenta_callback,
    ).grid(row=3, column=0, pady=5)

    # Frame para registrar empréstimo
    frame_emprestimo = tk.Frame(root)
    frame_emprestimo.pack(pady=10)

    tk.Label(frame_emprestimo, text='Nº da Ferramenta:').grid(row=0, column=0)
    ferramenta_id_entry = tk.Entry(frame_emprestimo)
    ferramenta_id_entry.grid(row=0, column=1)

    tk.Label(frame_emprestimo, text='Nº do Apartamento:').grid(row=1, column=0)
    apartamento_id_entry = tk.Entry(frame_emprestimo)
    apartamento_id_entry.grid(row=1, column=1)

    tk.Label(frame_emprestimo, text='Data de Empréstimo (YYYY-MM-DD):').grid(
        row=2, column=0
    )
    data_emprestimo_entry = tk.Entry(frame_emprestimo)
    data_emprestimo_entry.grid(row=2, column=1)

    tk.Label(frame_emprestimo, text='Data de Devolução (YYYY-MM-DD):').grid(
        row=3, column=0
    )
    data_devolucao_entry = tk.Entry(frame_emprestimo)
    data_devolucao_entry.grid(row=3, column=1)

    def registrar_emprestimo_callback():
        ferramenta_id = int(ferramenta_id_entry.get())
        apartamento_id = apartamento_id_entry.get()
        data_emprestimo = data_emprestimo_entry.get()
        data_devolucao = data_devolucao_entry.get()
        registrar_emprestimo(
            ferramenta_id, apartamento_id, data_emprestimo, data_devolucao
        )
        messagebox.showinfo('Sucesso', 'Empréstimo registrado com sucesso!')

    tk.Button(
        frame_emprestimo,
        text='Registrar Empréstimo',
        command=registrar_emprestimo_callback,
    ).grid(row=4, column=0, pady=5)

    # Frame para registrar devolução
    frame_devolucao = tk.Frame(root)
    frame_devolucao.pack(pady=10)

    tk.Label(frame_devolucao, text='Nº do Empréstimo:').grid(row=0, column=0)
    emprestimo_id_entry = tk.Entry(frame_devolucao)
    emprestimo_id_entry.grid(row=0, column=1)

    tk.Label(frame_devolucao, text='Data de Devolução (YYYY-MM-DD):').grid(
        row=1, column=0
    )
    data_devolvida_entry = tk.Entry(frame_devolucao)
    data_devolvida_entry.grid(row=1, column=1)

    def registrar_devolucao_callback():
        emprestimo_id = int(emprestimo_id_entry.get())
        data_devolvida = data_devolvida_entry.get()
        registrar_devolucao(emprestimo_id, data_devolvida)
        messagebox.showinfo('Sucesso', 'Devolução registrada com sucesso!')

    tk.Button(
        frame_devolucao,
        text='Registrar Devolução',
        command=registrar_devolucao_callback,
    ).grid(row=2, column=0, pady=5)

    # Frame para listar ferramentas
    frame_listar_ferramentas = tk.Frame(root)
    frame_listar_ferramentas.pack(pady=10)

    def listar_ferramentas_callback():
        ferramentas = listar_ferramentas()
        messagebox.showinfo(
            'Ferramentas', '\n'.join([str(f) for f in ferramentas])
        )

    tk.Button(
        frame_listar_ferramentas,
        text='Listar Ferramentas',
        command=listar_ferramentas_callback,
    ).pack()

    # Frame para listar empréstimos
    frame_listar_emprestimos = tk.Frame(root)
    frame_listar_emprestimos.pack(pady=10)

    def listar_emprestimos_callback():
        emprestimos = listar_emprestimos()
        messagebox.showinfo(
            'Empréstimos', '\n'.join([str(e) for e in emprestimos])
        )

    tk.Button(
        frame_listar_emprestimos,
        text='Listar Empréstimos',
        command=listar_emprestimos_callback,
    ).pack()

    root.mainloop()
