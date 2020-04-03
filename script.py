import os

current_path = os.getcwd()

# renaming function
# prev_name = 'folder/sample.txt'
# new_name = 'sample.txt'

# os.rename(prev_name,new_name)

items = os.listdir()
print(items)

# def createFolder(directory):
#     try:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#     except OSError:
#         print('Error: Creating directory. '+ directory)

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

