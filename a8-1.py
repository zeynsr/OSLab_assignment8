class fraction:
    def __init__(self,N=0,D=1):
        self.N=N
        if D!=0:
            self.D=D
        else:
            self.D=1

    def sum(self,other):
        res=fraction()
        if self.D == other.D:
            res.D=self.D
            res.N=self.N+other.N
        else:
            a=self.N * other.D
            b=self.D * other.N
            c=self.D * other.D
            res.N=a+b
            res.D=c
        return res

    def sub(self, other):
        res = fraction()
        if self.D == other.D:
            res.D = self.D
            res.N = self.N - other.N
        else:
            a = self.N * other.D
            b = self.D * other.N
            c = self.D * other.D
            res.N = a - b
            res.D = c
        return res

    def mul(self, other):
        res = fraction()
        res.N=self.N * other.N
        res.D=self.D * other.D
        return res

    def div(self, other):
        res = fraction()
        res.N=self.N * other.D
        res.D=other.N * self.D
        return res


    def simple(self):
        f=fraction()

        if self.N > self.D:
            Min = self.D
        else:
            Min = self.N
        for i in range(1, Min + 1):
            if ((self.N % i == 0) and (self.D % i == 0)):
                gcd = i
        if self.N % gcd==0 and self.D % gcd==0:
            f.N=int(self.N/gcd)
            f.D=int(self.D/gcd)

        return f


    def show(self):
        print(self.N,'/',self.D)


while True:
    print('enter the friction1 :')
    n1 = int(input())
    d1 = int(input())
    s1 = fraction(n1, d1)
    s1.show()
    print('enter the friction2 :')
    n2 = int(input())
    d2 = int(input())
    s2 = fraction(n2, d2)
    s2.show()
    while True:
        print('choose:\n1.add\n2.sub\n3.mul\n4.divide\n5.exit\n')
        c = int(input())
        if c == 1:
            S = s1.sum(s2)
            S.show()
            b=input('Do you want to see your deduction simplified? [y/n]')
            if b=='y':
                Su = S.simple()
                Su.show()
            if b=='n':
                break
        if c == 2:
            S = s1.sub(s2)
            S.show()
            b = input('Do you want to see your deduction simplified? [y/n]')
            if b == 'y':
                Su = S.simple()
                Su.show()
            if b == 'n':
                break
        if c == 3:
            S = s1.mul(s2)
            S.show()
            b = input('Do you want to see your deduction simplified? [y/n]')
            if b == 'y':
                Su = S.simple()
                Su.show()
            if b == 'n':
                break
        if c == 4:
            S = s1.div(s2)
            S.show()
            b = input('Do you want to see your deduction simplified? [y/n]')
            if b == 'y':
                Su = S.simple()
                Su.show()
            if b == 'n':
                break
        if c==5:
            break
    e = input('Do you want to continue with other fractions? [y/n]')
    if e == 'n':
        break
