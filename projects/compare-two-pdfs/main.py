# Compare two pdfs

import hashlib

def hash_file(fileName1, fileName2):
    h1 = hashlib.sha1() #hash of the file
    h2 = hashlib.sha1()

    with open(fileName1, "rb") as file: # rb - read binary 
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)

    with open(fileName2, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)

        return h1.hexdigest(), h2.hexdigest()

f1, f2 = hash_file("file1.pdf", "file2.pdf")

if(f1 != f2):
    print("These files are not identical.")
else:
    print("These files are identical.")