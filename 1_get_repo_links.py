import json
import tkinter as tk
from tkinter import filedialog

import requests as requests
from bs4 import BeautifulSoup


# for page in range(1, 4):
#     browser.get(
#         f'https://legacy.curseforge.com/minecraft/modpacks/m-tech-1-19-2/files/all?page={page}')
#     table = browser.find_element(By.XPATH,
#                                  '/html/body/div[1]/main/div[1]/div[2]/section/div/div/div/section/div[2]/div/table/tbody').find_elements(
#         By.XPATH, "./tr")

def choose_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    return file_path


def main():
    selected_file = choose_file()
    print("Selected file:", selected_file)

    with open(selected_file) as in_file:
        manifest = json.loads(in_file.read())

    # browser = webdriver.Firefox()
    out = {
        'found': [],
        'not_found': []
    }

    for project in manifest["files"]:
        id = project["projectID"]
        file_id = project["fileID"]
        r = requests.get(f"https://cflookup.com/{id}")
        soup = BeautifulSoup(r.text, 'lxml')

        name_elem = soup.findAll('a', {'class': 'text-white'})[0]
        project_name = name_elem.text
        project_link = name_elem.get('href')

        elems = soup.findAll('a', {
            'class': 'text-white fw-bold text-decoration-none'})
        source = None
        issues = None
        for elem in elems:
            if 'Source' in elem.text:
                source = elem.get('href')
            if 'Issues' in elem.text:
                issues = elem.get('href')

        out_elem = {
            "id": id,
            "file_id": file_id,
            "name": project_name,
            "curseforge": project_link,
        }
        if (source is None and
                issues is not None and
                issues.startswith('https://github.com/')):

            source = issues.split('issues')[0]

            if "MacawsModsIssues" in source:
                source = None
            else:
                out_elem['source_from_issues'] = True
        out_elem['source'] = source

        print(project_name, project_link, source)

        if source is None:
            out['not_found'].append(out_elem)
        else:
            github_params = str(source).replace("https://github.com/",
                                                "").split("/")
            out_elem["github_username"] = github_params[0]
            out_elem["github_repo_name"] = github_params[1]
            out['found'].append(out_elem)
    with open("source_links.json", 'w') as out_f:
        out_f.write(json.dumps(out))


if __name__ == "__main__":
    main()
