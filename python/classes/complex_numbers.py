import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return self.string_complex(real, imaginary)
        
    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return self.string_complex(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.imaginary * no.real + self.real * no.imaginary
        return self.string_complex(real, imaginary)

    def __truediv__(self, no):
        d = no.real ** 2 + no.imaginary ** 2
        real = (self.real * no.real + self.imaginary * no.imaginary) / d
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / d
        return self.string_complex(real, imaginary)

    def mod(self):
        return self.string_complex(
            (self.real ** 2 + self.imaginary ** 2) ** 0.5,
            0
        )

    def string_complex(self, real, imaginary):
        if imaginary == 0:
            result = "%.2f+0.00i" % (real)
        elif real == 0:
            if imaginary >= 0:
                result = "0.00+%.2fi" % (imaginary)
            else:
                result = "0.00-%.2fi" % (abs(imaginary))
        elif imaginary > 0:
            result = "%.2f+%.2fi" % (real, imaginary)
        else:
            result = "%.2f-%.2fi" % (real, abs(imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')