class WheelBeing:
    def __init__(self, kolvo, vid, v):
        self.kolvo = kolvo
        self.vid = vid
        self.v = v

    def __lt__(self, other):
        if (self.v, self.kolvo, self.vid) < (other.v, other.kolvo, other.vid):
            return True
        return False

    def __le__(self, other):
        if (self.v, self.kolvo, self.vid) <= (other.v, other.kolvo, other.vid):
            return True
        return False

    def __eq__(self, other):
        if (self.v, self.kolvo, self.vid) == (other.v, other.kolvo, other.vid):
            return True
        return False

    def __ne__(self, other):
        if (self.v, self.kolvo, self.vid) != (other.v, other.kolvo, other.vid):
            return True
        return False

    def __gt__(self, other):
        if (self.v, self.kolvo, self.vid) > (other.v, other.kolvo, other.vid):
            return True
        return False

    def __ge__(self, other):
        if (self.v, self.kolvo, self.vid) >= (other.v, other.kolvo, other.vid):
            return True
        return False

    def __isub__(self, number):
        if self.kolvo - number >= 10:
            self.kolvo -= number
        else:
            self.kolvo = 10
        self.v //= 2
        return WheelBeing(self.kolvo, self.vid, self.v)

    def __add__(self, other):
        return WheelBeing((self.kolvo + other.kolvo) // 2, sorted([self.vid, other.vid])[0], (self.v + other.v) // 2)

    def __truediv__(self, number):
        return [WheelBeing(self.kolvo // number, self.vid + f'{i + 1}', self.v) for i in range(0, number)]

    def __call__(self, number):
        return self.kolvo * number // self.v

    def add_insects(self, number):
        self.kolvo += number

    def __str__(self):
        return f'Wheel being with a volume of {self.v} accommodates {self.kolvo} insects of the species {self.vid}.'

    def __repr__(self):
        return f"WheelBeing({self.kolvo}, '{self.vid}', {self.v})"


wb = WheelBeing(120, "spider", 15)
wb1 = WheelBeing(120, "fly", 15)
print(wb > wb1, wb != wb1, wb <= wb1)
print(wb, wb1, sep="\n")
print()
wb -= 117
wb1.add_insects(-35)
wb2 = wb + wb1
print(wb, wb1, wb2, sep="\n")
