import math


def get_coffictent(number, power):
    q = math.floor(number/(3**power))
    res = number % (3**power)
    return q, res

def max_power(number):
    for i in range(20):
        a, res = get_coffictent(number, i)
        if (a > 0):
            coeficiente = i
    return coeficiente
    
def traductor_ternario(number):
    if number == 0:
        return [0,0,0]
    
    a = []
    M = max_power(number)
    residuo = number
    for i in range(M + 1):
        power = M - i
        coeficiente, residuo = get_coffictent(residuo, power)
        a.append(coeficiente)
    
    while (len(a) < 3):
        a.insert(0,0)
    return a
        
        
def main():
    for n in range(27):
        ternario = traductor_ternario(n)
        print(f"posicion: ", n+1)
        print(ternario)

if __name__ == "__main__":
    main()  