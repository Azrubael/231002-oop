class Timer:
    def __init__(self,h=0,m=0,s=0):
        self.__ct = [h,m,s]

    def __str__(self):
        z=[]
        for u in self.__ct:
            if 0 <= u < 10:
                z.append(f"0{u}")
            elif 10 <= u <= 59:
                z.append(str(u))
            else:
                raise ValueError
        return ":".join(z)
        
    def next_second(self):
        self.__ct[2] += 1
        if self.__ct[2] > 59:
            self.__ct[1] += self.__ct[2] // 60
            self.__ct[2] = self.__ct[2] % 60
        if self.__ct[1] > 59:
            self.__ct[0] += self.__ct[1] // 60
            self.__ct[1] = self.__ct[1] % 60
        if self.__ct[0] > 24:
            self.__ct[0] += self.__ct[1] // 24

    def prev_second(self):
        self.__ct[2] -= 1
        if self.__ct[2] < 0:
            self.__ct[1] -= 1
            self.__ct[2] = 59
        if self.__ct[1] < 0:
            self.__ct[0] -= 1
            self.__ct[1] = 59
        if self.__ct[0] < 0:
            self.__ct[0] = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

print('---')
timer2 = Timer(9, 0, 0)
timer2.prev_second()
print(timer2)