# PATHS

r"""
Use strings to create file paths
\ character needs to be escaped ie 'c:\\spam\\eggs.png'
use a raw string to avoid escaping r'c:\spam\eggs.png'
 Use the os module for different file things
 os.getcwd() returns the current working directory
 os.chdir(path here) changes the working directory
Absolute file path always contains the entire path ie c:\\folder1\\spam.png
relative file paths will just use the cwd ie 'folder\\spam.png'
use . to mean this directory, .. means parent folder
os.path.abspath('spam.png') returns absolut path of what you pass it
os.path.isabs() checks if a path is absolue
os.path.relpath(path1,path2) gives you the relative path to path 1 from path 2
os.path.dirname() retrieves the directory of your path
os.path.basename() retrieves the last part of the path, after the last \\'s
os.path.exists() Checks whether a file path actually exists or not
os.path.isfile() Checks if the path is a file
os.path.isdir() Checks if the path is a directory
os.path.getsize() returns the size in bytes as an integer of the file passed
os.listdir() returns a list of strings with all filenames in that directory
os.makedirs() creates the new path specified ie. c:\\spam\\bacon\\eggs
"""
import os


def ttlfilesize():
    totalSize = 0
    for filename in os.listdir(
        "c:\\users\\owner\\documents\\programming\\python\\practice"
    ):
        if not os.path.isfile(
            os.path.join(
                "c:\\users\\owner\\documents\\programming\\python\\practice", filename
            )
        ):
            continue
        totalSize = totalSize + os.path.getsize(
            os.path.join(
                "c:\\users\\owner\\documents\\programming\\python\\practice", filename
            )
        )
    print(totalSize)


ttlfilesize()

# READING AND WRITING PLAIN TEXT FILES

"""
open(file) opens a file in plain text read mode. Returns a file object
methods can be used on that file object ie open(file).read() || .close()
open(file,'w') can open in write mode which overwrites the file
open(file,'a') opens in append mode, adding new data to the bottom of the file
.write(string) allows you to write to a file object
\n new line isn't automatically added at the end of write, need to manually add
"""

hellofile = open("hello.txt")
hellofile.read()
hellofile.close()
content = hellofile.read()
print(content)
hellofile.readlines()  # Returns a list of strings

"""
use shelve module to create files to store lists, variables, dictionaries, etc
shelfFile = shelve.open(file) creates a shelf file in the cwd
shelfFile['cats'] = ['cat1','cat2'] Creates a dictionary like object in the shelf file
shelfFile.close() Closess the shelf file
shelfFile = Shelve.open(file) opens the shelf file at file location
shelfFile['cats'] returns ['cat1','cat2']
Can conveniently store variables, lists, etc this way in a file
Shelf files are similar to dictionaries
shelfFile.keys() returns a list like value for all values inside shelf
ShelfFile.Values() Returns all the values in the shelf
Stores all the content in a binary file instead of a plain text file like open
"""

# COPYING AND RENAMING FILES
"""
shutil package can manage files
shutil.copy('filepath','destination path') Copys the file to the destination
Specifying a file name will copy and rename the file
shutil.copy('c:\\spam.txt', 'c:\\delicious\\bacon.txt') Will copy spam to the delicious folder and rename it bacon
shutil.copytree(directory, destination) Will copy an entire folder and contents to new location
shutil.move(file,destination) will move the file
To rename, move the file to the same destination with a new name
shutil.move('c:\\spam.txt','c:\\eggs.txt')
"""


# DELETING FILES

"""
Files can be deleted using the following commands:
os.rmdir(Directory) To delete an empty folder2
os.unlink(File) To delete a file
shutil.rmtree(Path) To delete an entire folder tree and its contents
Be sure to always do a dry run of deleting
This can be done by writing the code to delete, then commenting out the delete command and inserting print
Example:
for filename in os.listdir():
	if filename.endswith('.rxt'):
		#os.unlink(filename)
		print(filename)
Use this to know exactly what you are deleting before you delete it
All these deletions are PERMENANT delete
Use the send2trash module to delete to the recycle bin
send2trash.send2trash(file)
"""


# Walking a directory tree

"""
Use os.walk to get a foldername, subfolders, and filenames in a directory
Returns the folder name, a list of subfolders, and a list of filenames
ex:
for FolderName, subfolders, filenames in os.walk('c:\\'):
    print(f'The folder is {FolderName})
    print(f'The subfolders in {FolderName} are: ' + str(subfolders))
    print(f'The filenames in {FolderName} are: ' + str(filenames))
    print()


"""