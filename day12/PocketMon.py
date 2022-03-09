class PocketMon:

    def set_data(self, num, name, hpoint, attack, defence, speed):
        self.num = num
        self.name = name
        self.hpoint = hpoint
        self.attack = attack
        self.defence = defence
        self.speed = speed

    def print_data(self):
        print(self.num, end=" | ")
        print(self.name, end=" | ")
        print(self.hpoint, end=" | ")
        print(self.attack, end=" | ")
        print(self.defence, end=" | ")
        print(self.speed)
