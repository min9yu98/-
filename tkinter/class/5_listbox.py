from tkinter import  *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode = "extended", height = 0) # extended:������ ���� , single:�Ѱ�����, height = 0�̸� �ٺ����ְ� height = 1�̸� �Ѱ��� ������

listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # listbox.delete(0) #�ǵڿ��� ���� 

    # ���� Ȯ��
    # print("list", listbox.size(), "count")

    # �׸� Ȯ�� (���� �ε���, �� �ε���)
    # print("1~3 num : ", listbox.get(0, 2))

    # ���õ� �׸� Ȯ��(��ġ��ȯ - �ε��� ���)
    print("selected part : ", listbox.curselection())

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()