from pathlib import Path
from filelib import File


def main():
    srcPath = Path(r"E:\Mipony")
    dstPath = Path(r"E:\books\ANDROID")
    files = File.get_files("pdf", "rar", "zip", "epub",
                           filename="Android", directory=srcPath)

    while not files.empty():
        File.copy_files(files.get(),dstPath)


if __name__ == "__main__":

    main()

