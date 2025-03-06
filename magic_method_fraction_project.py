class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.dem = d
    
    def __str__(self):
        return f"The fraction is {self.num} / {self.dem}"
    
    def __add__(self,other):
        temp_num = self.num * other.dem + other.num * self.dem
        temp_dem = self.dem * other.dem
        return f"{temp_num} / {temp_dem}"

    def __sub__(self,other):
        temp_num = self.num * other.dem - other.num * self.dem
        temp_dem = self.dem * other.dem
        return f"{temp_num}/{temp_dem}"
    
    def __mul__(self,other):
        temp_num = self.num * other.num
        temp_dem = self.dem * other.dem
        return f"{temp_num}/{temp_dem}"
    
    def __truediv__(self,other):
        temp_num = self.num * other.dem
        temp_dem = self.dem * other.num
        return f"{temp_num}/{temp_dem}"

y1, y2 = map(int,input("Enter the 1st fraction : ").split())
x1, x2 = map(int,input("Enter the 2st fraction : ").split())

y = Fraction(y1,y2)
x = Fraction(x1,x2)

while(True):
    option = input('''
        1. Enter (1) to print the fraction
        2. Enter (2) to add fraction
        3. Enter (3) to substract fraction
        4. Enter (4) to multiply fraction
        5. Enter (5) to divide fraction
        6. Enter (6) to exit 
        Enter your choice : ''')

    if option == "1":
        print(y)
        print(x)
        
    if option == "2":
        print(y + x)
    
    if option == "3":
        print(y - x)

    if option == "4":
        print(y * x)

    if option == "5":
        print(y / x)
    
    if option == "6":
        break
