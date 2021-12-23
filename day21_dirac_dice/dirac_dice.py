import dataclasses as dc
import numpy as np
import itertools

@dc.dataclass
class Player:
    position: int
    score: int = 0

    # def take_turn(
    #     self,
    #     die_n: int,
    # ):
    #     if (self.position + die_n) <= 10:
    #         self.position += die_n
    #     else:
    #         self.position = (die_n + self.position) % 10
    #     self.score += self.position

    def take_turn(self, die_n):
        self.position = self.position + die_n
        self.position = (self.position % 10) + 10 * (self.position % 10 == 0)
        self.score = self.score + self.position

@dc.dataclass 
class Die:
    n: float = 1

    def roll(self) -> int:
        if (self.n + 1) < 100:
            self.n += 1
        else:
            self.n = 1
        return self.n

def step(player:Player, die:Die):
    first, second, third = die.n, die.roll(), die.roll()
    print(first, second, third)
    player.take_turn(die_n=sum([first, second, third]))
    die.roll()
    return None

start_pos_p1 = 4
start_pos_p2 = 8

p1 = Player(position=start_pos_p1)
p2 = Player(position=start_pos_p2)
die = Die()

i = 0
while True:
    step(p1, die)
    step(p2, die)
    if (p1.score >= 1000) | (p2.score >= 1000):
        print(f"{i}, p1: {p1}, p2: {p2}")
        break
    i+=1

    print(f"{i}, p1: {p1}, p2: {p2}")


