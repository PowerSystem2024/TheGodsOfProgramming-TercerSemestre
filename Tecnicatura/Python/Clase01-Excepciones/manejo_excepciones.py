from NumerosIgualesException import NumerosIgualesException

resultado = None 

try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))

    if a == b:
        raise NumerosIgualesException('Los números son iguales.')
    resultado = a / b

except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')

except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')

except NumerosIgualesException as e:
    print(f'NumerosIgualesException - {e}')

except Exception as e:
    print(f'Excepción - Ocurrió un error: {type(e)}')

else:
    print('No se arrojó ninguna excepción.')

finally:
    print('Este bloque siempre se va a ejecutar.')

print(f'El resultado es: {resultado}')
print('Seguimos...')