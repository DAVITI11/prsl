from tkinter import *
from tkinter import ttk

from PrdSl import BaseHlpr as BsHl

root = Tk()
root.title("Product Sales")
root.geometry("1020x820")

frame = Frame(root)
frame.place(relx=0.5,rely=0.5,anchor="center")

PdSl = BsHl()
PdSl.create_tables()

slwnd, prdwnd, plw , sp, sw = None, None, None, None, None


def B1():
    global prdwnd
    if prdwnd is not None:
        return
    prdwnd = Toplevel(root)
    prdwnd.title("add product")
    prdwnd.geometry("600x600")
    
    nmlb = Label(prdwnd,text="შეიყვანე პროდუქციის დასახელება",width=35,height=2,anchor="w")
    nmlb.grid(row=1,column=1,padx=5,pady=5)

    nment = Entry(prdwnd,width=30)
    nment.grid(row=1,column=2,padx=5,pady=5)

    szlb = Label(prdwnd,text="შეიყვანე პროდუქციის ზომა",width=35,height=2,anchor="w")
    szlb.grid(row=2,column=1,padx=5,pady=5)

    szent = Entry(prdwnd,width=30)
    szent.grid(row=2,column=2,padx=5,pady=5)

    gtlb = Label(prdwnd,text="შეიყვანე მიღების ფასი",width=35,height=2,anchor="w")
    gtlb.grid(row=3,column=1,padx=5,pady=5)

    gtent = Entry(prdwnd,width=30)
    gtent.grid(row=3,column=2,padx=5,pady=5)

    sllb = Label(prdwnd,text="შეიყვანე გაყიდვის ფასი",width=35,height=2,anchor="w")
    sllb.grid(row=4,column=1,padx=5,pady=5)

    slent = Entry(prdwnd,width=30)
    slent.grid(row=4,column=2,padx=5,pady=5)

    cnlb = Label(prdwnd,text="შეიყვანე რაოდენობა",width=35,height=2,anchor="w")
    cnlb.grid(row=5,column=1,padx=5,pady=5)

    cnent = Entry(prdwnd,width=30)
    cnent.grid(row=5,column=2,padx=5,pady=5)

    erlb = Label(prdwnd,width=35,height=2,text="")
    erlb.grid(row=8,column=1,columnspan=2,padx=5,pady=5)
    
    def SavePrd():
        name = nment.get()
        size = szent.get()
        get_price = gtent.get()
        sale_price = slent.get()
        count = cnent.get()
        if (not name.strip() or not size.strip() or not get_price.strip() or not  sale_price.strip() or not count.strip()):
            erlb.config(text="შეიყვანე ყველა ველი",fg="red")
        else:
            PdSl.insert_prod(name,size,get_price,sale_price,count)
            nment.delete(0,END)
            szent.delete(0,END)
            gtent.delete(0,END)
            slent.delete(0,END)
            cnent.delete(0,END)
            erlb.config(text="პროდუქტი დაემატა ბაზაში",fg="green")
            prdwnd.after(3000,lambda: erlb.config(text=""))
            
        
    SbBt = Button(prdwnd,width=35,height=2,text="პროდუქციის დამატება",command=SavePrd)
    SbBt.grid(row=6,column=1,columnspan=2,padx=5,pady=5)

    def gm():
        global prdwnd
        prdwnd.destroy()
        prdwnd = None
    gmbt = Button(prdwnd,width=35,height=2,text="გამოსვლა",command=gm)
    gmbt.grid(row=7,column=1,columnspan=2,padx=5,pady=5)
    

    
Button1 = Button(frame,text="პროდუქციის დამატება",command=B1,width=30,height=2)
Button1.grid(column=1,row=1,padx=5,pady=5)


def B2():
    global slwnd
    if slwnd is not None:
        return
    slwnd = Toplevel(root)
    slwnd.title("add sales")
    slwnd.geometry("600x600")
    
    pdlb = Label(slwnd,width=35,height=2,text="შეიყვანე პროდუქციის ID",anchor="w")
    pdlb.grid(row=1,column=1,padx=5,pady=5)

    pdent = Entry(slwnd,width=30)
    pdent.grid(row=1,column=2,padx=5,pady=5)

    cnlb = Label(slwnd,width=35,height=2,text="შეიყვანეთ პროდუქტის რაოდენობა",anchor="w")
    cnlb.grid(row=2,column=1,padx=5,pady=5)

    cnent = Entry(slwnd,width=30)
    cnent.grid(row=2,column=2,padx=5,pady=5)

    erlb = Label(slwnd,width=35,height=2,text="")
    erlb.grid(row=5,column=1,columnspan=2,padx=5,pady=5)
    def sb():
        id = pdent.get()
        cnt = cnent.get()
        if (not id.strip() or not cnt.strip()):
            erlb.config(text="შეავსე ყველა ველი",fg="red")
        else:
            PdSl.sell_prod(id,cnt)
            erlb.config(text="წარმატებით დაემატა გაყიდვა",fg="green")
            pdent.delete(0,END)
            cnent.delete(0,END)
            slwnd.after(3000,lambda: erlb.config(text=""))
    sbmbt = Button(slwnd,width=35,height=2,text="გაყიდვის შენახვა",command=sb)
    sbmbt.grid(row=3,column=1,columnspan=2,padx=5,pady=5)

    def cl():
        global slwnd
        slwnd.destroy()
        slwnd = None
    clbt = Button(slwnd,width=35,height=2,command=cl,text="გამოსვლა")
    clbt.grid(row=4,column=1,columnspan=2,padx=5,pady=5)


