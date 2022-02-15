import tkinter as tk
import sys
sys.setrecursionlimit(10**6)
starting_symbol=""

def first(string,terminals,non_terminals,productions,productions_dict):
    #print("first({})".format(string))
    first_ = set()
    if string in non_terminals:
        alternatives = productions_dict[string]

        for alternative in alternatives:
            first_2 = first(alternative,terminals,non_terminals,productions,productions_dict)
            first_ = first_ |first_2

    elif string in terminals:
        first_ = {string}

    elif string=='' or string=='@':
        first_ = {'@'}

    else:
        first_2 = first(string[0],terminals,non_terminals,productions,productions_dict)
        if '@' in first_2:
            i = 1
            while '@' in first_2:
                #print("inside while")

                first_ = first_ | (first_2 - {'@'})
                #print('string[i:]=', string[i:])
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    break
                first_2 = first(string[i:],terminals,non_terminals,productions,productions_dict)
                first_ = first_ | first_2 - {'@'}
                i += 1
        else:
            first_ = first_ | first_2


    #print("returning for first({})".format(string),first_)
    return  first_


def follow(nT,terminals,non_terminals,productions,productions_dict):
    #print("inside follow({})".format(nT))
    follow_ = set()
    #print("FOLLOW", FOLLOW)
    prods = productions_dict.items()
    if nT==starting_symbol:
        follow_ = follow_ | {'$'}
    for nt,rhs in prods:
        #print("nt to rhs", nt,rhs)
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_ = follow_ | follow(nt,terminals,non_terminals,productions,productions_dict)
                    else:
                        follow_2 = first(following_str,terminals,non_terminals,productions,productions_dict)
                        if '@' in follow_2:
                            follow_ = follow_ | follow_2-{'@'}
                            follow_ = follow_ | follow(nt,terminals,non_terminals,productions,productions_dict)
                        else:
                            follow_ = follow_ | follow_2
    #print("returning for follow({})".format(nT),follow_)
    return follow_


# In[2]:



def first_and_follow():
    
    terminals = []

    non_terminals = []

    list_of_productions = l_prod.get("1.0","end-1c")
    list_of_productions=list_of_productions+"\n"

    productions = []
    Productions = ""

    for x in range(len(list_of_productions)):
        if list_of_productions[x]=="\n":
            if len(Productions)>0:
                productions.append(Productions)
                non_terminals.append(Productions[0])
                
                Productions=""
        else:
            Productions=Productions+list_of_productions[x]
            
    not_terminals=['-','>','/','@']
    for production in productions:
        for ter in production:
            if ter not in non_terminals and ter not in not_terminals :
                if ter not in terminals:
                    terminals.append(ter)
    
            
    starting_symbol=productions[0]
    starting_symbol=starting_symbol[0]
#     print(terminals)
#     print(non_terminals)
#     print(starting_symbol)
#     print(productions)
    

    productions_dict = {}
    for nT in non_terminals:
        productions_dict[nT] = []


    #print("productions_dict",productions_dict)

    for production in productions:
        nonterm_to_prod = production.split("->")
        alternatives = nonterm_to_prod[1].split("/")
        for alternative in alternatives:
            productions_dict[nonterm_to_prod[0]].append(alternative)

    #print("productions_dict",productions_dict)

    #print("nonterm_to_prod",nonterm_to_prod)
    #print("alternatives",alternatives)


    FIRST = {}
    FOLLOW = {}

    for non_terminal in non_terminals:
        FIRST[non_terminal] = set()

    for non_terminal in non_terminals:
        FOLLOW[non_terminal] = set()

    #print("FIRST",FIRST)

    for non_terminal in non_terminals:
        FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal,terminals,non_terminals,productions,productions_dict)

    #print("FIRST",FIRST)


    FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
    for non_terminal in non_terminals:
        FOLLOW[non_terminal] = FOLLOW[non_terminal] | follow(non_terminal,terminals,non_terminals,productions,productions_dict)

    #print("FOLLOW", FOLLOW)
    
    
    
    new_window =tk.Tk()

    new_window.attributes('-topmost',True)
    new_window.title("First And Follow")
    
    d=""
    data=[]
    head=tk.Label(new_window,text="{: ^20}{: ^20}{: ^20}".format('Non Terminals','First','Follow'),bg='dark gray',font='Helvetica 18 bold').grid(row=5)
    for non_terminal in non_terminals:
        d=d+"{: ^30}{: ^30}{: ^30}".format(non_terminal,str(FIRST[non_terminal]),str(FOLLOW[non_terminal]))
        d=d+"\n"

    body=tk.Label(new_window,text=d,bg='light gray',font='Helvetica 13 bold').grid(row=6)
    
    new_window.mainloop()
    
    
    
    
    


# In[3]:




def ins_command():
    ins.destroy()
#     mainwindow.attributes('-topmost',True)


    
    


# val=[]

#create window 
mainwindow =tk.Tk()
w_width=w_height=600
canvas=tk.Canvas(mainwindow,width=w_width,height=250,bg='light gray')
canvas.grid(columnspan=3,rowspan=5)
mainwindow.title("Input Grammer")



# Enter list of productions
l_prod_lab=tk.Label(mainwindow,text="Enter List of Productions",font='Helvetica 13 bold',bg='light gray').grid(row=1,column=1)
l_prod=tk.Text(mainwindow,width=40,height=7,font='Helvetica 15 bold')
l_prod.grid(row=2,column=1)

procede_to_firstt_follow = tk.Button(mainwindow, text ="Get First And Follow",font='Helvetica 13 bold',bg='dark gray', command = first_and_follow)
procede_to_firstt_follow.grid(row=3,column=1)


# close = tk.Button(mainwindow, text ="Close",font='Helvetica 13 bold',bg='dark gray', command = mainwindow.destroy)
# close.grid(row=3,column=2)




ins =tk.Tk()
span=3
canvas=tk.Canvas(ins,width=700,height=200,bg='light gray')
canvas.grid(columnspan=span,rowspan=7)
ins.title("Instruction")
ins.attributes('-topmost',True)
info_text="Important Instructions"
info1=tk.Label(ins,text=info_text,font='Helvetica 18',bg='light gray').grid(row=0,column=1)

info_text="{: ^30}{: ^30}".format("1.","write only  1 Terminal/Non-Termial/Productiioon rule in one line")
info1=tk.Label(ins,text=info_text,font='Helvetica 12',bg='light gray').grid(row=1,column=1)

info_text="{: ^30}{: ^30}".format("2","Use '->' after Non-Terminal to define Grammer Production Rule")
info2=tk.Label(ins,text=info_text,font='Helvetica 12',bg='light gray').grid(row=2,column=1)

info_text="{: ^30}{: ^10}".format("3","if have multiple Production for same No-Terminal seprate them using '/ '  ")
info3=tk.Label(ins,text=info_text,font='Helvetica 12',bg='light gray').grid(row=3,column=1)

but=tk.Button(ins,text="OK",font='Helvetica 12 bold',bg='dark gray',command=ins_command)
but.grid(row=4,column=1)

ins.mainloop()


mainwindow.mainloop()


# In[ ]:





# In[ ]:




