import requests
from bs4 import BeautifulSoup
import bkdb
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk 
from tkinter import ttk
from ttkthemes import ThemedTk
from datetime import datetime
import time

driver="global"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
driver = webdriver.Chrome('Windows drivers\chromedriver.exe',chrome_options=options)
bkdb.delete()
cr_data = 'global'
cr_data = datetime.today()
#cr_data = bkdb.data()

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
        all1=soup.find_all("td",{"class":"sell","data-currency":md})
        z=all1[1].text.replace(" ","").replace("\n","")
        all2=soup.find_all("td",{"class":"code"})
        x=all2[i].text.replace(" ","").replace("\n","")
        bkdb.insert(name,x,y,z,cr_data)
        i+=1  

def get_data_fom_BCR():
    driver.get('https://www.bcr.ro/ro/curs-valutar')
    nr=[1,2,3,4]
    name="BCR"
    for i in nr:
        print(i)
        x=driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div[1]/div/div/div/table/tbody/tr['+str(i)+']/td[2]').text
        print(driver.find_element_by_xpath('/html/body/div[3]/main/div[5]/div/div/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[3]'))
        y=driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div[1]/div/div/div/table/tbody/tr['+str(i)+']/td[3]').text
        print(y)
        z=driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div[1]/div/div/div/table/tbody/tr['+str(i)+']/td[4]').text
        print(z)
        bkdb.insert(name,x,y,z,cr_data)
        
def get_data_fom_BT():
    driver.get('https://www.bancatransilvania.ro/curs-valutar-spot/')
    name="BT"
    nr=[1,2,3,4]
    for i in nr:
        x=driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/table[2]/tbody/tr['+str(i)+']/td[1]/span').text
        y=driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/table[2]/tbody/tr['+str(i)+']/td[3]').text
        z=driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/table[2]/tbody/tr['+str(i)+']/td[4]').text
        bkdb.insert(name,x,y,z,cr_data)

def get_data_from_BRD():
    url='https://www.brd.ro/curs-valutar-si-dobanzi-de-referinta'
    driver.get(url)
    name="BRD"
    nr = [2,3,4]
    for i in nr:
        x=driver.find_element_by_xpath('//*[@id="tabAccountExchangeRates"]/div/div[2]/p['+str(i)+']').text
        y=driver.find_element_by_xpath('//*[@id="tabAccountExchangeRates"]/div/div[4]/p['+str(i)+']').text
        z=driver.find_element_by_xpath('//*[@id="tabAccountExchangeRates"]/div/div[5]/p['+str(i)+']').text
        bkdb.insert(name,x,y,z,cr_data)
    r=requests.get(url)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"col-sm-2 hidden-xs"})
    x=all[2].text.replace("\n","")[43:46]
    all1=soup.find_all("div",{"class":"col-xs-4 col-sm-2"})
    y=all1[0].text.replace(" ","").replace("\n","")[79:85]
    z=all1[1].text.replace(" ","").replace("\n","")[79:85]
    bkdb.insert(name,x,y,z,cr_data)
    
def get_data_from_Unicredit():
    driver.get('https://www.unicredit.ro/ro/institutional/Diverse/SchimbValutar.html')
    name="Unicredit"
    nr = [1,2,6,10]
    for i in nr:
        x=driver.find_element_by_xpath('//*[@id="currency_list_table"]/tr['+str(i)+']/td[1]/a/strong').text
        y=driver.find_element_by_xpath('//*[@id="currency_list_table"]/tr['+str(i)+']/td[3]/div').text
        z=driver.find_element_by_xpath('//*[@id="currency_list_table"]/tr['+str(i)+']/td[4]/div').text
        bkdb.insert(name,x,y,z,cr_data)
        
def get_data_from_Raiffeisen():
    driver.get('https://www.raiffeisen.ro/persoane-fizice/curs-valutar/')
    name='Raiffeisen'
    nr=[0,1,2,3]
    for i in nr:
        x=driver.find_element_by_xpath('//*[@id="_'+str(i)+'"]/td[2]').text
        y=driver.find_element_by_xpath('//*[@id="_'+str(i)+'"]/td[4]').text
        z=driver.find_element_by_xpath('//*[@id="_'+str(i)+'"]/td[5]').text
        bkdb.insert(name,x,y,z,cr_data)

def collect_data():
    get_data_fom_BCR()
    get_data_fom_ING()
    get_data_fom_BT()
    get_data_from_BRD()
    get_data_from_Unicredit()
    get_data_from_Raiffeisen()

def clear_screen():
    for i in tree.get_children():
        tree.delete(i)

def view():
    clear_screen()
    for row in bkdb.view(variable.get()):
        tree.insert("",END,values=row)

def eur(value):
    variable.set(value)
    view()

def usd(value):
    variable.set(value)
    view()

def gbp(value):
    variable.set(value)
    view()

def chf(value):
    variable.set(value)
    view()

def populate_menu(w, **cmds):
    menu = w['menu']
    menu.delete(0, "end")
    for name, func in cmds.items():
        menu.add_command(label=name, command=lambda name=name, func=func: func(name))

window = ThemedTk(theme="equilux")
window.geometry("260x220")
window.configure(bg='#424141')
window.title("Curs Valutar")

variable = StringVar(window)
variable.set("EUR") 

w = ttk.OptionMenu(window, variable, ())
w.grid(row=1,column=1)

populate_menu(w, EUR=eur, USD=usd, GBP=gbp, CHF=chf)

tree= ttk.Treeview(window, height=6, column=("column1", "column2", "column3",), show='headings')
tree.heading("#1", text="Banca")
tree.column("#1", minwidth=0, width=80, stretch=True, anchor=tk.CENTER)
tree.heading("#2", text="Cumparare")
tree.column("#2", minwidth=0, width=80, stretch=True, anchor=tk.CENTER)
tree.heading("#3", text="Vanzare")
tree.column("#3", minwidth=0, width=80, stretch=True, anchor=tk.CENTER)
tree.grid(row=2,column=0,rowspan=6,columnspan=4)

l1=ttk.Label(window, text="Alege moneda")
l1.grid(row=1,column=0)

data = bkdb.data()
l2=ttk.Label(window, text=data)
l2.grid(row=1, column=3)

collect_data()
view()
window.mainloop()