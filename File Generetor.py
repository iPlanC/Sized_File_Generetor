# UTF-8
import os

filesize = input("请输入要生成的文件大小(单位：b)\n>>>>")
char = input("要插入的字符\n>>>>")
file = input("请输入生成文件的路径\n>>>>")

if (file != "") :
    file = open(file, "w")
    print(file)
else :
    if (int(filesize) < 1024) :
        file = open(".\\" + str(int(filesize)) + "b.txt","w")
        print(str(int(filesize)) + "b")
    else :
        file = open(".\\" + str(int(filesize) / 1024) + "k.txt","w")
        print(str(int(filesize) / 1024) + "k")
    print(file)

for i in range(0, int(filesize)) :
    file.write(char)
file.close()
