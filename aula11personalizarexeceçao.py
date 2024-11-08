class Error(Exception):
    pass

class inputError(Error):
    def __init__(self,message):
        self.message = message


while True:
    try:
        x = int(input("Entre com uma nota de 0 a 10 :"))
        print(x)
        if x > 10:
            raise inputError('Nota nao pode ser maior que 10')
        if x < 0:
            raise inputError('Nota nao pode ser menor que 0')

        break
    except ValueError:
        print('Valor invalido. Deve-se  digitar apenas numeros' )

    except inputError as ex:
        print(ex)