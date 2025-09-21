# Jurko Janos
# 5-26-21
# Takes in a sentance, translates it to pig latin, 
# prints it and the OG to the console and writes it to a file.

print("Write a sentance that you want translated to Pig Latin")

while True:
    inp = input("\nSentance: ")
    lis = inp.split()
    translated = ""

    for word in lis:
        if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            translated += (word + "way ")
        else:
            translated += (word[1:] + word[0] + "ay ")
    
    print("\n" + inp)
    print(translated)

    with open("JurajPigLatin.txt", "a") as f:
        f.write(f"{str(inp)}\n{str(translated)}\n")

    while True:
        keepGoin = input("\ndo you want to do another (type y or n): ")

        if  keepGoin == "n":
            quit()
        elif keepGoin == "y":
            break
        else:
            print("invalid answer")
