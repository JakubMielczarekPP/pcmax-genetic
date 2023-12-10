import random

def getInput(msg, var):
    i = -1
    while i < var:
        try:
            i = int(input(msg))
        except ValueError:
            print("Podaj poprawna liczbe calkowita.")

    return i


# pobierz liczbe procesorow z inputu
processors = getInput("Podaj ilosc procesorow (>1): ", 2)
processes = getInput(f"Podaj ilosc procesow (>= {processors}): ", processors)
min = getInput("Podaj minimalna dlugosc procesu: ", 1)
max = getInput("Podaj maksymalna dlugosc procesu: ", 1)

tasks = random.sample(range(min, max), processes)

with open("procesy.txt", 'w') as file:
    file.write(f"{processors}\n{processes}\n")
    file.write('\n'.join(str(task) for task in tasks))

print(tasks)