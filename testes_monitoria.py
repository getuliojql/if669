lista = eval(input())

def soma(data):
    total_sum = 0
    for item in data:
        if isinstance(item, list):
            total_sum += soma(item)
        elif isinstance(item, (int, float)):
            total_sum += item
    return total_sum


def mais_interno(data):
    for item in data:
        if isinstance(item, list):
            mais_interno(item)
    item = soma(data)
    print(f"{item} -> {data}")

mais_interno(lista) 