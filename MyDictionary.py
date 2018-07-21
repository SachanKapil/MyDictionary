from tkinter import *
from tkinter import messagebox
import pymysql

def getWord():
    entered_word=textentry.get()
    output.delete(0.0,END)
    db=pymysql.connect("localhost","root","root","pythondb")
    cursor=db.cursor()
    query="select * from dictionary where word='%s' " % (entered_word)
    try:
        check=cursor.execute(query)
        if check>0:
          result=cursor.fetchall()
          var=result[0][1]
          output.insert(END,var)
        else:
          messagebox.showinfo("Word","Word is not exist !")
    except:
        messagebox.showinfo("Error", "Something wents wrong !")

def addWord():
    entered_text=dictword.get()
    entered_dif = dict_dif.get()

    db=pymysql.connect("localhost","root","root","pythondb")
    cursor=db.cursor()
    sql = "INSERT INTO dictionary(word , definition) VALUES ( '%s' , '%s')" % (entered_text, entered_dif)
    try:
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo("Dictionary","Word is added !")
    except:
        db.rollback()
        messagebox.showinfo("Error", "Something went worng !")
    db.close()


window=Tk()
window.title("My Dictionary")
window.configure(background="white")
window.geometry("800x800")

Label(window,text="\nEnter the word, which definition you want to search:\n",bg="white",font="none 18 bold").grid(row=1,column=0,sticky=W)

textentry=Entry(window,width=30,bd=7)
textentry.grid(row=2,column=0,pady=20,sticky=W)

Button(window,text="Search",width=6,font="none 10 bold",command=getWord).grid(row=3,column=0,sticky=W)
Button(window,text="Quit",width=6,font="none 10 bold",command=window.quit).grid(row=3,column=1,sticky=W)

Label(window,text="\n Definition:\n",bg="white",font="none 18 bold").grid(row=4,column=0,sticky=W)

output = Text(window, width=75, height=6,bd=7, wrap = WORD, background = "white")
output.grid(row=5, column=0, columnspan=2, stick=W)

Label(window,text="\nIf you want to add word,then enter:\n",bg="white",font="none 18 bold").grid(row=7,column=0,sticky=W)
Label(window,text="Word:",bg="white",font="none 18 bold").grid(row=8,column=0,sticky=W)

dictword=Entry(window,width=30,bd=7)
dictword.grid(row=9,column=0,sticky=W)

Label(window,text="Definition:",bg="white",font="none 18 bold").grid(row=8,column=1,sticky=W)

dict_dif=Entry(window,width=30,bd=7)
dict_dif.grid(row=9,column=1,pady=20,sticky=W)

Button(window,text="Add",width=6,font="none 10 bold",command=addWord).grid(row=10,column=0,sticky=W)

window.mainloop()

