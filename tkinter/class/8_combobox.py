import tkinter.ttk as ttk
from tkinter import  *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

values = [str(i) + "day" for i in range(1, 32)]
combobox = ttk.Combobox(root, height = 5, values = values) # ����ڰ� �Է°����� height�� �����ִ� ��ϰ���
combobox.pack()
combobox.set("card payment") #���ʸ���� ����

readonly_combobox = ttk.Combobox(root, height = 10, values = values, state = "readonly") # �б�����
readonly_combobox.current(0) #0��° �ε����� ��������
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # ���õ� ���� ���
    print(readonly_combobox.get())

btn = Button(root, text="selection", command=btncmd)
btn.pack()


root.mainloop()