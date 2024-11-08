# #Conjunto


conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}

conjunto_uniao = conjunto.union(conjunto2)
print("Uniao: {}".format(conjunto_uniao))

conjunto_intersecçao = conjunto.intersection(conjunto2)
print("intersecçao: {}".format(conjunto_intersecçao))

conjunto_diferença1 = conjunto.difference(conjunto2)
conjunto_diferença2 = conjunto.difference(conjunto)

print("Diferença entre 1 , 2: {}".format(conjunto_diferença1))
print("Diferença entre 2 , 1: {}".format(conjunto_diferença2))


conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print("Diferença simetrica: {}".format(conjunto_diff_simetrica))


# #subconjunto e superconjunto

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print("A subconjunto de B: {}".format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print("B superconjunto de A: {}".format(conjunto_superset))


# # tirando a duplicidade da lista 

lista = ["cachorro","cachorro","gato","gato","elefante"]
print(lista)

c_animais = set(lista)
print(c_animais)

l_animais = list(c_animais)
print(l_animais)

