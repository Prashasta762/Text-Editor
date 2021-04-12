import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.font as tkfont
def text_editor():
  def undo():
    try:
      text_box.edit_undo()
    except tk.TclError:
      pass
  def redo():
    try:
      text_box.edit_redo()
    except tk.TclError:
      pass
  def open_file():
      filepath = askopenfilename(filetypes=[ ("All Files", "*.*"),("Text Files", "*.txt"),('HTML Document','*.html')])
      if not filepath:
          return
      text_box.delete(1.0, tk.END)
      with open(filepath, "r") as input_file:
          try:
            text = input_file.read()
          except UnicodeDecodeError:
            root=tk.Tk()
            message1=tk.Message(root,text="This File Format Isn't Supported.")
            message1.pack()
          else:
            text_box.insert(tk.END, text)
          input_file.close()
      window.title(filepath)
  def save_as():
      filepath = asksaveasfilename(defaultextension="txt",filetypes=[('HTML Document','*.html'),("Text Files", "*.txt"), ("All Files", "*.*")],)
      if not filepath:
          return
      with open(filepath, "w") as output_file:
          text = text_box.get(1.0, tk.END)
          output_file.write(text)
      window.title(filepath)
  def save():
    content=text_box.get(1.0,tk.END)
    file=window.title()
    try:
      filepath=open(file,'r')
    except FileNotFoundError:
      save_as()
    else:
      filepath=open(file,'w')
      filepath.write(content)
  def about_us():
    root=tk.Tk()
    message1=tk.Message(root,text="This Text Editor is Made using Python's Tkinter Module by Prashasta Vaish")
    message1.pack()
  def Help():
    root=tk.Tk()
    message2=tk.Message(root,text='''You can save,save as,open another file or 
    a new file using the file menu.You can cut,copy,paste,undo,redo,find,replace 
    using the edit menu.You can change the font style and size using customize menu''')
    message2.pack()
  def  font():
    root=tk.Tk()
    label3=tk.Label(root)
    label3.grid(row=1,column=2)
    def select_style(event=None):
      try:
       try:
        font_index=listbox.curselection()
        font_index=font_index[0]
       except NameError:
        font_index=0
       label3.configure(font=fontStyle, text=fonts[font_index])
       text_box.configure(font=fontStyle)
      except IndexError:
       pass
      return font_index
    def select_size(event=None):
      try:
       try:
        font_size=listbox2.curselection()
       except NameError:
        font_size=18
       label3.configure(font=fontSize)
       text_box.configure(font=fontSize)
      except tk.TclError:
        pass
      return font_size
    fonts=list(tkfont.families())
    fontindex =select_style()
    fontsize=select_size()
    fontStyle = tkfont.Font(family=fonts[fontindex])
    fontSize = tkfont.Font(size=fontsize)
    label1=tk.Label(root,text='font Style')
    label1.grid(row=0,column=0,sticky="ew")
    listbox=tk.Listbox(root,height=8,width=34,activestyle='dotbox',selectmode=tk.SINGLE)
    listbox2=tk.Listbox(root,height=8,width=34,activestyle='dotbox',selectmode=tk.SINGLE)
    listbox.bind('<<ListboxSelect>>',select_style)
    listbox2.bind('<<ListboxSelect>>',select_size)
    for i in range(601):
      listbox2.insert(tk.END,i)
    for font in fonts:
      listbox.insert(tk.END,font)
    label2=tk.Label(root,text='Font Size')
    label2.grid(row=2,column=0)
    scrollbar1 = tk.Scrollbar(root, orient="vertical", command=listbox2.yview)
    scrollbar1.grid(row=3, column=1, sticky="ns")
    listbox2.configure(yscrollcommand=scrollbar1.set)
    listbox2.grid(row=3,column=0)
    scrollbar2 = tk.Scrollbar(root, orient="vertical", command=listbox.yview)
    scrollbar2.grid(row=1, column=1, sticky="ns")
    listbox.configure(yscrollcommand=scrollbar2.set)
    listbox.grid(row=1,column=0,sticky="nsew")
  def find():
    root = tk.Tk() 
    fram = tk.Frame(root) 
    tk.Label(fram,text='Text to find:').pack(side=tk.LEFT)   
    edit = tk.Entry(fram)   
    edit.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)  
    edit.focus_set()  
    butt = tk.Button(fram, text='Find')   
    butt.pack(side=tk.RIGHT)  
    fram.pack(side=tk.TOP) 
    def find(): 
      text_box.tag_remove('found', '1.0', tk.END)  
      try: 
        s = edit.get()
      except AttributeError:
        s='' 
      if s: 
        idx = '1.0'
        while 1: 
            idx = text_box.search(s, idx, nocase=1,  
                              stopindex=tk.END)  
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))  
            text_box.tag_add('found', idx, lastidx)  
            idx = lastidx 
        text_box.tag_config('found',background='red',foreground='yellow')  
      edit.focus_set() 
    butt.config(command=find) 
    root.mainloop() 
  def replace():
    fram=tk.Tk()
    tk.Label(fram,text='Text to find:').grid(row=0,column=0)
    tk.Label(fram,text='Text to Replace:').grid(row=1,column=0)
    edit1= tk.Entry(fram)
    edit1.grid(row=0,column=1)  
    edit2= tk.Entry(fram)
    edit2.grid(row=1,column=1)   
    def find(): 
      text_box.tag_remove('found', '1.0', tk.END)  
      try: 
        s = edit1.get()
      except AttributeError:
        s='' 
      if s: 
        idx = '1.0'
        while 1: 
            idx = text_box.search(s, idx, nocase=1,  
                              stopindex=tk.END)  
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))  
            text_box.tag_add('found', idx, lastidx)  
            idx = lastidx 
        text_box.tag_config('found',background='red',foreground='yellow')  
      edit1.focus_set() 
    def replace():
      text_box.tag_remove('found', '1.0', tk.END)  
      s = edit1.get()
      r = edit2.get()
      if (s and r):  
        idx = '1.0'
        while 1:    
            idx = text_box.search(s, idx, nocase = 1,stopindex = tk.END)
            if not idx: 
              break
            lastidx = '% s+% dc' % (idx, len(s)) 
            text_box.delete(idx, lastidx) 
            text_box.insert(idx, r)
            lastidx = '% s+% dc' % (idx, len(r)) 
            text_box.tag_add('found', idx, lastidx)  
            idx = lastidx    
      edit1.focus_set() 
    butt1= tk.Button(fram, text='Find',command=find).grid(row=0,column=2)
    butt2= tk.Button(fram, text='Replace',command=replace).grid(row=0,column=2)   
    fram.mainloop()
  window = tk.Tk()
  window.title("Untitled-Text Editor")
  window.rowconfigure(0, minsize=800, weight=1)
  window.columnconfigure(1, minsize=800, weight=1)
  text_box = tk.Text(window,wrap=tk.WORD,undo=True)
  text_box.grid(row=0,column=1,sticky='nsew')
  scrollbar = tk.Scrollbar(window, orient="vertical", command=text_box.yview)
  scrollbar.grid(row=0, column=2, sticky="ns")
  text_box.configure(yscrollcommand=scrollbar.set)
  menubar=tk.Menu(window)
  window.config(menu=menubar)
  filemenu=tk.Menu(window,tearoff=0)
  filemenu.add_command(label='New',command=text_editor)
  filemenu.add_command(label='Open',command=open_file)
  filemenu.add_command(label='Save',command=save)
  filemenu.add_command(label='Save As',command=save_as)
  filemenu.add_separator()
  filemenu.add_command(label='Exit',command=window.destroy)
  menubar.add_cascade(label='File',menu=filemenu)
  editmenu=tk.Menu(window,tearoff=0)
  editmenu.add_command(label='Undo',command=undo)
  editmenu.add_command(label='Redo',command=redo)
  editmenu.add_separator()
  editmenu.add_command(label='Cut',command=lambda: text_box.event_generate('<<Cut>>'))
  editmenu.add_command(label='Copy',command=lambda: text_box.event_generate('<<Copy>>'))
  editmenu.add_command(label='Paste',command=lambda: text_box.event_generate('<<Paste>>'))
  editmenu.add_separator()
  editmenu.add_command(label='Find',command=find)
  editmenu.add_command(label='Replace',command=replace) 
  menubar.add_cascade(label='Edit',menu=editmenu)
  helpmenu=tk.Menu(window,tearoff=0)
  helpmenu.add_command(label='About Us',command=about_us)
  helpmenu.add_separator()
  helpmenu.add_command(label='View Help',command=Help)
  menubar.add_cascade(label="Help",menu=helpmenu)
  customizemenu=tk.Menu(window,tearoff=0)
  customizemenu.add_command(label='Font Settings',command=font)
  menubar.add_cascade(label="Customize",menu=customizemenu)
  window.mainloop()
text_editor()
