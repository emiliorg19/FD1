"""
Imprimir en pantalla números del 1 a N
Si el número es divisible entre 3 imprimimos Fizz
Si el número es divisible entre 5 imprimimos Buzz
Si el número es divisible entre 3 y 5 imprimimos FizzBuzz
"""
def fizzBuzz(number):
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')    
        elif i % 5 == 0:
            print('Buzz')    
        else:
            print(i)
fizzBuzz(30)
"""
Llega hasta el numero 30
"""