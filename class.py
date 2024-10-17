'''1. Feladat: Egyszerű Osztály Definiálása
    Leírás: Hozz létre egy Dog nevű osztályt, amely a kutyák nevét és életkorát tárolja. Az osztálynak legyen egy metódusa, amely kiírja a kutya adatait.

    Feladat:

    Készíts egy osztályt, amelynek van egy __init__ metódusa (konstruktor), amely a kutya nevét és életkorát tárolja.

    Hozz létre egy metódust display_info() néven, amely kiírja a kutya nevét és életkorát.

    Példányosítsd az osztályt, és hívd meg a metódust.



2. Feladat: Banki Számla Osztály

    Leírás: Hozz létre egy BankAccount nevű osztályt, amely banki számlákat reprezentál. Az osztály képes legyen befizetést és pénzfelvételt végrehajtani, valamint a számla    egyenlegét lekérdezni.

    Feladat:

    Hozz létre egy osztályt, amely egy balance változót tárol.

    Készíts metódusokat:

    deposit(amount): hozzáadja az összeget az egyenleghez.

    withdraw(amount): levonja az összeget az egyenlegből, ha van elég pénz a számlán.

    get_balance(): visszaadja az aktuális egyenleget.

    Példányosítsd az osztályt, és végezz rajta befizetést, pénzfelvételt, és kérdezd le az egyenleget.


3. Feladat: Diák Osztály és Átlag Számítása
    Leírás: Készíts egy Student nevű osztályt, amely tárolja a diák nevét és jegyeit, és legyen képes kiszámolni az átlagukat.

    Feladat:

    Az osztály tárolja a diák nevét és egy jegyek listáját.
    Legyen egy metódus add_grade(grade), amely hozzáad egy jegyet a listához.
    Legyen egy metódus get_average(), amely kiszámolja és visszaadja az átlagot.
    Példányosíts egy diákot, adj hozzá jegyeket, és számold ki az átlagát.
'''


class Dog:
    def __init__(self,nev,eletkor):
        self.nev = nev
        self.eletkor = eletkor
        
    def display_info(self):
        return self.nev, self.eletkor
        


peldany1 = Dog("vmi", 12)



        
