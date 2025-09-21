# Constants
num_roles = 10000
file_name = "bruh.json"

if __name__ == "__main__": 
    from random import randint
    from statistics import mean
    import json

    # Making a list of the sums of rolling 3 die 10,000 times 
    num_list = []
    for _ in range(num_roles):
        num_list.append(randint(1, 6) + randint(1, 6) + randint(1, 6))

    # Write the sums of the rolls to a file
    with open(file_name , "w") as f:
        json.dump(num_list, f)

    # Find the average and print it...
    '''
    I Hate commenting with a passion. Code should talk for itself; 
    comments should only be used as notes to yourself and notes to others when it makes sense but not everywhere!!!!!!
    this comments right above is a great example of, whyyyyyy!!!!
    listen if this file had no comments at all it would look way better. Why are there comments???! It doesn't need them!!!!!
    '''
    avg = stat.mean(num_list)
    print(f'The average is: {avg}\n')
