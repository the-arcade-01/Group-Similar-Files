import os

current_path = os.getcwd()

# renaming function
# prev_name = 'folder/sample.txt'
# new_name = 'sample.txt'

# os.rename(prev_name,new_name)

# items = os.listdir()
# print(items)

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. '+ directory)

createFolder('./folder/')

