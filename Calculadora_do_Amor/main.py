from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

#CORES
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde

# JANELA --------------------------------------------------------------------------------------
janela = Tk()
janela.title("")
janela.geometry('410x400') #tamanho do ecrã
janela.configure(background=co1)
janela.resizable(width=FALSE,height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

janela.mainloop()
# FRAMES --------------------------------------------------------------------------------------

frameCima = Frame(janela, width=418, height=200, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=418, height=200, bg=co1, relief="solid")
frameMeio.grid(row=1, column=0)

# LOGO --------------------------------------------------------------------------------------
app_ = Label(frameCima,text="Calculadora do Amor",width=400, padx=5, relief=FLAT, anchor=NW, font=('Fixedsys 20'),bg=co7, fg=co1)
app_.place(x=0, y=0)