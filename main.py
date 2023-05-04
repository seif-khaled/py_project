import tkinter as tk 
import re
import os.path
import sys
from tkinter.ttk import * 
# from playsound import playsound
from pygame import mixer
# import tkfont
def replace_item_info(elements_to_replaced,splitted_senetence,indices):
    x=[]
    # while
    for i in range(len(splitted_senetence)):
        if i==len(splitted_senetence)-1:
            continue
        else:
            splitted_senetence[i]+=","
    for i in range(len(splitted_senetence)):
        if i in indices:
            x.insert(i,0)
        else:
            x.insert(i,splitted_senetence[i])
    print(elements_to_replaced,splitted_senetence,indices)
    print(x)
    zeros_left=x.count(0)
    index_of_item_replaced=0
    index_in_main_list=0
    while(zeros_left!=0):
        
        if x[index_in_main_list]==0:
            x[index_in_main_list]=elements_to_replaced[index_of_item_replaced]
            index_of_item_replaced+=1
            index_in_main_list+=1
        elif x[index_in_main_list]!=0:
            index_in_main_list+=1
        # x[indices[index_of_item_replaced]]=elements_to_replaced[indices[index_of_item_replaced]]
        # index_of_item_replaced+=1
        zeros_left=x.count(0)
    # for i in range(len(x)):
    #     if x[i]==0: 
    #         x[i]=elements_to_replaced[indices[index_of_item_replaced]]
    #         index_of_item_replaced+=1
    print("".join(x))
    return "".join(x)
    
def check_item_name(x):
    string=""
    found_comma=False
    found_deleitmer=False
    index_to_continue_from=-1
    while(found_comma==False):
        # print("hi")
        if(found_deleitmer==False):
                
            for i in range(len(x)):
                # print(string)
                if string=="item name=":
                    found_deleitmer=True
                    index_to_continue_from=i
                    string=""
                    break
                    
                else:
                    string+=x[i]
        else:
            for j in range(index_to_continue_from,len(x)):
                if x[j]==",":
                    found_comma=True
                    break 
                else:
                    # print(string,"\n")
                    string+=x[j]
    return string    
