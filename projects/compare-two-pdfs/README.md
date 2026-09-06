# Compare two pdfs

## About the project
To check the contents of two pdf files, if they have identical content or not. 

## Concepts Involved
- hashlib
- Functions
- File processing

## Algorithm
1. Declare a function with 2 arguments which is for file.
2. Declare two objects for hashlib.sha1()
3. Open files
4. Read the file by breaking the line into smaller chunks
5. Now return both file such as h1.hexdigest() which is of 160 bits.
6. Use hash_file() function to store the hash of a file.
7. Compare and generate appropriate message.


## Run
`cd python-mini-projects/projects/compare-two-pdfs`

`python main.py`