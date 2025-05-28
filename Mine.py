#!/media/try/Code_Card/Code_Folder/Python/Mine.py

import webbrowser, subprocess
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime


subprocess.call('cd /media/try/Code_Card/Code_Folder/Python', shell=True)

root = tk.Tk()
root.title ('It\'s A Codeiful Day')    
root.attributes('-alpha', 0.67)
root.attributes('-topmost', 2)
root.wm_geometry("700x70+900+500")

#Remove Cash Symbol to use a picture

#background_image=tk.PhotoImage(file=r"/home/try/Pictures/bg.png")
#background_label = tk.Label(root,
                            #image=background_image)
#background_label.place(x=0,
                       #y=0,
                       #relwidth=1,
                       #relheight=1)
#######################################################################################
#This function is used to display time on the label 
def time():
    #display format for the time and text
    string = strftime(' %a, %b %d %Y '+'  -Never Too Late To Code-  '+'%I:%M:%S %p  ')
    clock.config(text=string)
    #Refresh time ever 1000 micro seconds
    clock.after(1000,
                time) 
        
# Styling the label clocks font size and color
clock = tk.Label(root,
                 font=('fixedsys', 11),
                 background='darkred',
                 foreground='gold')
# Placing clocks location
clock.pack(side="bottom")

time()
#################################################################################
#Functions for web domains $ Applications
#Web tabs
#Tkinter Tutorial
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

def OpenUrl1():
    url1='https://www.pythontutorial.net/tkinter/'
    webbrowser.open_new(url1)
class Page1(Page):
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, 
                        text="Tkinter Tutorial")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)
#Python Tutorial 
def OpenUrl2():
    url2='https://www.pythontutorial.net/'
    webbrowser.open_new(url2)
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       label = tk.Label(self, 
                        text="Python Tutorial")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)   

#Crypto
def OpenUrl3():
    url3='https://coinmarketcap.com/'
    webbrowser.open_new(url3)
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, 
                        text="Crypto")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)      #Delta Dental 
def OpenUrl4():
    url4='https://auth.deltadental.com/'
    webbrowser.open_new(url4)
class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, 
                        text="Delta Dental")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)
#E-Trade 
def OpenUrl5():
    url5='https://us.etrade.com/etx/pxy/login'
    webbrowser.open_new(url5)
class Page5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, 
                        text="E-Trade")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)#Code Stats
def OpenUrl6():
    url6='https://codestats.net/'
    webbrowser.open_new(url6)
  class Page6(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, 
                        text="Code Stats")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)
####################################################################################
#Applications
#VS Code
def app1():
    subprocess.run('/usr/share/code/code --unity-launch', 
                   shell=True)
class AppPage1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, 
                        text="VS Code")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)#ThunderBird
def app2():
    subprocess.run('thunderbird', 
                   shell=True)
class AppPage2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, 
                        text="ThunderBird")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)
#Terminal
def app3():
    subprocess.run('gnome-terminal', 
                   shell=True)
class AppPage3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, 
                        text="Terminal")
       label.pack(side="top",
                  fill="both", 
                  expand=True)
#Files
def app4():
    subprocess.run('nemo', 
                   shell=True)
class AppPage4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, 
                        text="Files")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)
#Wmware
def app5():
    subprocess.run('/usr/bin/vmplayer #u', 
                   shell=True) 
class AppPage5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, 
                        text="VMware")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)
#Transmission
def app6():
    subprocess.run('transmission-gtk %U', 
                   shell=True) 
class AppPage6(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, 
                        text="Transmission")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)
   


##############################################################################
class MainView(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        #Web
        #Tkinter Tutorial
        p1 = Page1(self)
        #Python Tutorial
        p2 = Page2(self)
        #Crypto
        p3 = Page3(self)
        #Delta Dental
        p4 = Page4(self)
        #E-Trade
        p5 = Page5(self)
        #Code Stats
        p6 = Page6(self)
#######################################################################################
        #Applications6
        #VS Code
        ap1 = AppPage1(self)
        #ThunderBird
        ap2 = AppPage2(self)
        #Terminal
        ap3 = AppPage3(self)
        #Files
        ap4 = AppPage4(self)
        #VMware
        ap5 = AppPage5(self)
        #Transmission
        ap6 = AppPage6(self)
#######################################################################################
        #Buttons Position
        #Web
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)

        buttonframe.pack(side="top",
                         fill="x",
                         expand=False)
        container.pack(side="top",
                       fill="both",
                       expand=True)
#######################################################################################
        #Applications
        buttonframe2 = tk.Frame(self)
        container2 = tk.Frame(self)

        buttonframe2.pack(side="top",
                          fill="x",
                          expand=False)        
        container2.pack(side="top",
                        fill="both",
                        expand=True)
