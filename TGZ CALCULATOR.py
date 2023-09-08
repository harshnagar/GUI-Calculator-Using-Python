from tkinter import *
from PIL import ImageTk, Image
import webbrowser
import tkinter.messagebox as mb
import ctypes

main = Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
main.tk.call('tk', 'scaling', 1.0)
main.geometry('250x400+550+100')
main.title("TGZ Calculator")
icon=ImageTk.PhotoImage(file="Themes/TGZ_Calculator.ico")
main.iconphoto(False, icon)
main.resizable(0,0)
img=PhotoImage(file="Themes/calcbg.png")
lb=Label(main,image=img).pack()
expression=""
final_result=StringVar()
entry_box=Entry(main,textvariable=final_result,bg="white",fg="red",relief=FLAT,font='100').place(x=18,y=20,width=214,height=46)
about_us_window=BooleanVar()


def press(num):
    global expression
    expression=expression+str(num)
    final_result.set(expression)


def equalsto():
    try:
        try:
            global exp1
            exp1=final_result.get()
            total=str(eval(exp1))
            final_result.set(total)

        except:
            global exp
            exp = final_result.get()
            total2=str(eval(exp))
            final_result.set(total2)
            exp=""
    except:
        final_result.set("0")
        expression=""


def cls():
    global expression
    expression=""
    final_result.set("")


def theme_default():
    img.config(file="Themes/calcbg.png")


def theme2():
    img.config(file="Themes/calcbg2.png")


def theme3():
    img.config(file="Themes/calcbg3.png")


def theme4():
    img.config(file="Themes/calcbg4.png")


def theme5():
    img.config(file="Themes/calcbg5.png")


def theme6():
    img.config(file="Themes/calcbg4.png")


def theme7():
    img.config(file="Themes/calcbg4.png")


def theme8():
    img.config(file="Themes/calcbg4.png")


def about_us(event):
    if about_us_window.get()==0:
        about_us_window.set(1)
        head = Toplevel()
        head.title("About Us")
        head.geometry("220x275+325+300")
        head.config(bg="black")
        head.resizable(0, 0)
        head.iconbitmap("Themes/TGZ_Calculator.ico")
        logo = PhotoImage(file="Themes/log.gif")
        tgz_logo = Label(head, image=logo, bg="blue", cursor="hand2")
        tgz_logo.pack()
        Label(head, bg="black", fg="white",
              text="Designed And Programmed By\n Harsh Nagar. For Any\n Help Email Us At -\n "
                   "nagar8339@gmail.com Or\n thegamerszone59@gmail.com.\n||Be Happy And "
                   "Programe Your Life||").pack()

        github_logo = ImageTk.PhotoImage(Image.open("Themes/github_image.png").resize((30, 30), Image.ANTIALIAS))
        github_label = Label(head, image=github_logo, text="Follow us on Github", compound=LEFT, cursor="hand2")
        github_label.place(x=20, y=150, width=180)
        instagram_logo = ImageTk.PhotoImage(Image.open("Themes/instagram_image.png").resize((30, 30), Image.ANTIALIAS))
        instagram_label = Label(head, image=instagram_logo, text="Follow us on Instagram", compound=LEFT,
                                cursor="hand2")
        instagram_label.place(x=20, y=190, width=180)
        facebook_logo = ImageTk.PhotoImage(Image.open("Themes/facebook_image.png").resize((50, 40), Image.ANTIALIAS))
        facebook_label = Label(head, image=facebook_logo, text="Follow us on Facebook", compound=LEFT, cursor="hand2")
        facebook_label.place(x=20, y=230, width=180, height=35)

        def open_tgz(event):
            webbrowser.open_new_tab("https://www.facebook.com/thegamerszoneofficial/")

        def open_github(event):
            webbrowser.open_new_tab("https://github.com/harshnagar")

        def open_instagram(event):
            webbrowser.open_new_tab("https://www.instagram.com/harshnagarx/")

        def open_facebook(event):
            webbrowser.open_new_tab("https://www.facebook.com/harshnagarx")

        def fb_bg_change(event):
            facebook_label.configure(bg="blue", fg="white")

        def fb_bg_change_2(event):
            facebook_label.configure(bg="white", fg="black")

        def insta_bg_change(event):
            instagram_label.configure(bg="blue", fg="white")

        def insta_bg_change_2(event):
            instagram_label.configure(bg="white", fg="black")

        def git_bg_change(event):
            github_label.configure(bg="blue", fg="white")

        def git_bg_change_2(event):
            github_label.configure(bg="white", fg="black")

        def tgz_bg_change(event):
            tgz_logo.configure(bg="red")

        def tgz_bg_change_2(event):
            tgz_logo.configure(bg="blue")

        tgz_logo.bind('<Button-1>', open_tgz)
        github_label.bind('<Button-1>', open_github)
        instagram_label.bind('<Button-1>', open_instagram)
        facebook_label.bind('<Button-1>', open_facebook)
        facebook_label.bind('<Enter>', fb_bg_change)
        facebook_label.bind('<Leave>', fb_bg_change_2)
        instagram_label.bind('<Enter>', insta_bg_change)
        instagram_label.bind('<Leave>', insta_bg_change_2)
        github_label.bind('<Enter>', git_bg_change)
        github_label.bind('<Leave>', git_bg_change_2)
        tgz_logo.bind('<Enter>', tgz_bg_change)
        tgz_logo.bind('<Leave>', tgz_bg_change_2)

        def destroy_about_us():
            about_us_window.set(0)
            head.destroy()

        head.protocol("WM_DELETE_WINDOW", destroy_about_us)
        head.mainloop()

    else:
        msg="About us Window is already Opened, Please close it then retry"
        mb.showinfo("Already Opened",msg)


