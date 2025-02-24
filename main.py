from src.models.database import criar_tabelas
from src.views.interface import criar_interface

if __name__ == '__main__':
    criar_tabelas()  # Cria as tabelas no banco de dados
    criar_interface()  # Inicia a interface gráfica
