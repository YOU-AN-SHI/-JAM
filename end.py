from tkinter import*
tk = Tk()
tk.title('window')
tk.geometry('1000x1000')
canvas = Canvas(tk,width=1000,height=1000)
canvas.pack(side=TOP)
canvas.create_text(520, 700, text='恭喜你過關囉~ 相比你的程式，你的眼力還算不錯呦~~~',fill = '#000000', font=('Arial', 20))
photo7 = PhotoImage(file='pange(7).gif')
photoL7 = Label(tk,image = photo7)
photoL7.place(x = 180 , y = 100)
tk.mainloop()