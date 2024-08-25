import os

def find_files(find_dir,find_target):
    dirs = os.listdir(find_dir)
    for dir in dirs:
        if dir:
            tmpdir = find_dir + "/" + dir
            if dir == find_target:
                print(tmpdir)
            if os.path.isdir(tmpdir):
                find_files(tmpdir,find_target)

find_dir = "./tree"
find_target = "python"
find_files(find_dir,find_target)
