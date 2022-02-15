import tkinter
import sys

args = sys.argv
filePath = args[1]
f = open(filePath, 'r')
data = f.read()
f.close()

tkObj = tkinter.Tk()
tkObj.title("テキスト編集")
tkObj.geometry("800x1000")


def getTextInput():
    result = text.get("1.0", tkinter.END)
    uf = open(filePath, 'w')
    uf.write(result)
    uf.close()
    tkObj.destroy()


def cancelEdit():
    tkObj.destroy()


frame = tkinter.Frame(tkObj)
frame.pack(fill=tkinter.BOTH, expand=True)
text = tkinter.Text(frame)
vbar = tkinter.Scrollbar(frame, orient=tkinter.VERTICAL)
text.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
vbar.pack(side=tkinter.RIGHT, fill=tkinter.Y, expand=False)
text["yscrollcommand"] = vbar.set
vbar["command"] = text.yview
text.insert(1.0, data)

btnCancel = tkinter.Button(tkObj, text="Cancel", width=10, command=cancelEdit)
btnCancel.pack(side=tkinter.RIGHT)

btnRead = tkinter.Button(tkObj, text="OK", width=10, command=getTextInput)
btnRead.pack(side=tkinter.RIGHT)

tkObj.mainloop()
