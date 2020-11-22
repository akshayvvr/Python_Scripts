#!/usr/bin/env python3
import os
import glob
from subprocess import Popen


def listdir_nohidden(path):
    return glob.glob(os.path.join(path, '*'))


listdir = listdir_nohidden(os.curdir)
print("\nFiltering only Directories in the Current Folder")
directories_in_curdir = filter(os.path.isdir, listdir)
# print(directories_in_curdir)

for number, repo in enumerate(sorted(directories_in_curdir)):
    try:
        print(f'\n\nPulling from {repo}')
        git_pull = Popen(f'git pull', shell=True, cwd=f'./{repo}').wait()

    except Exception as e:
        print(f'Exception Found at Repo {repo}')
        print(e)

print(f'All Done')
