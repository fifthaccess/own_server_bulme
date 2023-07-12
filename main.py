from git.repo import Repo
repository = Repo.init('test_folder.git', bare =True)
f = open("test_folder.git/myfiles.txt", "w")
f.close()
print(repository.untracked_files)