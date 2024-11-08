
class Calculadora:

    def soma (self , a , b):
        return a+b

        
    def subtracao (self , a , b):
        return a-b


    def divisao (self , a , b):
        return a/b


    def multiplicacao (self , a , b):
        return a*b


if __name__ == "__main__":
    calculadora = Calculadora()

    print(calculadora.soma(10,2))
    print(calculadora.subtracao(5,2))
    print(calculadora.divisao(40,2))
    print(calculadora.multiplicacao(6,2))



print(str("Calculadora2"))
    

class Calculadora2:

    def __init__(self , a , b):
        self.a = a
        self.b = b

    def soma (self):
        return self.a + self.b

        
    def subtracao (self ):
        return self.a - self.b


    def divisao (self):
        return self.a / self.b


    def multiplicacao (self):
        return self.a  * self.b


if __name__ == "__main__":

    calculadora2 = Calculadora2(10 , 2)
    print(calculadora2.soma())
    print(calculadora2.subtracao())
    print(calculadora2.divisao())
    print(calculadora2.multiplicacao())





















