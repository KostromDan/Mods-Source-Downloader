import json
import os
import re
import shutil
import tkinter
from tkinter import filedialog

import requests
from bs4 import BeautifulSoup


# Instantiate the CurseForgeAPy client
def choose_dir():
    root = tkinter.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory()

    return file_path


def main():
    with open("correct_branch.json") as in_file:
        source_links = json.loads(in_file.read())
    mods = choose_dir()
    try:
        os.mkdir("raw_mods")
    except FileExistsError:
        pass
    for project in source_links['not_found']:
        id = project['id']
        r = requests.get(f"https://cflookup.com/{id}")
        soup = BeautifulSoup(r.text, 'lxml')
        file = soup.find_all('table', {
            'class': 'table table-striped table-dark text-start table-bordered caption-top'})[
            -1].find_all('td')[0].text.lower()
        mod_name_splited = re.split('-|_|\.', file)
        mod_name = mod_name_splited[0]
        possible_mods = []
        for mod in os.listdir(mods):
            if mod.lower() \
                    .replace('-', '') \
                    .replace('_', '') \
                    .replace('.', '').startswith(mod_name):
                possible_mods.append(mod)
        idx = 2
        while len(possible_mods) > 1:
            mod_name = ''.join(mod_name_splited)[0:idx]
            for mod in possible_mods:
                if not mod.lower() \
                        .replace('-', '') \
                        .replace('_', '') \
                        .replace('.', '').startswith(mod_name):
                    possible_mods.remove(mod)
            idx += 1
        if len(possible_mods) == 0:
            print('err', mod_name, file)
            continue
        mod = possible_mods[0]
        print(mod, mod_name)
        shutil.copyfile(os.path.join(mods, mod), os.path.join('raw_mods', mod))


if __name__ == "__main__":
    main()
