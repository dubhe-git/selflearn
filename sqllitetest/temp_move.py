import os
import shutil


def move_files(src_dir):
    for root, dirs, files in os.walk(src_dir, topdown=False):
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(src_dir, file)
            shutil.move(src_file, dst_file)
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))


src_dir = 'D:\\bluefilm'
move_files(src_dir)