Button2 = Button(frame,text="გაყიდვების დამატება",command=B2,width=30,height=2)
Button2.grid(column=1,row=2,padx=5,pady=5)

def B3():
    global sp
    if sp is not None:
        return
    
    sp = Toplevel(root)
    sp.title("Sales List")
    sp.geometry("600x600")

    idlb = Label(sp,width=30,height=2,text="შეიყვანე პროდუქტის ID")
    idlb.grid(column=1,row=1,padx=5,pady=5)

    ident = Entry(sp,width=30)
    ident.grid(row=1,column=2,padx=5,pady=5)

    def sb():
        id = ident.get()
        prf = PdSl.get_profit(id)
        if prf is None:
            shpr.config(text="პროდუქტი ვერ მოიძებნა")
            sp.after(5000,lambda: shpr.config(text=""))
        else:
            shpr.config(text=f"{id} პროდუტქის მოგებაა {prf}")
            sp.after(5000,lambda: shpr.config(text=""))

        
    sbbt = Button(sp,width=30,height=2,text="მოგების ნახვა",command=sb)
    sbbt.grid(column=1,row=2,columnspan=2,padx=5,pady=5)
    
    def gm():
        global sp
        sp.destroy()
        sp = None
    gmbt = Button(sp,width=30,height=2,command=gm,text="გამოსვლა")
    gmbt.grid(row=3,column=1,columnspan=2,padx=5,pady=5)

    shpr = Label(sp,width=30,height=2)
    shpr.grid(row=4,column=1,columnspan=2,padx=5,pady=5)

Button3 = Button(frame,text="მოგების ნახვა",width=30,height=2,command=B3)
Button3.grid(column=1,row=3,padx=5,pady=5)

def B4():
    global plw
    if plw is not None:
        return
    plw = Toplevel(root)
    plw.title("Product List")
    plw.geometry("600x600")

    tree = ttk.Treeview(plw)

    tree["columns"] = ("id","name","size","get_price","sale_price","count")

    tree.column("#0",width=0,stretch=NO)

    tree.column("id",width=50)
    tree.column("name",width=120)
    tree.column("size",width=80)
    tree.column("get_price",width=100)
    tree.column("sale_price",width=100)
    tree.column("count",width=80)

    tree.heading("id",text="ID")
    tree.heading("name",text="Name")
    tree.heading("size",text="Size")
    tree.heading("get_price",text="Buy price")
    tree.heading("sale_price",text="Sell price")
    tree.heading("count",text="Count")

    tree.pack(fill=BOTH,expand=True)

    rows = PdSl.select_prod()
    for i in rows:
        tree.insert("",END,values=i)
    def cl():
        global plw
        plw.destroy()
        plw = None
    clbt = Button(plw,text="გამოსვლა",command=cl)
    clbt.pack(pady=10)


Button4 = Button(frame,text="პროდუქციის სიის ნახვა",width=30,height=2,command=B4)
Button4.grid(column=1,row=4,padx=5,pady=5)
def B5():
    global sw
    if sw is not None:
        return
    sw = Toplevel(root)
    sw.title("Sales List")
    sw.geometry("500x400")

    tree = ttk.Treeview(sw)

    tree["columns"] = ("id", "name", "count")

    tree.column("#0", width=0, stretch=NO)

    tree.column("id", width=50)
    tree.column("name", width=200)
    tree.column("count", width=100)

    tree.heading("id", text="Sale ID")
    tree.heading("name", text="Product Name")
    tree.heading("count", text="Count")

    tree.pack(fill=BOTH, expand=True)

    rows = PdSl.select_sale()

    for row in rows:
        tree.insert("", END, values=row)
    def cl():
        global sw
        sw.destroy()
        sw = None
    clbt = Button(sw,text="გამოსვლა",command=cl)
    clbt.pack(pady=10)

Button5 = Button(frame,text="გაყიდვების სიის ნახვა",width=30,height=2,command=B5)
Button5.grid(column=1,row=5,padx=5,pady=5)

def B6():
    root.destroy()
Button6 = Button(frame,text="გამოსვლა",width=30,height=2,command=B6)
Button6.grid(column=1,row=6,padx=5,pady=5)

root.mainloop()