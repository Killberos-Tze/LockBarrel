#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 07:37:01 2023

@author: tze
"""

from tkinter import Frame, Button, Label, GROOVE, StringVar
from PIL import ImageTk, Image
import os

class Rotate(Frame):
    def __init__(self,**kwargs):
        kwargs=self.process_kwargs(**kwargs)
        super().__init__(kwargs['parent'])
        kwargs['parent']=self
        self.choice=kwargs['typevar']
        self.choice_list=kwargs['choice_list']
        self.command=kwargs['command']
        if kwargs['direction'] == 'horizontal' or kwargs['direction'] != 'vertical':
            self.prepare_elements(0,180,**kwargs)
            self.direction_horizontal()
        else:
            self.prepare_elements(90,270,**kwargs)
            self.direction_vertical()
        self.choice.set(self.choice_list[0])
        
    def process_kwargs(self,**kwargs):
        if 'parent' not in kwargs:
            kwargs['parent']=None
        if 'typevar' not in kwargs:
            kwargs['typevar']=StringVar()
        if 'imagepath' not in kwargs:
            kwargs['imagepath']=os.path.join(os.path.dirname(__file__), 'images', "button.png")
        if 'choice_list' not in kwargs:
            kwargs['choice_list']=['a','b','c']
        if 'command' not in kwargs:
            kwargs['command']=self.placeholder
        if 'direction' not in kwargs:
            kwargs['direction']='horizontal'
        if 'width' not in kwargs:
            kwargs['width']=10
        return kwargs
        
    def prepare_elements(self,*args,**kwargs):
        image = Image.open(kwargs['imagepath'])
        self.imageminus=ImageTk.PhotoImage(image.rotate(args[0]))
        self.imageplus=ImageTk.PhotoImage(image.rotate(args[1]))
        self.minus=Button(kwargs['parent'], image=self.imageminus,command=lambda lidx=-1: self.choice_change(lidx),bg='lightblue')
        self.plus=Button(kwargs['parent'], image=self.imageplus,command=lambda lidx=+1: self.choice_change(lidx),bg='lightblue')
        self.label=Label(kwargs['parent'], textvariable=self.choice, borderwidth=2,relief=GROOVE, width=kwargs['width'])
        
                
    def placeholder(self,*args):
        pass
    
    def direction_horizontal(self):
        self.minus.grid(row=1,column=1)
        self.label.grid(row=1,column=2)
        self.plus.grid(row=1,column=3)
        
    
    def direction_vertical(self):
        self.minus.grid(row=3,column=1)
        self.label.grid(row=2,column=1)
        self.plus.grid(row=1,column=1)
        
    
    def choice_change(self,idx):
        idx=(self.choice_list.index(self.choice.get())+idx) % len(self.choice_list)
        self.choice.set(self.choice_list[idx])
        self.command(self.choice.get())