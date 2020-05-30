# _*_coding : UTF-8 _*_
# Author    : 妙林
# Day time  : 2020/5/26  下午11:30
# File name : run.py
# Tools     : PyCharm

import os,time


class DirHandle:
    '''
    对目录进行操作
    '''
    def input_path(self):
        """
        输入一个路径，如果输入的不是路径
        或是空文件夹都会让重新输入
        如果正确则会返回路径
        """
        while True:
            path = input("请输入需要操作的文件夹路径：")
            try:
                file_list = os.listdir(path)
                if len(file_list) == 0:
                    print("文件夹为空,请重新输入")
                    time.sleep(1)
                    continue
                elif os.path.isdir(path) is True:
                    break
            except:
                print("请输入正确的目录路径!")
                print("参考以下:")
                print(r"windows:C:\Users\lx\Desktop")
                print("linux:/home/name/file")
                time.sleep(1)
                continue
        return path
    
    def sys_list(self):
        print("\n=================================\n\n"
              "请输入序号选择要进行的操作：\n\n"
              "1. 选择当前文件夹\n\n"
              "2. 手动输入其他文件夹\n\n"
              "3. 退出\n\n"
              "=================================")
        
    def change_dir(self, path):
        os.chdir(path)
        print(f"切换成功！当前工作目录为： {path}")
        time.sleep(1)
  

    def in_dir(self):
        """
        选择当前路径
        """
        path = os.getcwd()
        os.chdir(path)
        print(f"已选择当前目录{path}")
        time.sleep(1)
        return path


class PostfixHandle:
    """
    对路径内的文件进行操作
    可进行批量添加/清除/修改后缀
    """
    
    def postfix_list(self):
        print("\n=================================\n\n"
              "请输入需要序号进行操作：\n\n"
              "1. 查看当前目录下的文件\n\n"
              "2. 添加后缀(针对没有后缀的文件)\n\n"
              "3. 清除后缀\n\n"
              "4. 修改后缀\n\n"
              "5. 返回主菜单\n\n"
              "=================================")
    
    def list_file(self, path):
        """
        列出当前路径下的所有文件
        """
        file_list = os.listdir(path)
        print(f"当前目录下的文件为： {file_list}")
        time.sleep(1)
        return file_list
    
    def add_postfix(self, file_list):
        """
        需要输入一个后缀，如：.mp3
        针对所有文件批量添加后缀
        """
        postfix = input("请输入想要添加的后缀：")
        # 生成新的文件名列表
        for i in file_list:
            if os.path.isdir(i) is True:
                continue
            else:
                new_name = i + postfix
                os.rename(i, new_name)
                print(f"已将文件名{i}修改为{new_name}")
                time.sleep(1)
    
    def change_postfix(self, file_list):
        """
        需要两个参数
        如：想把目录下所有.doc文件更改为.txt
        第一个是要被批量替换的.doc
        第二个是批量替换后的.txt
        """
        postfix = input("请输入将被替换的后缀：")
        new_postfix = input("请输入您要用来替换的后缀:")
        for i in file_list:
            if i.endswith(postfix) is True:
                file = os.path.splitext(i)
                new_name = file[0] + new_postfix
                os.rename(i, new_name)
                print(f"已将文件名{i}修改为{new_name}")
                time.sleep(1)
            else:
                continue
    
    def clear_postfix(self, file_list):
        """
        清空所有文件的后缀
        """
        for i in file_list:
            if os.path.isdir(i) is True:
                continue
            else:
                file = os.path.splitext(i)
                new_name = file[0]
                os.rename(i, new_name)
                print(f"已将{new_name}后缀清除")
                time.sleep(1)
                
def run(path):
    """
    进行后缀操作的函数，根据输入序号采取相应操作
    """
    postfix_handle = PostfixHandle()
    file_list = postfix_handle.list_file(path)
    while True:
        postfix_handle.postfix_list()
        user_num = input(">>>")
        if user_num == '1':
            postfix_handle.list_file(path)
        elif user_num == '2':
            postfix_handle.add_postfix(file_list)
        elif user_num == '3':
            postfix_handle.clear_postfix(file_list)
        elif user_num == '4':
            postfix_handle.change_postfix(file_list)
        elif user_num == '5':
            break
        else:
            input("输入有误,请输入正确的序号")
            continue
    

if __name__ == "__main__":
    dir_handle = DirHandle()
    while True:
        dir_handle.sys_list()
        num = input(">>>")
        if num == '3':
            print("感谢您的使用,再会！")
            time.sleep(1)
            break
        elif num == '2':
            path = dir_handle.input_path()
            dir_handle.change_dir(path)
            run(path)
            time.sleep(1)
        elif num == '1':
            path = dir_handle.in_dir()
            run(path)
        else:
            print("请输入正确的序号!")
            time.sleep(1)
            continue
            
    
    
    
    
    
    
    
    
    
    
    
    

