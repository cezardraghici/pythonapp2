import requests
from bs4 import BeautifulSoup
import bkdb
from selenium import webdriver
import pandas as pd
import psutil
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk 
from tkinter import PhotoImage



driver="global"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
driver = webdriver.Chrome('C:\Local Drivers\chromedriver.exe',chrome_options=options)
bkdb.delete()
def get_data_fom_ING():
    r=requests.get("https://ing.ro/ing-in-romania/informatii-utile/curs-valutar")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    monede=["EUR","USD","GBP","CHF"]
    name="ING"
    i=0
    for md in monede:
        all=soup.find_all("td",{"class":"buy","data-currency":md})
        y=all[1].text.replace(" ","").replace("\n","")
        #print (all)
        all1=soup.find_all("td",{"class":"sell","data-currency":md})
        z=all1[1].text.replace(" ","").replace("\n","")
        #print(all1)
        all2=soup.find_all("td",{"class":"code"})
        x=all2[i].text.replace(" ","").replace("\n","")
        bkdb.insert(name,x,y,z)
        i+=1
        # print(name)
        # print(x)
        # print(y)
        # print(z)
    #bkdb.view_all()

# def get_data_fom_ING1():
#     driver.get('https://www.bcr.ro/ro/curs-valutar')
#     i=1
#     name="ING"
#     monede=["EUR","USD","GBP","CHF"]
#     while i<5:
#         a=driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div[1]/table/tbody/tr['+str(i)+']/td[2]')
#         x=a.text
#         b=driver.find_element_by_xpath('//*[@id="exchange-first-tab"]/div/div[1]/table/tbody/tr['+str(i)+']/td[4]')
#         y=b.text
#         c=driver.find_element_by_xpath('//*[@id="exchange-first-tab"]/div/div[1]/table/tbody/tr['+str(i)+']/td[5]')
#         z=c.text
#         bkdb.insert(name,x,y,z)
#         i+=1
        

def get_data_fom_BCR():
    
    driver.get('https://www.bcr.ro/ro/curs-valutar')
    i=1
    name="BCR"
    while i<5:
        a=driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div[1]/div/div/div/table/tbody/tr['+str(i)+']/td[2]')
        x=a.text
        b=driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div[1]/div/div/div/table/tbody/tr['+str(i)+']/td[3]')
        y=b.text
        c=driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div[1]/div/div/div/table/tbody/tr['+str(i)+']/td[4]')
        z=c.text
        d=driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div[1]/div/div/div/table/tbody/tr['+str(i)+']/td[1]/div')
        bkdb.insert(name,x,y,z)
        i+=1
        
        # print(name)
        # print(x)
        # print(y)
        # print(z)
        
    #bkdb.view_all()

def collect_data():
    get_data_fom_BCR()
    get_data_fom_ING()

def view_all():
    for row in bkdb.view_all():
        tree.insert("",END,values=row)

def delete_db():
    bkdb.delete()

def clear_screen():
    for i in tree.get_children():
        tree.delete(i)

def view():
    clear_screen()
    for row in bkdb.view(variable.get()):
        tree.insert("",END,values=row)


window = tk.Tk()
window.geometry("1350x600")
window.title("Curs Valutar")


tree= ttk.Treeview(window, height=30, column=("column1", "column2", "column3",), show='headings')

tree.heading("#1", text="Banca")
tree.column("#1", minwidth=0, width=300, stretch=True)
tree.heading("#2", text="Cumparare")
tree.column("#2", minwidth=0, width=250, stretch=True, anchor=tk.CENTER)
tree.heading("#3", text="Vanzare")
tree.column("#3", minwidth=0, width=250, stretch=True, anchor=tk.CENTER)
tree.grid(row=2,column=1,rowspan=20,columnspan=10)

variable = StringVar(window)
variable.set("EUR") # default value
l1=tk.Label(window, text="Alege moneda")
l1.grid(row=1,column=0)
w = OptionMenu(window, variable, "EUR", "USD", "GBP","CHF")
w.grid(row=1,column=1)

b0=tk.Button(window,text="View", command=view,width=15)
b0.grid(row=1, column = 2)
b1=tk.Button(window,text="Collect Data", command=collect_data,width=15)
b1.grid(row=1, column = 3)
b2=tk.Button(window,text="View All", command=view_all,width=15)
b2.grid(row=1, column = 4)
b3=tk.Button(window,text="Delete DB", command=delete_db,width=15)
b3.grid(row=1, column = 5)
b4=tk.Button(window,text="Clear Screen", command=clear_screen, width=15)
b4.grid(row=1, column = 6)


img=PhotoImage(file="img/EUR.gif").subsample(100,80)
tree.insert("",'end',image=img)

#get_data_fom_ING()
#get_data_fom_BCR()
# bkdb.view_all()
#bkdb.drop()
window.mainloop()