import tkinter as tk

def calc():
    gas=var_gas.get()
    efficiency=var_eff.get()
    distance_str=var_dis.get()
    distance=int(distance_str)
    freeway_str=var_fre.get()
    freeway=int(freeway_str)
    car=var_car.get()
    num=var_num.get()
    res=(gas/efficiency*distance+freeway*2)*car/num
    label_7["text"]=round(res,0)

root=tk.Tk()
root.geometry("1600x900")

var_gas=tk.IntVar(value=160)
var_eff=tk.IntVar(value=10)
var_car=tk.IntVar(value=4)
var_num=tk.IntVar(value=20)

label_1=tk.Label(root,text="ガソリン代",font=("",24))
label_2=tk.Label(root,text="距離",font=("",24))
label_3=tk.Label(root,text="高速代",font=("",24))
label_4=tk.Label(root,text="燃費",font=("",24))
label_5=tk.Label(root,text="車の台数",font=("",24))
label_6=tk.Label(root,text="人数",font=("",24))
label_7=tk.Label(root,text="計算結果",font=("",24))

spinbox_1=tk.Spinbox(root,width=3,from_=0,to=200,font=("",24),increment=1,textvariable=var_gas)
var_dis=tk.Entry(root,width=5,font=("",24))
var_fre=tk.Entry(root,width=5,font=("",24))
spinbox_2=tk.Spinbox(root,width=2,from_=0,to=20,font=("",24),increment=1,textvariable=var_eff)
spinbox_3=tk.Spinbox(root,width=2,from_=0,to=10,font=("",24),increment=1,textvariable=var_car)
spinbox_4=tk.Spinbox(root,width=2,from_=0,to=50,font=("",24),increment=1,textvariable=var_num)

button_1=tk.Button(root,text="計算",font=("",24),command=calc)

for i in range(2):
    root.columnconfigure(i,weight=1)
for i in range(8):
    root.rowconfigure(i,weight=1)

label_1.grid(column=0,row=0)
spinbox_1.grid(column=1,row=0)
label_2.grid(column=0,row=1)
var_dis.grid(column=1,row=1)
label_3.grid(column=0,row=2)
var_fre.grid(column=1,row=2)
label_4.grid(column=0,row=3)
spinbox_2.grid(column=1,row=3)
label_5.grid(column=0,row=4)
spinbox_3.grid(column=1,row=4)
label_6.grid(column=0,row=5)
spinbox_4.grid(column=1,row=5)
button_1.grid(column=0,row=6,columnspan=2)
label_7.grid(column=0,row=7,columnspan=2)

root.mainloop()