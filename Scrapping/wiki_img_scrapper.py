import bs4
import requests as rq
import os

site = "https://en.wikipedia.org/wiki/Cat"

def save_html(r):
    with open("page.html", "a") as f:
        f.truncate(0)
        unicode_error_counter = 0

        for char in r.text:
            try:
                f.write(str(char))
            except UnicodeEncodeError:
                f.write("UnicodeError")
                unicode_error_counter += 1

        print(f"there were {unicode_error_counter} Unicode Errors")

def download(r):
    # get all the images
    broh = bs4.BeautifulSoup(r.text, "html.parser")
    imgs = broh.select("div > div > div > div > div > div > a > img")
    
    # make img folder if not there already
    folder_path = f"{os.getcwd()}\\images"
    os.makedirs(folder_path) if not os.path.isdir(folder_path) else None
        
    # download each one
    for img in imgs:
        imgURL = f'https:{img.attrs["src"]}'
        imgName = imgURL.split("/")[-1]
        imgPath = f'{folder_path}\\{imgName}'

        if not os.path.isfile(imgPath):
            r = rq.get(imgURL)
            r.raise_for_status()
            with open(imgPath, "wb") as f:
                f.write(r.content)
        else:
            print(f"{imgName} already exists")
        
if __name__ == "__main__":
    r = rq.get(site)
    r.raise_for_status()

    # save_html(r)
    download(r)