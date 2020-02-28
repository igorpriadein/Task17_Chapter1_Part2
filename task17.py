

# def say(saying):
#     if saying == 'Hello':
#         print(offices)
#     else:
#         print('Type "Hello" to see all offices')

offices = "1 - google_KG\n 2 - google_paris\n 3 - google_uar"
def func(key):
    if key == 1:
        with open('google_KG.txt', 'w+') as file:
            file.write(input('Enter your commit '))
    elif key == 2:
        with open('google_paris.txt', 'w+') as file:
            file.write(input('Enter your commit '))
    elif key == 3:
        with open('google_uar.txt', 'w+') as file:
            file.write(input('Enter your commit '))
    else:
        print("There's no such office")

print(offices)
key = int(input('Enter number of office '))

func(key)



