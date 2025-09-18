import os
from tkinter.filedialog import askdirectory # Importa uma função de uma Biblioteca que permite selecionar arquivos

caminho = askdirectory(title="Seleciona uma pasta") # Abre pop-up para selecionar a pasta

lista_arquivos = os.listdir(caminho)    # Lista todos os arquivos dentro da lista selecionada

# Deifine os tipos de arquivos
locais = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".svg"],
    "Planilhas": [".xlsx", ".gsheet", ".csv"],
    "PDFs": [".pdf"],
    "Words": [".docx"]
}

# Percorre a lista de arquivos
for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")   # Separa o arquivo em nome e extensão
    for pasta in locais:    # Para cada pasta "imagens", "planilhas", "pdfs", "words"
        if extensao in locais[pasta]:   # Verifica se as extensões existem na pasta
            if not os.path.exists(f"{caminho}/{pasta}"):    # Se não existirem as pastas "imagens", "planilhas", "pdfs" ou "words"
                os.mkdir(f"{caminho}/{pasta}")  # Cria as pastas

            #os.rename("caminho/nome_antigo", "caminho/pasta/nome_novo")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")   # Organiza as pastas com os seus arquivos