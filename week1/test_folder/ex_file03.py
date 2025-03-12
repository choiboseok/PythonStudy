import os
import shutil
# week1 하위의 파일(만) 모두 test_folder에 복사

dir = os.getcwd()
file_list = os.listdir(dir)
for file_nm in file_list :
    if os.path.isfile(file_nm):
        source = file_nm
        copy_dir = './test_folder'

        copy_path = os.path.join(copy_dir, file_nm)
        shutil.copy(source, copy_path)