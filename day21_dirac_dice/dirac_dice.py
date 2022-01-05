import dataclasses as dc
import numpy as np
import itertools

@dc.dataclass
class Player:
    position: int
    score: int = 0

    def take_turn(
        self,
        die_n: int,
    ):
        self.position = (die_n + self.position) % 10

        if self.position == 0:
            self.score += 10
        else:
            self.score += self.position

@dc.dataclass 
class Die:
    n: int = 1
    n_times_rolled: int = 0

    def roll(self) -> int:
        if (self.n + 1) <= 100:
            self.n += 1
        else:
            self.n = 1
        self.n_times_rolled += 1
        return self.n

def step(player:Player, die:Die):
    first, second, third = die.n, die.roll(), die.roll()
    player.take_turn(die_n=sum([first, second, third]))
    die.roll()
    return None

start_pos_p1 = 7
start_pos_p2 = 10

p1 = Player(position=start_pos_p1)
p2 = Player(position=start_pos_p2)
die = Die()

i = 0
while True:
    step(p1, die)
    if p1.score >= 1000:
        print('p1 won')
        print(p2.score, p2.score * die.n_times_rolled)
        break

    step(p2, die)
    if p1.score >= 1000:
        print('p2 won')
        print(p1.score, p1.score * die.n_times_rolled)
        break
    i+=1

    print(f"{i}, p1: {p1}, p2: {p2}")


