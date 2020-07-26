import os
import  shutil
kmodl = open(input('Enter kmodl absolute path: '))
ugcs = []
for line in kmodl:
    parts = line.split('|')
    ugcs += [parts[4].strip('ugc_').rstrip('.mod')]


def copyandreplacedir(source, dest):
    for root, dirs, files in os.walk(source):
        for file in files:
            destpath = root.replace(source, dest) #creates destination path from root to preserve relative paths
            if not os.path.isdir(destpath): #if a path does not exist it is made
                os.makedirs(destpath)
            shutil.copyfile(os.path.join(root, file), os.path.join(destpath, file))


src = input('Input absolute src path: ')
if src.endswith(os.sep): #adds kwarg for UGC for subfolder and appropriate character separator
    src = src.rstrip() + '{ugc}'
else:
    src = src.rstrip() + os.sep + '{ugc}'

    
dest = input('Input absolute dest path: ')
dest = dest.rstrip(os.sep) #removes trailing os path separators for uniformity


for ugc in ugcs:
    try:
        copyandreplacedir(src.format(ugc = ugc), dest)
    except Exception as exception:
        print(exception, ugc)
print('Done')