bt=Button(main,text="1",bg="black",fg="white",relief=FLAT,command=lambda: press('1'),font='20')
bt.place(x=37,y=90,width=40,height=40)
bt2=Button(main,text="2",bg="black",fg="white",relief=FLAT,command=lambda: press('2'),font='20')
bt2.place(x=82,y=90,width=40,height=40)
bt3=Button(main,text="3",bg="black",fg="white",relief=FLAT,command=lambda: press('3'),font='20')
bt3.place(x=127,y=90,width=40,height=40)
bt4=Button(main,text="CE",bg="light green",fg="black",relief=FLAT,command=cls,font='20')
bt4.place(x=172,y=90,width=40,height=40)
bt5=Button(main,text="4",bg="black",fg="white",relief=FLAT,command=lambda: press('4'),font='20')
bt5.place(x=37,y=135,width=40,height=40)
bt6=Button(main,text="5",bg="black",fg="white",relief=FLAT,command=lambda: press('5'),font='20')
bt6.place(x=82,y=135,width=40,height=40)
bt7=Button(main,text="6",bg="black",fg="white",relief=FLAT,command=lambda: press('6'),font='20')
bt7.place(x=127,y=135,width=40,height=40)
bt8=Button(main,text="–",bg="light green",fg="black",relief=FLAT,command=lambda: press('-'),font='20')
bt8.place(x=172,y=135,width=40,height=40)
bt9=Button(main,text="7",bg="black",fg="white",relief=FLAT,command=lambda: press('7'),font='20')
bt9.place(x=37,y=180,width=40,height=40)
bt10=Button(main,text="8",bg="black",fg="white",relief=FLAT,command=lambda: press('8'),font='20')
bt10.place(x=82,y=180,width=40,height=40)
bt11=Button(main,text="9",bg="black",fg="white",relief=FLAT,command=lambda: press('9'),font='20')
bt11.place(x=127,y=180,width=40,height=40)
bt12=Button(main,text="*",bg="light green",fg="black",relief=FLAT,command=lambda: press('*'),font='100')
bt12.place(x=172,y=180,width=40,height=40)
bt13=Button(main,text="+",bg="light green",fg="black",relief=FLAT,command=lambda: press('+'),font='30')
bt13.place(x=37,y=225,width=40,height=40)
bt14=Button(main,text="0",bg="black",fg="white",relief=FLAT,command=lambda: press('0'),font='20')
bt14.place(x=82,y=225,width=40,height=40)
bt15=Button(main,text="/",bg="light green",fg="black",relief=FLAT,command=lambda: press('/'),font='20')
bt15.place(x=127,y=225,width=40,height=40)
bt16=Button(main,text="●",bg="light green",fg="black",relief=FLAT,command=lambda: press('.'),font='100')
bt16.place(x=172,y=225,width=40,height=40)
bt17=Button(main,text="Default",bg="orange",fg="black",relief=FLAT,command=theme_default)
bt17.place(x=37,y=285,width=40,height=40)
bt18=Button(main,text="1",bg="orange",fg="black",relief=FLAT,command=theme2,font='20')
bt18.place(x=80,y=285,width=20,height=40)
bt19=Button(main,text="2",bg="orange",fg="black",relief=FLAT,command=theme3,font='20')
bt19.place(x=103,y=285,width=20,height=40)
bt20=Button(main,text="3",bg="orange",fg="black",relief=FLAT,command=theme4,font='20')
bt20.place(x=126,y=285,width=20,height=40)
bt21=Button(main,text="4",bg="orange",fg="black",relief=FLAT,command=theme5,font='20')
bt21.place(x=149,y=285,width=20,height=40)

bt23=Button(main,text="=",bg="light green",fg="black",relief=FLAT,command=equalsto,font='20')
bt23.place(x=172,y=285,width=40,height=40)
lb2=Label(main,text="Themes",bg="black",fg="white",font="Agency").place(x=37,y=267,height=17,width=60)

TGZ_image=ImageTk.PhotoImage(Image.open("Themes/hg.png").resize((30, 30), Image.ANTIALIAS))
hg_Label=Label(main,image=TGZ_image,cursor="hand2")
hg_Label.place(x=210, y=360)
hg_Label.bind('<Button-1>', about_us)
main.mainloop()