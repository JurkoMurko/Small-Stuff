import statistics as stat
import json

# Constants 
file_name = "bruh.json"
possible_nums = list(range(3, 19))

# returns a list of the frequency of each number
def calc_freq(nums):
    why_am_i_spending_the_time = []  # freqency list should be a frquency dictionary not a list
    
    for i in possible_nums:
        why_am_i_spending_the_time.append(nums.count(i))

    return why_am_i_spending_the_time

# data
with open(file_name, "r") as f:
    num_list = json.load(f)

frequency_list = calc_freq(num_list)
pstdev = stat.pstdev(num_list)

if __name__ == "__main__":
    # prints
    print(frequency_list)
    print(f'\nThe p Standard Deviation is: {pstdev}')
    print("\n")

    for i, freq in zip(possible_nums, frequency_list):
        print(f'{str(i).zfill(2)} - {freq}')
