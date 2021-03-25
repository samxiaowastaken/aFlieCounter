for i in range (1,42):
    if i/10<1:
        num="0"+str(i)
    else:
        num=str(i)
    f=open("files\\"+num+".txt","w+")
    f.write("none")
    f.close()
