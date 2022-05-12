if __name__=="__main__":
    #code has been written here
    import socket
    from tkinter import *
    from tkinter.filedialog import askopenfilename
    from tkinter import messagebox as ms
    print("succesfully loded code response(1)")
    s=socket.socket(socket.AF_INET)
    def sed():
        try:
            s.bind((sgh.get(),spor.get()))
            s.listen(2)
            con,addr=s.accept()
            print(f"Connected to {addr}")
            f=open(fil,"rb")
            data=f.read(2048)
            while data:
                con.send(data)
                data=f.read(2048)
            s.close()
            f.close()
            ms.showinfo("Indian Xender","File sent!!")
        except Exception as e:
            print(e)
            s.close()
            f.close()
            ms.showerror("Indian Xender","File not send")
            
    r=Tk()
    ms.showinfo("Indian Xender","If you are a reciver fill the reciver's entry\n  if you are a sender fill sender details")
    gh=StringVar()
    por=IntVar()
    sgh=StringVar()
    spor=IntVar()
    def fi():
        global fil
        fil=askopenfilename(filetypes=(("Textfiles","*.txt"),("All Files","*.*")))
        print(fil)
    def re():
        f=open("recv.txt","wb")
        try:
            s.connect((gh.get(),por.get()))
            obj=s.recv(2048)
            while obj:
                f.write(obj)
                obj=s.recv(2048)
            f.close()
            s.close()
            ms.showinfo("Indian Xender",f"File recived from {gh.get()} at port {por.get()}")
        except:
            ms.showerror("Indian Xender",f"No Inder service on {gh.get}  at port {por.get}")
            
    r.title("Indian build xender")
    Label(r,text="Indian Build Xender",font="lucida 16 bold",fg="blue").grid(row=0,column=0)
    Label(r,text="Sender column",font="lucida 13 bold",fg="Green").grid(row=1,column=0)
    Label(r,text="Enter your ip:-").grid(row=2,column=0)
    e=Entry(textvariable=sgh).grid(row=2,column=1)
    Label(r,text="Enter your port:-").grid(row=3,column=0)
    e=Entry(textvariable=spor).grid(row=3,column=1)
    Label(r,text="Reciver column",font="lucida 13 bold",fg="orange").grid(row=4,column=0)
    Label(r,text="Enter Reciver ip:-").grid(row=5,column=0)
    e=Entry(textvariable=gh).grid(row=5,column=1)
    Label(r,text="Enter Reciver port:-").grid(row=6,column=0)
    e=Entry(textvariable=por).grid(row=6,column=1)
    op=Button(r,text="Open File",bg="cyan",fg="white",padx=100,command=fi).grid(row=7,column=0)
    sen=Button(r,text="Send",bg="green",fg="white",padx=45,command=sed).grid(row=8,column=0)
    rec=Button(r,text="Recive",bg="orange",fg="white",padx=45,command=re).grid(row=8,column=1)
    r.mainloop()
elif __name__=="__main__":
    print("application has been crashed as main.py is'nt executed first")
