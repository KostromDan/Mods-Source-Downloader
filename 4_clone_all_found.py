import json
import os
import threading
import time


def clone(username, project_id, branch):
    os.system(
        f'cd result && git clone -b {branch} https://github.com/{username}/{project_id}')


def main():
    with open("correct_branch.json") as in_file:
        source_links = json.loads(in_file.read())

    try:
        os.mkdir("result")
    except FileExistsError:
        pass
    for project in source_links["found"]:
        t = threading.Thread(target=clone, args=(
            project['github_username'],
            project['github_repo_name'],
            project['selected_branch']))
        t.start()
        while threading.active_count() >= 20:
            time.sleep(0.1)


if __name__ == "__main__":
    main()
