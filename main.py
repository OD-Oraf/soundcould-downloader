import subprocess


def download_mp3s(urls):
    download_path = "/home/od/Downloads"
    for url in urls:
        subprocess.run(["scdl", "--onlymp3", "-l", url, "--path", download_path])


def clear_file(urls):
    urls.truncate(0)



file = "urls.txt"
urls = open(file, "r+")
assert(len(urls.readlines())) > 0, "File is empty"
download_mp3s(urls)
clear_file(urls)
urls.close()
