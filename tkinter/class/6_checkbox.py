from tkinter import  *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

chkvar = IntVar() # chkvar�� int������ ���� �����Ѵ�
checkbox = Checkbutton(root, text="Don't watch today", variable = chkvar)
# checkbox.select() # �ڵ�����ó��
# checkbox.deselect() # ��������ó��
checkbox.pack()

chkvar2 = IntVar()
checkbox2 = Checkbutton(root, text = "Don't watch week", variable = chkvar2)
checkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: üũ���� 1: üũ
    print(chkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()