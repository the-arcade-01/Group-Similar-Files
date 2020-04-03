import os

current_path = os.getcwd()

items = os.listdir()

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. '+ directory)

# createFolder('./folder/')

extension_dict = {}

for item in items:
    filename_list = item.split('.')
    ext = filename_list[-1]
    del filename_list[-1]
    filename = ''.join(filename_list)
    if ext in extension_dict:
        extension_dict[ext].append(filename)
    else:
        extension_dict[ext] = [filename]

print(extension_dict)

for item in extension_dict:
    folder_name = f'{item}-Folder'
    files = extension_dict[item]
    directory = f'./{folder_name}/'
    createFolder(directory)
    for name in files:
        prev_name = f'{name}.{item}'
        new_name = f'{folder_name}/{name}.{item}'
        os.rename(prev_name,new_name)
