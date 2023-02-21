import tkinter as tk
class Calculator():
    def __init__(self,master):
        
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg = 'grey')
        master.resizable(False,False)
        
        self.Equation = tk.StringVar()
        self.entry_Value=''
        tk.Entry(width= 20, bg ='lightblue',font=('Times New Roman',28),textvariable=self.Equation).place(x=0,y=0)
        
        tk.Button(width=11,height=4,text='(',relief='flat',bg='white',command=lambda:self.show('(')).place(x=0,y=50)
        tk.Button(width=11,height=4,text=')',relief='flat',bg='white',command=lambda:self.show(')')).place(x=90,y=50)
        tk.Button(width=11,height=4,text='%',relief='flat',bg='white',command=lambda:self.show('%')).place(x=180,y=50)
        tk.Button(width=11,height=4,text='1',relief='flat',bg='white',command=lambda:self.show(1)).place(x=0,y=125)
        tk.Button(width=11,height=4,text='2',relief='flat',bg='white',command=lambda:self.show(2)).place(x=90,y=125)
        tk.Button(width=11,height=4,text='3',relief='flat',bg='white',command=lambda:self.show(3)).place(x=180,y=125)
        tk.Button(width=11,height=4,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=0,y=200)
        tk.Button(width=11,height=4,text='5',relief='flat',bg='white',command=lambda:self.show(5)).place(x=90,y=200)
        tk.Button(width=11,height=4,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=180,y=200)
        tk.Button(width=11,height=4,text='7',relief='flat',bg='white',command=lambda:self.show(7)).place(x=0,y=275)
        tk.Button(width=11,height=4,text='8',relief='flat',bg='white',command=lambda:self.show(8)).place(x=180,y=275)
        tk.Button(width=11,height=4,text='9',relief='flat',bg='white',command=lambda:self.show(9)).place(x=90,y=275)
        tk.Button(width=11,height=4,text='0',relief='flat',bg='white',command=lambda:self.show(0)).place(x=90,y=350)
        tk.Button(width=11,height=4,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=180,y=350)
        tk.Button(width=11,height=4,text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=270,y=275)
        tk.Button(width=11,height=4,text='-',relief='flat',bg='white',command=lambda:self.show('-')).place(x=270,y=200)
        tk.Button(width=11,height=4,text='/',relief='flat',bg='white',command=lambda:self.show('/')).place(x=270,y=50)
        tk.Button(width=11,height=4,text='x',relief='flat',bg='white',command=lambda:self.show('*')).place(x=270,y=125)
        tk.Button(width=11,height=4,text='=',relief='flat',bg='lightblue',command=self.solve).place(x=270,y=350)
        tk.Button(width=11,height=4,text='C',relief='flat',command=lambda:self.clear).place(x=0,y=350)
    def show(self,value):
        self.entry_Value+= str(value)
        self.Equation.set(self.entry_Value)
    def clear(self):
        self.entry_Value=''
        self.Equation.set(self.entry_Value)
    def solve(self):
        result = eval(self.entry_Value)
        self.Equation.set(result)
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

