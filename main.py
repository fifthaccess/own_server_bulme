from git.repo import Repo
repository = Repo.init('/var/python_projects/test_folder.git', bare =True)
f = open("myfiles.txt", "x")
f.close()
print(repository.untracked_files)