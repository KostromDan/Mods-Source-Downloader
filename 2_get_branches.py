import json

from github import Github, UnknownObjectException

import tokens


def serialize_branch_workflow(obj):
    out = []
    for elem in obj:
        out.append(str(elem.name))
    return out


def main():
    with open("source_links.json") as in_file:
        source_links = json.loads(in_file.read())

    # Create a GitHub instance using the access token
    g = Github(tokens.GITHUB_TOKEN)

    repo_not_found = []

    for project in source_links["found"]:
        username = project["github_username"]
        repository_name = project["github_repo_name"]

        # Get the repository
        print(project["source"])
        try:
            repo = g.get_repo(f'{username}/{repository_name}')
            repo_url = repo.html_url
            print("Actual repository URL:", repo_url)

            # Get a list of branches
            branches = repo.get_branches()

            project["branches"] = serialize_branch_workflow(branches)

            project["source"] = repo_url
            github_params = str(repo_url).replace("https://github.com/",
                                                  "").split("/")
            project["github_username"] = github_params[0]
            project["github_repo_name"] = github_params[1]
        except UnknownObjectException:
            print("Exception: repo unavailable!")
            repo_not_found.append(project)
    for i in repo_not_found:
        source_links['found'].remove(i)
        source_links['not_found'].append(i)
    with open("branches.json", 'w') as out_f:
        out_f.write(json.dumps(source_links))


if __name__ == "__main__":
    main()
