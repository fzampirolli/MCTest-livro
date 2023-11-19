import os
import filecmp
import difflib

pasta1 = './livro-git'
pasta2 = './livro-overleaf'

for raiz, _, arquivos in os.walk(pasta1):
    for arquivo in arquivos:
        if arquivo.endswith('.tex'):
            caminho_arquivo1 = os.path.join(raiz, arquivo)
            caminho_arquivo2 = os.path.join(pasta2, os.path.relpath(caminho_arquivo1, pasta1))

            if os.path.isfile(caminho_arquivo2):
                if not filecmp.cmp(caminho_arquivo1, caminho_arquivo2):
                    print(f'Os arquivos {caminho_arquivo1} e {caminho_arquivo2} têm conteúdos diferentes.')
                    
                    with open(caminho_arquivo1, 'r') as arquivo1, open(caminho_arquivo2, 'r') as arquivo2:
                        diff = difflib.unified_diff(arquivo1.readlines(), arquivo2.readlines(), lineterm='')
                        diff_string = '\n'.join(diff)
                        print(diff_string)
                    
                    # Aqui você pode adicionar as ações desejadas para manipular os arquivos com conteúdos diferentes
            else:
                print(f'O arquivo {caminho_arquivo2} não está presente em {pasta2}')