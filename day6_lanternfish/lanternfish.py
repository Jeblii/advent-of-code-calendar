input = [4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2]
NUM_DAYS = 256

# days_to_birth; state = 0 day to birth, 2 days to birth, ...., 8 days to birth = newborn
fish_count_days_to_birth = [0] * 9

# init the counts with the input list
for fish in input:
    fish_count_days_to_birth[fish] += 1

for i in range(NUM_DAYS):
    # fishes on position 0 give birth to the guppies
    fishes_given_birth = fish_count_days_to_birth[0]

    # Shift the state of the days; the guppies that the fishes have produced should be equal so this is placed in last state of the list
    fish_count_days_to_birth.append(fish_count_days_to_birth.pop(0)) 

    # the fishes that have given birth takes 6 days to give birth again
    fish_count_days_to_birth[6] += fishes_given_birth
    
print(sum(fish_count_days_to_birth))
# print(f'Total lanternfish after 256 days: {sum(days)}')
