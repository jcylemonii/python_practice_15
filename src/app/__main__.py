from utils.files import download_file
from os.path import exists

def main():

    resource = "https://storage.yandexcloud.net/academy.ai/A_Z_Handwritten_Data.csv"
    destination = "./src/datasets/A_Z_Handwritten_Data.csv"

    if exists(destination) is False:
        print(f"The file does not exist at {destination}")
        download_file(resource, destination)
    else:
        print(f"The file already exists at {destination}")

if __name__ == "__main__":
    main()