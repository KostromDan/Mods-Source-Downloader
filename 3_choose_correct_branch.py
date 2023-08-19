import json
from pprint import pprint

accepted_options = [
    "1.19.2",
    "1902",
    "mc1.19.2/dev",
    "multiloader/1.19.2",
    "multiloader/1.19.x",
    'Forge-1.19.2',
    "1.19.2/0.5.1-dev",
    '1.19.2/dev',
    '1.19.2-forge',
    '1.19.2-Forge',
    'dev/1.19.2',
    'TB-1.19.x-2.x.x',

    '1.19.X',
    "1.19.x",
    '1.19.X',

    "multiloader/1.19",
    "1.19/dev",
    "mc1.19/dev",
    "1.19",
    '1.19/forge',
    '1.19-forge',
    'Integrated_Stronghold_1.19',
    'architectury/1.19',

    '1.19.1-forge',

    "main",
    "master",

    "4.x",
    'v8',
    'architectury',
    'forge',
    'multi-loader',
    'all-in-one',
]


def main():
    with open("branches.json") as in_file:
        source_links = json.loads(in_file.read())

    for project in source_links["found"]:
        branches: list = project["branches"].copy()
        selected = False
        for option in accepted_options:
            for branch in branches:
                if ("fabric" in branch):
                    continue
                if option == branch:
                    project["selected_branch"] = branch
                    selected = True
                    break
            if selected:
                break
        if not selected:
            print(project['name'])
            print(project['source'])
            print(f"Can't select branch from:")
            pprint(branches)
            print(f"Add one of these to accepted_options")

    with open("correct_branch.json", 'w') as out_f:
        out_f.write(json.dumps(source_links))


if __name__ == "__main__":
    main()
