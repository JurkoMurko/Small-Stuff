if __name__ == "__main__":
    import os

    folder_name = "fun"
    folder_path = f"{os.getcwd()}\{folder_name}"
    if not os.path.isdir(folder_path):
        os.mkdir("fun")

    def create(folder = folder_path):
        solar = ["Mercury", "Venus", 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

        try:
            for i in solar:
                with open(f"{folder}\{i} - #{solar.index(i) + 1}.txt", "x"):
                    pass
        except FileExistsError:
            print("\nFile(s) already exists\n")

    def delete(folder = folder_path):
        for file in os.listdir(folder):
            os.remove(f"{folder}\{file}")
    
    def reset(delete_enabled = False, folder = folder_path):
        if delete_enabled == True:
            delete(folder)
        create(folder)

    def rename(folder = folder_path):
        for file in os.listdir(folder):
            try:
                file_name = file.split(".")[0]
                p1, p2 = file_name.split(" - ")

                new_name = f"{p2[1:]} - {p1}.txt"
                os.rename(f"{folder}\{file}", f"{folder}\{new_name}")
            except FileExistsError:
                print(f"Unsuccessful Rename: {file}: Can't name a file a name that already exsits")
            except ValueError:
                print(f'Unsuccessful Rename: {file}: There must be a "-"')
            else:
                print(f"Successful Rename: {file}")