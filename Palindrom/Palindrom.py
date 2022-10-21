# Napisz program, który pobierze od użytkownika łańcuch znaków 
# i wyświetli na konsoli jego długość, informację czy jest to palindrom

napis = input("Podaj napis: ")

print("Długość napisu: ", len(napis))

if napis == napis[::-1]:
    print("Jest to palindrom...")
else:
    print("No nie jest to palindrom...")


