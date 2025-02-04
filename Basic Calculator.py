from tkinter import *

expression=''
def press(num):
    global expression
    expression=expression + str(num)
    text.set(expression)

def equal():
    try:
        global expression
        result=str(eval(expression))
        text.set(result)
        expression=''
    except:
        text.set('error')
        expression=''

def erase():
    global expression
    a=len(expression)
    expression=expression[:a-1]
    text.set(expression)

def clearall():
    global expression
    expression=''
    text.set(expression)
    

rj=Tk()
rj.title('calculator')
text=StringVar()

ebox=Entry(rj,textvariable=text).grid(columnspan=4,ipady=10,ipadx=30)

button1=Button(rj,text='1',command=lambda:press(1),height=2,width=5).grid(row=3,column=0,sticky=W)
button2=Button(rj,text='2',command=lambda:press(2),height=2,width=5).grid(row=3,column=1,sticky=W)
button3=Button(rj,text='3',command=lambda:press(3),height=2,width=5).grid(row=3,column=2,sticky=W)
button4=Button(rj,text='4',command=lambda:press(4),height=2,width=5).grid(row=4,column=0,sticky=W)
button5=Button(rj,text='5',command=lambda:press(5),height=2,width=5).grid(row=4,column=1,sticky=W)
button6=Button(rj,text='6',command=lambda:press(6),height=2,width=5).grid(row=4,column=2,sticky=W)
button7=Button(rj,text='7',command=lambda:press(7),height=2,width=5).grid(row=5,column=0,sticky=W)
button8=Button(rj,text='8',command=lambda:press(8),height=2,width=5).grid(row=5,column=1,sticky=W)
button9=Button(rj,text='9',command=lambda:press(9),height=2,width=5).grid(row=5,column=2,sticky=W)
button0=Button(rj,text='0',command=lambda:press(0),height=2,width=5).grid(row=6,column=1,sticky=W)
plus=Button(rj,text='+',command=lambda:press('+'),height=2,width=5).grid(row=3,column=3,sticky=W)
minus=Button(rj,text='-',command=lambda:press('-'),height=2,width=5).grid(row=4,column=3,sticky=W)
multiply=Button(rj,text='x',command=lambda: press('*'),height=2,width=5).grid(row=5,column=3,sticky=W)
divide=Button(rj,text='/',command=lambda:press('/'),height=2,width=5).grid(row=6,column=3,sticky=W)
decimal=Button(rj,text='.',command=lambda:press('.'),height=2,width=5).grid(row=6,column=0,sticky=W)
equal=Button(rj,text='=',command=equal,height=2,width=5).grid(row=6,column=2,sticky=W)
clear=Button(rj,text='<--',command=erase,height=2,width=5).grid(row=2,column=3,sticky=W)
clear=Button(rj,text='clear all',command=clearall,height=2,width=5).grid(row=2,column=0,sticky=W)
rj.mainloop()
