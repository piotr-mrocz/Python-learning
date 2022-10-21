import turtle

#turtle.pensize(10) # rozmiar pędzla
#turtle.pencolor(('red')) # kolor pędzla na czerwony
#for i in range(4): 
#     turtle.forward(100) # poruszanie do przodu
#     turtle.right(90) # skręć w prawo o 90 stopni


#turtle.pencolor(('green')) # kolor pędzla na zielony

#turtle.goto(100,0)  # Rysowanie linii do punktu o podanych współrzędnych bezwzględnych
#turtle.goto(100,100)
#turtle.goto(0,100)
#turtle.goto(0,0)

#print(turtle.position()) # Bieżące współrzędne położenia żółwia

#turtle.clear() # Czyszczenie okna rysowania
#turtle.reset() # Resetowanie ustawień rysowania z jednoczesnym czyszczeniem obszaru rysowania
#turtle.undo() # Cofanie ostatnio wykonanej operacji rysowania
## turtle.redo() # Przywracanie ostatnio cofniętej operacji rysowania


windows = turtle.Screen()
windows.bgcolor("black")
turtle.pensize(15)
angle = 32
iter = 150

for i in range(iter):
    #turtle.pencolor((i / iter, (iter - i) / iter, 0))
    turtle.pencolor((i / iter + 0.00008, (iter - i + 0.08) / iter, 0.5))
    turtle.forward(i)
    turtle.circle(i, angle)