#######################################################################################    
        #Buttons Size
        #Web
        #Tkinter Tutorial
        p1.place(in_=container,
                 x=0,
                 y=0,
                 relwidth=1,
                 relheight=1)
        #Python Tutorial
        p2.place(in_=container,
                 x=0,
                 y=0,
                 relwidth=1,
                 relheight=1)
        #Crypto
        p3.place(in_=container,
                 x=0,
                 y=0,
                 relwidth=1,
                 relheight=1)
        #Delta Dental
        p4.place(in_=container,
                 x=0,
                 y=0,
                 relwidth=1,
                 relheight=1)
        #E-Trade
        p5.place(in_=container,
                 x=0,
                 y=0,
                 relwidth=1,
                 relheight=1)
        #Code Stats
        p6.place(in_=container,
                 x=0,
                 y=0,
                 relwidth=1,
                 relheight=1)
#######################################################################################
        #Applications
        #VS Code
        ap1.place(in_=container2,
                  x=0,
                  y=0,
                  relwidth=1,
                  relheight=1)
        #ThunderBird
        ap2.place(in_=container2,
                  x=0,
                  y=0,
                  relwidth=1,
                  relheight=1)
        #Terminal
        ap3.place(in_=container2,
                  x=0,
                  y=0,
                  relwidth=1,
                  relheight=1)
        #VMware
        ap5.place(in_=container2,
                  x=0,
                  y=0,
                  relwidth=1,
                  relheight=1)
        #Transmission
        ap6.place(in_=container2,
                  x=0,
                  y=0,
                  relwidth=1,
                  relheight=1)
        #######################################################################################
        #Buttons Look & Actions
        #Web
        #Tkinter Tutorial
        b1 = tk.Button(buttonframe,
                       bg="black",
                       fg="lightgreen",
                       text="Tkinter Tutorial",
                       command=OpenUrl1)
        #Python Tutorial
        b2 = tk.Button(buttonframe,
                       bg="black",
                       fg="lightgreen",
                       text="Python Tutorial",
                       command=OpenUrl2)
        #Crypto
        b3 = tk.Button(buttonframe,
                       bg="black",
                       fg="lightgreen",
                       text="Crypto",
                       command=OpenUrl3)
        #Delta Dental
        b4 = tk.Button(buttonframe,
                       bg="black",
                       fg="lightgreen",
                       text="Delta Dental",
                       command=OpenUrl4)
        #E-Trade
        b5 = tk.Button(buttonframe,
                       bg="black",
                       fg="lightgreen",
                       text="E-Trade",
                       command=OpenUrl5)
        #Code Stats
        b6 = tk.Button(buttonframe,
                       bg="black",
                       fg="lightgreen",
                       text="Code Stats",
                       command=OpenUrl6)
#######################################################################################
        #Applications
        #VS Code
        ab1 = tk.Button(buttonframe2,
                        bg="black",
                        fg="lightgreen",
                        text="VS Code",
                        command=app1)
        #ThunderBird
        ab2 = tk.Button(buttonframe2,
                        bg="black",
                        fg="lightgreen",
                        text="ThunderBird",
                        command=app2)
        #Terminal
        ab3 = tk.Button(buttonframe2,
                        bg="black",
                        fg="lightgreen",
                        text="Terminal",
                        command=app3)
        #Files
        ab4 = tk.Button(buttonframe2,
                        bg="black",
                        fg="lightgreen",
                        text="Files",
                        command=app4)
        #VMware
        ab5 = tk.Button(buttonframe2,
                        bg="black",
                        fg="lightgreen",
                        text="VMware",
                        command=app5)
        #Transmission
        ab6 = tk.Button(buttonframe2,
                        bg="black",
                        fg="lightgreen",
                        text="Transmission",
                        command=app6)
#######################################################################################
        #Buttons Location
        #Web
        #Tkinter Tutorial
        b1.pack(side="left")
        #Python Tutorial
        b2.pack(side="left")
        #Crypto
        b3.pack(side="left")
        #Delta Dental
        b4.pack(side="left")
        #E-Trade
        b5.pack(side="left")
        #Code Stats
        b6.pack(side="left")
#######################################################################################
        #Applications
        #VS Code
        ab1.pack(side="left")
        #ThunderBird
        ab2.pack(side="left")
        #Terminal
        ab3.pack(side="left")
        #Files
        ab4.pack(side="left")
        #VMware
        ab5.pack(side="left")
        #Transmission
        ab6.pack(side="left")
#######################################################################################
#Window settings
if __name__ == "__main__":   
    main = MainView(root)
    main.pack(side="top", fill="none", expand=False)
    root.mainloop()
