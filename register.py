from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

def register():
    if entryfirstname.get() == '' or entrylastname.get() == '' or entryemail.get() == '' or entrycontact.get() == ''\
            or  entrypassword.get() == '' or entryconfirmpassword.get() == '' or comboquestion.get() == 'Select'\
            or entryanswer.get() == '':
        showerror('Error', "All Fields Are Required")

    elif entrypassword.get()!=entryconfirmpassword.get():
        showerror('Error', 'Password Missmatch')

    elif check.get()==0:
        showerror('Error', 'Please agree our terms and conditions')




root = Tk()
root.geometry('1350x710+0+10')
root.title('Registration Form')

bg = PhotoImage(file='bg.png')
bgLabel = Label(root, image=bg)
bgLabel.place(x=0, y=0)

registerFrame = Frame(root, bg='white', width=600, height=580)
registerFrame.place(x=635, y=30)

titleLabel = Label(registerFrame, text='Registration Form', font=('arial', 22, 'bold '), bg='white',
                   fg='gold',)
titleLabel.place(x=20, y=5)

firstnameLabel = Label(registerFrame, text='First Name', font=('times new roman', 18, 'bold'), bg='white',
                       fg='gray20', )
firstnameLabel.place(x=20, y=70)
entryfirstname = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entryfirstname.place(x=20, y=105, width=220)

lastnameLabel = Label(registerFrame, text='Last Name', font=('times new roman', 18, 'bold'), bg='white',
                      fg='gray20', )
lastnameLabel.place(x=350, y=70)
entrylastname = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entrylastname.place(x=350, y=105, width=220)

contactLabel = Label(registerFrame, text='Contact Number', font=('times new roman', 18, 'bold'), bg='white',
                     fg='gray20', )
contactLabel.place(x=20, y=175)
entrycontact = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entrycontact.place(x=20, y=210, width=220)

emailLabel = Label(registerFrame, text='Email', font=('times new roman', 18, 'bold'), bg='white', fg='gray20', )
emailLabel.place(x=350, y=175)
entryemail = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entryemail.place(x=350, y=210, width=220)

questionLabel = Label(registerFrame, text='Security Question', font=('times new roman', 18, 'bold'), bg='white',
                      fg='gray20', )
questionLabel.place(x=20, y=280)

comboquestion = ttk.Combobox(registerFrame, font=('times new roman', 16), state='readonly', justify=CENTER)
comboquestion['values'] = ('Select', 'Your First Pet Name?', 'Your Birth Place Name?', 'Your Best Friend Name?',
                           'Your Favourite Teacher?', 'Your Favourite Hobby?')
comboquestion.place(x=20, y=315, width=220)
comboquestion.current(0)

answerLabel = Label(registerFrame, text='Answer', font=('times new roman', 18, 'bold'), bg='white',
                    fg='gray20', )
answerLabel.place(x=350, y=280)
entryanswer = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entryanswer.place(x=350, y=315, width=220)

passwordLabel = Label(registerFrame, text='Password', font=('times new roman', 18, 'bold'), bg='white',
                      fg='gray20', )
passwordLabel.place(x=20, y=385)
entrypassword = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entrypassword.place(x=20, y=420, width=220)

confirmpasswordLabel = Label(registerFrame, text='Confirm Password', font=('times new roman', 18, 'bold'),
                             bg='white',
                             fg='gray20', )
confirmpasswordLabel.place(x=350, y=385)
entryconfirmpassword = Entry(registerFrame, font=('times new roman', 18), bg='lightgray')
entryconfirmpassword.place(x=350, y=420, width=220)

check = IntVar()
checkButton = Checkbutton(registerFrame, text='I Agree All The Terms & Conditions', onvalue=1,
                          offvalue=0, variable=check, font=('times new roman', 14, 'bold'))
checkButton.place(x=20, y=470)

button = PhotoImage(file='button.png')
registerbutton = Button(registerFrame, image=button, bd=0, cursor='hand2', command=register)
registerbutton.place(x=250, y=520)

loginimage = PhotoImage(file='login.png')
loginbutton1 = Button(root, image=loginimage, bd=0, cursor='hand2')
loginbutton1.place(x=240, y=315)

root.mainloop()
