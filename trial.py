from github import Github
g = Github("maniteja123", "MAni@1995")
for repo in g.get_user().get_repos():
    print repo.name
