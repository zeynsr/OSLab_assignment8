class Time:
    def __init__(self,h=0,m=0,s=0):
        self.h=h
        self.m=m
        self.s=s

    def show(self):
        print(self.h,' : ',self.m,' : ',self.s)

    def fix(self):
        if self.s > 60:
            self.s -=60
            self.m +=1

        if self.m > 60:
            self.m -=60
            self.h +=1

        if self.s < 0:
            self.s =0

        if self.m < 0:
            self.m =0

    def sum(self,other):
        res=Time()
        res.h=  self.h + other.h
        res.m = self.m + other.m
        res.s = self.s + other.s
        res.fix()
        return res

    def sub(self,other):
        res=Time()
        res.h=  self.h - other.h
        res.m = self.m - other.m
        res.s = self.s - other.s
        res.fix()
        return res

    def time_to_sec(self):
        sec=(self.h*3600)+(self.m*60)+(self.s)
        print(sec)

    def sec_to_time(self,sec):
        self.h = int(sec / 3600)
        sec = int(sec - (int(self.h) * 3600))
        self.m = int(sec / 60)
        self.s = int(sec - (int(self.m) * 60))



while True:
    print('enter the Time1 :')
    h1 = int(input())
    m1 = int(input())
    s1 = int(input())
    t1 = Time(h1 ,m1,s1)
    t1.show()
    print('enter the Time2 :')
    h2 = int(input())
    m2 = int(input())
    s2 = int(input())
    t2 = Time(h2, m2,s2)
    t2.show()
    while True:
        print('choose:\n1.add\n2.sub\n3.turn time to second\n4.turn second to time\n5.exit\n')
        c = int(input())
        if c==1:
            T=t1.sum(t2)
            T.show()
        if c==2:
            T = t1.sub(t2)
            T.show()
        if c==3:
           ch=int(input('which time do you want to convert? [1/2]'))
           if ch==1:
               t1.time_to_sec()
           if ch==2:
               t2.time_to_sec()
        if c==4:
            sec = int(input('Enter the amount of seconds : '))
            t1.sec_to_time(sec)
            t1.show()
        if c==5:
            break
    e = input('Do you want to continue with other times? [y/n]')
    if e == 'n':
        break