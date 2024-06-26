from tkinter import filedialog
from tqdm import tqdm
from rules import rules
import time
import os
import tkinter


print("文件批量重命名")
print("请选择使用模式：")
mode = input("""[1]文件重命名
[2]创建文件""")

if mode == "1":
    root = tkinter.Tk()
    root.withdraw()
    while True:
        file_paths = filedialog.askopenfilenames()
        if not file_paths:
            print("您没有选择文件，请重新选择！")
            continue
        break
    print("请选择重命名规则")
    rename_rule = input("""[1]删除指定字符
[2]添加指定内容""")
    if rename_rule == "1":
        character = input('请输入要删去的内容：')
        for file_path in tqdm(file_paths, desc='renaming:'):
            file_tuple = os.path.split(file_path)
            result = rules.rules.delete(character, file_tuple)
            dst = os.path.join(result[0], result[1])
            try:
                os.rename(src=file_path, dst=dst)
                time.sleep(0.02)
            finally:
                pass
    elif rename_rule == "2":
        add_rule = input("""[1]在文件名后加序号
[2]在文件名前加序号
[3]在文件名后加自定义内容
[4]在文件名前加自定义内容
""")
        if add_rule == "1" or add_rule == "2":
            for index, file_path in tqdm(enumerate(file_paths), desc='renaming:'):
                file_tuple = os.path.split(file_path)
                if add_rule == "1":
                    result = rules.rules.addNumberBehind(
                        number=index, file=file_tuple)
                elif add_rule == "2":
                    result = rules.rules.addNumberAhead(
                        number=index, file=file_tuple)
                dst = os.path.join(result[0], result[1])
                os.rename(src=file_path, dst=dst)
                time.sleep(0.02)
        elif add_rule == "3" or add_rule == "4":
            character = input("请输入要添加的内容：")
            for file_path in tqdm(file_paths, desc='renaming:'):
                if add_rule == "3":
                    file_tuple = os.path.split(file_path)
                    result = rules.rules.addBehind(
                        character=character, file=file_tuple)
                elif add_rule == "4":
                    file_tuple = os.path.split(file_path)
                    result = rules.rules.addAhead(
                        character=character, file=file_tuple)
                dst = os.path.join(result[0], result[1])
                os.rename(src=file_path, dst=dst)
                time.sleep(0.02)


print("已完成重命名")
