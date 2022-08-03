


import os
import webbrowser
from tkinter import *

# Creating variable
body = 'Stay tuned for our amazing summer sale!'  



# Clears 'Textbox' - using with 'Default Web Page' button
# to replace text with 'body' string
def clearText(obj, txt):
   obj.delete('1.0', END)
   obj.insert('1.0', txt)

# Creating GUI window
def myGUI():
   # Styling window - title, size
   win = Tk()
   win.title('Web Page Generator')
   win.resizable(width=False, height=False)

   # Creating Textbox - size, position
   textbox = Text(win, width=50, height=10, wrap=WORD)
   textbox.grid(row=1, column=1, columnspan=3, padx=(20,20), pady=(20,20), sticky=N+E+S+W)

   # Creating Buttons - configuration, size, and position
   b1 = Button(win, text = "Default Web Page")
   b2 = Button(win, text = "Generate Web Page")
   b3 = Button(win, text = "Exit Program")

   b1.config(height=2, command=lambda obj=textbox, txt=body: clearText(obj, txt))
   b2.config(height=2, command=lambda newBody=textbox: userContent(newBody))
   b3.config(height=2, command=lambda: win.destroy())

   b1.grid(row=2, column=1, padx=(20,20), pady=(0,20), sticky=S+W)
   b2.grid(row=2, column=2, padx=(20,20), pady=(0,20), sticky=S)
   b3.grid(row=2, column=3, padx=(20,20), pady=(0,20), sticky=E+S)
    


# Generates webpage - populates wildcard
# within HTML with content from Textbox
def createPage():
   global webpage
   webpage = """
      <!DOCTYPE html>
         <html lang='en'>
            <head>
               <meta charset='utf-8'>
            </head>
            
            <body>
               {}
            </body>
            
         </html>    
      """
   print(webpage)

# Creates and populates webpage / HTML with inserted
# wildcard / user's text from newBody/textbox
def userContent(newBody):
   if isinstance(newBody,str):
        newPage = webpage.format(newBody)
   else:
        newPage = webpage.format(newBody.get('1.0',END).strip())
   print(newPage)   
   writePage(newPage)    
    
# Writes code into file, displays pathname, and opens file in browser
def writePage(newPage):
   file = open('index.html','w')
   file.write(newPage)
   file.close()
   webbrowser.open('file://'+os.path.realpath('index.html'))
   print('Generated web page has been saved here:\n{}'.format(os.path.realpath('index.html')))    




      
if __name__ == '__main__':
   myGUI()
   createPage()
