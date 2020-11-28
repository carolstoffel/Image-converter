from PIL import Image
from os import listdir
from os.path import splitext
import os
import shutil


def main(path, backup, format):
    global target_directory
    global back
    global new_extension
    target_directory = path
    back = backup
    new_extension = format
    target_directory = manage_path(target_directory)
    change_dir_to = os.chdir("{}".format(target_directory))
    files(target_directory)


def manage_path(target_directory):
    tg = target_directory.replace('/', '\\')
    return tg


def files(target_directory):
    image_extension = ['.bmp', '.jpg', '.png', '.jpeg', '.gif']
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if 'BKP_OLD_IMAGES' not in root:
                dir = os.path.join(root, name)
                dir_new = dir.split('\\')
                filename = dir_new[-1]
                file, extension = splitext(filename)
                dir = target_directory + root[1:]
                if extension in image_extension:
                    convert(file, extension, dir, new_extension, filename)


def convert(file, extension, dir, new_extension, filename):
    if extension != new_extension:
        try:
            print(os.path.join(dir, file + extension))
            im = Image.open(os.path.join(dir, file + extension))
            im.save(os.path.join(dir, file + new_extension))
            print('converted image: {}'.format(filename))
        except OSError as error:
            print("It's not possible to convert the file {}.\nError code: {}".format(
                filename, repr(error)))
        if back == True:
            do_backup(dir, file, extension)
        elif back == False:
            do_exclusion(dir, file, extension)


def do_backup(dir, file, extension):
    try:
        if not os.path.isdir(os.path.join(dir, 'BKP_OLD_IMAGES')):
            # creates the backup directory
            os.mkdir(os.path.join(dir, 'BKP_OLD_IMAGES'))
            print('Created the {} directory'.format('BKP_OLD_IMAGES'))
    except:
        print("It wasn't possible to create the dir")
    try:
        dest = os.path.join(dir, 'BKP_OLD_IMAGES', file + extension)
        source = os.path.join(dir, file + extension)
        shutil.move(source, dest)
    except:
        print("It wasn't possible to move")


def do_exclusion(dir, file, extension):
    source = os.path.join(dir, file + extension)
    try:
        os.remove(source)
    except:
        print("It wasn't possible to delete")
