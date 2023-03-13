def estPair(n : int)-> bool:
    '''indique si un nombre est pair'''
    assert type(n) == int and n>=0, "Le nombre doit être un entier >=0"
    return n%2==0

print("Nom module: ",__name__)

if __name__ == "__main__":
    print(f'Le nombre 20 est pair {estPair(20)}')
    print(f'Le nombre 27 est pair {estPair(27)}')