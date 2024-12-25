# Any-Quick-Laucher
Open any application or webpage simple by adjusting the source code.

OS Friendly

To change Webpage destiation

    def OpenUrlX():
              #Paste Website Address in replace of "Website Address"
        urlX='Website Address'
        webbrowser.open_new(urlX)

    class PageX(Page):
        def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

       label = tk.Label(self, 
                         #Type in Webpage Name to Display in replace of "Web Page Name"
                        text="Web Page Name")
       label.pack(side="top", 
                  fill="both", 
                  expand=True)

        b1 = tk.Button(buttonframe,
                       bg="black",
                       fg="lightgreen",
                       #Type in Webpage Name to Display in replace of "Display Name"
                       text="Display Name",
                       command=OpenUrlX)

To Change Applications

      def appX():
          subprocess.run('Path To desired Application and Executable', 
                   shell=True)


      class AppPage1(Page):
         def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
       
           label = tk.Label(self, 
                             #Type Name in replace of "Application Display Name"
                        text="Application Display Name")
           label.pack(side="top", 
                  fill="both", 
                  expand=True)

          abX = tk.Button(buttonframe2,
                        bg="black",
                        fg="lightgreen",
                        #Type Name in replace of "Application Display Name"
                        text="Application Display Name",
                        command=app1)


            
#Python Tutorial
