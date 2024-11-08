import shutil

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota=arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_n = x.split(',')
        aluno = lista_n[0]
        lista_n.pop(0)
        media = lambda notas: sum([int(i) for i in notas])/4
        lista_media.append({aluno:media(lista_n)})
    return lista_media


def copy_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '/home/gerson/Downloads')


def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '/home/gerson/Downloads')

if __name__ == '__main__':
    #copy_arquivo('notas.txt')
    #lista_media=media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('primeira linha')
    #aluno = 'gabriel,2,4,7,1\n'
    #atualizar_arquivo('notas.txt' , aluno)
    ler_arquivo('notas.txt')
