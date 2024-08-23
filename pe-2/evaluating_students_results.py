from os import strerror

class StudentsDataException(Exception):
        pass

class BadLine(StudentsDataException):
    def __init__(self, line, message="BadLine!!"):
        StudentsDataException.__init__(self, message)
        self.line = line

class FileEmpty(StudentsDataException):
    def __init__(self, line, message="FileEmpty!!"):
        StudentsDataException.__init__(self, message)
        self.line = line

scores = {}
tmplst = []

try:
    filename = input("Enter file name: ")
    f = open(filename, 'rt')
    line = f.readline()
    if not line:
        raise FileEmpty(line)
except FileEmpty as e:
    print(e, ':', e.line)
    exit()
except Exception as e:
    print("Cannot open file: ", strerror(e.errno))
    exit(e.errno)

try:
    while line:
        tmplst = line.replace('\n','').rsplit("\t",1)     
        if len(tmplst) != 2:
            raise BadLine(line)
        if tmplst[0] not in scores:
            scores.setdefault(tmplst[0], float(tmplst[1]))
        else:
            scores[tmplst[0]] += float(tmplst[1])
        line = f.readline()
    f.close()
except BadLine as e:
    print(e, ':', e.line)
    exit()
except Exception as e:
    print(tmplst)
    print(e)
    exit()

sorted_scores = sorted(scores)
for k in sorted_scores:
    print(k,scores[k],sep="\t")
