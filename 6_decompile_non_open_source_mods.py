import os
import tkinter
from tkinter import filedialog

from pretty_downloader import pretty_downloader


# Instantiate the CurseForgeAPy client
def choose_dir():
    root = tkinter.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory()

    return file_path


def main():
    pretty_downloader.download(
        'https://github.com/Vineflower/vineflower/releases/download/1.9.2/vineflower-1.9.2.jar')
    for mod in os.listdir('raw_mods'):
        os.system(
            fr'java -jar vineflower-1.9.2.jar -dgs=1 .\raw_mods\{mod} .\result\decompiled-{mod.replace(".jar", "")}')


if __name__ == "__main__":
    main()
