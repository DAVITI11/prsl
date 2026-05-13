from tkinter import *
from tkinter import ttk

from Main import BaseHlpt as BsHl

root = Tk()
root.title("Product Sales")
root.geometry("1020x820")

frame = Frame(root)
frame.place(relx=0.5,rely=0.5,anchor="center")

PdSl = BsHl()
PdSl.create_tables()

slwnd, prdwnd, plw , sp, sw, t = None, None, None, None, None, None


def B1():
    global sw
    if sw is not None:
        return
    sw = Toplevel(root)
    sw.title("Student List")
    sw.geometry("500x400")

    tree = ttk.Treeview(sw)

    tree["columns"] = ("id", "name", "age")

    tree.column("#0", width=0, stretch=NO)

    tree.column("id", width=50)
    tree.column("name", width=200)
    tree.column("age", width=100)

    tree.heading("id", text="ID")
    tree.heading("name", text="Name")
    tree.heading("age", text="Age")

    tree.pack(fill=BOTH, expand=True)

    rows = PdSl.select_students()

    for row in rows:
        tree.insert("", END, values=row)
    def cl():
        global sw
        sw.destroy()
        sw = None
    clbt = Button(sw,text="გამოსვლა",command=cl)
    clbt.pack(pady=10)
    
Button1 = Button(frame,text="სტუდენტების სიის ნახვა",command=B1,width=30,height=2)
Button1.grid(column=1,row=1,padx=5,pady=5)


def B2():
    global slwnd
    if slwnd is not None:
        return
    slwnd = Toplevel(root)
    slwnd.title("add sales")
    slwnd.geometry("600x600")
    
    pdlb = Label(slwnd,width=35,height=2,text="შეიყვანე სტუდენტის სახელი",anchor="w")
    pdlb.grid(row=1,column=1,padx=5,pady=5)

    pdent = Entry(slwnd,width=30)
    pdent.grid(row=1,column=2,padx=5,pady=5)

    cnlb = Label(slwnd,width=35,height=2,text="შეიყვანეთ სტუდენტის ასაკი",anchor="w")
    cnlb.grid(row=2,column=1,padx=5,pady=5)

    cnent = Entry(slwnd,width=30)
    cnent.grid(row=2,column=2,padx=5,pady=5)

    erlb = Label(slwnd,width=35,height=2,text="")
    erlb.grid(row=5,column=1,columnspan=2,padx=5,pady=5)
    def sb():
        name = pdent.get()
        age = cnent.get()
        if (not name.strip() or not age.strip()):
            erlb.config(text="შეავსე ყველა ველი",fg="red")
        else:
            PdSl.add_student(name,age)
            erlb.config(text="წარმატებით დაემატა",fg="green")
            pdent.delete(0,END)
            cnent.delete(0,END)
            slwnd.after(3000,lambda: erlb.config(text=""))
    sbmbt = Button(slwnd,width=35,height=2,text="შენახვა",command=sb)
    sbmbt.grid(row=3,column=1,columnspan=2,padx=5,pady=5)

    def cl():
        global slwnd
        slwnd.destroy()
        slwnd = None
    clbt = Button(slwnd,width=35,height=2,command=cl,text="გამოსვლა")
    clbt.grid(row=4,column=1,columnspan=2,padx=5,pady=5)

Button2 = Button(frame,text="სტუდენტების დამატება",command=B2,width=30,height=2)
Button2.grid(column=1,row=2,padx=5,pady=5)

def B3():

    global sp

    if sp is not None and sp.winfo_exists():
        return

    sp = Toplevel(root)
    sp.title("Student List")
    sp.geometry("500x400")

    tree = ttk.Treeview(sp)

    tree["columns"] = ("name", "sb", "mark")

    tree.column("#0", width=0, stretch=NO)

    tree.column("name", width=120)
    tree.column("sb", width=150)
    tree.column("mark", width=80)

    tree.heading("name", text="Name")
    tree.heading("sb", text="Subject")
    tree.heading("mark", text="Mark")

    tree.pack(fill=BOTH, expand=True)

    def sb():

        for item in tree.get_children():
            tree.delete(item)

        id = ident.get()

        if not id.strip():
            return

        rows = PdSl.select_student_info(id)

        for row in rows:
            tree.insert("", END, values=row)

    def cl():

        global sp

        sp.destroy()
        sp = None
    ident = Entry(sp, width=35)
    ident.pack(pady=5)

    sbbt = Button(sp, width=30, command=sb, text="ნახვა")
    sbbt.pack(pady=5)

    clbt = Button(sp, width=30,text="გამოსვლა", command=cl)
    clbt.pack(pady=10)

    sp.protocol("WM_DELETE_WINDOW", cl)
