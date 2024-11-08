
lista = [1,10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10/1
    numero = lista[3]
except ZeroDivisionError:
    print('Nao e possivel realizar divisao por 0')

except ArithmeticError:
    print("HOuve um erro ao realizar a operaçao aritimetica")

except IndexError:
    print('Erro ao acessar o index na lista')

except Exception as ex:
    print('erro desconhecido Erro : {}'.format(ex))


else:
    print('Execute quando nao ocorre exceçao')

finally:
    print("sempre executa")
    print("fechando arquivo")
    arquivo.close()