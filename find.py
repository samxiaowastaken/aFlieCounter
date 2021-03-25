import tkinter as tk
import os

def TXTRead_Writeline(filename):

    ms=open("files\\"+filename, encoding='utf-8')

    for line in ms.readlines():

        with open("f-"+filename+".doc" , "w") as mon:

            mon.write(line)

def TXTtoWord():
    for i in all:
        TXTRead_Writeline(i)
    win=tk.Tk()
    win.title("提示")
    tk.Label(win,text="转换完成！").pack()
    win.mainloop()

def cnki():
    text=["none"]
    ki=[]
    noki=[]
    for i in all:
        sen=open("files\\" + i, encoding='utf-8').read()
        for a in text:
            if sen=="none":
                pass
            elif a==sen:
                ki.append(sen)
                noki.append(i)
                break
            else:
                text.append(sen)
    l2 = []
    [l2.append(i) for i in ki if not i in l2]
    win = tk.Tk()
    win.title("提示")
    tk.Label(win, text="查重结束！").pack()
    cf=tk.LabelFrame(win,text="重复内容")
    cf.pack(expand=True,fill="both",anchor="s",padx=5,pady=5)
    for i in l2:
        tk.Label(cf,text=i).pack()
    nocf = tk.LabelFrame(win, text="重复文件")
    nocf.pack(expand=True, fill="both", anchor="s", padx=5, pady=5)
    for i in noki:
        tk.Label(nocf,text=i).pack()
    win.mainloop()


main = tk.Tk()
main.title("查看上传情况")
f1 = tk.Frame(main)
f1.pack(expand=True)
f2 = tk.LabelFrame(main,text="信息")
f2.pack(expand=True,fill="x",anchor="s",padx=5,pady=5)
f3=tk.LabelFrame(main,text="工具")
f3.pack(expand=True,fill="x",anchor="s",padx=5,pady=5)
tk.Button(f3,text="全部转doc",command=TXTtoWord).grid(row=0,column=0,padx=3)
tk.Button(f3,text="一键查重",command=cnki).grid(row=0,column=1,padx=3)
f4=tk.LabelFrame(main,text="信息")
f4.pack(expand=True,fill="x",anchor="s",padx=5,pady=5)
tk.Label(f4,text="bulid 05 by samxiaowastaken").pack()
tk.Label(f4,text="本作品采用知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议进行许可").pack()
# 初始化框架

all = list(os.walk("files"))[0][2]
# 查找所有文件s

row = 0
column = 0
alc=0
dnf = 0
err = 0
fin = 0
for i in all:
    alc=alc+1
    if (open("files\\" + i, "r",encoding='utf-8').read() == "none"):
        color = "RED"
        dnf = dnf + 1
    elif (len(open("files\\" + i, "r",encoding='utf-8').read()) < 4 or len(open("files\\" + i, "r",encoding='utf-8').read()) > 30):
        color = "YELLOW"
        err = err + 1
    else:
        color = "GREEN"
        fin = fin + 1
    tk.Button(f1, text=i, bg=color, command=lambda arg=i: check(arg)).grid(row=row, column=column, ipadx=30, ipady=10,
                                                                           padx=2, pady=2)
    row = row + 1
    if (row == 5):
        column = column + 1
        row = 0
tk.Label(f2,text="总人数："+str(alc)).pack()
tk.Label(f2,text="完成人数："+str(fin)).pack()
tk.Label(f2,text="错误人数："+str(err)).pack()
tk.Label(f2,text="未完成人数："+str(dnf)).pack()

# 按钮布局，显示状态

def check(file_name):
    l2 = tk.Tk()
    l2.title(file_name + "查询")
    txt = open("files\\" + file_name, "r",encoding='utf-8').read()
    tk.Label(l2, text="查询文件：" + file_name).pack(anchor="w")
    tk.Label(l2, text="内容：" + txt).pack(anchor="w")
    if (txt == "none"):
        tk.Label(l2, text="状态：未填写").pack(anchor="w")
    elif (len(txt) < 4 or len(txt) > 30):
        tk.Label(l2, text="状态：字数过多或过少").pack(anchor="w")
    else:
        tk.Label(l2, text="状态：已填写，正常").pack(anchor="w")
    l2.mainloop()



main.mainloop()