Button3 = Button(frame,text="სტუდენტების ისტორიის ნახვა",width=30,height=2,command=B3)
Button3.grid(column=1,row=3,padx=5,pady=5)

def bg():
    global prdwnd
    if prdwnd is not None:
        return
    prdwnd = Toplevel(root)
    prdwnd.title("add sales")
    prdwnd.geometry("600x600")
    
    pdlb = Label(prdwnd,width=35,height=2,text="შეიყვანე სტუდენტის სახელი",anchor="w")
    pdlb.grid(row=1,column=1,padx=5,pady=5)

    pdent = Entry(prdwnd,width=30)
    pdent.grid(row=1,column=2,padx=5,pady=5)

    
    erlb = Label(prdwnd,width=35,height=2,text="")
    erlb.grid(row=5,column=1,columnspan=2,padx=5,pady=5)
    def sb():
        name = pdent.get()
        if (not name.strip()):
            erlb.config(text="შეავსე ყველა ველი",fg="red")
        else:
            PdSl.add_sb(name)
            erlb.config(text="წარმატებით დაემატა",fg="green")
            pdent.delete(0,END)
            prdwnd.after(3000,lambda: erlb.config(text=""))
    sbmbt = Button(prdwnd,width=35,height=2,text="შენახვა",command=sb)
    sbmbt.grid(row=3,column=1,columnspan=2,padx=5,pady=5)

    def cl():
        global prdwnd
        prdwnd.destroy()
        prdwnd = None
    clbt = Button(prdwnd,width=35,height=2,command=cl,text="გამოსვლა")
    clbt.grid(row=4,column=1,columnspan=2,padx=5,pady=5)

Bg = Button(frame,text="საგნების დამატება",width=30,height=2,command=bg)
Bg.grid(column=1,row=4,padx=5,pady=5)

def admk():
    global t
    if t is not None:
        return
    t = Toplevel(root)
    t.title("add sales")
    t.geometry("600x600")
    
    pdlb = Label(t,width=35,height=2,text="შეიყვანე სტუდენტის ID",anchor="w")
    pdlb.grid(row=1,column=1,padx=5,pady=5)

    pdent = Entry(t,width=30)
    pdent.grid(row=1,column=2,padx=5,pady=5)

    cnlb = Label(t,width=35,height=2,text="შეიყვანეთ საგნის ID",anchor="w")
    cnlb.grid(row=2,column=1,padx=5,pady=5)

    cnent = Entry(t,width=30)
    cnent.grid(row=2,column=2,padx=5,pady=5)

    mrk = Label(t,width=35,height=2,text="შეიყვანე ქულა",anchor="w")
    mrk.grid(row=3,column=1,padx=5,pady=5)

    mrkent = Entry(t,width=30)
    mrkent.grid(row=3,column=2,padx=5,pady=5)

    erlb = Label(t,width=35,height=2,text="")
    erlb.grid(row=6,column=1,columnspan=2,padx=5,pady=5)
    def sb():
        st_id = pdent.get()
        sb_id = cnent.get()
        mk = mrkent.get()
        if (not st_id.strip() or not sb_id.strip() or not mk.strip()):
            erlb.config(text="შეავსე ყველა ველი",fg="red")
        else:
            PdSl.add_mark(st_id,sb_id,mk)
            erlb.config(text="წარმატებით დაემატა",fg="green")
            pdent.delete(0,END)
            cnent.delete(0,END)
            mrkent.delete(0,END)
            
    sbmbt = Button(t,width=35,height=2,text="შენახვა",command=sb)
    sbmbt.grid(row=4,column=1,columnspan=2,padx=5,pady=5)

    def cl():
        global t
        t.destroy()
        t = None
    clbt = Button(t,width=35,height=2,command=cl,text="გამოსვლა")
    clbt.grid(row=5,column=1,columnspan=2,padx=5,pady=5)

admrk = Button(frame,text="ქულის დამატება",width=30,height=2,command=admk)
admrk.grid(column=1,row=5,padx=5,pady=5)

def B4():
    root.destroy()

Button4 = Button(frame,text="გამოსვლა",width=30,height=2,command=B4)
Button4.grid(column=1,row=6,padx=5,pady=5)
root.mainloop()