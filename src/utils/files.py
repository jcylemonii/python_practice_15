import requests


def download_file(url: str, destination: str) -> None:

    print(f"Starting download from {url} to {destination}")

    response = requests.get(url, stream=True)
    response.raise_for_status()

    loaded_content = 0
    content_length = response.headers.get("Content-Length")

    if content_length is None:
        print("Content length is not provided")
        return

    content_length = int(content_length)

    with open(destination, "wb") as file:
        for chunk in response.iter_content(chunk_size=4096):

            file.write(chunk)

            loaded_content += len(chunk)

            done = round((loaded_content / content_length) * 100, 2)

            print(f"\rDownloading... {done}%", end="")
