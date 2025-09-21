if __name__ == "__main__":
    import os

    folder_path = "C:\\Users\\juraj\\Desktop\\Code\\file_automations\\fun\\"

    for file in os.listdir(folder_path):
        try:
            file_name = file.split(".")[0]
            p1, p2 = file_name.split(" - ")

            new_name = f"{p2[1:]} - {p1}.txt"
            os.rename(folder_path + file, folder_path + new_name)
        except FileExistsError:
            print(f"Unsuccessful Rename: {file}: Can't name a file a name that already exsits")
        except ValueError:
            print(f'Unsuccessful Rename: {file}: There must be a "-"')
        else:
            print(f"Successful Rename: {file}")

    # print("\n")