class retail_store_inventory:
    def __init__(self,filepath):
        self.db=filepath
        
    def main_loop(self):
        mixer.init()
        mixer.music.load("The-Godfather-Theme-Song.mp3")
        mixer.music.play(-1)
        self.window=tk.Tk()
        self.window.geometry("1280x720")
        self.window.iconbitmap("shop-512.ico")
        self.window.title("Shop")
        self.item_name = tk.Label(text="ITEM NAME")
        # self.background=tk.PhotoImage(file = "market-supermarket-grocery-store-shop.jpg")
        # self.bg_label = tk.Label( self.window, image = self.background)
        # self.bg_label.place(x = 0,y = 0)
        self.item_name.grid(row=0,columnspan=2,padx=5,pady=5)
        self.item_name_entry=tk.Entry(self.window,relief='sunken',width=50)
        self.item_name_entry.grid(row=0,column=2,columnspan=3)
        self.DESCRIPTION = tk.Label(text="DESCRIPTION")
        self.Label_s=tk.Label(text="HoRuS",fg="red",font=("Cambria",10,'bold'))
        self.Label_s.grid(row=18,column=0,rowspan=5,padx=25,pady=25)
        self.DESCRIPTION.grid(row=1,columnspan=2,padx=5,pady=5)
        self.DESCRIPTION_entry=tk.Entry(self.window,relief='sunken',width=50)
        self.DESCRIPTION_entry.grid(row=1,column=2,columnspan=3)
        self.PRICE_PER_ITEM = tk.Label(text="PRICE PER ITEM")
        self.PRICE_PER_ITEM.grid(row=2,columnspan=2,padx=5,pady=5)
        self.PRICE_PER_ITEM_entry=tk.Entry(self.window,relief='sunken',width=50)
        self.PRICE_PER_ITEM_entry.grid(row=2,column=2,columnspan=3)
        self.QUANTITY = tk.Label(text="QUANTITY")
        self.QUANTITY.grid(row=3,columnspan=2,padx=5,pady=5)
        self.QUANTITY_entry=tk.Entry(self.window,relief='sunken',width=50)
        self.QUANTITY_entry.grid(row=3,column=2,columnspan=3)
        self.button=tk.Button(self.window,text= "ADD ITEM", command= self.add_items,width=15,height=4,bg="blue",font=('Times New Roman',10,"bold"))
        self.button.grid(row=5,column=0,columnspan=2,padx=7,pady=7)
        self.label=tk.Label(text="",font=('Times New Roman',17,'bold'))
        self.label.grid(row=7,column=4,columnspan=3,padx=15,pady=15)
        self.button_2=tk.Button(self.window,text= "UPD ITEM", command= self.update_items,width=15,height=4,bg="green",font=('Times New Roman',10,"bold"))
        self.button_2.grid(row=5,column=1,columnspan=2,padx=7,pady=7)
        self.item_name_remove=tk.Label(text="enter item name to be removed")
        self.item_name_remove.grid(row=8,column=1 ,padx=5,pady=5)
        self.item_name_entry_deleted=tk.Entry(self.window,relief='sunken',width=50)
        self.item_name_entry_deleted.grid(row=8,column=2)
        self.item_name_B_deleted=tk.Button(self.window,text= "DEL ITEM", command= self.remove_item,width=20,height=4,bg="red",font=('Times New Roman',10,"bold"))
        self.item_name_B_deleted.grid(row=8,column=4,padx=15,pady=15)
        self.quit_b=tk.Button(self.window,text= "EXIT", command= self.exit_p,width=20,height=4,bg="cyan",font=('Times New Roman',10,"bold"))
        self.quit_b.grid(row=9,column=1,padx=15,pady=15)
        self.label_2=tk.Label(text="",font=('Times New Roman',17,'bold'))
        self.label_2.grid(row=10,column=2,columnspan=3,padx=15,pady=15)
        self.quit_b.grid(row=9,column=1,padx=15,pady=15)
        self.show_items_B=tk.Button(self.window,text= "Show Items", command= self.view_item,width=20,height=4,bg="cyan",font=('Times New Roman',10,"bold"))
        self.show_items_B.grid(row=9,column=2,padx=15,pady=15)
        # playsound('The-Godfather-Theme-Song.mp3')
        self.window.mainloop()
    
    def add_items(self):
        self.entry_1_val=self.item_name_entry.get()
        self.entry_2_val=self.DESCRIPTION_entry.get()
        self.entry_3_val=self.PRICE_PER_ITEM_entry.get()
        self.entry_4_val=self.QUANTITY_entry.get()
        if os.path.isfile(self.db):
            # print("iam here")
            if ((len(self.entry_1_val)!=0) and (len(self.entry_2_val)!=0) and (len(self.entry_3_val)!=0) and(len(self.entry_4_val)!=0)):
                    if((self.entry_2_val != self.entry_1_val)  and (self.entry_3_val != self.entry_1_val)  and (self.entry_4_val != self.entry_1_val)):
                        if((self.entry_3_val != self.entry_2_val) and (self.entry_4_val != self.entry_2_val)):
                             self.f_read=open(self.db,'r')
                             self.LIst=self.f_read.readlines()
                             self.f_read.close()
                             self.flag=0
                             for i in range(len(self.LIst)):
                                 if(self.LIst[i]=="\n"):
                                     continue
                                 item_name=check_item_name(self.LIst[i])
                                 if(self.entry_1_val==item_name):
                                     self.flag=1
                                     self.label.config(text="cannot add this item since it already exists ",fg='green',font=('Times New Roman',15,'bold'))
                                     self.label.grid(row=7,column=5,columnspan=3,padx=15,pady=15)
                                     break
                                     
                             if(self.flag==0):
                                self.file=open(self.db,'a')
                                self.file.write("item name="+ self.entry_1_val+','+"Description="+self.entry_2_val+','+"Price/item="+self.entry_3_val+','+"Quantity="+self.entry_4_val)
                                self.file.write("\n")
                                self.file.close()
                                self.label.config(text="added successfully",fg='green',font=('Times New Roman',15,'bold'))
                                self.label.grid(row=7,column=5,columnspan=3,padx=15,pady=15)
                        else:
                            self.label.config(text="cannot write description text in quantity field or price field ",fg='red',font=('Times New Roman',15,'bold'))
                            self.label.grid(row=7,column=5,columnspan=3,padx=15,pady=15)
                    else:
                        self.label.config(text="item name cannot be written multiple times in other fields",fg='red',font=('Times New Roman',15,'bold'))
                        self.label.grid(row=7,column=5,columnspan=3,padx=15,pady=15)
                        
            else:
                self.label.config(text="cannot insert empty field/s",fg='red',font=('Times New Roman',15,'bold'))
                self.label.grid(row=7,column=5,columnspan=3,padx=15,pady=15)            
        else:
            sys.exit("file doesn't exist")
       
    def update_items(self):
        self.entry_1_val=self.item_name_entry.get()
        self.entry_2_val=self.DESCRIPTION_entry.get()
        self.entry_3_val=self.PRICE_PER_ITEM_entry.get()
        self.entry_4_val=self.QUANTITY_entry.get()
        # print(self.entry_2_val)
       
        self.LIst=""
        if os.path.isfile(self.db):
            if(len(self.entry_1_val)!=0):
                self.f_read=open(self.db,'r')
                self.LIst=self.f_read.readlines()
                self.index_item=-1
                self.old_values=[]
                self.flag=0
                self.old_value_item=""
                for i in range(len(self.LIst)):
                    if(self.LIst[i]=="\n"):
                        continue
                    item_name=check_item_name(self.LIst[i])
                    # self.old_values.app
                    if(self.entry_1_val==item_name):
                        self.flag=1
                        self.index_item=i
                        break
                for i in range(len(self.LIst)):
                    if i!=self.index_item and self.LIst[i]!="\n":
                        self.old_values.append(self.LIst[i])
                    elif i==self.index_item:
                        self.old_value_item=self.LIst[i]
                self.old_sentence=self.LIst[self.index_item]
                self.old_value_item= self.old_value_item.split(',')  
                self.f_read.close()
                if(self.flag==1):
                    if((len(self.entry_2_val)!=0) or (len(self.entry_3_val)!=0) or (len(self.entry_4_val)!=0)):
                         if((self.entry_2_val != self.entry_1_val)  and (self.entry_3_val != self.entry_1_val)  and (self.entry_4_val != self.entry_1_val)):
                              self.marker=0
                              if len(self.entry_2_val)==0:
                                  self.entry_2_val="@#$@%"
                                  self.marker=1
                                #   print("helo",self.entry_2_val)
                              if((self.entry_3_val != self.entry_2_val) or (self.entry_4_val != self.entry_2_val)):
                                    if self.marker==1:
                                        self.entry_2_val=""
                                    self.entry_vals=[self.entry_1_val,self.entry_2_val,self.entry_3_val,self.entry_4_val]
                                    self.entry_values_write=["item name="+self.entry_1_val+',',"Description="+self.entry_2_val+','
                                                        ,"Price/item="+self.entry_3_val+',',"Quantity="+self.entry_4_val+"\n"]
                                    self.items_to_be_passed=[]
                                    self.indices_to_replace=[]
                                    for i in range(len(self.entry_vals)):
                                        if(len(self.entry_vals[i])!=0):
                                            self.items_to_be_passed.append(self.entry_values_write[i])
                                            self.indices_to_replace.append(i)
                                    
                                    
                                    self.new_line=replace_item_info(self.items_to_be_passed,self.old_value_item,self.indices_to_replace)
                                    self.f_write=open("test.txt",'w')
                                    for i in range(len(self.LIst)):
                                        if i ==self.index_item:
                                            if(i==len(self.LIst)-1): 
                                                self.f_write.write(self.new_line)
                                                # self.f_write.write("\n")
                                            
                                            else:
                                                self.f_write.write(self.new_line)
                                                # self.f_write.write("\n")
                                        else:
                                            if(i==len(self.LIst)-1): 
                                                self.f_write.write(self.LIst[i])
                                                # self.f_write.write("\n")
                                            
                                            else:
                                                self.f_write.write(self.LIst[i])
                                                # self.f_write.write("\n")
                                            
                                            
                                    self.f_write.close()        
                                    self.label.config(text="updated successfully",fg='green',font=('Times New Roman',15,'bold'))
                                    self.label.grid(row=7,column=5,columnspan=3,padx=15,pady=15)
                              else:
                                    self.label.config(text="cannot write description text in quantity field or price field ",fg='red',font=('Times New Roman',15,'bold'))
                                    self.label.grid(row=7,column=5,columnspan=3,padx=15,pady=15)
                         else:
                            self.label.config(text="item name cannot be written multiple times in other fields",fg='red',font=('Times New Roman',15,'bold'))
                            self.label.grid(row=7,column=5,columnspan=3,padx=15,pady=15)
                    else:
                        self.label.config(text="need to type sth in at least one field in order to update the info of the that item ",fg='red',font=('Times New Roman',13,'bold'))
                        self.label.grid(row=7,column=3,columnspan=3,padx=15,pady=15)
            
                else:
                    self.label.config(text="cannot update item since it doesn't exist ",fg='red',font=('Times New Roman',15,'bold'))
                    self.label.grid(row=7,column=5,columnspan=3,padx=15,pady=15)
            else:
                self.label.config(text="item name must be passed in order to update it ",fg='red',font=('Times New Roman',15,'bold'))
                self.label.grid(row=7,column=5,columnspan=3,padx=15,pady=15)
        else:
            sys.exit("File Doesn't exist")
            
        
    def remove_item(self):
        self.item_name_entry_D=self.item_name_entry_deleted.get()
        if os.path.isfile(self.db):
            if(len(self.item_name_entry_D)!=0):
                self.f_read=open("test.txt",'r')
                self.flag=0
                self.indx=-1
                self.LIst=self.f_read.readlines()
                for i in range(len(self.LIst)):
                    check_item=check_item_name(self.LIst[i])
                    if self.item_name_entry_D== check_item:
                        self.flag=1
                        self.indx=i
                        break
                self.f_read.close()
                if self.flag==1:
                    self.f_write=open("test.txt",'w')
                    for i in range(len(self.LIst)):
                        if i ==self.indx:
                            continue
                        else:
                            self.f_write.write(self.LIst[i])
                    self.f_write.close()
                    self.label_2.config(text="deleted successfully",fg='green',font=('Times New Roman',15,'bold'))
                    self.label_2.grid(row=10,column=2,columnspan=3,padx=15,pady=15)
                else:
                    self.label_2.config(text="cannot delete an item that doesn't exist ",fg='red',font=('Times New Roman',15,'bold'))
                    self.label_2.grid(row=10,column=2,columnspan=3,padx=15,pady=15)            
                    
            else:
                self.label_2.config(text="cannot delete an item without first passing its name ",fg='red',font=('Times New Roman',15,'bold'))
                self.label_2.grid(row=10,column=2,columnspan=3,padx=15,pady=15)
        else:
            sys.exit("File Doesnt exist")
        
    def view_item(self):
        self.another_rootwindow=tk.Tk()
        self.another_rootwindow.geometry("512x512")
        self.another_rootwindow.iconbitmap("shop-512.ico")
        self.window.title("items")
        canvas = tk.Canvas(self.another_rootwindow)
        scrollbar = tk.Scrollbar(self.another_rootwindow, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        self.f_read=open("test.txt",'r')
        self.LIst=self.f_read.readlines()
        self.row_num=0
        self.f_read.close()
        for i in range(len(self.LIst)):
            if self.LIst[i]=="\n":
                continue
            else:
                self.Lab=tk.Label(scrollable_frame,text=self.LIst[i],font=('Times New Roman',15,'bold'))
                self.Lab.grid(row=self.row_num,column=0,padx=15,pady=15)
                self.row_num+=1
        self.another_rootwindow.resizable(True, True)
        
        self.another_rootwindow.mainloop()
    def exit_p(self):
        sys.exit()
    
        
x=retail_store_inventory(r"test.txt")
x.main_loop()

