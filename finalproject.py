''' A simple tkinter software with db connectivity '''
''' software name : contact collection '''
''' software type : contact management system '''
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk #(in cmd : pip install pillow)
import pymysql                #(in cmd : pip install pymysql)
import re



### DB CONNECTION ###
try:
    con = pymysql.connect('localhost','root','root','myproject1')
    cur = con.cursor()
    print("db connected")
except:
    print("DB not connected")



class contactlst:
    def __init__(self):
        main_win = Tk()
        main_win.state("zoomed")
        main_win.title("contact list")
        bg_img =  Image.open ('contlst5.jpg')
        photo = ImageTk.PhotoImage(bg_img)
        img_label = Label(main_win,image = photo)
        img_label.pack()
        
        #add button
        add_btn = Button(main_win,text="+Add New Contact", command = self.add, activebackground="#A9A9A9",font=("arial",26,"bold"),fg="#ffffff",width=15,borderwidth=3,relief="raised",bg="#000000")
        add_btn.place(x=630,y=360)

        #view all contacts
        view_btn = Button(main_win,text="View All Contacts", command = self.view, activebackground="#A9A9A9",font=("arial",26,"bold"),fg="#ffffff",width=14,borderwidth=3,relief="raised",bg="#808080")
        view_btn.place(x=800,y=490)


        main_win.mainloop()

      ################# ADD NEW CONTACT  #####################
        

    def add(self):
        ad_win = Toplevel()
        ad_win.geometry("680x430")
        ad_win.resizable(0,0)
        ad_win.title("ADD NEW CONTACT")
        
        FormTitle = Frame(ad_win)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(ad_win)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm)
        Gender=StringVar()
        Male = Radiobutton(RadioGroup,variable=Gender, text="Male", value="Male",  font=('arial', 20,'bold')).pack(side=LEFT)
        Female = Radiobutton(RadioGroup,variable=Gender, text="Female", value="Female",  font=('arial', 20,'bold')).pack(side=LEFT)

        lbl_title = Label(FormTitle, text="Adding New Contacts", font=('arial', 24,'bold'),fg="#ffffff", bg="#5C246E",  width = 300)
        lbl_title.pack(fill=X)

        Name1 = Label(ContactForm, text="Name", font=('arial', 20,'bold'), bd=5)
        Name1.grid(row=0,column=0)
        Name = Entry(ContactForm, font=('arial', 20))
        Name.grid(row=0, column=1)

        Gender1 = Label(ContactForm, text="Gender", font=('arial', 20,'bold'), bd=5)
        Gender1.grid(row=1, column=0)
        RadioGroup.grid(row=1, column=1)
            
        DOB1 = Label(ContactForm, text="DOB(yyyy-mm-dd)", font=('arial', 20,'bold'), bd=5)
        DOB1.grid(row=2, column=0)
        DOB = Entry(ContactForm,  font=('arial', 20))
        DOB.grid(row=2, column=1)
            
        Address1 = Label(ContactForm, text="Address", font=('arial', 20,'bold'), bd=5)
        Address1.grid(row=3, column=0)
        Address = Entry(ContactForm, font=('arial', 20))
        Address.grid(row=3, column=1)
            
        Contact1 = Label(ContactForm, text="Contact", font=('arial', 20,'bold'), bd=5)
        Contact1.grid(row=4,column=0)
        Contact = Entry(ContactForm,  font=('arial', 20))
        Contact.grid(row=4, column=1)
            
        Email1 = Label(ContactForm, text="Email", font=('arial', 20,'bold'), bd=5)
        Email1.grid(row=5, column=0)
        Email = Entry(ContactForm, font=('arial', 20))
        Email.grid(row=5, column=1)




        #add function
        def SubmitData():
            if re.search('[0-9]',Name.get()):
                messagebox.showerror("Invalid","Incorrect Name")        

            elif(len(Name.get())!=0 and len(Contact.get())==10 and len(Address.get())!=0 ):
                try:
                    n=str(Name.get())
                    g=str(Gender.get())
                    b=str(DOB.get())
                    ad=str(Address.get())
                    c=int(Contact.get())
                    e=str(Email.get())
                    val=(n,g,b,ad,c,e)
                    sql1="""insert into contlst(nm, gen, bdt, addrs, contact,email) values(%s,%s,%s,%s,%s,%s)"""
                    cur.execute(sql1,val)
                    con.commit()
                    messagebox.showinfo("Success","Insertion Successful")
                except:
                    messagebox.showerror("DB error","data not inserted")
            else:
                messagebox.showerror("Invalid","Incorrect Data")        

        btn_addcon = Button(ContactForm, text="Save", width=20,font=('arial', 20,'bold'), command=SubmitData)
        btn_addcon.grid(row=6, columnspan=2, pady=10)


        

   

       ###################### view all contact ########################

    def view(self):
        vw_win = Toplevel()
        vw_win.resizable(0,0)
        vw_win.state("zoomed")
        vw_win.title("View all contacts")
        
        #scrollbar
        scr_bar = Scrollbar(vw_win)

        #mention number of columns
        cols=("column0","column1", "column2", "column3", "column4", "column5","column6")

        tree = ttk.Treeview(vw_win, column = cols, show = 'headings' , height=39, yscrollcommand = scr_bar.set ) 

        #treeview styling

        ttk.Style().theme_use('classic')
        ttk.Style().configure('Treeview',background = "#ffffff",foreground='#000000',font=('arial',16,'bold'))
        ttk.Style().configure("Treeview.Heading", background = '#5C246E',foreground="#ffffff",font=('arial',18,'bold'))
        tree.heading("#1",text="Id")
        tree.heading("#2",text="Name")
        tree.heading("#3",text="Gender")
        tree.heading("#4",text="DOB")
        tree.heading("#5",text="Address")
        tree.heading("#6",text="Contact")
        tree.heading("#7",text="Email")

        tree.place(x=10,y=100)

        #configuration of scroll bar
        scr_bar.place(x=1505,y=100,height=605)
        scr_bar.config(command = tree.yview)

        #updating window and adjusting column size
        for col in cols:
            tree.column("column0",width=50)
            tree.column("column1",width=280,anchor="center")
            tree.column("column2",width=150,anchor="center")
            tree.column("column3",width=150,anchor="center")
            tree.column("column4",width=300,anchor="center")
            tree.column("column5",width=180,anchor="center")
            tree.column("column6",width=400,anchor="center")

        vw_win.update()
        

        #fetching data from db and storing it in variable
        slct_query = """select*from contlst"""
        cur.execute(slct_query)
        rows = cur.fetchall()
        #print(rows)
        for row in rows:
            tree.insert("",END,values=row)

        def DeleteData():
            if not tree.selection():
                result = messagebox.showwarning('', 'Please Select Something First!', icon="warning")
            else:
                result = messagebox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
                if result == 'yes':
                    curItem = tree.focus()
                    contents =(tree.item(curItem))
                    selecteditem = contents['values']
                    tree.delete(curItem)
                    cur.execute("DELETE FROM contlst WHERE id = %d" % selecteditem[0])
                    con.commit()
                    
                    
        btn_delete = Button(vw_win, text="DELETE", command=DeleteData,activebackground="#7A378B",font=("arial",20,"bold"),fg="#ffffff",width=6,borderwidth=3,relief="raised",bg="#5C246E")
        btn_delete.place(x=1390,y=25)


        def update_address():
            updt_win = Toplevel()
            updt_win.geometry("400x200")
            updt_win.resizable(0,0) #disables maximize option of window
            updt_win.title("update address")

            FormTitle = Frame(updt_win)
            FormTitle.pack(side=TOP)
            ContactForm = Frame(updt_win)
            ContactForm.pack(side=TOP, pady=10)
            lbl_title = Label(FormTitle, text="updating address", font=('arial', 24,'bold'), fg="#ffffff", bg="#5C246E",  width = 300)
            lbl_title.pack(fill=X)

            id1 = Label(ContactForm, text="id", font=('arial', 14,'bold'), bd=5)
            id1.grid(row=0, column=0)
            id = Entry(ContactForm,  font=('arial', 14))
            id.grid(row=0, column=1)
            
            Address1 = Label(ContactForm, text="Address", font=('arial', 14,'bold'), bd=5)
            Address1.grid(row=1, column=0)
            Address = Entry(ContactForm, font=('arial', 14))
            Address.grid(row=1, column=1)


            def updtadd():
                try:
                    ad=str(Address.get())
                    i=int(id.get())
                    updt_query = "update contlst set addrs= '%s'  where id = '%s' " % (ad,i)
                    cur.execute(updt_query)
                    con.commit()
                    messagebox.showinfo("Success","Update Successful")
                    updt_win.destroy() #destroys or closes the window
                except:
                    messagebox.showinfo("Error","Update Unsuccessful")
                

            btn_updtcon = Button(ContactForm, text="update", width=50, command=updtadd)
            btn_updtcon.grid(row=6, columnspan=2, pady=10)
        
        btn_updt = Button(vw_win, text="UPDATE ADDRESS", command=update_address,activebackground="#7A378B",font=("arial",18,"bold"),fg="#ffffff",width=15,borderwidth=3,relief="raised",bg="#5C246E")
        btn_updt.place(x=80,y=30)
        
            
        def update_contact():
            updt_win = Toplevel()
            updt_win.geometry("400x200")
            updt_win.resizable(0,0) #disables maximize option of window
            updt_win.title("update contact")

            FormTitle = Frame(updt_win)
            FormTitle.pack(side=TOP)
            ContactForm = Frame(updt_win)
            ContactForm.pack(side=TOP, pady=10)
            lbl_title = Label(FormTitle, text="updating Contact", font=('arial', 24,'bold'), fg="#ffffff", bg="#5C246E",  width = 300)
            lbl_title.pack(fill=X)

            id1 = Label(ContactForm, text="id", font=('arial', 14), bd=5)
            id1.grid(row=0, column=0)
            id = Entry(ContactForm,  font=('arial', 14))
            id.grid(row=0, column=1)
            
            Contact1 = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
            Contact1.grid(row=1,column=0)
            Contact = Entry(ContactForm,  font=('arial', 14))
            Contact.grid(row=1, column=1)
            

            def updtcont():
                try:
                    c=int(Contact.get())
                    i=int(id.get())
                    updt_query = "update contlst set contact= '%s'  where id = '%s' " % (c,i)
                    cur.execute(updt_query)
                    con.commit()
                    messagebox.showinfo("Success","Update Successful")
                    updt_win.destroy() #destroys or closes the window
                except:
                    messagebox.showinfo("Error","Update Unsuccessful")
                

            btn_updtcon = Button(ContactForm, text="update", width=50, command=updtcont)
            btn_updtcon.grid(row=6, columnspan=2, pady=10)
        
        btn_updt = Button(vw_win, text="UPDATE CONTACT", command=update_contact,activebackground="#7A378B",font=("arial",18,"bold"),fg="#ffffff",width=15,borderwidth=3,relief="raised",bg="#5C246E")
        btn_updt.place(x=350,y=30)


        def update_email():
            updt_win = Toplevel()
            updt_win.geometry("400x200")
            updt_win.resizable(0,0) #disables maximize option of window
            updt_win.title("update email")

            FormTitle = Frame(updt_win)
            FormTitle.pack(side=TOP)
            ContactForm = Frame(updt_win)
            ContactForm.pack(side=TOP, pady=10)
            lbl_title = Label(FormTitle, text="updating Email", font=('arial', 24,'bold'), fg="#ffffff", bg="#5C246E",  width = 300)
            lbl_title.pack(fill=X)

            id1 = Label(ContactForm, text="id", font=('arial', 14), bd=5)
            id1.grid(row=0, column=0)
            id = Entry(ContactForm,  font=('arial', 14))
            id.grid(row=0, column=1)
            
            Email1 = Label(ContactForm, text="Email", font=('arial', 14), bd=5)
            Email1.grid(row=1, column=0)
            Email = Entry(ContactForm, font=('arial', 14))
            Email.grid(row=1, column=1)
            

            def updtemail():
                try:
                    e=str(Email.get())
                    i=int(id.get())
                    updt_query = "update contlst set email= '%s'  where id = '%s' " % (e,i)
                    cur.execute(updt_query)
                    con.commit()
                    messagebox.showinfo("Success","Update Successful")
                    updt_win.destroy() #destroys or closes the window
                except:
                    messagebox.showinfo("Error","Update Unsuccessful")
                

            btn_updtemail = Button(ContactForm, text="update", width=50, command=updtemail)
            btn_updtemail.grid(row=6, columnspan=2, pady=10)
        
        btn_updt = Button(vw_win, text="UPDATE EMAIL", command=update_email,activebackground="#7A378B",font=("arial",18,"bold"),fg="#ffffff",width=15,borderwidth=3,relief="raised",bg="#5C246E")
        btn_updt.place(x=620,y=30)


contactlst()
