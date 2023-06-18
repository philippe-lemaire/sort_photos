from PIL import Image
import os
import shutil

# set the source path of the pictures
folder = "photos"

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

def main():
    for img in os.listdir(folder):
        current_path = f"{folder}/{img}"
        date = get_date_taken(current_path)
        year = date[:4]
        month = date[5:7]
        os.makedirs(f"{folder}/{year}/{month}", exist_ok=True)
        new_path = f"{folder}/{year}/{month}/{img}"
        os.replace(current_path, new_path)

if __name__ == '__main__':
    main()
