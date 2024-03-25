from tkinter import filedialog
from tqdm import tqdm
from rules import rules
import time
import os
import tkinter

root = tkinter.Tk()
root.withdraw
file_paths = filedialog.askopenfilenames()
character = input('请输入要删去的内容：')
for file_path in tqdm(file_paths, desc='renaming:'):
    file_tuple = os.path.split(file_path)
    result = rules.rules.delete(character, file_tuple)
    dst = os.path.join(result[0], result[1])
    os.rename(src=file_path, dst=dst)
    time.sleep(0.05)


print("已完成重命名")
