import sys


class Complex:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]


class ComplexNumbers:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def plus(self, c2):
        self.real = self.real + c2.real
        self.imaginary = self.imaginary + c2.imaginary

    def multiply(self, c2):
        a = self.real
        b = self.imaginary
        self.real = self.real * c2.real - (self.imaginary * c2.imaginary)
        self.imaginary = a * c2.imaginary + (b * c2.real)

    def show(self):
        sys.stdout.write(str(self.real) + " + i" + str(self.imaginary))


c1 = ComplexNumbers(4, 5)
c2 = ComplexNumbers(1, 2)

choice = 1
if choice == 1:
    c1.plus(c2)
    c1.show()
elif choice == 2:
    c1.multiply(c2)
    c1.show()
else:
    pass

# a.multiply(b)
# print a.real,a.imaginary
