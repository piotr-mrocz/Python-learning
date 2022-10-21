# Napisać program służący do konwersji wartości temperatury podanej w stopniach Celsjusza
# na stopnie w skali Fahrenheita (stopnie Fahrenheita = 1.8 * stopnie Celsjusza + 32.0)

celsjusz = int(input("Stopnie celsjusza: "))
fahrenheit = (celsjusz *1.8) + 32

print("Stopnie Fahrenheita: ", fahrenheit)
