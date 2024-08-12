import os

def list_first_level_subfolders(startpath):
    for root, dirs, files in os.walk(startpath):
        # Calculate the current depth
        depth = root.replace(startpath, '').count(os.sep)
        if depth == 0:
            print('{}{}/'.format('', os.path.basename(root)))
            subindent = ' ' * 4
            for d in dirs:
                print('{}{}/'.format(subindent, d))
        # Stop the walk after the first level
        break

# Replace the path with your actual folder path
list_first_level_subfolders(r'C:\Users\MA\OneDrive - University of St Andrews\Project\PKG - AML-Cytomorphology_LMU')
