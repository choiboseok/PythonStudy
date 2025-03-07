import os
import shutil
# week1 하위의 파일(만) 모두 test_folder에 복사

dir = os.getcwd()
file_list = os.listdir(dir) # 파일 조회
for file_nm in file_list :
    path = os.path.join(dir, file_nm)
    if os.path.isfile(path):
        source = file_nm
        copy_dir = './test_folder'
        # 파일만
        copy_path = os.path.join(copy_dir, file_nm)
        shutil.copy(path, copy_path) # shutil.copy('원본경로', '저장경로')
