c_letras = lambda lista: [len(x) for x in lista]

listaanimal = ['cachorro','gato']
print(c_letras(listaanimal))

calculadora = {
    'soma': lambda a,b: a+b,
    'subtraçao': lambda a,b: a-b,
    'multiplicaçao': lambda a,b: a*b
}

soma = calculadora['soma']
print(soma(10,2))


