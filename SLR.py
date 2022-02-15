#!/usr/bin/env python
# coding: utf-8

# In[13]:




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


def SLR():
    
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

#     print("FOLLOW", FOLLOW)

    
    
    

    table_dict={}
    for x in non_terminals:
        table_dict[x]={}
        for y in terminals:
            table_dict[x][y]=[]
        table_dict[x]['$']=[]

    for  productionss in productions_dict:
        temp=FIRST[productionss]
        
        for x in range(0,len(productions_dict[productionss])):
            if productions_dict[productionss][x][0]=='@':
                for flw  in  FOLLOW[productionss]:
                    table_dict[productionss][flw].append('@')
            elif productions_dict[productionss][x][0] in temp:
                table_dict[productionss][productions_dict[productionss][x][0]].append(productions_dict[productionss][x])
    
    
    item_num=1
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


    my_prod=productions
    productions=[]
    for prod in my_prod:
        prod=prod.replace('->','->.')
        productions.append(prod)

        
    productions_dict = {}
    for nT in non_terminals:
        productions_dict[nT] = []
        
    for prod in productions:
        productions_dict[prod[0]].append(prod)

    
    items=[]
    new_item=[]
    temp=starting_symbol+"'->."+starting_symbol
    new_item.append(temp)
    
    
    
    
    for  item in new_item:
        for i in range(0,len(item)):
            if item[i]=='.':
                if item[i+1] in non_terminals:
                    new_item.extend(productions_dict[item[i+1]])
                    
    items.append(new_item)
    new_item=[]
    for item_list  in items:
        for item in item_list:
            for x in range(0,len(item)):
                if item[-1]=='.':
                    break
                elif item[x]=='.':
                    new_item.append(item.replace('.'+item[x+1],item[x+1]+'.'))
                    
                    for  n_item in new_item:
                        for i in range(0,len(n_item)):
                            if n_item[-1]=='.':
                                pass
                            elif n_item[i]=='.':
                                if n_item[i+1] in non_terminals:
                                    new_item.extend(productions_dict[n_item[i+1]])
                            pass
                    if new_item in items:
                        new_item=[]
                        pass
                    else:
                        items.append(new_item)
                        new_item=[]
                    break
    
#     print(productions_dict)
    item_num=0
    reduce_list={}
    for reduce in productions_dict:
        reduce_list[item_num]=productions_dict[reduce]
        item_num+=1
    

    table={}
    item_num=0
    for item in items:
        table[item_num]=[]
        item_num+=1
    first_letter=[]
    for x in range(0,item_num):
        temp=items[x][0][3]
        first_letter.append(temp)
        
    all_ter_and_non=[]
    for ter in terminals:
        all_ter_and_non.append(ter)
    all_ter_and_non.append("$")
    for non_ter in non_terminals:
        all_ter_and_non.append(non_ter)
        
    count=0
    for item in items:
        for row in item:
#             print(row)
            for x in range(0,len(row)):
                if row[-1]=='.':
                    for reduce in reduce_list:
                        temp="['"+str(row)+"']"
                        reduce_list[reduce]=str(reduce_list[reduce]).replace(".","")
                        temp=temp.replace(".","")
                        
                        if row=="S'->S.":
                            for single_ter in terminals:
                                table[1].append("accept")
                            table[1].append("accept")
                            for single_noo_ter in non_terminals:
                                table[count].append(" ")
                            break
                        elif temp==reduce_list[reduce]:
                            my_reduce=[]
                            for single_follow in FOLLOW:
                                my_reduce=FOLLOW[row[0]]
                            for itm in all_ter_and_non:
                                if itm in my_reduce:
                                    table[count].append("r"+str(reduce+1))
                                else:
                                    table[count].append(" ")
#                             for single_ter in terminals:
                                
                                
#                                 table[count].append("r"+str(reduce+1))
#                             table[count].append("r"+str(reduce+1))
#                             for single_noo_ter in non_terminals:
#                                 table[count].append(" ")
                            break
                    break
                elif row[x]=='.':
                    shift_num=0
                    for shift_num in range(0,item_num):
                        if row[x+1] == first_letter[shift_num]:
                            break
                    for num in range(0,len(all_ter_and_non)):
                        if row[x+1]==all_ter_and_non[num]:
                            if row[x+1] in terminals:
                                table[count].append("s"+str(shift_num))
                            else:
                                table[count].append(str(shift_num))

                        else:
                            table[count].append(" ")
                            
        count+=1
    
#     print(table)
    new_table={}
    
    for row in table:
        new_table[row]=[]
        
    for row in table:
        if len(table[row])>len(all_ter_and_non):
            iter=len(table[row])/len(all_ter_and_non)
            temp=[]
            x_temp=[]
            for x in range (0,int(iter)):
                lwr_lm=x*len(all_ter_and_non)
                upr_lm=x*len(all_ter_and_non)+len(all_ter_and_non)
                temp.append(table[row][lwr_lm:upr_lm])
            for x in range(0,len(all_ter_and_non)):
                data=""
                for y in range(0, int(iter)):
                    data=data+temp[y][x]
                    data=data.replace("  "," ")
                x_temp.append(data)
            new_table[row]=x_temp
        else:
            new_table[row]=table[row]
            
    
               
    
    
    
    
                
    new_window =tk.Tk()

    canvas=tk.Canvas(new_window,width=800,height=700,bg='light gray')
    canvas.grid(columnspan=10,rowspan=30)
    new_window.title("SLR(1)")   
    r=0
    c=0
    count=0
    for item in items:
        tk.Label(new_window,text=str("I"+str(count)),font='Helvetica 18 bold').grid(column=1+c,row=2)
        r=0
        for item_list in item:
            tk.Label(new_window,text=item_list,font='Helvetica 18 bold').grid(column=1+c,row=4+r)
            r+=1
        c+=1
        count+=1
    r+=8
   
    c=1
    for item in all_ter_and_non:
        tk.Label(new_window,text=item,font='Helvetica 18 bold').grid(column=1+c,row=r+2)
        c+=1
    count=0
    for item_list in new_table:
        c=1
        
        tk.Label(new_window,text=str("I"+str(count)),font='Helvetica 18 bold').grid(column=1,row=4+r)
        for item in new_table[item_list]:
            
            tk.Label(new_window,text=item,font='Helvetica 18 bold').grid(column=1+c,row=4+r)
            c+=1
        r+=1
        count+=1
    
    count+=1
    
    
    
   
    new_window.mainloop()
    
    
    

    
    
    
    
mainwindow =tk.Tk()
w_width=w_height=600
canvas=tk.Canvas(mainwindow,width=w_width,height=250,bg='light gray')
canvas.grid(columnspan=3,rowspan=5)
mainwindow.title("Input Grammer")



# Enter list of productions
l_prod_lab=tk.Label(mainwindow,text="Enter List of Productions",font='Helvetica 13 bold',bg='light gray').grid(row=1,column=1)
l_prod=tk.Text(mainwindow,width=40,height=7,font='Helvetica 15 bold')
l_prod.grid(row=2,column=1)

procede_to_firstt_follow = tk.Button(mainwindow, text ="Get SLR(1) Table",font='Helvetica 13 bold',bg='dark gray', command = SLR)
procede_to_firstt_follow.grid(row=3,column=1)

mainwindow.mainloop()


# In[ ]:





# In[ ]:




