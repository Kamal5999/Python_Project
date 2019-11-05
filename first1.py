from tkinter import  *
import os
import numpy as np
def register():
    global rs
    rs = Toplevel(ms)
    rs.geometry("500x500")
    rs.title("Register")

    global username
    global password
    global username_entry
    global password_entry
    global name
    global age
    global phone_no
    global name_entry
    global phone_entry
    global age_entry
    username = StringVar()
    password = StringVar()
    name=StringVar()
    age=StringVar()
    phone_no=StringVar()

    Label(rs, text="Please enter the  details ", bg="blue").pack(fill=X)
    Label(rs, text="").pack()
    username_lable = Label(rs, text="Username : ")
    username_lable.pack()
    username_entry = Entry(rs, textvariable=username)
    username_entry.pack()
    password_lable = Label(rs, text="Password : ")
 
    password_lable.pack()
    password_entry = Entry(rs, textvariable=password, show='*')
    password_entry.pack()
    Label(rs, text="please enter the personal details",bg="blue").pack(fill=X)
    Label(rs,text=" ").pack()
    Label(rs,text="Name: ").pack()
    name_entry=Entry(rs,textvariable=name)
    name_entry.pack()
    Label(rs,text="Age: ").pack()
    age_entry=Entry(rs,textvariable=age)
    age_entry.pack()
    Label(rs,text=":Phone no: ").pack()
    phone_entry=Entry(rs,textvariable=phone_no)
    phone_entry.pack()
    Label(rs,text=" ").pack()
    Button(rs, text="Register", height=1, bg="blue", command = register_user).pack()

def login():
    global ls
    ls = Toplevel(ms,bg="white")
    ls.geometry("500x500")
    ls.title("Login")
    Label(ls,bg="white",text="Please enter the details login").pack(fill="x")
    Label(ls,bg="white", text="").pack()

    global uv
    global pv

    uv = StringVar()
    pv = StringVar()

    global username_login_entry
    global password_login_entry

    Label(ls,bg="white", text="Username * ").pack()
    username_login_entry = Entry(ls, textvariable=uv)
    username_login_entry.pack()
    Label(ls,bg="white", text="").pack()
    Label(ls,bg="white", text="Password * ").pack()
    password_login_entry = Entry(ls, textvariable=pv, show= '*')
    password_login_entry.pack()
    Label(ls,bg="white", text="").pack()
    Button(ls,bg="black",fg="blue", text="Login",height=1, command = login_verify).pack()

