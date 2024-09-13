def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_successor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, successor #obs: esses valores são retornados em uma tupla, que é uma estrutura imutável.


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_successor(10))  # (9, 11)
