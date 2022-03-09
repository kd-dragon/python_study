class PocketMon:

    def set_data(self, num, name, hpoint, attack, defence, speed):
        self.num = num
        self.name = name
        self.hpoint = hpoint
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.sum = self.hpoint + self.attack + self.defence + self.speed

    def set_sum(self):
        self.sum = self.hpoint + self.attack + self.defence + self.speed

    def print_data(self):
        print(self.num, end=" ")
        print(self.name, end=" ")
        print(self.hpoint, end=" ")
        print(self.attack, end=" ")
        print(self.defence, end=" ")
        print(self.speed, end=" | ")
        print(self.sum)

    def __init__(self):
        self.num = ""
        self.name = ""
        self.hpoint = 0
        self.attack = 0
        self.defence = 0
        self.speed = 0
        self.sum = 0