import tkinter as tk
from concurrent import futures
import time
 
thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)
 
class MainFrame(tk.Frame):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = tk.Label(self, text='not running')
        self.label.pack()
        self.listbox = tk.Listbox(self)
        self.listbox.pack()
        self.button = tk.Button(
            self, text='blocking task', command=self.on_button)
        self.button.pack(pady=15)
        self.pack()
 
    def on_button(self):
        print('Button clicked')
        thread_pool_executor.submit(self.blocking_code)
 
 
    def set_label_text(self, text=''):
        self.label['text'] = text
 
    def listbox_insert(self, item):
        self.listbox.insert(tk.END, item)
 
    def blocking_code(self):
        self.after(0, self.set_label_text, 'running')
 
        for number in range(5):
            self.after(0, self.listbox_insert, number)
            print(number)
            time.sleep(1)
 
        self.after(0, self.set_label_text, ' not running')
 
 
if __name__ == '__main__':
    app = tk.Tk()
    main_frame = MainFrame()
    app.mainloop()
