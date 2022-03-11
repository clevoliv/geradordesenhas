import random
import string

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,message):
        self.message=message

while True:
    try:
        tamanho = int(input(" Entre com a senha de no minimo 6 e máximo 20 caracteres: "))
        #print(tamanho)
        if tamanho > 20:
            raise InputError('Numero deve ser menor ou igual a 20!')
        elif tamanho<6:
            raise InputError('Numero deve ser maior ou igual a 6!')
        break
    except ValueError:
        print('entrar com o tamanho')
    except InputError as ex:
        print(ex)

chars = string.ascii_letters + string.digits + '!@#$&%*()ç=+,;:/?<>'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
print(" Senha criada com sucesso!")