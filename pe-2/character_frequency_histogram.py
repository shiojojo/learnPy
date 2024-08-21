from os import strerror

filename = input("Enter file name: ")

histogram = {}
try:
    filedata = open(filename, 'rt')
    ch = filedata.read(1)
    while ch != '':
        if not ch.isalpha():
            ch = filedata.read(1)
            continue

        lowerch = ch.lower()
        if lowerch not in histogram:
            histogram.setdefault(lowerch, 1)
        else:
            histogram[lowerch] += 1
            
        ch = filedata.read(1)
    filedata.close()
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

sortedhistogram = sorted(histogram.keys())

for key in sortedhistogram:
    print(key, "->", histogram[key])


