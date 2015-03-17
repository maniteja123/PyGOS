from github import Github
# import numpy as np

ACCESS_TOKEN = 'a06271f35dbcf494b65372db76618168d9010b3b'

USER = 'maniteja123'
REPO = 'scipy'
ORG  = 'scipy'

client = Github(ACCESS_TOKEN, per_page=100)

user = client.get_user(USER)
repo = user.get_repo(REPO)

## Code to get repo tags

tags = repo.get_tags()
for tag in tags:
    print tag.name

## Code to get repo watchers

watchers = repo.get_watchers()
'''
print 'Hook by karan'
count = 0
for watcher in watchers:
     print watcher.name
     count+=1
print count
'''
# Gives the list of stargazers.

## Code to get repos of a user
'''
repos = user.get_repos()

for repo in repos:
    print repo.name
'''

## Code to get repos, commits and stargazers
'''
repos = user.get_repos()
print "Repo","Commits","Stars"
print "-------------------"
for repo in repos:

    name = repo.name
    print name,
    commits = [ s for s in repo.get_commits() ]
    commits_length = len(commits)
    print commits_length,
    stargazers = [ s for s in repo.get_stargazers() ]
    stargazers_length = len(stargazers)

    print stargazers_length

    saveLine = name + ',' + str(commits_length) + ',' + str(stargazers_length) + '\n'
    print saveLine
    saveFile = open('newFile.csv','a')
    saveFile.write(saveLine)
    saveFile.close()
'''

organization = client.get_organization(ORG)

## Code to get repositories of the organization
'''
repos = organization.get_repos()
for repo in repos:
     print repo.name
'''

## Code to get members of organization
'''
repo_members = organization.get_members()

for member in repo_members:
    print member.name
'''

## Code to get commits in a repo
'''
commits = [ s for s in repo.get_commits() ]
print "Number of commits:", len(commits)
'''

## Code to get issues in a repo
'''
issues =  [ s for s in repo.get_issues() ]
print "Number of issues:", len(issues)
'''
