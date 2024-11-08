from aula7televisao import Televisao
from aula7calculadora import Calculadora2
from aula8contadordeletras import c_letras
from aula7calculadora import Calculadora

televisao = Televisao()
print(televisao.ligada)
televisao.Power()
print(televisao.ligada)

calc =  Calculadora()
print(calc.soma(2,1))

calc2 = Calculadora2(11,2)
print(calc2.multiplicacao())


lista = ['cachorro','gato']
print(c_letras(lista))