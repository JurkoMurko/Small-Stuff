if __name__ == "__main__":
    import os

    # this code needs to have a feture where if there is no folder called fun at this path it will create one.
    folder_path = "C:\\Users\\juraj\\Desktop\\Code\\file_automations\\fun\\"

    def create(folder:str):
        solar = ["Mercury", "Venus", 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

        try:
            for i in solar:
                with open(folder + f"{i} - #{solar.index(i) + 1}.txt", "x"):
                    pass
        except FileExistsError:
            print("\nFile(s) already exists\n")

    def delete(folder:str):
        for file in os.listdir(folder):
            os.remove(folder + file)
    
    delete(folder_path)
    create(folder_path)