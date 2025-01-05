class EmptyFileError(Exception):
    pass


filename = ["filename1", "nonExistent", "emptyFile", "myfile2"]
for file in filename:
    try:
        f = open(file, 'r')
        line = f.readline()
        if line == "":
            f.close()
            raise EmptyFileError("%s: is empty" % file)
    except IOError as error:
        print("%s: could not be opened: %s" % (file, error.strerror))
    except EmptyFileError as error:
        print(error)
    else:
        print("%s: %s" % (file, f.readline()))
    finally:
        print("Done processing", file)

filename = "myfile.txt"
with open(filename, "r") as f:
    for line in f:
        print(f)

filename = "myfile.txt"
try:
    f = open(filename, "r")
    for line in f:
        print(f)
except Exception as e:
    raise e
finally:
    f.close()
