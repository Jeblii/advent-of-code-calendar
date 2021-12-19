import dataclasses as dc

@dc.dataclass
class Probe:
    x_position: float
    y_position: float
    x_velocity: float
    y_velocity: float

    def in_target_area(self, target_min_x, target_max_x, target_min_y, target_max_y) -> bool:
        if self.x_position > target_min_x and self.x_position < target_max_x:
            if self.y_position > target_min_y and self.y_position < target_max_y:
                return True
        return False

@dc.dataclass 
class TargetArea:
    min_x: float
    max_x: float
    min_y: float
    max_y: float

def step(probe):
    # The probe's x position increases by its x velocity.
    # The probe's y position increases by its y velocity.
    # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    # Due to gravity, the probe's y velocity decreases by 1.
    probe.x_position += probe.x_velocity
    probe.y_position += probe.y_velocity
    # drag
    if probe.x_velocity > 0:
        probe.x_velocity -= 1
    elif probe.x_velocity < 0:
        probe.x_velocity += 1
    # gravity
    probe.y_velocity -= 1

    return probe

def check_probe_T(probe):
    pass

x_velo = 17
y_velo = -4
probe = Probe(x_position=0., y_position=0., x_velocity=x_velo, y_velocity=y_velo)
target_area = TargetArea(min_x=20, max_x=30, min_y=-10, max_y=-5)

i = 0
# while the probe has not passed the target area 
while probe.x_position < target_area.max_x:
    step(probe)
    i += 1
    if probe.in_target_area(target_area.min_x, target_area.max_x, target_area.min_y, target_area.max_y):
        print(probe)
        print(i)
        break

# part one - grid search
def probe_max_height(probe, target):
    max_y = 0.
    while probe.x_position < target.max_x:
        probe = step(probe)
        if probe.y_position > max_y:
            max_y = probe.y_position
        if probe.in_target_area(target_area.min_x, target_area.max_x, target_area.min_y, target_area.max_y):
            return max_y
    return 0.

# for i in range(-20, 20):
#     for j in range(-20, 20):

y = probe_max_height(probe, target_area)
print(y)
