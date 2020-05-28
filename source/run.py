# _*_coding : UTF-8 _*_
# Author    : 妙林
# Day time  : 2020/5/26  下午11:30
# File name : run.py
# Tools     : PyCharm

import os,time


class AddPostfix:
    """
    输入一个路径
    对路径内的文件进行操作
    可进行批量添加/清除/修改后缀
    """
    def __init__(self, path):
        """
        输入一个文件路径
        """
        self.path = path
    
    def ch_dir(self):
        """
        检查path是否为路径，是则切换至路径下
        """
        if os.path.isdir(path) is True:
            os.chdir(path)
            print(f"切换成功！当前工作目录为： {path}")
            return 'yes'
        else:
            print("请输入正确的目录路径")

    def list_dir(self):
        """
        列出当前路径下的所有文件
        """
        file_list = os.listdir(path)
        if len(file_list) == 0:
            print("文件夹为空")
        else:
            print(f"当前目录下的文件为： {file_list}")
            return file_list
    
    def add_postfix(self):
        """
        需要输入一个后缀，如：.mp3
        针对所有文件批量添加后缀
        """
        postfix = input("请输入想要添加的后缀：")
        file_list = self.list_dir()
        # 生成新的文件名列表
        for i in file_list:
            if os.path.isdir(i) is True:
                continue
            else:
                new_name = i + postfix
                os.rename(i, new_name)
                print(f"已将文件名{i}修改为{new_name}")
    
    def change_postfix(self):
        """
        需要两个参数
        如：想把目录下所有.doc文件更改为.txt
        第一个是要被批量替换的.doc
        第二个是批量替换后的.txt
        """
        file_list = self.list_dir()
        postfix = input("请输入将被替换的后缀：")
        new_postfix = input("请输入您要用来替换的后缀:")
        for i in file_list:
            if i.endswith(postfix) is True:
                file = os.path.splitext(i)
                new_name = file[0] + new_postfix
                os.rename(i, new_name)
                print(f"已将文件名{i}修改为{new_name}")
            else:
                continue
    
    def clear_postfix(self):
        """
        清空所有文件的后缀
        """
        file_list = self.list_dir()
        for i in file_list:
            if os.path.isdir(i) is True:
                continue
            else:
                file = os.path.splitext(i)
                new_name = file[0]
                os.rename(i, new_name)
                print(f"已将{new_name}后缀清除")

if __name__ == "__main__":
    path = input("请输入需要操作的文件夹路径：")
    lx_add = AddPostfix(path)
    if lx_add.ch_dir() == 'yes':
        lx_add.list_dir()
        while True:
            print("\n=================================\n\n"
                  "请输入需要序号进行操作：\n\n"
                  "1. 添加后缀(针对没有后缀的文件)\n\n"
                  "2. 清除后缀\n\n"
                  "3. 修改后缀\n\n"
                  "4. 查看当前目录下的文件\n\n"
                  "5. 退出\n\n"
                  "=================================")
            
            user_num = input(">>>")
            if user_num == '1':
                lx_add.add_postfix()
            elif user_num == '2':
                lx_add.clear_postfix()
            elif user_num == '3':
                lx_add.change_postfix()
            elif user_num == '4':
                lx_add.list_dir()
            elif user_num == '5':
                print("感谢您的使用,再会！")
                time.sleep(2)
                break
            else:
                input("输入有误,请输入正确的序号")

