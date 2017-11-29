class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im >= 0:
            return str(self.re) + '+' + str(self.im) + 'i'
        return str(self.re) + str(self.im) + 'i'

    def absolute(self):
        ab = (self.re**2+self.im**2)**0.5
        return round(ab, 2)

    def add(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)

    def conjugate(self):
        self.im *= -1


a, b, c, d = [int(e) for e in input().strip().split()]
complex1 = ComplexNum(a, b)
complex2 = ComplexNum(c, d)

print(complex1, end=' ')
complex1.conjugate()
print(complex1, end=' ')
print(complex1.absolute())

print(complex2, end=' ')
complex2.conjugate()
print(complex2, end=' ')
print(complex2.absolute())

print(complex1.add(complex2))
