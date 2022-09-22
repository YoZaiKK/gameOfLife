import logging
from struct import pack
import threading
import time
from tkinter import Tk, Button, Label, ALL, EventType
from color_picker import pick_color
color = 0, 0, 0


def color_celula(root):
    color = pick_color(root)
    print(color)

def color_gradient():
    print('pick color')
    root = Tk()
    Label(root, text="This window will get closed after 3 seconds...",
          font=('Helvetica 20 bold')).pack(pady=20)
    print("Hola desde dentro de la funcion")
    Button(root, text="Elegir color para celula",
           command=lambda: color_celula(root)).place(x=50, y=50)
    root.mainloop()


def thread_function(name, palabra):
    if palabra:
        print(palabra)
    logging.info("Thread %s: starting", name)
    time.sleep(3)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,),
                         kwargs={'palabra': 'muy buenas'})
    y = threading.Thread(target=color_gradient)
    logging.info("Main    : before running thread")
    x.start()
    y.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")
    print(color)
