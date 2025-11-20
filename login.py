import tkinter as tk
from tkinter import messagebox
def fetch():
    try:
        import mysql.connector
        conn2=mysql.connector.connect(
        host='localhost',
        user='root',
        password='seshupraveen3612',
        database='58r',
        port=3306,
        autocommit=False
        )
        curr=conn2.cursor(buffered=True)
        querry=('''  select * from login_db where user_name= %s  and pass_word= %s ''')
        values=(user_name1.get(),pass_word1.get())
        curr.execute(querry,values)
    except Exception as e:
        print(e)
        messagebox.showerror('error',e)
        print("Account not found")
    else:
        res=curr.fetchall()
        if res:
            print(f'Login Success  {res}')
            messagebox.showinfo('info','Login Success')
        else:
            print(f'Invalid username or password')
            messagebox.showerror('error',"Invalid username or password")
    finally:
        curr.close()
        conn2.close()
        messagebox
#tkinter gui
root=tk.Tk()
root.title("login form")
root.geometry("500x500")
#to enter user name
tk.Label(root,text="User Name:",font=("Arial",16)).grid(row=1,column=1)
user_name1=tk.Entry(root)
user_name1.grid(row=1,column=2,padx=100)
#for password
tk.Label(root,text="Enter Password:",font=("Ariel",16)).grid(row=2,column=1,padx=30)
pass_word1=tk.Entry(root,show='*')
pass_word1.grid(row=2,column=2,padx=100)
#submitbutton
tk.Button(root,text="Submit",command=fetch).grid(row=3,column=1,padx=50,pady=50)
root.mainloop()