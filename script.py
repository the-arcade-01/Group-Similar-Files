import os

# to get the current directory path
current_path = os.getcwd()

# stores the items present in the directory
directory_items = os.listdir()

# function for creating a folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. '+ directory)

# stores file name in respective extension
extension_dict = {}
# Example :
#  extension_dict = {'txt': [ 'sample', 'sample1'],'cpp': ['code1', 'code2']}

# adds data into extension_dict
for item in directory_items:
    filename_list = item.split('.')
    ext = filename_list[-1]
    del filename_list[-1]
    filename = ''.join(filename_list)
    if ext in extension_dict:
        extension_dict[ext].append(filename)
    else:
        extension_dict[ext] = [filename]

# moves the files in their respective folders
for item in extension_dict:
    folder_name = f'{item}-Folder'
    files = extension_dict[item]
    directory = f'./{folder_name}/'
    createFolder(directory)
    for name in files:
        prev_name = f'{name}.{item}'
        new_name = f'{folder_name}/{name}.{item}'
        os.rename(prev_name,new_name)
