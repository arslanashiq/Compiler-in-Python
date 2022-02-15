
import tkinter as tk
import sys


starting_symbol=""
def first_and_follow():
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
                            for single_ter in terminals:
                                table[count].append("r"+str(reduce+1))
                            table[count].append("r"+str(reduce+1))
                            for single_noo_ter in non_terminals:
                                table[count].append(" ")
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
    new_window.title("LR(1)")   
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

procede_to_firstt_follow = tk.Button(mainwindow, text ="Get LR(1) Table",font='Helvetica 13 bold',bg='dark gray', command = first_and_follow)
procede_to_firstt_follow.grid(row=3,column=1)

mainwindow.mainloop()

