import tkinter as tk
import requests

API_URL = 'https://api.myip.com'

class Window(tk.Tk):
  def __init__(self, master=None):
    tk.Tk.__init__(self, master)
    self.configure(background='black')
    self.attributes('-topmost', True)
    self.attributes('-alpha', 0.3)
    self.overrideredirect(True)
    self.geometry('200x40')
    self._offsety = 0
    self.bind('<Button-1>', self.clickwin)
    self.bind('<B1-Motion>', self.dragwin)
    self.get_ip()
  def dragwin(self, event):
    x = self.winfo_pointerx() - self._offsetx
    y = self.winfo_pointery() - self._offsety
    self.geometry('+{x}+{y}'.format(x=x, y=y))
  def clickwin(self, event):
    self._offsetx = event.x
    self._offsety = event.y
  def get_ip(self):
    res = requests.get(API_URL)
    data = res.json()
    if 'ip' in data:
      lbl = tk.Label(self, text=data['ip'], font=('Arial', 20), bg='#000000', fg='#1EE76A')
      lbl.pack(side='top', anchor='center')

if __name__ == '__main__':
  win = Window()
  win.mainloop()