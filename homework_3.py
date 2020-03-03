#Write 'def()' that asks for an integer and print square of it.
# Used 'try' 'except' and 'else' and loop 'while'

def ask():
    while True:
        try:
            ask = int(input('Введите целое число: '))

        except:
            print('Похоже вы ввели не целое число!')
            continue
        else:
            print(ask**2)
        break

ask()


