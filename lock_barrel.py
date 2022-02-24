#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 23:42:22 2022
@author: tzework
"""

import tkinter as tk
from PIL import Image, ImageTk
import os

class Lock_barrel():
    def __init__(self):
        self.no_digits=3
        self.no_rows=2
        try:
            with open(os.path.join(os.path.dirname(__file__),'lock_barrel.ini'), 'r') as f:
                for line in f:
                    a=line.strip()
                    tmp=a.split('=')
                    if tmp[0]=='No. of digits':            
                        self.no_digits=int(tmp[-1])
                    if tmp[0]=='No. of rows':            
                        self.no_rows=int(tmp[-1]) 
        except:
            pass
        
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title("Lock Barrel App")
        self.init_mainframe()
    
    def init_start(self):
        self.root.mainloop()
        
    def init_mainframe(self):
        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid(column=0,row=0)
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)
        self.mainframe.pack(pady = (50,50), padx = (50,50))
        self.init_stuff()
        
    def increase(self,idx):
        if self.counter[idx]<9:
            self.counter[idx]+=1
        else:
            self.counter[idx]=0
        self.variables[idx].set(str(self.counter[idx]))
        
    def decrease(self,idx):
        if self.counter[idx]>0:
            self.counter[idx]-=1
        else:
            self.counter[idx]=9
        self.variables[idx].set(str(self.counter[idx]))
        
        
    def init_stuff(self):
        dirname=os.path.dirname(__file__)#path of this __file__ not the __main__
        imagepath=os.path.join(dirname, 'images', "button.png")
        image = Image.open(imagepath)
        self.imageup=ImageTk.PhotoImage(image)
        self.imagedown=ImageTk.PhotoImage(image.rotate(180))
        self.counter=[]
        self.variables=[]
        self.index=[]
        for mm in range(0,self.no_rows):
            for nn in range(0,self.no_digits):
                idx=mm*self.no_digits+nn
                self.index.append(idx)
                self.counter.append(0)
                self.variables.append(tk.StringVar(self.root))
                self.variables[idx].set(str(self.counter[idx]))
                tk.Label(self.mainframe, textvariable=self.variables[idx], borderwidth=2,relief=tk.GROOVE).grid(row=mm*4+2,column=nn)
                tk.Button(self.mainframe, image=self.imageup, command=lambda lidx=idx: self.increase(lidx)).grid(row=mm*4+1,column=nn)#This may look magical, but here's what's happening. When you use that lambda to define your function, the open_this call doesn't get the value of the variable i at the time you define the function. Instead, it makes a closure, which is sort of like a note to itself saying "I should look for what the value of the variable i is at the time that I am called". Of course, the function is called after the loop is over, so at that time i will always be equal to the last value from the loop.
#Using the i=i trick causes your function to store the current value of i at the time your lambda is defined, instead of waiting to look up the value of i later.
#https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments
                tk.Button(self.mainframe, image=self.imagedown, command=lambda lidx=idx: self.decrease(lidx)).grid(row=mm*4+3,column=nn)
            if mm<self.no_rows-1:
                tk.Label(self.mainframe, text='\t').grid(row=mm*4+4,column=0, columnspan=self.no_digits)
if __name__=='__main__':
    Lock_barrel.init_start(Lock_barrel())
