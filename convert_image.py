from PIL import Image
from os import listdir
from os.path import splitext
import os
import shutil


target_directory = str(
    input('Which directory do you want to have the images converted?'))
change_dir_to = os.chdir("{}".format(target_directory))

old_extension = '.bmp'
new_extension = '.jpg'

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if 'BKP_OLD_IMAGES' not in root:
            dir = os.path.join(root, name)
            dir_new = dir.split('\\')
            filename = dir_new[-1]
            file, extension = splitext(filename)
            dir = target_directory+root[1:]
            if extension == old_extension:
                try:
                    print(dir+'\\'+file+extension)
                    im = Image.open(dir+'\\'+file+extension)
                    im.save(dir+'\\'+file+new_extension)
                    print('converted image: {}'.format(filename))
                except OSError as error:
                    print("It's not possible to convert the file {}.\nError code: {}".format(
                        filename, repr(error)))
                try:
                    if not os.path.isdir(dir + './' + 'BKP_OLD_IMAGES'):
                        # creates the backup directory
                        os.mkdir(dir+'./{}'.format('BKP_OLD_IMAGES'))
                        print('Created the {} directory'.format('BKP_OLD_IMAGES'))
                except:
                    print("It wasn't possible to create the dir")
                try:
                    destino = dir + '\\BKP_OLD_IMAGES\\'+file+extension
                    source = dir+'\\'+file+extension
                    shutil.move(source, destino)
                except:
                    print("It wasn't possible to move")