def register_user():

    global username_info
    global password_info
    global name_info
    global age_info
    global phone_info
    username_info = username.get()
    password_info = password.get()
    name_info=name.get()
    age_info=age.get()
    phone_info=phone_no.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info+ "\n")
    file.write(age_info+ "\n")
    file.write(name_info+"\n")
    file.write(phone_info+"\n")
    file.close()
    username_info+="p"

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(rs, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    rs.destroy()

def login_verify():
    global username1
    global password1
    username1 = uv.get()
    password1 = pv.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            ls.destroy()
            restaurant()


        else:
            password_not_recognised()

    else:
        user_not_found()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(ls)
    password_not_recog_screen.title("Success")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(ls)
    user_not_found_screen.title("Success")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def restaurant():
    top=Toplevel(ms)
    top.geometry("500x500")
    Label(top, text="Please enter the details login",height="5",bg="blue").pack(fill="x")
    Label(top, text="").pack()
    Button(top,text=" OM SWEETS",height="2",width="30",bg="white",command=ok).pack()
    Button(top,text="QUALITY DHABA",height="2",width="30",bg="white",command=ok).pack()
    Button(top,text="DAANA PANI",height="2",width="30",bg="white",command=ok).pack()
    Button(top,text="SUKHDEV",height="2",width="30",bg="white",command=ok).pack()
    Button(top,text="MANNAT",height="2",width="30",bg="white",command=ok).pack()
    Button(top,text="HASHTAG",height="2",width="30",bg="white",command=ok).pack()
    Button(top,text="HUNGRY",height="2",width="30",bg="white",command=ok).pack()
    Button(top,text="TIKKA POINT",height="2",width="30",bg="white",command=ok).pack()

def ok():
     global jk
     global item
     jk=Toplevel(ms)
     jk.geometry("1800x900")
     Label(jk,text="MENU",height="3",width="1000",font=("calibri",18),bg="light green").pack(fill="x")
     def IND():
        

        label1=Label(jk,text="SELECT ITEM",bg="blue",fg="red",font=("bold",30))
        label1.pack(fill="x")
        lb=Listbox(jk,width=130,height=34)
        lb.insert(1,"1  SAMOSA ________________________________________ 25")
        lb.insert(2,"2  DOSA __________________________________________ 100")
        lb.insert(3,"3  KACHORI _______________________________________ 20")
        lb.insert(4,"4  ALOO PARATHA __________________________________ 50")
        lb.insert(5,"5  PLAIN PARATHA _________________________________ 30")
        lb.insert(6,"6  PANEER PARATHA ________________________________ 60")
        lb.place(x=300,y=90)     
        def function4():
                    clicked_item=lb.curselection()
                    item=lb.get(clicked_item)
                    advise() 
                    learning(item)
        Button(jk,text="SELECT",height="5",width="20",bg="red",fg="blue",command=function4).pack()
     def bevg():
        


        label1=Label(jk,text="SELECT ITEM",bg="blue",fg="red",font=("bold",30))
        label1.pack(fill="x")
        lb=Listbox(jk,width=130,height=34,selectmode="multiple")
        lb.insert(1,"1  COFFEE ________________________________________ 15")
        lb.insert(2,"2  TEA __________________________________________  10")
        lb.insert(3,"3  PEPSI _______________________________________ 35")
        lb.insert(4,"4  COLD COFFEE __________________________________ 50")
        lb.place(x=300,y=90)     
        def function4():

                    clicked_item=lb.curselection()
                    item=lb.get(clicked_item)
                    advise() 
                    learning(item)
        Button(jk,text="SELECT",height="5",width="20",bg="red",fg="blue",command=function4).pack()
     def DST():

        label1=Label(jk,text="SELECT ITEM",bg="blue",fg="red",font=("bold",30))
        label1.pack(fill="x")
        lb=Listbox(jk,width=130,height=34,selectmode="multiple")
        lb.insert(1,"1  GULAB JAMUN ________________________________ 25")
        lb.insert(2,"2  ICECREAM ___________________________________100")
        lb.insert(3,"3  CAKE _______________________________________ 20")
        lb.place(x=300,y=90)     
        def function4():
                    clicked_item=lb.curselection()
                    item=lb.get(clicked_item)
                    
                    advise() 
                    learning(item)
        Button(jk,text="SELECT",height="5",width="20",bg="red",fg="blue",command=function4).pack()
     def SNK():

        label1=Label(jk,text="SELECT ITEM",bg="blue",fg="red",font=("bold",30))
        label1.pack(fill="x")
        lb=Listbox(jk,width=130,height=34,selectmode="multiple")
        lb.insert(1,"1  VEG BURGER ________________________________________ 25")
        lb.insert(2,"2  CHICKEN BURGER____________________________________ 100")
        lb.insert(3,"3  SPRING ROLL _______________________________________ 20")
        lb.insert(4,"4  ALOO PARATHA __________________________________ 50")
        lb.place(x=300,y=90)     
        def function4():
                    clicked_item=lb.curselection()
                    item=lb.get(clicked_item)
                    
                    advise()
                    learning(item)
    
        Button(jk,text="SELECT",height="5",width="20",bg="red",fg="blue",command=function4).pack()

     Label(jk,height="200",width="200",image=snacks).place(x=20,y=100)
     Label(jk,height="200",width="200",image=beverage).place(x=500,y=100)
     Button(jk,text="Beverages",height="5",width="26",bg="white",command=bevg).place(x=500,y=310)
     Button(jk,text="Snacks",height="5",width="26",bg="white",command=SNK).place(x=20,y=310)
     Label(jk,height="200",width="200",image=desert).place(x=1000,y=100)
     Button(jk,text="desert",height="5",width="26",bg="white",command=DST).place(x=1000,y=310)
     Label(jk,height="200",width="200",image=indian).place(x=500,y=450)
     Button(jk,text="indian",height="5",width="26",bg="white",command=IND).place(x=500,y=660)

def advise():
    global adv
    global ansv
    ansv=StringVar()
    adv=Toplevel(ms)
    adv.geometry("1800x900")
    Label(adv,text="People also baught").pack(fill=X)
    Entry(adv,textvariable=ansv).pack(fill=X)

def learning(item):
    global ans
    row=5
    column=5
    map_dish={
        "1  SAMOSA ________________________________________ 25": 11,
        "2  DOSA __________________________________________ 100": 12,
        "3  KACHORI _______________________________________ 20": 13,
        "4  ALOO PARATHA __________________________________ 50": 14,
        "5  PLAIN PARATHA _________________________________ 30": 15,
        "6  PANEER PARATHA ________________________________ 60": 16,
        "1  COFFEE ________________________________________ 15": 21,
        "2  TEA __________________________________________  10": 22,
        "3  PEPSI _______________________________________ 35": 23,
        "4  COLD COFFEE __________________________________ 50":24

        }


    age_inf=StringVar()
    id_inf=username1
    f2=open(id_inf,"r")
    nf=f2.readline()
    pf=f2.readline()
    age_inf=f2.readline()
    f2.close()
    age_no=int(age_inf)

    item_no=map_dish[item]
    li=list()
    database=dict()
    database={
     21:(13,35,1),
     22:(15,50,1),
     23:(12,14,1),
     24:(14,24,1)
    }
    fans=1000000
    fset=0
    fstring=""
    for i in database:
        li=database[i]
        a1=li[0]-item_no
        b1=li[0]-age_no
        ans1=a1*a1+b1*b1
        if ans1<fans:
            fans=ans1
            fset=i
    p=1
    for i in map_dish:
        if map_dish[i]==fset:
            fstring=i
            p=0
            break
    if p==1:
        ansv.set(fset)
    else:
        ansv.set(fstring)




    # arr=[]
    # arr.append(age_no)
    # arr.append(map_dish("item"))
    #  matrix.append(arr)
    # ans=t_fres[0]+t_fres[1]*item_no+t_fres[2]*age_no
    # ansv.set(ans)


def location():
    lc=Toplevel(jk)
    pn=StringVar()
    add=StringVar()
    hno=StringVar()
    Label(lc,text="Enter your location",bg="yellow",height="5",font=("calibri",17)).pack(fill=X)
    Label(lc, text="pincode : ").pack()
    Entry(lc, textvariable=pn).pack()
    Label(lc, text="").pack()
    Label(lc, text="ADDRESS").pack()
    Entry(lc, textvariable=add).pack()
    Label(lc, text="").pack()
    Label(lc,text="HOUSE NO").pack()
    Entry(lc, text="house no",textvariable=hno,show="*").pack()
    Label(lc, text="").pack()
    Button(lc, text="Enter",command=payment).pack()
def payment():
    global ps
    ps=Toplevel(jk)
    ps.title("payment")
    Label(ps,text="Enter Card Details", bg="yellow", width="1000", height="3", font=("Calibri", 13)).pack(fill=X)
    Label(text="").pack()

    global cn
    global cey
    global cvv
    cn = StringVar()
    cey = StringVar()
    cvv = StringVar()


    Label(ps, text="Card No : ").pack()
    Entry(ps, textvariable=cn).pack()
    Label(ps, text="").pack()
    Label(ps, text="Card Expiry year : ").pack()
    Entry(ps, textvariable=cey).pack()
    Label(ps, text="").pack()
    Entry(ps, text="CVV",textvariable=cvv,show="*").pack()
    Label(ps, text="").pack()
    Button(ps, text="Enter",command=card_verify).pack()
    
def card_verify():
    cardn=cn.get()
    cardey=cey.get()
    cardvv=cvv.get()
    if len(cardn)!=16 or int(cardey)< 2019:
        incorrect()
    else :
        pay_success()

def pay_success():
    global pss
    pss= Toplevel(ps)
    pss.title("ticket booked")
    file=open(username_info,"a")
    file.write("train name: Gareeb Rath \n train no : 123456 \n Seat_no : D65")
    file.close()
    Label(pss, text="ticket booked").pack(fill="y")
    Button(pss, text="print ticket",command=print_ticket).pack()
def print_ticket():
    file=open(username_info,"r")
    print(file.read())
    main_account_screen()
def incorrect():
    global inc
    inc= Toplevel(ps)
    inc.title("incorrect")
    Label(inc, text="incorrect details").pack(fill="y")
    Button(inc, text="OK", command=delete_incorrect).pack()


def main_account_screen():
    global ms
    ms = Tk()
    global beverage
    global snacks
    global indian
    global desert
    beverage=PhotoImage(file="beverage.png")
    desert=PhotoImage(file="desert.png")
    indian=PhotoImage(file="indian.png")
    snacks=PhotoImage(file="snack.png")
    image2=PhotoImage(file="zam.png")
    image3=PhotoImage(file="i1.png")
    Label(text="Welcome to foodie",height="5",font=("calibri",14),bg="yellow").pack(fill=X)
    Label(text="Select Your Choice",height="300", font=("Calibri", 13),image=image2).pack(fill=X)
    Label(text="",bg="white").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="",bg="white").pack()
    Button(text="Register", height="2" ,width="30", command=register).pack()
    ms.configure(background="white")
    ms.mainloop()
main_account_screen()
