#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 23:42:22 2022

@author: tzework
"""

import tkinter as tk
from PIL import Image, ImageTk
import os
from tkWindget.tkWindget import Rotate

class Lock_barrel():
    def __init__(self):
        try:
            with open(os.path.join(os.path.dirname(__file__),'lockbarrel.ini'), 'r') as f:
                for line in f:
                    a=line.strip()
                    tmp=a.split('=')
                    if tmp[0]=='No. of digits':            
                        self.no_digits=int(tmp[-1])
                    if tmp[0]=='No. of rows':            
                        self.no_rows=int(tmp[-1])
                    if tmp[0]=='Digits':
                        digits=tmp[1].split('|')
        except:
            self.no_digits=3
            self.no_rows=2
            digits=[0,1,2,3,4,5,6,7,8,9]
            
        self.digits=[int(item) for item in digits]
        
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
   
        
    def init_stuff(self):

        self.variables=[]
        #self.index=[]
        for mm in range(0,self.no_rows):
            for nn in range(0,self.no_digits):
                idx=mm*self.no_digits+nn
                self.variables.append(Rotate(parent=self.mainframe,direction='vertical',width=2,choice_list=self.digits,typevar=tk.IntVar()))
                self.variables[idx].grid(row=mm,column=nn)
      
if __name__=='__main__':
    Lock_barrel.init_start(Lock_barrel())
