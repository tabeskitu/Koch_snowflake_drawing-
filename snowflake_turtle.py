

from turtle import *
  
# definiowanie funkcji, rysującej jeden bok fraktalu
def snowflake(lengthSide, levels):
    if levels == 0:
        flake.forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1)
    flake.left(60)
    snowflake(lengthSide, levels-1)
    flake.right(120)
    snowflake(lengthSide, levels-1)
    flake.left(60)
    snowflake(lengthSide, levels-1)
  
# okrslenie poziomu szczegółów (n) i koloru (color)
n = numinput("Poziom fraktalu", "podaj poziom szczegółów fraktalu (od 0 do 10): ", minval=0, maxval=10)
col = numinput("Kolor fraktalu", "1 - czarny, 2 - niebieski, 3 - czerwony: ", minval=1, maxval=3)
wall = numinput("Ilość ścian fraktalu", "podaj ilość ścian (od 1 do 7): ", minval=1, maxval=7)

n = int(n)
col = int(col)
wall = int(wall)

# obliczanie liczby boków
wynik = wall*4**n

# zmiana wartosci wyników z intów na stringi
wynik_str = str(wynik)
n_str = str(n)
wall_str = str(wall)
    
# main function
if __name__ == "__main__":
    
    # zapobieganie crushowaniu
    TurtleScreen._RUNNING=True
    
    # tytuł programu
    title("Koch snowflake")
    
    # wskazniki w programie
    flake = Turtle()        # rysowanie fraktalu
    sides = Turtle()        # liczba bokow
    detail = Turtle()       # poziom szczegółów
    walls = Turtle()        # ilość ścian fraktalu
    
    # ustawienie szybkosci wskaznika i dlugosci jednej scianki
    flake.speed(0)
    sides.speed(0) 
    detail.speed(0)
    walls.speed(0)                  
    if wall > 3:
        length = window_width()/wall
    elif wall == 3:
        length = window_width()/3
    else:
        length = window_width()/2 
    
    # boost prędkosci - ignorowanie odswiezania ekranu - im wieksze n tym szybciej, nie można odrazu największej bo pomija klatki
    if n < 5:
        k = 2
    elif n < 7:
        k = 6
    elif n < 9:
        k = 120
    else:
        k = 4000
    tracer(k, 0)

    # ustawianie koloru fraktalu
    if col == 1:
        flake.color("black")
    elif col == 2:
        flake.color("blue")
    else:
        flake.color("red")
    
    # wyświetlanie liczby boków
    sides.penup()
    sides.hideturtle()
    sides.goto(0, length/2.0)
    sides.write("liczba boków: " + wynik_str, align="center", font=("Calibri", 15, "italic"))
    
    # wyświetlanie poziomu szczegółów
    detail.penup()
    detail.hideturtle()
    detail.goto(0, length/2.0 + 30)
    detail.write("poziom szegółów: " + n_str, align="center", font=("Calibri", 15, "italic"))

    # wyświetlanie ilości ścian
    walls.penup()
    walls.hideturtle()
    walls.goto(0, length/2.0 + 60)
    walls.write("ilość ścian: " + wall_str, align="center", font=("Calibri", 15, "italic"))
  
    # Pull the pen up – no drawing when moving.
    flake.penup()                     
      
    # ustawienie wskaznika płatka w początkowym miejscu
    flake.backward(length/2.0)
   
    #flake.left(90)
    #flake.forward(length/3.0)
    #flake.right(90)      
  
    # parametry rysowania fraktalu
    flake.pendown() 
    flake.hideturtle()
    
    for i in range(wall):    
        snowflake(length, n)
        flake.right(360/wall)       
  
    # Kontrola zamknięcia programu
    mainloop()