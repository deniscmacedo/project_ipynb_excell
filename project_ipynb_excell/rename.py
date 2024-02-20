import os

# Especifique o diretório que contém os arquivos
diretorio = 'project_ipynb_excell\\files3'

# Iterar sobre todos os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    # Crie o caminho completo para o arquivo
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)
    
    # Verifique se é realmente um arquivo (não um diretório)
    if os.path.isfile(caminho_arquivo):
        # Separe o nome do arquivo de sua extensão
        nome_base, extensao = os.path.splitext(nome_arquivo)
        # Remova os espaços do nome do arquivo
        novo_nome_base = nome_base.replace(' ', '_').replace('.', '_')
        # Junte o novo nome base com a extensão original
        novo_nome_arquivo = novo_nome_base + extensao
        # Crie o caminho completo para o novo nome do arquivo
        novo_caminho_arquivo = os.path.join(diretorio, novo_nome_arquivo)
        
        # Renomeie o arquivo
        os.rename(caminho_arquivo, novo_caminho_arquivo)
