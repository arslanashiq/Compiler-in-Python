import re
import tkinter as tk
import sys
sys.setrecursionlimit(10**6)


my_re=""
my_str=""
def regular_expression():
    my_re=R_E.get("1.0","end-1c")
    my_re="^"+my_re+"$"
    my_str=STR.get("1.0","end-1c")
    
    if len(my_str)>0 and len(my_re)>0:
        match=re.match(my_re,my_str)
        if match:
            Result=tk.Label(mainwindow,text="String Accepted",font='Helvetica 13 bold',bg='light gray').grid(row=8,column=1)
        else:
            Result=tk.Label(mainwindow,text="String Rejected",font='Helvetica 13 bold',bg='light gray').grid(row=8,column=1)
    
        

mainwindow =tk.Tk()
w_width=w_height=600
canvas=tk.Canvas(mainwindow,width=w_width,height=250,bg='light gray')
canvas.grid(rowspan=8,columnspan=3)
mainwindow.title("Compiler")
l1=tk.Label(mainwindow,text="Enter Regular Expression",font='Helvetica 13 bold',bg='light gray').grid(row=1,column=1)
R_E=tk.Text(mainwindow,width=50,height=2,font='Helvetica 15 bold')
R_E.grid(row=2,column=1)

l2=tk.Label(mainwindow,text="Pass String",font='Helvetica 13 bold',bg='light gray').grid(row=4,column=1)
STR=tk.Text(mainwindow,width=50,height=4,font='Helvetica 15 bold')
STR.grid(row=5,column=1)


r_e=tk.Button(mainwindow,text="Execute",font='Helvetica 13 bold',bg='dark gray',command=regular_expression).grid(row=6,column=1)


mainwindow.mainloop()


# In[ ]:





# In[ ]:




