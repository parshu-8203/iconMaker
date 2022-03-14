from tkinter import *

App = Tk()
App.title("Icon Creator")
App.geometry('300x150')
lbl = Label(App, text='Select the image')


def img_choose():
    global img
    from PIL import Image
    from tkinter import filedialog
    App.img_dir = filedialog.askopenfilename(initialdir='C:', title='Select Image', filetypes=(('PNG Images', '*.png'),
                                                                                           ('JPG Images', '*.jpg'),
                                                                                           ('All Images', '*.*')))
    img = Image.open(App.img_dir)


b = Button(App, text='Choose', command=img_choose)
lbl1 = Label(App, text='Select the icon size')
lt = [16, 24, 32, 48, 64, 128, 255]
fr = IntVar()
drop = OptionMenu(App, fr, *lt)
txt = Entry(App)


def img_convert():
    try:
        from PIL import Image
        img.save(f'{txt.get()}.ico', format='ICO', sizes=[(fr.get(), fr.get())])
        win = Toplevel()

        win.title('Success')
        msg = Label(win, text='Icon converted successfully')
        msg.pack()

        win.mainloop()
    except:
        win1 = Toplevel()
        win1.title('Failure')

        msg1 = Label(win1, text='Something went wrong')
        msg1.pack()

        win1.mainloop()


b2 = Button(App, text='Convert', foreground='blue', command=img_convert)


def img_preview():
    pre = Toplevel()
    pre.title('Preview')
    pre.iconbitmap(f'{txt.get()}.ico')

    msg = Label(pre, text='Check your icon!!!')
    msg.pack()

    pre.mainloop()


b3 = Button(App, text='Preview', foreground='blue', command=img_preview)
b3.grid(row=3, column=1, padx=10, pady=5)
b2.grid(row=3, column=0, padx=20, pady=5)
txt.grid(row=2, column=1, padx=10, pady=5)
lbl2 = Label(App, text='Enter the icon name')
lbl2.grid(row=2, column=0, padx=20, pady=5)
drop.grid(row=1, column=1, padx=10, pady=5)
lbl1.grid(row=1, column=0, padx=20, pady=5)
lbl.grid(row=0, column=0, padx=20, pady=5)
b.grid(row=0, column=1, padx=10, pady=5)

App.mainloop()
