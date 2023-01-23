from calendar import month
from math import nan
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import requests
import lxml.html
import pandas as pd
import numpy as np
import datetime
import os
import glob
import re
import locale
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from tkinter.filedialog import FileDialog
import tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        #Configuración de aspecto
        self.title('Extractor de datos')
        self.resizable(0,0)
        self.geometry('800x500')    
        
            #Variables  globales
        #Path 
        self.path = tk.StringVar()
        self.ruta = ChromeService(ChromeDriverManager().install())

            #Variables de selección
        #China
        self.cn_reservas = tk.IntVar()
        self.cn_tipo_de_cambio = tk.IntVar()
        self.cn_exportaciones = tk.IntVar()
        self.cn_liquidez = tk.IntVar()
        self.cn_solvencia = tk.IntVar()
        self.cn_portafolio = tk.IntVar()
        self.cn_deuda = tk.IntVar()
        self.cn_pbi = tk.IntVar()
        self.cn_inflacion = tk.IntVar()

        #Japon
        self.jp_reservas = tk.IntVar()
        self.jp_tipo_de_cambio = tk.IntVar()
        self.jp_exportaciones = tk.IntVar()
        self.jp_liquidez = tk.IntVar()
        self.jp_solvencia = tk.IntVar()
        self.jp_portafolio = tk.IntVar()
        self.jp_deuda = tk.IntVar()
        self.jp_pbi = tk.IntVar()
        self.jp_inflacion = tk.IntVar()

        #Mexico
        self.mx_reservas = tk.IntVar()
        self.mx_tipo_de_cambio = tk.IntVar()
        self.mx_exportaciones = tk.IntVar()
        self.mx_liquidez = tk.IntVar()
        self.mx_solvencia = tk.IntVar()
        self.mx_portafolio = tk.IntVar()
        self.mx_deuda = tk.IntVar()
        self.mx_pbi = tk.IntVar()
        self.mx_inflacion = tk.IntVar()

        #Union Europea
        self.ue_reservas = tk.IntVar()
        self.ue_tipo_de_cambio = tk.IntVar()
        self.ue_exportaciones = tk.IntVar()
        self.ue_liquidez = tk.IntVar()
        self.ue_solvencia = tk.IntVar()
        self.ue_portafolio = tk.IntVar()
        self.ue_deuda = tk.IntVar()
        self.ue_pbi = tk.IntVar()
        self.ue_inflacion = tk.IntVar()

        #Estados Unidos
        self.us_reservas = tk.IntVar()
        self.us_tipo_de_cambio = tk.IntVar()
        self.us_exportaciones = tk.IntVar()
        self.us_liquidez = tk.IntVar()
        self.us_solvencia = tk.IntVar()
        self.us_portafolio = tk.IntVar()
        self.us_deuda = tk.IntVar()
        self.us_pbi = tk.IntVar()
        self.us_inflacion = tk.IntVar()

        #Pantalla principal
        self.errores = tk.Text(self)
        self.errores.grid(row=1, column=1, rowspan=5, columnspan=3,padx=5,sticky=tk.E+tk.W+tk.S+tk.N)

        #botones país:
        btn_cn = tk.Button(self, text="China", command = self.cn_SelectionWindow).grid(row=1,column=0,padx=5, pady = 5,sticky=tk.E+tk.W+tk.S+tk.N)
        btn_jp = tk.Button(self, text="Japon", command = self.jp_SelectionWindow).grid(row=2,column=0,padx=5, pady = 5,sticky=tk.E+tk.W+tk.S+tk.N)
        btn_mex = tk.Button(self, text="Mexico", command = self.mx_SelectionWindow).grid(row=3,column=0,padx=5, pady = 5 ,sticky=tk.E+tk.W+tk.S+tk.N)
        btn_us = tk.Button(self, text="Estados Unidos", command = self.us_SelectionWindow).grid(row=4,column=0,padx=5, pady = 5 ,sticky=tk.E+tk.W+tk.S+tk.N)
        btn_ue = tk.Button(self, text="Union Europea", command = self.ue_SelectionWindow).grid(row=5,column=0,padx=5, pady = 5,sticky=tk.E+tk.W+tk.S+tk.N)
        
        #boton extracción:
        btn_extaer = tk.Button(self, text="Extraer", command=self.Extract).grid(row=6,column=0,padx=10, pady = 10,sticky=tk.E+tk.W+tk.S+tk.N)

        #boton procesado:
        btn_procesado = tk.Button(self, text="Procesar", command=self.Procesar).grid(row=7,column=0,padx=10, pady = 10,sticky=tk.E+tk.W+tk.S+tk.N)
        
        #selector de path
        label = tk.Label(self, text='Ubicación: ').grid(row=6,column=1, padx=(5,0), sticky=tk.W+tk.S+tk.N+tk.E)
        entry = tk.Entry(self, text='Seleccione una Ubicación', textvariable=self.path).grid(row=6,column=2, padx = (0,5), columnspan=1, sticky=tk.W+tk.E)
        btn_path = tk.Button(self, text="Seleccionar", command=self.select_path).grid(row=6,column=3,sticky=tk.E+tk.W)
    
        #Labels:
        label_pais = tk.Label(self, text="Pais").grid(row=0, column=0)
        label_error = tk.Label(self, text="Error").grid(row=0, column=1)

    def select_path(self):
        path = tk.filedialog.askdirectory()
        self.path.set(path)
        print(path)

    def root_destroy_cn(self, root):
        if self.cn_reservas.get() == 1:
            self.errores.insert(tk.END, "cn_reservas seleccionado\n")
        if self.cn_tipo_de_cambio.get() == 1:
            self.errores.insert(tk.END, "cn_tipo_de_cambio seleccionado\n")
        if self.cn_exportaciones.get() == 1:
            self.errores.insert(tk.END, "cn_exportaciones seleccionado\n")
        if self.cn_liquidez.get() == 1:
            self.errores.insert(tk.END, "cn_liquidez seleccionado\n")
        if self.cn_solvencia.get() == 1:
            self.errores.insert(tk.END, "cn_solvencia seleccionado\n")
        if self.cn_portafolio.get() == 1:
            self.errores.insert(tk.END, "cn_portafolio seleccionado\n")
        if self.cn_deuda.get() == 1:
            self.errores.insert(tk.END, "cn_deuda seleccionado\n")
        if self.cn_pbi.get() == 1:
            self.errores.insert(tk.END, "cn_pbi seleccionado\n")
        if self.cn_inflacion.get() == 1:
            self.errores.insert(tk.END, "cn_inflacion seleccionado\n")
        root.destroy()
        
    def root_destroy_jp(self, root):
        if self.jp_reservas.get() == 1:
            self.errores.insert(tk.END, "jp_reservas seleccionado\n")
        if self.jp_tipo_de_cambio.get() == 1:
            self.errores.insert(tk.END, "jp_tipo_de_cambio seleccionado\n")
        if self.jp_exportaciones.get() == 1:
            self.errores.insert(tk.END, "jp_exportaciones seleccionado\n")
        if self.jp_liquidez.get() == 1:
            self.errores.insert(tk.END, "jp_liquidez seleccionado\n")
        if self.jp_solvencia.get() == 1:
            self.errores.insert(tk.END, "jp_solvencia seleccionado\n")
        if self.jp_portafolio.get() == 1:
            self.errores.insert(tk.END, "jp_portafolio seleccionado\n")
        if self.jp_deuda.get() == 1:
            self.errores.insert(tk.END, "jp_deuda seleccionado\n")
        if self.jp_pbi.get() == 1:
            self.errores.insert(tk.END, "jp_pbi seleccionado\n")
        if self.jp_inflacion.get() == 1:
            self.errores.insert(tk.END, "jp_inflacion seleccionado\n")
        root.destroy()

    def root_destroy_mx(self, root):
        if self.mx_reservas.get() == 1:
            self.errores.insert(tk.END, "mx_reservas seleccionado\n")
        if self.mx_tipo_de_cambio.get() == 1:
            self.errores.insert(tk.END, "mx_tipo_de_cambio seleccionado\n")
        if self.mx_exportaciones.get() == 1:
            self.errores.insert(tk.END, "mx_exportaciones seleccionado\n")
        if self.mx_liquidez.get() == 1:
            self.errores.insert(tk.END, "mx_liquidez seleccionado\n")
        if self.mx_solvencia.get() == 1:
            self.errores.insert(tk.END, "mx_solvencia seleccionado\n")
        if self.mx_portafolio.get() == 1:
            self.errores.insert(tk.END, "mx_portafolio seleccionado\n")
        if self.mx_deuda.get() == 1:
            self.errores.insert(tk.END, "mx_deuda seleccionado\n")
        if self.mx_pbi.get() == 1:
            self.errores.insert(tk.END, "mx_pbi seleccionado\n")
        if self.mx_inflacion.get() == 1:
            self.errores.insert(tk.END, "mx_inflacion seleccionado\n")
        root.destroy()

    def root_destroy_ue(self, root):
        if self.ue_reservas.get() == 1:
            self.errores.insert(tk.END, "ue_reservas seleccionado\n")
        if self.ue_tipo_de_cambio.get() == 1:
            self.errores.insert(tk.END, "ue_tipo_de_cambio seleccionado\n")
        if self.ue_exportaciones.get() == 1:
            self.errores.insert(tk.END, "ue_exportaciones seleccionado\n")
        if self.ue_liquidez.get() == 1:
            self.errores.insert(tk.END, "ue_liquidez seleccionado\n")
        if self.ue_solvencia.get() == 1:
            self.errores.insert(tk.END, "ue_solvencia seleccionado\n")
        if self.ue_portafolio.get() == 1:
            self.errores.insert(tk.END, "ue_portafolio seleccionado\n")
        if self.ue_deuda.get() == 1:
            self.errores.insert(tk.END, "ue_deuda seleccionado\n")
        if self.ue_pbi.get() == 1:
            self.errores.insert(tk.END, "ue_pbi seleccionado\n")
        if self.ue_inflacion.get() == 1:
            self.errores.insert(tk.END, "ue_inflacion seleccionado\n")
        root.destroy()

    def root_destroy_us(self, root):
        if self.us_reservas.get() == 1:
            self.errores.insert(tk.END, "us_reservas seleccionado\n")
        if self.us_tipo_de_cambio.get() == 1:
            self.errores.insert(tk.END, "us_tipo_de_cambio seleccionado\n")
        if self.us_exportaciones.get() == 1:
            self.errores.insert(tk.END, "us_exportaciones seleccionado\n")
        if self.us_liquidez.get() == 1:
            self.errores.insert(tk.END, "us_liquidez seleccionado\n")
        if self.us_solvencia.get() == 1:
            self.errores.insert(tk.END, "us_solvencia seleccionado\n")
        if self.us_portafolio.get() == 1:
            self.errores.insert(tk.END, "us_portafolio seleccionado\n")
        if self.us_deuda.get() == 1:
            self.errores.insert(tk.END, "us_deuda seleccionado\n")
        if self.us_pbi.get() == 1:
            self.errores.insert(tk.END, "us_pbi seleccionado\n")
        if self.us_inflacion.get() == 1:
            self.errores.insert(tk.END, "us_inflacion seleccionado\n")
        root.destroy()

        #Funciones para ventanas de selección
    #China
    def cn_SelectionWindow(self):
        root=tk.Toplevel()
        root.title("Datos China")
        root.geometry("280x300")
        chk_cn_reservas = tk.Checkbutton(root, text="Reservas", variable=self.cn_reservas,onvalue=1, offvalue=0).grid(row=0,column=0,sticky=tk.W, padx=2, pady=2)
        chk_cn_tipo_de_cambio = tk.Checkbutton(root, text="Tipo_de_cambio", variable=self.cn_tipo_de_cambio,onvalue=1, offvalue=0).grid(row=1,column=0,sticky=tk.W, padx=2, pady=2)
        chk_cn_exportaciones = tk.Checkbutton(root, text="Exportaciones", variable=self.cn_exportaciones,onvalue=1, offvalue=0).grid(row=2,column=0,sticky=tk.W, padx=2, pady=2)
        chk_cn_liquidez = tk.Checkbutton(root, text="Liquidez", variable=self.cn_liquidez,onvalue=1, offvalue=0).grid(row=3,column=0,sticky=tk.W, padx=2, pady=2)
        chk_cn_solvencia = tk.Checkbutton(root, text="Solvencia", variable=self.cn_solvencia,onvalue=1, offvalue=0).grid(row=4,column=0,sticky=tk.W, padx=2, pady=2)
        chk_cn_portafolio = tk.Checkbutton(root, text="Portafolio", variable=self.cn_portafolio,onvalue=1, offvalue=0).grid(row=5,column=0,sticky=tk.W, padx=2, pady=2)
        chk_cn_deuda = tk.Checkbutton(root, text="Deuda", variable=self.cn_deuda,onvalue=1, offvalue=0).grid(row=6,column=0,sticky=tk.W, padx=2, pady=2)
        chk_cn_pbi = tk.Checkbutton(root, text="Pbi", variable=self.cn_pbi,onvalue=1, offvalue=0).grid(row=7,column=0,sticky=tk.W, padx=2, pady=2)
        chk_cn_inflacion = tk.Checkbutton(root, text="Inflacion", variable=self.cn_inflacion,onvalue=1, offvalue=0).grid(row=8,column=0,sticky=tk.W, padx=2, pady=2)
        bt_extraer = tk.Button(root, text="Seleccionar", command=lambda: self.root_destroy_cn(root)).grid(row=9,column=0,sticky=tk.W, padx=2, pady=2)

    #Japon
    def jp_SelectionWindow(self):
        root=tk.Toplevel()
        root.title("Datos Japón")
        root.geometry("280x300")
        chk_jp_reservas = tk.Checkbutton(root, text="Reservas", variable=self.jp_reservas,onvalue=1, offvalue=0).grid(row=0,column=0,sticky=tk.W, padx=2, pady=2)
        chk_jp_tipo_de_cambio = tk.Checkbutton(root, text="Tipo_de_cambio", variable=self.jp_tipo_de_cambio,onvalue=1, offvalue=0).grid(row=1,column=0,sticky=tk.W, padx=2, pady=2)
        chk_jp_exportaciones = tk.Checkbutton(root, text="Exportaciones", variable=self.jp_exportaciones,onvalue=1, offvalue=0).grid(row=2,column=0,sticky=tk.W, padx=2, pady=2)
        chk_jp_liquidez = tk.Checkbutton(root, text="Liquidez", variable=self.jp_liquidez,onvalue=1, offvalue=0).grid(row=3,column=0,sticky=tk.W, padx=2, pady=2)
        chk_jp_solvencia = tk.Checkbutton(root, text="Solvencia", variable=self.jp_solvencia,onvalue=1, offvalue=0).grid(row=4,column=0,sticky=tk.W, padx=2, pady=2)
        chk_jp_portafolio = tk.Checkbutton(root, text="Portafolio", variable=self.jp_portafolio,onvalue=1, offvalue=0).grid(row=5,column=0,sticky=tk.W, padx=2, pady=2)
        chk_jp_deuda = tk.Checkbutton(root, text="Deuda", variable=self.jp_deuda,onvalue=1, offvalue=0).grid(row=6,column=0,sticky=tk.W, padx=2, pady=2)
        chk_jp_pbi = tk.Checkbutton(root, text="Pbi", variable=self.jp_pbi,onvalue=1, offvalue=0).grid(row=7,column=0,sticky=tk.W, padx=2, pady=2)
        chk_jp_inflacion = tk.Checkbutton(root, text="Inflacion", variable=self.jp_inflacion,onvalue=1, offvalue=0).grid(row=8,column=0,sticky=tk.W, padx=2, pady=2)
        bt_extraer = tk.Button(root, text="Seleccionar", command=lambda: self.root_destroy_jp(root)).grid(row=9,column=0,sticky=tk.W, padx=2, pady=2)

    #Mexico
    def mx_SelectionWindow(self):
        root=tk.Toplevel()
        root.title("Datos Mexico")
        root.geometry("280x300")
        chk_mx_reservas = tk.Checkbutton(root, text="Reservas", variable=self.mx_reservas,onvalue=1, offvalue=0).grid(row=0,column=0,sticky=tk.W, padx=2, pady=2)
        chk_mx_tipo_de_cambio = tk.Checkbutton(root, text="Tipo_de_cambio", variable=self.mx_tipo_de_cambio,onvalue=1, offvalue=0).grid(row=1,column=0,sticky=tk.W, padx=2, pady=2)
        chk_mx_exportaciones = tk.Checkbutton(root, text="Exportaciones", variable=self.mx_exportaciones,onvalue=1, offvalue=0).grid(row=2,column=0,sticky=tk.W, padx=2, pady=2)
        chk_mx_liquidez = tk.Checkbutton(root, text="Liquidez", variable=self.mx_liquidez,onvalue=1, offvalue=0).grid(row=3,column=0,sticky=tk.W, padx=2, pady=2)
        chk_mx_solvencia = tk.Checkbutton(root, text="Solvencia", variable=self.mx_solvencia,onvalue=1, offvalue=0).grid(row=4,column=0,sticky=tk.W, padx=2, pady=2)
        chk_mx_portafolio = tk.Checkbutton(root, text="Portafolio", variable=self.mx_portafolio,onvalue=1, offvalue=0).grid(row=5,column=0,sticky=tk.W, padx=2, pady=2)
        chk_mx_deuda = tk.Checkbutton(root, text="Deuda", variable=self.mx_deuda,onvalue=1, offvalue=0).grid(row=6,column=0,sticky=tk.W, padx=2, pady=2)
        chk_mx_pbi = tk.Checkbutton(root, text="Pbi", variable=self.mx_pbi,onvalue=1, offvalue=0).grid(row=7,column=0,sticky=tk.W, padx=2, pady=2)
        chk_mx_inflacion = tk.Checkbutton(root, text="Inflacion", variable=self.mx_inflacion,onvalue=1, offvalue=0).grid(row=8,column=0,sticky=tk.W, padx=2, pady=2)
        bt_extraer = tk.Button(root, text="Seleccionar", command=lambda: self.root_destroy_mx(root)).grid(row=9,column=0,sticky=tk.W, padx=2, pady=2)

    #Union Europea
    def ue_SelectionWindow(self):
        root=tk.Toplevel()
        root.title("Datos UE")
        root.geometry("280x300")
        chk_ue_reservas = tk.Checkbutton(root, text="Reservas", variable=self.ue_reservas,onvalue=1, offvalue=0).grid(row=0,column=0,sticky=tk.W, padx=2, pady=2)
        chk_ue_tipo_de_cambio = tk.Checkbutton(root, text="Tipo_de_cambio", variable=self.ue_tipo_de_cambio,onvalue=1, offvalue=0).grid(row=1,column=0,sticky=tk.W, padx=2, pady=2)
        chk_ue_exportaciones = tk.Checkbutton(root, text="Exportaciones", variable=self.ue_exportaciones,onvalue=1, offvalue=0).grid(row=2,column=0,sticky=tk.W, padx=2, pady=2)
        chk_ue_liquidez = tk.Checkbutton(root, text="Liquidez", variable=self.ue_liquidez,onvalue=1, offvalue=0).grid(row=3,column=0,sticky=tk.W, padx=2, pady=2)
        chk_ue_solvencia = tk.Checkbutton(root, text="Solvencia", variable=self.ue_solvencia,onvalue=1, offvalue=0).grid(row=4,column=0,sticky=tk.W, padx=2, pady=2)
        chk_ue_portafolio = tk.Checkbutton(root, text="Portafolio", variable=self.ue_portafolio,onvalue=1, offvalue=0).grid(row=5,column=0,sticky=tk.W, padx=2, pady=2)
        chk_ue_deuda = tk.Checkbutton(root, text="Deuda", variable=self.ue_deuda,onvalue=1, offvalue=0).grid(row=6,column=0,sticky=tk.W, padx=2, pady=2)
        chk_ue_pbi = tk.Checkbutton(root, text="Pbi", variable=self.ue_pbi,onvalue=1, offvalue=0).grid(row=7,column=0,sticky=tk.W, padx=2, pady=2)
        chk_ue_inflacion = tk.Checkbutton(root, text="Inflacion", variable=self.ue_inflacion,onvalue=1, offvalue=0).grid(row=8,column=0,sticky=tk.W, padx=2, pady=2)
        bt_extraer = tk.Button(root, text="Seleccionar", command=lambda: self.root_destroy_ue(root)).grid(row=9,column=0,sticky=tk.W, padx=2, pady=2)

    #Estados Unidos
    def us_SelectionWindow(self):
        root=tk.Toplevel()
        root.title("Datos US")
        root.geometry("280x300")
        chk_us_reservas = tk.Checkbutton(root, text="Reservas", variable=self.us_reservas,onvalue=1, offvalue=0, command=lambda: print(self.us_reservas.get())).grid(row=0,column=0,sticky=tk.W, padx=2, pady=2)
        chk_us_tipo_de_cambio = tk.Checkbutton(root, text="Tipo_de_cambio", variable=self.us_tipo_de_cambio,onvalue=1, offvalue=0).grid(row=1,column=0,sticky=tk.W, padx=2, pady=2)
        chk_us_exportaciones = tk.Checkbutton(root, text="Exportaciones", variable=self.us_exportaciones,onvalue=1, offvalue=0).grid(row=2,column=0,sticky=tk.W, padx=2, pady=2)
        chk_us_liquidez = tk.Checkbutton(root, text="Liquidez", variable=self.us_liquidez,onvalue=1, offvalue=0).grid(row=3,column=0,sticky=tk.W, padx=2, pady=2)
        chk_us_solvencia = tk.Checkbutton(root, text="Solvencia", variable=self.us_solvencia,onvalue=1, offvalue=0).grid(row=4,column=0,sticky=tk.W, padx=2, pady=2)
        chk_us_portafolio = tk.Checkbutton(root, text="Portafolio", variable=self.us_portafolio,onvalue=1, offvalue=0).grid(row=5,column=0,sticky=tk.W, padx=2, pady=2)
        chk_us_deuda = tk.Checkbutton(root, text="Deuda", variable=self.us_deuda,onvalue=1, offvalue=0).grid(row=6,column=0,sticky=tk.W, padx=2, pady=2)
        chk_us_pbi = tk.Checkbutton(root, text="Pbi", variable=self.us_pbi,onvalue=1, offvalue=0).grid(row=7,column=0,sticky=tk.W, padx=2, pady=2)
        chk_us_inflacion = tk.Checkbutton(root, text="Inflacion", variable=self.us_inflacion,onvalue=1, offvalue=0).grid(row=8,column=0,sticky=tk.W, padx=2, pady=2)
        bt_extraer = tk.Button(root, text="Seleccionar", command=lambda: self.root_destroy_us(root)).grid(row=9,column=0,sticky=tk.W, padx=2, pady=2)

        #Reseteo de variables:
    def flush(self):
    #China
        self.cn_reservas.set(0)
        self.cn_tipo_de_cambio.set(0)
        self.cn_exportaciones.set(0)
        self.cn_liquidez.set(0)
        self.cn_solvencia.set(0)
        self.cn_portafolio.set(0)
        self.cn_deuda.set(0)
        self.cn_pbi.set(0)
        self.cn_inflacion.set(0)

    #Japón
        self.jp_reservas.set(0)
        self.jp_tipo_de_cambio.set(0)
        self.jp_exportaciones.set(0)
        self.jp_liquidez.set(0)
        self.jp_solvencia.set(0)
        self.jp_portafolio.set(0)
        self.jp_deuda.set(0)
        self.jp_pbi.set(0)
        self.jp_inflacion.set(0)

    #Mexico
        self.mx_reservas.set(0)
        self.mx_tipo_de_cambio.set(0)
        self.mx_exportaciones.set(0)
        self.mx_liquidez.set(0)
        self.mx_solvencia.set(0)
        self.mx_portafolio.set(0)
        self.mx_deuda.set(0)
        self.mx_pbi.set(0)
        self.mx_inflacion.set(0)

    #Unión Europea
        self.ue_reservas.set(0)
        self.ue_tipo_de_cambio.set(0)
        self.ue_exportaciones.set(0)
        self.ue_liquidez.set(0)
        self.ue_solvencia.set(0)
        self.ue_portafolio.set(0)
        self.ue_deuda.set(0)
        self.ue_pbi.set(0)
        self.ue_inflacion.set(0)

    #Estados Unidos
        self.us_reservas.set(0)
        self.us_tipo_de_cambio.set(0)
        self.us_exportaciones.set(0)
        self.us_liquidez.set(0)
        self.us_solvencia.set(0)
        self.us_portafolio.set(0)
        self.us_deuda.set(0)
        self.us_pbi.set(0)
        self.us_inflacion.set(0)

    def create_driver(self):
        driver = webdriver.Chrome(service = self.ruta)
        return driver

    def write_to_path(self, df, país):
        #1.- Decides donde se va a poner el dato
        if país == 'US':
            archivo = 'indicadores_trimestrales_US.xlsx'
            #Cambia el archivo
        elif país == 'MX':
            archivo = 'indicadores_trimestrales_MX.xlsx'
            #Cambia
        elif país == 'UE':
            archivo = 'indicadores_trimestrales_UE.xlsx'
            #Cambia
        elif país == 'CN':
            archivo = 'indicadores_trimestrales_CN.xlsx'
            #Cambia
        elif país == 'JP':
            archivo = 'indicadores_trimestrales_JP.xlsx'
            #Cambia el archivo
        else:
            print('??') # Acá va una excepción

        #2 .- Extrae del dataframe el nombre del dato:
        nombre = df.columns[0]

        #3 .- Genera la ubicación del archivo
        ubicacion = self.path.get() + '/' + archivo

        #print(df.head())
        try:
            writer = pd.ExcelWriter(ubicacion, if_sheet_exists = 'replace', mode='a')
        except:
            writer = pd.ExcelWriter(ubicacion)
        df.to_excel(writer, sheet_name = nombre)
        writer.save()

    def Procesar(self):
        ruta = self.path.get()
        for ruta in glob.glob(ruta+"/indicadores_trimestrales_*.xlsx"):
            print(ruta)
            archivo = pd.ExcelFile(ruta)
            fichas = archivo.sheet_names
            if ("Exportaciones" in fichas) & ('Deuda Externa' in fichas):
                Exportaciones = archivo.parse(sheet_name="Exportaciones")[['Fecha','Exportaciones']].set_index('Fecha')
                print(Exportaciones)
                Deuda = archivo.parse(sheet_name = "Deuda Externa")[['Fecha', 'Deuda Externa']].set_index('Fecha')
                print(Deuda)
            Deuda_Export = pd.DataFrame()
            Deuda_Export['Deuda_Export'] = Deuda['Deuda Externa']/Exportaciones['Exportaciones']
            print(Deuda_Export)
            df = self.episodios_estilo(Deuda_Export)
            self.write_to_path(df, ruta[-7:-5])

    def Extract(self):
        #Validación del path:
    
        path = self.path.get()
        if len(path) < 2:
            self.errores.insert(tk.END, "Porfavor ingrese la ubicación del archivo\n")
        else:
            #China
            ##CREAR UN METODO DE DRIVER.RELOAD()

            if self.cn_reservas.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_cn_reservas(driver)
                    self.errores.insert(tk.END,"Correcta extracción de cn_reservas\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de cn_reservas\n")               
                
            if self.cn_tipo_de_cambio.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_cn_tipo_de_cambio(driver)
                    self.errores.insert(tk.END,"Correcta extracción de cn_tipo_de_cambio\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de cn_tipo_de_cambio\n")                   


            if self.cn_exportaciones.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_cn_exportaciones(driver)
                    self.errores.insert(tk.END,"Correcta extracción de cn_exportaciones\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de cn_exportaciones\n")             

            if self.cn_liquidez.get()==1 and self.cn_solvencia.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_cn_liquidez_solvencia(driver)
                    self.errores.insert(tk.END,"Correcta extracción de cn_solvencia\n")
                    self.errores.insert(tk.END,"Correcta extracción de cn_liquidez\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de cn_solvencia\n")
                    self.errores.insert(tk.END,"Error en extracción de cn_liquidez\n")                           
            
            elif self.cn_liquidez.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_cn_liquidez(driver)
                    self.errores.insert(tk.END,"Correcta extracción de cn_liquidez\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de cn_liquidez\n")
            
        
            elif self.cn_solvencia.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_cn_solvencia(driver)
                    self.errores.insert(tk.END,"Correcta extracción de cn_solvencia\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de cn_solvencia\n")

            if self.cn_portafolio.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_cn_portafolio(driver)
                    self.errores.insert(tk.END,"Correcta extracción de cn_portafolio\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de cn_portafolio\n")           


            if self.cn_deuda.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_cn_deuda(driver)
                    self.errores.insert(tk.END,"Correcta extracción de cn_deuda\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de cn_deuda\n")                     
       
     
            if self.cn_pbi.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_cn_pbi(driver)
                    self.errores.insert(tk.END,"Correcta extracción de cn_pbi\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de cn_pbi\n")                

            if self.cn_inflacion.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_cn_inflacion(driver)
                    self.errores.insert(tk.END,"Correcta extracción de cn_inflacion\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de cn_inflacion\n")

            #Japon
            if self.jp_reservas.get()==1:
                try:
                    self.ex_jp_reservas()
                    self.errores.insert(tk.END,"Correcta extracción de jp_reservas\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de jp_reservas\n")
            if self.jp_tipo_de_cambio.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_jp_tipo_de_cambio(driver)
                    self.errores.insert(tk.END,"Correcta extracción de jp_tipo_de_cambio\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de jp_tipo_de_cambio\n")

            if self.jp_exportaciones.get()==1:
                try:
                    self.ex_jp_exportaciones()
                    self.errores.insert(tk.END,"Correcta extracción de jp_exportaciones\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de jp_exportaciones\n")           

                self.ex_jp_exportaciones()
                self.errores.insert(tk.END,"Correcta extracción de jp_exportaciones\n")

            if self.jp_liquidez.get()==1:
                try:
                    self.ex_jp_liquidez()
                    self.errores.insert(tk.END,"Correcta extracción de jp_liquidez\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de jp_liquidez\n")
            if self.jp_solvencia.get()==1:
                try:
                    self.ex_jp_solvencia()
                    self.errores.insert(tk.END,"Correcta extracción de jp_solvencia\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de jp_solvencia\n")
            if self.jp_portafolio.get()==1:
                try:
                    self.ex_jp_portafolio()
                    self.errores.insert(tk.END,"Correcta extracción de jp_portafolio\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de jp_portafolio\n")
            if self.jp_deuda.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_jp_deuda(driver)
                    self.errores.insert(tk.END,"Correcta extracción de jp_deuda\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de jp_deuda\n")               
            if self.jp_pbi.get()==1:
                try:
                    self.ex_jp_pbi()
                    self.errores.insert(tk.END,"Correcta extracción de jp_pbi\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de jp_pbi\n")
            if self.jp_inflacion.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_jp_inflacion(driver)
                    self.errores.insert(tk.END,"Correcta extracción de jp_inflacion\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de jp_inflacion\n")

            #Mexico
            if self.mx_reservas.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_mx_reservas(driver)
                    self.errores.insert(tk.END,"Correcta extracción de mx_reservas\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de mx_reservas\n")                

            if self.mx_tipo_de_cambio.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_mx_tipo_de_cambio(driver)
                    self.errores.insert(tk.END,"Correcta extracción de mx_tipo_de_cambio\n")
                except:
                    self.errores.insert(tk.END, "Error en extracción de mx_tipo_de_cambio\n")           

            
            if self.mx_exportaciones.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_mx_exportaciones(driver)
                    self.errores.insert(tk.END,"Correcta extracción de mx_exportaciones\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de mx_exportaciones\n")                 
  
            if self.mx_liquidez.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_mx_liquidez(driver)
                    self.errores.insert(tk.END,"Correcta extracción de mx_liquidez\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de mx_liquidez\n")                  

            if self.mx_solvencia.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_mx_solvencia(driver)
                    self.errores.insert(tk.END,"Correcta extracción de mx_solvencia\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de mx_solvencia\n")               


            if self.mx_portafolio.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_mx_portafolio(driver)
                    self.errores.insert(tk.END,"Correcta extracción de mx_portafolio\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de mx_portafolio\n")              
 

            if self.mx_deuda.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_mx_deuda(driver)
                    self.errores.insert(tk.END,"Correcta extracción de mx_deuda\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de mx_deuda\n")                   
            

            if self.mx_pbi.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_mx_pbi(driver)                
                    self.errores.insert(tk.END,"Correcta extracción de mx_pbi\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de mx_pbi\n")            


            if self.mx_inflacion.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_mx_inflacion(driver)                
                    self.errores.insert(tk.END,"Correcta extracción de mx_inflacion\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de mx_inflacion\n")              

            #Union Europea
            if self.ue_reservas.get()==1:
                try:
                    self.ex_ue_reservas()
                    self.errores.insert(tk.END,"Correcta extracción de ue_reservas\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de ue_reservas\n")               


            if self.ue_tipo_de_cambio.get()==1:
                try:
                    self.ex_ue_tipo_de_cambio()
                    self.errores.insert(tk.END,"Correcta extracción de ue_tipo_de_cambio\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de ue_tipo_de_cambio\n")
            if self.ue_exportaciones.get()==1:
                try:
                    self.ex_ue_exportaciones()
                    self.errores.insert(tk.END,"Correcta extracción de ue_exportaciones\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de ue_exportaciones\n")
            if self.ue_liquidez.get()==1:
                try:
                    self.ex_ue_liquidez()
                    self.errores.insert(tk.END,"Correcta extracción de ue_liquidez\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de ue_liquidez\n")
            if self.ue_solvencia.get()==1:  
                try:
                    self.ex_ue_solvencia()
                    self.errores.insert(tk.END,"Correcta extracción de ue_solvencia\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de ue_solvencia\n")
            if self.ue_portafolio.get()==1:
                try:
                    self.ex_ue_portafolio()
                    self.errores.insert(tk.END,"Correcta extracción de ue_portafolio\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de ue_portafolio\n")
            if self.ue_deuda.get()==1:
                try:
                    self.ex_ue_deuda()
                    self.errores.insert(tk.END,"Correcta extracción de ue_deuda\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de ue_deuda\n")
            if self.ue_pbi.get()==1:
                try:
                    self.ex_ue_pbi()
                    self.errores.insert(tk.END,"Correcta extracción de ue_pbi\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de ue_pbi\n")
            if self.ue_inflacion.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_ue_inflacion(driver)
                    self.errores.insert(tk.END,"Correcta extracción de ue_inflacion\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de ue_inflacion\n")               
              
            #Estados Unidos
            if self.us_reservas.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_us_reservas(driver)
                    self.errores.insert(tk.END,"Correcta extracción de us_reservas\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de us_reservas\n")
            if self.us_tipo_de_cambio.get()==1:
                '''
                try:
                    self.ex_us_tipo_de_cambio()
                    self.errores.insert(tk.END,"Correcta extracción de us_tipo_de_cambio\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de us_tipo_de_cambio\n")               
                '''
                self.ex_us_tipo_de_cambio()
                self.errores.insert(tk.END,"Correcta extracción de us_tipo_de_cambio\n")

            if self.us_exportaciones.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_us_exportaciones(driver)
                    self.errores.insert(tk.END,"Correcta extracción de us_exportaciones\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de us_exportaciones\n")                     


            if self.us_liquidez.get()==1:
                try:
                    self.ex_us_liquidez()
                    self.errores.insert(tk.END,"Correcta extracción de us_liquidez\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de us_liquidez\n")              
            
            if self.us_solvencia.get()==1:
                try:
                    self.ex_us_solvencia()
                    self.errores.insert(tk.END,"Correcta extracción de us_solvencia\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de us_solvencia\n")
            if self.us_portafolio.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_us_portafolio(driver)
                    self.errores.insert(tk.END,"Correcta extracción de us_portafolio\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de us_portafolio\n")
            if self.us_deuda.get()==1:
                try:
                    self.ex_us_deuda()
                    self.errores.insert(tk.END,"Correcta extracción de us_deuda\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de us_deuda\n")
            if self.us_pbi.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_us_pbi(driver)
                    self.errores.insert(tk.END,"Correcta extracción de us_pbi\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de us_pbi")
            if self.us_inflacion.get()==1:
                try:
                    driver = self.create_driver()
                    self.ex_us_inflacion(driver)
                    self.errores.insert(tk.END,"Correcta extracción de us_inflacion\n")
                except:
                    self.errores.insert(tk.END,"Error en extracción de us_inflacion")

            #Se limpian las variables:
            self.flush()

            #Funciones de Extracción:
     ########################################Estados Unidos########################################
     ##############################################################################################

    ###Funciones de apoyo###
    def episodios(self, df, columns_names):
        df['Media Movil']=df[columns_names[-1]].rolling(window=8).mean()
        df['D.E']=df[columns_names[-1]].rolling(window=8).std()
        df['Sistem Alertas'] = (df[columns_names[-1]]-df['Media Movil'])/df['D.E']
        conditionlist = []

        # Indicadores en alerta y crisis con valores negativos
        if(columns_names[0] == 'Liquidez' or columns_names[0] == 'Solvencia' or 
        columns_names[0] == 'Reservas Internacionales' or columns_names[0] == 'GDP' or columns_names[0] == 'Inversión de Portafolio'):
            conditionlist = [
                ((-1.5 >= df['Sistem Alertas'])) & ((df['Sistem Alertas'] > -2.0)),
                (-2.0 >= df['Sistem Alertas']),
                (-1.5 < df['Sistem Alertas'])]
        # Indicadores en alerta y crisis con valores positivos
        else:
            conditionlist = [
                ((1.5 <= df['Sistem Alertas'])) & ((df['Sistem Alertas'] < 2.0)),
                (2.0 <= df['Sistem Alertas']),
                (1.5 > df['Sistem Alertas'])]
        choicelist = ['Alerta', 'Crisis', 'Sin Episodio']
        df['Episodio'] = np.select(conditionlist, choicelist, default='Not Specified')
        return df

    def is_float(self,numero):
        #Función accesorio para limpiar datos
        try:
            numero_corregido = float(numero.replace(',',''))
            return numero_corregido
        except:
            pass
    

    def fecha_mod(self, fecha):
        try:
            return(int(fecha[0:4]))
        except:
            pass

    def create_date(self, año,mes):
        if mes < 10:
            str_date  = str(año) + str(0) + str(mes)
        else:
            str_date  = str(año)+str(mes)   
        return str_date   
    
    def reemplazo_solvencia(self, i):
        year = i.split()[0]

        match i.split()[1]:
            case 'Q1':
                year = str(int(year)-1)
                cuarto = '12'
            case 'Q2':
                cuarto = '03'
            case 'Q3':
                cuarto = '06'
            case 'Q4':
                cuarto = '09'

        return year + " " + cuarto 
    
    def replacement(self, data):
        #    str(i.split()[1])+i.split()[0].replace('March',' 01').replace('June',' 04').replace('September','07').replace('December',' 10')
        year = int(data.split()[1])

        match data.split()[0]:
            case 'March':
                mes = ' 03'
            case 'June':
                mes = ' 06'
            case 'September':
                mes = ' 09'
            case 'December':
                mes = ' 12'
        return str(year) + mes

    def Preprocesado_Vertical(self, datos, columna,crecimiento=False, positivo = False):
        datos_final = {str(fecha)+' '+semestre: valor for fecha,trimestre_valor in datos.items() for semestre,valor in trimestre_valor.items()}
        #date_value = list(map(lambda x:datetime.datetime.strptime(x.replace('Q1', '01').replace('Q2', '04').replace('Q3', '07').replace('Q4', '10'),"%Y %m").date(),datos_final.keys()))
        date_value = list(map(lambda x:datetime.datetime.strptime(x.replace('Q1', '03').replace('Q2', '06').replace('Q3', '09').replace('Q4', '12'),"%Y %m").date(),datos_final.keys()))

        datos_mod_df = pd.DataFrame(data= datos_final.values(), index = pd.DatetimeIndex(date_value), columns=[columna]) 
        datos_mod_df.index.names=['Fecha']

        temp = []
        if crecimiento == True:
            datos_mod_df["Tasa Crecimiento"] = datos_mod_df[columna].pct_change()*100
            datos_mod_df["Media Movil"] = datos_mod_df["Tasa Crecimiento"].rolling(window=8).mean()
            datos_mod_df["Desviación Estándar"] = datos_mod_df["Tasa Crecimiento"].rolling(window=8).std()
            datos_mod_df["Sistem Alertas"] = (datos_mod_df["Tasa Crecimiento"] - datos_mod_df["Media Movil"])/datos_mod_df["Desviación Estándar"]

            if positivo==True:
                for i in datos_mod_df['Sistem Alertas']:
                    if np.isnan(i):
                        temp.append('Not Specified')
                    elif i>=2:
                        temp.append('Crisis')
                    elif i>=1.5:
                        temp.append('Alerta')
                    else:
                        temp.append('Sin Episodio')
                #dataframe_vertical["Episodio"] = ["Crisis" if i>=2 else ("Alerta" if i>=1.5 else "Sin Episodio") for i in dataframe_vertical["Sistem Alertas"]] 
            else:
                for i in datos_mod_df['Sistem Alertas']:
                    if np.isnan(i):
                        temp.append('Not Specified')
                    elif i<=-2:
                        temp.append('Crisis')
                    elif i<=-1.5:
                        temp.append('Alerta')
                    else:
                        temp.append('Sin Episodio') 
            '''
            if positivo==True:
                datos_mod_df["Episodio"] = ["Crisis" if i>=2 else ("Alerta" if i>=1.5 else "Sin Episodio") for i in datos_mod_df["Sistem Alertas"]] 
            else:
                datos_mod_df["Episodio"] = ["Crisis" if i<=-2 else ("Alerta" if i<=-1.5 else "Sin Episodio") for i in datos_mod_df["Sistem Alertas"]]          
            '''

        else:      
            datos_mod_df["Media Movil"] = datos_mod_df[columna].rolling(window=8).mean()
            datos_mod_df["Desviación Estándar"] = datos_mod_df[columna].rolling(window=8).std()
            datos_mod_df["Sistem Alertas"] = (datos_mod_df[columna] - datos_mod_df["Media Movil"])/datos_mod_df["Desviación Estándar"]
            #datos_mod_df["Alerta"] = ["Crisis" if abs(i)>=2 else ("Alerta" if abs(i)>=1.5 else "Sin  Episodio") for i in datos_mod_df["Sistema Alertas "+columna]]

            if positivo==True:
                for i in datos_mod_df['Sistem Alertas']:
                    if np.isnan(i):
                        temp.append('Not Specified')
                    elif i>=2:
                        temp.append('Crisis')
                    elif i>=1.5:
                        temp.append('Alerta')
                    else:
                        temp.append('Sin Episodio')
                #dataframe_vertical["Episodio"] = ["Crisis" if i>=2 else ("Alerta" if i>=1.5 else "Sin Episodio") for i in dataframe_vertical["Sistem Alertas"]] 
            else:
                for i in datos_mod_df['Sistem Alertas']:
                    if np.isnan(i):
                        temp.append('Not Specified')
                    elif i<=-2:
                        temp.append('Crisis')
                    elif i<=-1.5:
                        temp.append('Alerta')
                    else:
                        temp.append('Sin Episodio') 

            '''
            if positivo==True:
                datos_mod_df["Episodio"] = ["Crisis" if i>=2 else ("Alerta" if i>=1.5 else "Sin Episodio") for i in datos_mod_df["Sistem Alertas"]] 
            else:
                datos_mod_df["Episodio"] = ["Crisis" if i<=-2 else ("Alerta" if i<=-1.5 else "Sin Episodio") for i in datos_mod_df["Sistem Alertas"]]           
            '''

        datos_mod_df['Episodio'] = temp
        return datos_mod_df

    def Preprocesado_Vertical_DataFrame(self, dataframe,columna,crecimiento=False, positivo=False):
        dataframe_spe = dataframe.to_dict(orient='list')
        Valores = [i[0] for i in dataframe_spe.values()]

        Fechas_Pre=[]
        for fecha in dataframe_spe.keys():
            if type(fecha) is str:
                Fechas_Pre.append(fecha)
            elif type(fecha) == tuple:
                Fechas_Pre.append(str(fecha[0])+' '+str(fecha[1]))

        try:
            #Fechas_Keys=list(map(lambda x:datetime.datetime.strptime(x.replace('Q1', '01').replace('Q2', '04').replace('Q3', '07').replace('Q4', '10'),"%m %Y").date() , Fechas_Pre))
            Fechas_Keys=list(map(lambda x:datetime.datetime.strptime(x.replace('Q1', '03').replace('Q2', '06').replace('Q3', '09').replace('Q4', '12'),"%m %Y").date() , Fechas_Pre))
        except:
            #Fechas_Keys=list(map(lambda x:datetime.datetime.strptime(x.replace('Q1', '01').replace('Q2', '04').replace('Q3', '07').replace('Q4', '10'),"%Y %m").date() , Fechas_Pre))
            Fechas_Keys=list(map(lambda x:datetime.datetime.strptime(x.replace('Q1', '03').replace('Q2', '06').replace('Q3', '09').replace('Q4', '12'),"%Y %m").date() , Fechas_Pre))
        
        dataframe_vertical = pd.DataFrame(data=Valores,index=pd.DatetimeIndex(Fechas_Keys),columns=[columna])
        dataframe_vertical.index.names = ['Fecha']

        temp = []
        if crecimiento==True:
            dataframe_vertical["Tasa Crecimiento"] =  dataframe_vertical[columna].pct_change()*100
            dataframe_vertical["Media Movil"] = dataframe_vertical["Tasa Crecimiento"].rolling(window=8).mean()
            dataframe_vertical["Desviación Estándar"] = dataframe_vertical["Tasa Crecimiento"].rolling(window=8).std()
            dataframe_vertical["Sistem Alertas"] = (dataframe_vertical["Tasa Crecimiento"] - dataframe_vertical["Media Movil"])/dataframe_vertical["Desviación Estándar"]
            #dataframe_vertical["Alerta"] = ["Crisis" if abs(i)>=2 else ("Alerta" if abs(i)>=1.5 else "Sin  Episodio") for i in dataframe_vertical["Sistema Alertas "+columna]]

            if positivo==True:
                for i in dataframe_vertical['Sistem Alertas']:
                    if np.isnan(i):
                        temp.append('Not Specified')
                    elif i>=2:
                        temp.append('Crisis')
                    elif i>=1.5:
                        temp.append('Alerta')
                    else:
                        temp.append('Sin Episodio')
                #dataframe_vertical["Episodio"] = ["Crisis" if i>=2 else ("Alerta" if i>=1.5 else "Sin Episodio") for i in dataframe_vertical["Sistem Alertas"]] 
            else:
                for i in dataframe_vertical['Sistem Alertas']:
                    if np.isnan(i):
                        temp.append('Not Specified')
                    elif i<=-2:
                        temp.append('Crisis')
                    elif i<=-1.5:
                        temp.append('Alerta')
                    else:
                        temp.append('Sin Episodio')                
                #dataframe_vertical["Episodio"] = ["Crisis" if i<=-2 else ("Alerta" if i<=-1.5 else "Sin Episodio") for i in dataframe_vertical["Sistem Alertas"]] 
        else:
            dataframe_vertical["Media Movil"] = dataframe_vertical[columna].rolling(window=8).mean()
            dataframe_vertical["Desviación Estándar"] = dataframe_vertical[columna].rolling(window=8).std()
            dataframe_vertical["Sistem Alertas"] = (dataframe_vertical[columna] - dataframe_vertical["Media Movil"])/dataframe_vertical["Desviación Estándar"]
            #dataframe_vertical["Alerta"] = ["Crisis" if abs(i)>=2 else ("Alerta" if abs(i)>=1.5 else "Sin  Episodio") for i in dataframe_vertical["Sistema Alertas "+columna]]
            if positivo==True:
                for i in dataframe_vertical['Sistem Alertas']:
                    if np.isnan(i):
                        temp.append('Not Specified')
                    elif i>=2:
                        temp.append('Crisis')
                    elif i>=1.5:
                        temp.append('Alerta')
                    else:
                        temp.append('Sin Episodio')
                #dataframe_vertical["Episodio"] = ["Crisis" if i>=2 else ("Alerta" if i>=1.5 else "Sin Episodio") for i in dataframe_vertical["Sistem Alertas"]] 
            else:
                for i in dataframe_vertical['Sistem Alertas']:
                    if np.isnan(i):
                        temp.append('Not Specified')
                    elif i<=-2:
                        temp.append('Crisis')
                    elif i<=-1.5:
                        temp.append('Alerta')
                    else:
                        temp.append('Sin Episodio')                
                #dataframe_vertical["Episodio"] = ["Crisis" if i<=-2 else ("Alerta" if i<=-1.5 else "Sin Episodio") for i in dataframe_vertical["Sistem Alertas"]] 
            '''
            if positivo==True:
                dataframe_vertical["Episodio"] = ["Crisis" if i>=2 else ("Alerta" if i>=1.5 else "Sin Episodio") for i in dataframe_vertical["Sistem Alertas"]] 
            else:
                dataframe_vertical["Episodio"] = ["Crisis" if i<=-2 else ("Alerta" if i<=-1.5 else "Sin Episodio") for i in dataframe_vertical["Sistem Alertas"]]          
            '''
        dataframe_vertical["Episodio"] = temp
        return dataframe_vertical
    
    ###Funciones de extracción###
    #############################
    def ex_us_reservas(self,driver):
        driver.get("https://www.imf.org/external/np/sta/ir/IRProcessWeb")
        driver.maximize_window()
        time.sleep(5)

        xpaths_1 = ['//*[@id="form1"]/table/tbody/tr/td[5]/p[1]/a[2]','//*[@id="MenuWidget164766"]/div[1]/div[3]/div/div[1]/a[4]'] #Actualizar tabla

        for i in xpaths_1:
            element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, i)))
            element.click()  

        #Este elemento tarda bastante en cargar y puede ser una fuente de error:
        loops = 0
        while loops!=60:
            try:
                time.sleep(1)
                element = driver.find_element(By.XPATH, '(//div[@class="DeleteIndBtn"])[3]')
                element.click()
                break
            except:
                loops +=1

        time.sleep(2) 
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td/div/div/div[1]/div/div[1]/table/tbody/tr/td[2]/input')))
        element.send_keys('United States')
        element.send_keys(Keys.ENTER)

        xpaths_2 = ['//*[@id="TLVNodeRow#S#UNITED_STATES"]/td/div/div[2]/div[2]/span',
        '//td[@class="PPDialogButtons"]//div[1]','(//div[@class="MenuIndBtn"])[1]']

        for i in xpaths_2:
            loops = 0
            while loops!=60:
                time.sleep(2)
                try:
                    element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, i)))
                    element.click()  
                    break
                except:
                    loops +=1

        xpaths_3=['/html/body/div[4]/div[1]/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td/div/div[1]/div[2]',
        '//div[@class="FrequencyLayout"]/span/div','//div[@class="FrequencyLayout"]/span[4]/div','//div[@class="FrequencyLayout"]/span[6]/div',
        '//div[@class="RelPeriodLayout"]/div//div[2]','//li[@class="PPItemsContainer"]/div[3]']

        for i in xpaths_3:
            loops = 0
            while loops!=60:
                time.sleep(2)
                try:
                    element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, i)))
                    element.click()  
                    break
                except:
                    loops += 1

        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="PPTextBoxInput"][1]')))
        element.clear()
        element.send_keys('10')
        element.send_keys(Keys.ENTER)

        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//td[@class="PPDialogButtons"][1]//div/div[1]')))
        element.click()

        loops = 0
        while loops!=60:
            time.sleep(2)
            try:
                element = driver.find_element(By.XPATH,'(//div[@class="PPSel"])[2]')
                click_slider = ActionChains(driver).click_and_hold(element)
                click_slider.perform()
                break
            except:
                loops += 1

        time.sleep(3)

        valores = []
        x_off = 100 #Frágil
        y_off = 0

        try:
            while True:
                doc = lxml.html.fromstring(driver.page_source)
                fila = doc.xpath('(//tbody)[3]//tr[2]//td//text()')
                slide = ActionChains(driver).move_by_offset(x_off,y_off)
                slide.perform()
                time.sleep(3)
                valores = valores + list(filter(lambda x:x not in valores, fila))
        except:
            pass

        valor_Q4_2000=valores[1] 
        valores = valores[2:]

        fechas = [i for i in range(2001,datetime.datetime.now().year+1)]
        datos={}
        datos=datos.fromkeys(fechas, 0)
        ciclador = 0
        for fecha in datos.keys():
            i = 1
            datos[fecha] = {}
            for valor in valores[ciclador:ciclador+4]:
                try:
                    datos[fecha]['Q'+str(i)] = self.is_float(valor)
                    i=i+1
                except:
                    datos[fecha]['Q'+str(i)] = None
            ciclador = ciclador + 4

        datos_2000 = {}
        datos_2000[2000] = {}
        datos_2000[2000]['Q4'] = self.is_float(valor_Q4_2000)

        datos_2000.update(datos)


        datos_final = {(fecha,semestre): valor for fecha,trimestre_valor in datos_2000.items() for semestre,valor in trimestre_valor.items()}
        Reservas_Internacionales = pd.DataFrame.from_dict(datos_final,orient='index').transpose()
        Reservas_Internacionales.columns = pd.MultiIndex.from_tuples(Reservas_Internacionales.columns)

        Reservas_Internacionales_vertical = self.Preprocesado_Vertical(datos_2000,"Reservas Internacionales",crecimiento=True)
        #df_resumen = pd.concat([df_resumen,Reservas_Internacionales_vertical['Sistema Alertas Reservas Internacionales'],Reservas_Internacionales_vertical['Reservas Internacionales Crecimiento']],axis=1)
        driver.quit()
        self.write_to_path(Reservas_Internacionales_vertical, 'US')
        

    def ex_us_tipo_de_cambio(self):
        #Requiere una actualización urgente
        fecha_actual = datetime.datetime.today()
        año = fecha_actual.year
        mes = fecha_actual.month

        url_template = "https://stats.bis.org/statx/srs/table/I1?c=&p="
        url_ending = "&m=N"
        query_date = self.create_date(año,mes)
        query = url_template+query_date+url_ending

        datos = {}

        while año >= 1999:
            html = requests.get(query)
            doc = lxml.html.fromstring(html.content)
            
            fechas = doc.xpath('//*[@id="statx-data-table"]/thead/tr[2]/th[position()=7 or position()=8 or position()=9 or position()=10]/text()')
            fechas.reverse()
            elementos = doc.xpath('//*[@id="statx-data-table"]/tbody//tr[@class="rl3"]//td[position()=8 or position()=9 or position()=10 or position()=11]/a/text()')
            elementos = [self.is_float(valor) for valor in elementos if (self.is_float(valor)!=None)]

            i1,i2,i3,i4 = 0,1,2,3

            for fecha in fechas:
                datos[str(fecha)] = []

            for i in range(int(len(elementos)/4)):
                datos[str(fechas[0])].append(elementos[i4])
                datos[str(fechas[1])].append(elementos[i3])
                datos[str(fechas[2])].append(elementos[i2])
                datos[str(fechas[3])].append(elementos[i1])

                i1 = i1 + 4
                i2 = i2 + 4
                i3 = i3 + 4
                i4 = i4 + 4
            
            año = año - 1 
            query_date= self.create_date(año,mes)
            query = url_template+query_date+url_ending
                
        paises = ['Australia','Austria','Belgium','Canada','Chinese Taipei','Denmark','Finland','France','Germany',
        'Greece','Hong Kong SAR','Ireland','Italy','Japan','Korea','Netherlands','New Zealand','Norway','Portugal',
        'Singapore','Spain','Sweden','Switzerland','United Kingdom','United States','Euro area']
        
        print({k:len(v) for k,v in list(datos.items())})
        Tipo_De_Cambio = pd.DataFrame(data=datos, index=paises).loc[['Euro area']]
        Tipo_De_Cambio = Tipo_De_Cambio.loc[:,::-1]
        Tipo_De_Cambio_Vertical = self.Preprocesado_Vertical_DataFrame(Tipo_De_Cambio,"Tipo de Cambio",positivo=True)
        self.write_to_path(Tipo_De_Cambio_Vertical, 'US')

    def ex_us_exportaciones(self, driver):
        driver.get("https://apps.bea.gov/iTable/iTable.cfm?reqid=62&step=2&isuri=1&6210=1#reqid=62&step=2&isuri=1&6210=1")
        time.sleep(5)

        xpaths = ['//*[@id="myform2"]/div/div/div[1]/a', #Entrar al link
        '//div[@class="icon_tableOptions"]', #Modificar tabla
        '//*[@id="myformfilter"]/div[1]/div/select/option[3]', #Desseleccionar 2020
        '//*[@id="myformfilter"]/div[1]/div/select/option[2]', #Desseleccionar 2021
        '//*[@id="myformfilter"]/div[1]/div/select/option[1]', #Seleccionar todos los años
        '//*[@id="myformfilter"]/div[3]/div/select/option[1]', #Quitar All Lines
        '//*[@id="myformfilter"]/div[3]/div/select/option[4]', #Elegir Exportaciones
        '//*[@id="tableOptions-modal"]/div/div/div[3]/button[1]'] #Actualizar tabla

        for i in xpaths:
            #Evitar el anuncio de feedback
            try:
                time.sleep(1) #Tiempo de Espera del Feedback
                feedback = driver.find_element(By.XPATH,'//*[@id="acsMainInvite"]/div/a[1]')
                feedback.click()
                element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, i)))
                element.click()  
            except:
                loops = 0
                while loops!=60:
                    time.sleep(1)
                    try:
                        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, i)))
                        element.click()  
                        break
                    except:
                        loops += 1

        loaded = 0
        loops = 0
        

        while loaded==0:
                time.sleep(1)
                doc = lxml.html.fromstring(driver.page_source)
                fechas=doc.xpath('//*[@id="tbl_wrapper"]/div/div[2]/div[1]/div/table/thead/tr[2]/th/text()')
                fechas = [self.fecha_mod(i) for i in fechas if i[0:4].isdigit()]
                if len(fechas)>=6:
                    loaded = 1
                if loops==60:
                    raise Exception("Tiempo de espera muy largo, revise su conexión a internet")
                loops += 1 

        valores = doc.xpath('//*[@id="tbl"]/tbody/tr[3]/td/text()')
        valores = list(map(lambda x:int(x.replace(',','')),valores[1:]))

        datos={}
        datos=datos.fromkeys(fechas, 0)
        ciclador = 0

        for fecha in datos.keys():
            i = 1
            datos[fecha] = {}
            for valor in valores[ciclador:ciclador+4]:
                try:
                    datos[fecha]['Q'+str(i)] = valor
                    i=i+1
                except:
                    datos[fecha]['Q'+str(i)] = None
            ciclador = ciclador + 4

        datos = {(fecha,semestre): valor for fecha,trimestre_valor in datos.items() for semestre,valor in trimestre_valor.items()}
        Exportaciones = pd.DataFrame.from_dict(datos,orient='index').transpose()
        Exportaciones.columns = pd.MultiIndex.from_tuples(Exportaciones.columns)
        Exportaciones = Exportaciones.loc[:,2000:]
        Exportaciones_Vertical = self.Preprocesado_Vertical_DataFrame(Exportaciones,columna="Exportaciones",crecimiento=True)
        self.write_to_path(Exportaciones_Vertical,'US')

    def ex_us_liquidez(self):
        html = requests.get("https://www.fdic.gov/analysis/quarterly-banking-profile/statistics-at-a-glance/")
        doc = lxml.html.fromstring(html.content)
        urls = doc.xpath('//a[@class="excelicon"]/@href')
        urls = list(map(lambda x:"https://www.fdic.gov/"+x,urls))
        liquideces = []
        for i in urls[2:]:
            file_extension = re.search('\.xl.*', i).group().strip()
            print(file_extension)
            if file_extension == '.xlsx':
                df = pd.read_excel(i, engine='openpyxl')
            elif file_extension == '.xls':
                df = pd.read_excel(i, engine='xlrd')
            date = df.iloc[0,0]
            try:
                df[df.columns[0]]=df[df.columns[0]].str.strip()
                temp=df[(df[df.columns[0]] == "Total Assets") | (df[df.columns[0]] == "Domestic Deposits")]
                liquidez = temp.iloc[1,2] / temp.iloc[0,2]
                
            except:
                df.columns = list(map(lambda x:x.strip(),df.columns))
                liquidez = df['Domestic Deposits'].iloc[3]/df['Total Assets'].iloc[3]
            
            liquideces.append(liquidez)

        fechas = doc.xpath('//a[@class="pdficon"]/text()')[2:-33]
        liquideces.reverse()
        fechas.reverse()
        sticky_liquideces = dict(zip(list(map(lambda x:x[:-6], fechas)),liquideces))
        Liquidez=pd.DataFrame([sticky_liquideces])

        Liquidez_fechas = [self.replacement(i) for i in fechas]
        Liquidez_fechas = [datetime.datetime.strptime(fecha,"%Y %m").date() for fecha in Liquidez_fechas]
        Liquidez_vertical = pd.DataFrame(data=liquideces, index=pd.DatetimeIndex(Liquidez_fechas), columns=["Liquidez"])
        Liquidez_vertical.index.names = ["Fecha"]
        Liquidez_vertical["Media Movil"] = Liquidez_vertical["Liquidez"].rolling(window=8).mean()
        Liquidez_vertical["Desviación Estándar"] = Liquidez_vertical["Liquidez"].rolling(window=8).std()
        Liquidez_vertical["Sistema Alertas"] = (Liquidez_vertical["Liquidez"] - Liquidez_vertical["Media Movil"])/Liquidez_vertical["Desviación Estándar"]
        #Liquidez_vertical["Episodio"] = ["Crisis" if i<=-2 else ("Alerta" if i<=-1.5 else "Sin Episodio") for i in Liquidez_vertical["Sistem Alertas"]]
        temp = []
        for i in Liquidez_vertical['Sistema Alertas']:
            if i == np.nan:
                temp.append('Not Specified')
            elif i<=-2:
                temp.append('Crisis')
            elif i<=-1.5:
                temp.append('Alerta')
            else:
                temp.append('Sin Episodio')
        Liquidez_vertical['Episodio'] = temp
        self.write_to_path(Liquidez_vertical,'US')

    def ex_us_solvencia(self):
            #LinkActualizado
        url_base = 'https://fred.stlouisfed.org/'
        html = requests.get("https://fred.stlouisfed.org/release/tables?rid=22&eid=822714")
        doc = lxml.html.fromstring(html.content)
        elemento = doc.xpath('//*[@id="main-content-column"]/table//tr[2]/td/a/@href')
        url_act = url_base + elemento[0]

        #Búsqueda actual
        html = requests.get(url_act)
        doc = lxml.html.fromstring(html.content)

        #Fecha:
        elemento = doc.xpath('//*[@id="release-elements-tree"]/thead/tr/th[4]/span/text()')
        elemento = elemento[0].split()

        year = elemento[1]
        cuarto = elemento[0]

        match cuarto:
            case 'Q1':
                marker = "01"
            case 'Q2':
                marker = "04"
            case 'Q3':
                marker = "07"
            case 'Q4':
                marker = "10"

        query = year+"-"+marker+"-"+"01"

        base = "https://fred.stlouisfed.org/release/tables?rid=22&eid=822750&od="
        datos = {str(k):{'Q1':None, 'Q2':None, 'Q3':None, 'Q4':None} for k in range(2000,int(year)+1)}
        link = base+query
        fechas = []


        while year != "1999" :
            html = requests.get(link)
            doc = lxml.html.fromstring(html.content)

            Pasivo = doc.xpath('//*[@id="release-elements-tree"]/tbody/tr[@data-tt-id="822783"]/td[@class="fred-rls-elm-vl-td"][1]/text()')
            Activo = doc.xpath('//*[@id="release-elements-tree"]/tbody/tr[@data-tt-id="822776"]/td[@class="fred-rls-elm-vl-td"][1]/text()')
            Solvencia = float(Pasivo[0].strip())/float(Activo[0].strip())
            
            datos[year][cuarto] = Solvencia
            

            if marker=="01":
                marker="10"
                cuarto = "Q4"
                fechas.append(year)
                year = str(int(year)-1)
            elif marker=="04":
                marker="01"
                cuarto = "Q1"
            elif marker=="07":
                marker="04"
                cuarto = "Q2"
            else:
                marker="07"
                cuarto = "Q3"

            query = year+"-"+marker+"-"+"01"
            link = base+query

        datos2 = datos.copy()
        datos = {(fecha,semestre): valor for fecha,trimestre_valor in datos.items() for semestre,valor in trimestre_valor.items()}

        #Solvencia_Vertical = Preprocesado_Vertical(datos,"Solvencia")
        datos_final = {str(fecha)+' '+semestre: valor for fecha,trimestre_valor in datos2.items() for semestre,valor in trimestre_valor.items()}
        Solvencia_Fechas = [self.reemplazo_solvencia(i) for i in datos_final.keys()]
        Solvencia_Fechas = [datetime.datetime.strptime(fecha,"%Y %m").date() for fecha in Solvencia_Fechas]
        Solvencia_Vertical = pd.DataFrame(data= datos_final.values(), index = pd.DatetimeIndex(Solvencia_Fechas), columns=["Solvencia"]) 
        Solvencia_Vertical.index.names=['Fecha']
        Solvencia_Vertical["Media Movil"] = Solvencia_Vertical["Solvencia"].rolling(window=8).mean()
        Solvencia_Vertical["Desviación Estándar"] = Solvencia_Vertical["Solvencia"].rolling(window=8).std()
        Solvencia_Vertical["Sistema Alertas"] = (Solvencia_Vertical["Solvencia"] - Solvencia_Vertical["Media Movil"])/Solvencia_Vertical["Desviación Estándar"]
        #Solvencia_Vertical["Episodio"] = ["Crisis" if i<=-2 else ("Alerta" if i<=-1.5 else "Sin Episodio") for i in Solvencia_Vertical["Sistem Alertas"]]  
        temp = []
        for i in Solvencia_Vertical['Sistema Alertas']:
            if i == np.nan:
                temp.append('Not Specified')
            elif i<=-2:
                temp.append('Crisis')
            elif i<=-1.5:
                temp.append('Alerta')
            else:
                temp.append('Sin Episodio')
        Solvencia_Vertical['Episodio'] = temp
        self.write_to_path(Solvencia_Vertical,'US')
    

    def ex_us_portafolio(self,driver):
        driver.get("https://apps.bea.gov/iTable/iTable.cfm?reqid=62&step=2&isuri=1&6210=1#reqid=62&step=2&isuri=1&6210=1")
        time.sleep(5)

        xpaths = ['//*[@id="myform2"]/div/div/div[1]/a', #Entrar al link
        '//div[@class="icon_tableOptions"]', #Modificar tabla
        '//*[@id="myformfilter"]/div[1]/div/select/option[3]', #Desseleccionar 2020
        '//*[@id="myformfilter"]/div[1]/div/select/option[2]', #Desseleccionar 2021
        '//*[@id="myformfilter"]/div[1]/div/select/option[1]', #Seleccionar todos los años
        '//*[@id="myformfilter"]/div[3]/div/select/option[1]', #Quitar All Lines
        '//*[@id="myformfilter"]/div[3]/div/select/option[25]', #Elegir Inversión de Portafolio
        '//*[@id="tableOptions-modal"]/div/div/div[3]/button[1]'] #Actualizar tabla

        for i in xpaths:
            #Evitar el anuncio de feedback
            try:
                time.sleep(1) #Tiempo de Espera del Feedback
                feedback = driver.find_element(By.XPATH,'//*[@id="acsMainInvite"]/div/a[1]')
                feedback.click()
                element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, i)))
                element.click()  
            except:
                loops = 0
                while loops!=60:
                    time.sleep(1)
                    try:
                        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, i)))
                        element.click() 
                        break
                    except:
                        loops += 1  

        loaded = 0
        loops = 0
        while loaded==0:
            time.sleep(1)
            doc = lxml.html.fromstring(driver.page_source)
            fechas=doc.xpath('//*[@id="tbl_wrapper"]/div/div[2]/div[1]/div/table/thead/tr[2]/th/text()')
            fechas = [self.fecha_mod(i) for i in fechas if i[0:4].isdigit()]
            if len(fechas)>=6:
                loaded = 1
            if loops==60:
                raise Exception("Tiempo de espera muy largo, revise su conexión a internet")
            loops += 1 


        valores = doc.xpath('//*[@id="tbl"]/tbody/tr[3]/td/text()')
        valores = list(map(lambda x:int(x.replace(',','')),valores[1:]))

        datos={}
        datos=datos.fromkeys(fechas, 0)
        ciclador = 0
        for fecha in datos.keys():
            i = 1
            datos[fecha] = {}
            for valor in valores[ciclador:ciclador+4]:
                datos[fecha]['Q'+str(i)] = valor
                i=i+1
            ciclador = ciclador + 4

        datos = {(fecha,semestre): valor for fecha,trimestre_valor in datos.items() for semestre,valor in trimestre_valor.items()}
        Inversion_de_Portafolio = pd.DataFrame.from_dict(datos,orient='index').transpose()
        Inversion_de_Portafolio.columns = pd.MultiIndex.from_tuples(Inversion_de_Portafolio.columns)
        Inversion_de_Portafolio = Inversion_de_Portafolio.loc[:,2000:]

        Inversion_de_Portafolio_Vertical = self.Preprocesado_Vertical_DataFrame(Inversion_de_Portafolio,columna="Inversión de Portafolio",crecimiento=True)
        driver.quit()
        self.write_to_path(Inversion_de_Portafolio_Vertical,'US')
    #df_resumen = pd.concat([df_resumen,Inversion_de_Portafolio_Vertical['Sistema Alertas Inversion de Portafolio'],Inversion_de_Portafolio_Vertical['Inversion de Portafolio Crecimiento']],axis=1)   
    
    def ex_us_deuda(self):
        size = (datetime.date.today().year - 2000)*365 + 1000
        query = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?filter=record_calendar_year:gt:1999&filter=record_calendar_year:lt:2022&page[size]='+str(size)
        #try:
        data = requests.get(query).json()['data']
        df=pd.DataFrame(data)

        valores = []
        for i in range(2000,2022):
            for j in range(1,5):
                temp = df[(df['record_calendar_year']==str(i)) & (df['record_calendar_quarter']==str(j))]
                valores.append(np.mean(temp['tot_pub_debt_out_amt'].astype(float)))

        fechas = [i for i in range(2000,datetime.date.today().year)]
        cols = pd.MultiIndex.from_product([fechas,['Q1','Q2','Q3','Q4']])
        Deuda_Externa = pd.DataFrame([valores],columns=cols)

        Deuda_Externa_Vertical = self.Preprocesado_Vertical_DataFrame(Deuda_Externa,columna="Deuda Externa",crecimiento=True, positivo=True)
        #df_resumen = pd.concat([df_resumen,Deuda_Externa_Vertical['Sistema Alertas Deuda Externa'],Deuda_Externa_Vertical['Deuda Externa Crecimiento']],axis=1)
        self.write_to_path(Deuda_Externa_Vertical,'US')

    def ex_us_pbi(self,driver):
        driver.get("https://apps.bea.gov/iTable/iTable.cfm?reqid=19&step=2#reqid=19&step=2&isuri=1&1921=survey")
        time.sleep(10)

        xpaths = ['//*[@id="vertical_container_2"]/div[1]/div[1]/a',
        '//*[@id="tabpanel_3_5_2_0_19"]',
        '//*[@id="icon_tableOptions"]/a/div',
        #'//*[@id="myformfilter"]/div[1]/div/select',
        #'//*[@id="myformfilter"]/div[1]/div/select/option[@value="2005"]',
        '//*[@id="1"]',
        '//*[@id="tableOptions-modal"]/div/div/div[3]/button[1]']

        for i in xpaths:
            #Evitar el anuncio de feedback
            try:
                time.sleep(1) #Tiempo de Espera del Feedback
                feedback = driver.find_element(By.XPATH,'//*[@id="acsMainInvite"]/div/a[1]')
                feedback.click()
                element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, i)))
                element.click()  
            except:
                loops = 0
                while loops!=60:
                    time.sleep(1)
                    try:
                        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, i)))
                        element.click()  
                        break
                    except:
                        loops += 1

        loaded = 0
        loops = 0
        while loaded==0:
            time.sleep(1)
            doc = lxml.html.fromstring(driver.page_source)
            fechas=doc.xpath('//*[@id="tbl_wrapper"]/div/div[2]/div[1]/div/table/thead/tr[1]/th/text()')

            if len(fechas)>=6:
                fechas = [self.fecha_mod(i) for i in fechas if i.isdigit()]
                loaded = 1
            if loops==60:
                raise Exception("Tiempo de espera muy largo, revise su conexión a internet")
            loops += 1 


        valores = doc.xpath('//*[@id="tbl"]/tbody/tr[1]/td/text()')
        valores = list(map(lambda x:float(x.replace(',','')),valores))[1:]

        datos={}
        datos=datos.fromkeys(fechas, 0)
        ciclador = 0
        for fecha in datos.keys():
            i = 1
            datos[fecha] = {}
            for valor in valores[ciclador:ciclador+4]:
                datos[fecha]['Q'+str(i)] = valor
                i=i+1
            ciclador = ciclador + 4

        datos = {(fecha,semestre): valor for fecha,trimestre_valor in datos.items() for semestre,valor in trimestre_valor.items()}
        GDP = pd.DataFrame.from_dict(datos,orient='index').transpose()
        GDP.columns = pd.MultiIndex.from_tuples(GDP.columns)
        GDP = GDP.loc[:,2000:]

        GDP_Vertical=self.Preprocesado_Vertical_DataFrame(GDP,"PIB",crecimiento=True)
        driver.quit()
        self.write_to_path(GDP_Vertical, 'US')

    def ex_us_inflacion(self, driver):
        driver.get("https://fred.stlouisfed.org/series/CPIAUCSL")
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="input-cosd"]'))).click()  
        time.sleep(10)
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-cosd"]'))).send_keys(Keys.CONTROL, 'a')    
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-cosd"]'))).send_keys(Keys.BACKSPACE)
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-cosd"]'))).send_keys('2000-01-01') 
        time.sleep(5)
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="download-button"]'))).click()  
        url = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="download-data"]'))).get_attribute("href")
        df = pd.read_excel(url)
        df = df.iloc[10:]
        df['Fecha'] = pd.to_datetime(df[df.columns[0]])
        df = df.drop(df.columns[0], axis=1)
        df = df.set_index('Fecha')
        df = df.rename(columns = {df.columns[0]:'Inflacion'})
        df = df.resample('Q').mean()
        df.index = df.index.to_series().apply(self.correccion_fecha)
        df = self.episodios(df, list(df.columns))
        self.write_to_path(df, 'US')

################Funciones Europa###################
###################################################

#Funciones de apoyo
#Función que extrae la información de cada url
    def infoSplitDf_EU(self, info_extraction, indicador):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #YA

        period_list, value_list = [], []

        for i in range(0,len(info_extraction), 3):
            element = info_extraction[i:i+3]

            if('Q1' in element[0]):
                element[0] = element[0][0:4]+'-03'
            elif('Q2' in element[0]):
                element[0] = element[0][0:4]+'-06'
            elif('Q3' in element[0]):
                element[0] = element[0][0:4]+'-09'
            elif('Q4' in element[0]):
                element[0] = element[0][0:4]+'-12'
            
            if(element[0]== '1999-12'):
                break
            elif (element[1] == 'N/E'):
                value_list.append(np.nan)
            else:
                value = locale.atof(element[1])
                value_list.append(value)
            element_date = datetime.datetime.strptime(element[0], '%Y-%m')
            period_list.append(str(element_date))

        data = {'Fecha': period_list,
            indicador: value_list}
        df = pd.DataFrame(data, columns=['Fecha', indicador])
        return df

    def data_extraction(self,k,url):
        #header necesario para evitar bloqueos
        encabezados = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        }

        response= requests.get(url, headers=encabezados) #obtención del html de la url
        parser = lxml.html.fromstring(response.text) #Parseo del html

        #Empleo de xpath para extraer la información deseada: period, value, y obs. status dentro de la tabla
        info_extraction = parser.xpath("//table[@id = 'dataTableID']//td[contains(@class, 'light') or contains(@class, 'dark')]/text()")

        #Separando la información y guardandola en un Data Frame
        df = self.infoSplitDf_EU(info_extraction, k)

        #Limpieza de datos
        if (k == 'Reservas Internacionales' or k == 'Tipo de Cambio' 
        or k == 'Solvencia' or k == 'Inversión de Portafolio'):
            df = self.dataCleaning_EU(df)
            quarterly = df.resample('Q').mean()
            quarterly = quarterly.reset_index()
            lista_fechas = []
            for fecha in quarterly['Fecha']:
                dias = int(fecha.strftime('%d'))-1
                fecha_nueva = fecha - datetime.timedelta(days = dias)
                lista_fechas.append(fecha_nueva)
            quarterly['Fecha'] = lista_fechas
            quarterly = quarterly.set_index('Fecha')
            return quarterly
        else:
            df = df.set_index('Fecha')
            df.dropna()
            df = df.sort_index()
            return df

    #Se usa para europa tambien
    def dataCleaning(self, df, date_format):
        df['Fecha'] = pd.to_datetime(df['Fecha'], format= date_format)
        df = df.set_index('Fecha')
        df.dropna() 
        df = df.sort_index()
        return df

    def dataCleaning_EU(self, df):
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        df = df.set_index('Fecha')
        df.dropna() 
        df = df.sort_index()
        return df

    def tasaCrecimiento(self, df, columna):
        tasa_crecimiento_list = [np.nan]
        for i in range(1, len(df[columna]-1)):
            try:
                v2 = df.iloc[i][columna][0] #Útil para PBI china
                v1 = df.iloc[i-1][columna][0]
            except:
                v2 = df.iloc[i][columna]
                v1 = df.iloc[i-1][columna]
            tasa_crecimiento = ((v2-v1)/v1)*100
            tasa_crecimiento_list.append(tasa_crecimiento)
        df['Tasa Crecimiento'] = tasa_crecimiento_list    
        return df

    def text_format(self, val):
        color = 'white'
        if (val == 'Crisis'):
            color = '#ff0000'
        elif (val == 'Alerta'):
            color = '#ffff00'
        return 'background-color: %s' % color

    def espisodios(self, df, columns_names):
        df['Media Movil']=df[columns_names[-1]].rolling(window=8).mean()
        df['D.E']=df[columns_names[-1]].rolling(window=8).std()
        df['Sistem Alertas'] = (df[columns_names[-1]]-df['Media Movil'])/df['D.E']
        conditionlist = []

        if(columns_names[0] == 'Liquidez' or columns_names[0] == 'Solvencia'
        or columns_names[0] == 'Reservas Internacionales' 
        or columns_names[0] == 'PIB' or columns_names[0] == 'Inversión de Portafolio'):
            conditionlist = [
                ((-1.5 >= df['Sistem Alertas'])) & ((df['Sistem Alertas'] > -2.0)),
                (-2.0 >= df['Sistem Alertas']),
                (-1.5 < df['Sistem Alertas'])]
        # Indicadores en alerta y crisis con valores positivos
        else:
            conditionlist = [
                ((1.5 <= df['Sistem Alertas'])) & ((df['Sistem Alertas'] < 2.0)),
                (2.0 <= df['Sistem Alertas']),
                (1.5 > df['Sistem Alertas'])]

        choicelist = ['Alerta', 'Crisis', 'Sin Episodio']
        df['Episodio'] = np.select(conditionlist, choicelist, default='Not Specified')
        return df

    def episode_count(self, df, indicador):
        crisis = 0
        alertas = 0
        for episodio in df['Episodio']:
            if(episodio == 'Alerta'):
                alertas += 1
            elif (episodio == 'Crisis'):
                crisis += 1
        episode_quantity = [indicador, alertas, crisis]
        return episode_quantity

    def ex_ue_reservas(self):
        df = self.data_extraction(k="Reservas Internacionales",url="https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=340.RA6.M.N.U2.W1.S121.S1.LE.A.FA.R.F._Z.EUR.X1._X.N")
        #Tasa de crecimiento
        columns_names = list(df.columns.values)
        df = self.tasaCrecimiento(df, columns_names[-1])
        df = self.episodios(df, columns_names)

        #FALTA REVISAR SI EXISTE
        '''
            list_quantity = self.episode_count(df, columns_names[0])
            df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
            df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)        
        '''

        df = df.style.applymap(self.text_format)
        self.write_to_path(df, 'UE')

    def ex_ue_tipo_de_cambio(self):
        df = self.data_extraction(k="Tipo de Cambio",url="https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=120.EXR.M.USD.EUR.SP00.A")
        columns_names = list(df.columns.values)
        df = self.episodios(df, columns_names)

        #FALTA REVISAR SI EXISTE
        '''
            list_quantity = self.episode_count(df, columns_names[0])
            df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
            df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)        
        '''

        df = df.style.applymap(self.text_format)
        self.write_to_path(df, 'UE')

    def ex_ue_exportaciones(self):
        df = self.data_extraction(k="Exportaciones",url="https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=320.MNA.Q.N.I8.W1.S1.S1.D.P6._Z._Z._Z.EUR.LR.N")
        columns_names = list(df.columns.values)
        df = self.episodios(df, columns_names)

        #FALTA REVISAR SI EXISTE
        '''
            list_quantity = self.episode_count(df, columns_names[0])
            df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
            df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)        
        '''

        df = df.style.applymap(self.text_format)
        self.write_to_path(df, 'UE')

    def ex_ue_liquidez(self):
        df = self.data_extraction(k="Liquidez",url="https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=117.BSI.Q.U2.N.F.T00.A.4.Z5.0000.Z01.E")
        columns_names = list(df.columns.values)
        df = self.episodios(df, columns_names)

        #FALTA REVISAR SI EXISTE
        '''
            list_quantity = self.episode_count(df, columns_names[0])
            df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
            df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)        
        '''

        df = df.style.applymap(self.text_format)
        self.write_to_path(df, 'UE')

    def ex_ue_solvencia(self):
        df = self.data_extraction(k="Solvencia",url="https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=117.BSI.M.U2.N.A.A20.A.1.U2.1100.Z01.E")
        columns_names = list(df.columns.values)
        df = self.episodios(df, columns_names)

        #FALTA REVISAR SI EXISTE
        '''
            list_quantity = self.episode_count(df, columns_names[0])
            df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
            df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)        
        '''

        df = df.style.applymap(self.text_format)
        self.write_to_path(df,'UE')

    def ex_ue_portafolio(self):
        df = self.data_extraction(k="Inversión de Portafolio",url="https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=338.BP6.M.N.I8.W1.S1.S1.T.L.FA.P.F._Z.EUR._T.M.N")
        #Tasa de crecimiento
        columns_names = list(df.columns.values)
        df = self.tasaCrecimiento(df, columns_names[-1])
        df = self.episodios(df, columns_names)

        #FALTA REVISAR SI EXISTE
        '''
            list_quantity = self.episode_count(df, columns_names[0])
            df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
            df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)        
        '''

        df = df.style.applymap(self.text_format)
        self.write_to_path(df, 'UE')

    def ex_ue_deuda(self):
        df = self.data_extraction(k="Deuda Externa",url="https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=338.BP6.Q.N.I8.W1.S1.S1.LE.L.FA._T.FGED._Z.EUR._T._X.N")
        columns_names = list(df.columns.values)
        df = self.episodios(df, columns_names)

        #FALTA REVISAR SI EXISTE
        '''
            list_quantity = self.episode_count(df, columns_names[0])
            df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
            df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)        
        '''

        df = df.style.applymap(self.text_format)
        self.write_to_path(df, 'UE')

    def ex_ue_pbi(self):
        df = self.data_extraction(k="PIB",url="https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=320.MNA.Q.N.I8.W2.S1.S1.B.B1GQ._Z._Z._Z.EUR.V.N")
        #Tasa de crecimiento
        columns_names = list(df.columns.values)
        df = self.tasaCrecimiento(df, columns_names[-1])
        df = self.episodios(df, columns_names)

        #FALTA REVISAR SI EXISTE
        '''
            list_quantity = self.episode_count(df, columns_names[0])
            df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
            df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)        
        '''

        df = df.style.applymap(self.text_format)
        self.write_to_path(df, 'UE')

    def ex_ue_inflacion(self, driver):
        driver.get("https://ec.europa.eu/eurostat/databrowser/view/PRC_HICP_MANR__custom_3302350/default/table?lang=en")
        driver.maximize_window()
        driver.get("https://ec.europa.eu/eurostat/databrowser/view/PRC_HICP_MANR__custom_3302350/default/table?lang=en")
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="geo"]/div[1]/button'))).click()  
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/div[6]/div[1]/custom-extraction/div[2]/form/div/div/div/div/div[2]/div[1]/dimension-position-selector/div/div[3]/md-content[1]/div[4]/ng-include/div/div/button[2]'))).click() 
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="embedded-Selector-geo"]/div/div[2]/div[3]/span/md-checkbox/div[1]'))).click()  
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="dimension-2"]'))).click()  
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="freqIdFrom_M"]'))).click()  
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="search-term-for-time-from"]'))).send_keys('1997-01')
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="select_option_83"]'))).click()  
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/div[6]/div[1]/custom-extraction/div[3]/table/tbody/tr/td[3]/button'))).click()  

        now = time.time()
        timediff = 0 

        while timediff < 30:
            try:
                WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="dropdownDownload"]'))).click()  
            except:
                pass

            timediff = time.time() - now

        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="xlsx__OnThisPageOnlyDownload"]'))).click()  

        patron = '/prc*'
        nombre = self.getDownLoadedFileName(patron)
        excel_path = nombre.replace('\\','/')
        now = time.time()
        timelapse = 0
        espera = 5 
        #Espera 5 segundos hasta que el archivo este por seguridad
        while timelapse < espera:
            try:
                archivo_excel = pd.ExcelFile(excel_path)
                break
            except:
                pass
            timelapse = time.time() - now 


        df = pd.read_excel(excel_path, sheet_name=2)
        df = df.iloc[[6,8]].T.dropna()
        df = df.reset_index()
        df = df[df.columns[1:]].iloc[2:]
        df = df.rename(columns={df.columns[0]:'Fecha', df.columns[1]:'Inflacion'})
        df.index = pd.to_datetime(df['Fecha'], format='%Y-%m')
        df = df.drop('Fecha',axis=1)
        df = df.replace(to_replace=':', value=np.nan)
        df = df.dropna()
        df = pd.DataFrame(df['Inflacion'].resample('Q').mean())
        df.index = df.index.to_series().apply(self.correccion_fecha)
        
        indicador = df
        columns_names = list(indicador.columns.values)
        indicador = self.episodios(indicador, columns_names)
        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)      
        '''
        driver.quit()
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'UE')
        pass
    
################Funciones Mexico###################
###################################################
    def correccion_fecha(self, fecha):
        fecha = fecha.replace(day=1)
        return fecha
        
    def infoSplitDf_Mx(self, list_info, indicador):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

        fecha_text, datos_text= [], []
        
        print(list_info)
        for dato in list_info:
            info_text = dato.text.split()
            
            if (indicador == 'PIB'):

                if('/01' in info_text[0]):
                    info_text[0] = info_text[0][0:4]+'/03'
                elif('/02' in info_text[0]):
                    info_text[0] = info_text[0][0:4]+'/06'
                elif('/03' in info_text[0]):
                    info_text[0] = info_text[0][0:4]+'/09'
                elif('/04' in info_text[0]):
                    info_text[0] = info_text[0][0:4]+'/12'

            if(info_text[0] == '31/12/1999' or info_text[0] == '1999/04' or info_text[0] == '1999/12'):
                break
            elif (info_text[1] == 'N/E'):
                datos_text.append(np.nan)
            else:
                dato_text = locale.atof(info_text[1])
                datos_text.append(dato_text)
            fecha_text.append(info_text[0])

        data = {'Fecha': fecha_text,
            indicador: datos_text}
        df = pd.DataFrame(data, columns=['Fecha', indicador])
        return df

    #def getDownLoadedFileName(waitTime, driver):
    def getDownLoadedFileName(self, patron):
        #Usando comandos de terminal:
        path = self.path.get() #Esto deve de ser ingresado por el usuario de alguan forma
        flag = 0 #Revisa el nombre del archivo
        timestart = time.time()

        while flag == 0 :
            archivos = sorted(glob.glob(path+patron))

            if len(archivos) > 0:
                flag = 1

            if time.time() - timestart > 180: #Regresar a 180
                self.errores.insert(tk.END, "Tiempo de espera excedido\n")
                flag = 1
                return None 

        return archivos[0]


    def ex_mx_reservas(self, driver):
        # Inicializar el navegador
        driver.get('https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CF106&locale=es')
        driver.maximize_window()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
            'button#graph_nodo_6_SF43707')))\
                .click()

        driver.switch_to.frame(driver.find_element(By.ID, 'iframeGrafica'))

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
            'button#btnDatos')))\
                .click()
        
        #Limpieza de datos y almacenamiento en Data Frame
        reservas = driver.find_elements('xpath',"//table[@id = 'tableData']//tr[@data-ts]")
        df = self.infoSplitDf_Mx(reservas, 'Reservas')
        df = self.dataCleaning(df, '%d/%m/%Y')
        prom_mensual = df.resample('M').mean()

        quarterly = prom_mensual.resample('Q').mean()
        quarterly = quarterly.reset_index()
        lista_fechas = []
        for fecha in quarterly['Fecha']:
            dias = int(fecha.strftime('%d'))-1
            fecha_nueva = fecha - datetime.timedelta(days = dias)
            lista_fechas.append(fecha_nueva)
        quarterly['Fecha'] = lista_fechas
        quarterly = quarterly.set_index('Fecha')
        columns_names = list(quarterly.columns.values)
        quarterly = self.tasaCrecimiento(quarterly, columns_names[-1])
        quarterly = self.espisodios(quarterly, columns_names)
        list_quantity = self.episode_count(quarterly, columns_names[0])
        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)    
        '''
        quarterly = quarterly.style.applymap(self.text_format)
        driver.quit()
        self.write_to_path(quarterly,'MX')

    def ex_mx_tipo_de_cambio(self,driver):
        # Inicializar el navegador
        driver.get('https://www.banxico.org.mx/tipcamb/main.do?page=tip&idioma=sp')
        try:
            driver.maximize_window()
        except:
            pass

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
            'a.liga')))\
                .click()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
            'input.renglonNon')))\
                .send_keys(Keys.CONTROL, 'a')

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
            'input.renglonNon')))\
                .send_keys(Keys.BACKSPACE)

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
            'input.renglonNon')))\
                .send_keys('01/01/2000')     

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
            'input.botonesSIE')))\
                .click()

        driver.switch_to.window(driver.window_handles[1])

        tipo_cambio_fecha = driver.find_elements("xpath","//body//table//td[@valign='top' and @align='center']//tr[@align='left']/td")
        tipo_cambio_datos = driver.find_elements("xpath", "//body//table//td[@valign='top' and @align='center']//tr[@align='right']/td")

        del tipo_cambio_datos[len(tipo_cambio_fecha):]

        fecha_text_list, datos_text_list = [], []

        for dato in tipo_cambio_datos:
            dato_text = dato.text

            if(dato_text == 'N/E'):
                datos_text_list.append(np.nan)
            else:
                datos_text_list.append(float(dato_text))

        for fecha in tipo_cambio_fecha:
            fecha_text = fecha.text
            fecha_text_list.append(fecha_text)

        diccionario_tipo_cambio = {'Fecha': fecha_text_list,
                    'Tipo de Cambio': datos_text_list
                    }

        df = pd.DataFrame(diccionario_tipo_cambio, columns=['Fecha', 'Tipo de Cambio'])
        #Limpieza de datos
        df = self.dataCleaning(df, '%d/%m/%Y')



        #Promedio mensual
        prom_mensual = df.resample('M').mean()

        quarterly = prom_mensual.resample('Q').mean()
        quarterly = quarterly.reset_index()
        lista_fechas = []
        for fecha in quarterly['Fecha']:
            dias = int(fecha.strftime('%d'))-1
            fecha_nueva = fecha - datetime.timedelta(days = dias)
            lista_fechas.append(fecha_nueva)
        quarterly['Fecha'] = lista_fechas
        quarterly = quarterly.set_index('Fecha')
        columns_names = list(quarterly.columns.values)
        quarterly = self.espisodios(quarterly, columns_names)
        '''
        list_quantity = self.episode_count(quarterly, columns_names[0])
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)    
        '''
        driver.quit()
        quarterly = quarterly.style.applymap(self.text_format)
        self.write_to_path(quarterly, 'MX')


    def ex_mx_exportaciones(self,driver):
        # Inicializar el navegador
        driver.get('https://www.inegi.org.mx/sistemas/bie/')
        try:
            driver.maximize_window()
        except:
            pass

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="fila_contextTopics_1000_4"]/div[1]')))\
                .click()

        time.sleep(5)

        driver.execute_script("window.scrollTo(0, 500)") #Por seguridad

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="fila_contextTopics_10000520_8"]')))\
                .click()

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//div[@class="derecha"]/label[contains(text(),"Series originales")]')))\
                .click()

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//label[contains(text(),"Exportaciones")]')))\
                .click()

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//label[contains(text(),"Valores absolutos")]')))\
                .click()

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//label[contains(text(),"Total (Millones de dólares)")]')))\
                .click()

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="btn_tabladivfastview"]'))).click()

        time.sleep(15)

        ''' 
        Version anterior
        exportaciones = driver.find_elements(By.XPATH ,"//div[@id = 'ctl00_cphPage_ContentUpdatePanel2']/center//tr[@valign='top']")

        #Separando la info, pasando los datos a números y obteniendo data frame
        df = self.infoSplitDf_Mx(exportaciones, 'Exportaciones')        
        '''
        tablas = pd.read_html(driver.page_source)
        df =  tablas[0]
        mapeo = {'Ene':'Jan','Abr':'Apr','Ago':'Aug','Dic':'Dec'}

        df['Fecha'] = df['Periodo'].str.split().str[0] +' '+df['Periodo'].str.split().str[1].replace(mapeo)
        df = df.drop('Periodo',axis=1)
        indicador = self.dataCleaning(df, '%Y %b')
        quarterly = indicador.resample('Q').mean()
        quarterly = quarterly.reset_index()
        lista_fechas = []
        for fecha in quarterly['Fecha']:
            dias = int(fecha.strftime('%d'))-1
            fecha_nueva = fecha - datetime.timedelta(days = dias)
            lista_fechas.append(fecha_nueva)
        quarterly['Fecha'] = lista_fechas
        quarterly = quarterly.set_index('Fecha')
        columns_names = list(quarterly.columns.values)
        #quarterly.to_excel(writer, sheet_name = columns_names[0])
        quarterly = self.espisodios(quarterly, columns_names)

        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = self.episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)
        '''
        quarterly = quarterly.style.applymap(self.text_format)
        #indicador.to_excel(writer, sheet_name = columns_names[0])
        driver.quit()
        self.write_to_path(quarterly, 'MX')
        
    def ex_mx_liquidez(self,driver):
        driver.get('https://www.cnbv.gob.mx/SECTORES-SUPERVISADOS/BANCA-MULTIPLE/Paginas/Información-Estadística.aspx')
        try:
            driver.maximize_window()
        except:
            pass

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//p[@style = "text-align:left;"]/a')))\
                .click()

        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//table[@class="MsoNormalTable "]/tbody/tr/td/div/span/a/span[@lang="ES" and @style="font-size: 10pt; text-decoration: none; color: blue"]')))\
                .click()

        driver.switch_to.window(driver.window_handles[-1])

        excel_url = driver.find_element(By.XPATH, '//tr[@id="1"]//a').get_attribute('href')

        archivo_excel = pd.ExcelFile(excel_url)

        df_2 = archivo_excel.parse('SH', skiprows=1)
        df = df_2.iloc[:,4:]
        df.columns = df.iloc[0]
        df = df.set_index('Estado de Situación Financiera (millones de pesos corrientes)')
        Activo = df.loc['Activo'][:-4]
        Pasivo = df.loc['Pasivo'][:-4]
        Capital = df.loc['Capital Contable'][:-4]
        df_liquidez_solvencia = pd.DataFrame()
        df_liquidez_solvencia['Liquidez'] = Pasivo/Activo
        df_liquidez_solvencia['Solvencia'] = Capital/Activo 
        '''
        Anterior versión

        #Cambiando el indice del data frame
        df = df.set_index('Indicadores del Balance General (millones de pesos corrientes)')

        #Eliminando columnas innecesarias
        df = df.drop(['Unnamed: 0'], axis = 1)

        #Cambiando Columnas por filas
        df = df.transpose()

        #Data frame con sólo la info necesaria
        df_resumen = df[['Pasivo', 'Activo','Capital contable']]

        #Data frame liquidez y solvencia calculada
        df_liquidez_solvencia = pd.DataFrame()
        df_liquidez_solvencia['Liquidez'] = df_resumen['Pasivo']/df_resumen['Activo']
        df_liquidez_solvencia['Solvencia'] = df_resumen['Capital contable']/df_resumen['Activo']      
        '''

        df_liquidez_solvencia = df_liquidez_solvencia.sort_index()
        df_liquidez_solvencia.index.name = 'Fecha'
        indicador = df_liquidez_solvencia['Liquidez']
        quarterly = indicador.resample('Q').mean()
        quarterly = quarterly.reset_index()
        lista_fechas = []
        for fecha in quarterly['Fecha']:
            dias = int(fecha.strftime('%d'))-1
            fecha_nueva = fecha - datetime.timedelta(days = dias)
            lista_fechas.append(fecha_nueva)
        quarterly['Fecha'] = lista_fechas
        quarterly = quarterly.set_index('Fecha')
        columns_names = list(quarterly.columns.values)
        #quarterly.to_excel(writer, sheet_name = columns_names[0])
        quarterly = self.espisodios(quarterly, columns_names)

        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = self.episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)
        '''
        quarterly = quarterly.style.applymap(self.text_format)
        #indicador.to_excel(writer, sheet_name = columns_names[0])
        self.write_to_path(quarterly,'MX')
        driver.quit()
        

    def ex_mx_solvencia(self, driver):
        driver.get('https://www.cnbv.gob.mx/SECTORES-SUPERVISADOS/BANCA-MULTIPLE/Paginas/Información-Estadística.aspx')
        try:
            driver.maximize_window()
        except:
            pass

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//p[@style = "text-align:left;"]/a')))\
                .click()

        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//table[@class="MsoNormalTable "]/tbody/tr/td/div/span/a/span[@lang="ES" and @style="font-size: 10pt; text-decoration: none; color: blue"]')))\
                .click()

        driver.switch_to.window(driver.window_handles[-1])

        excel_url = driver.find_element(By.XPATH, '//tr[@id="1"]//a').get_attribute('href')

        archivo_excel = pd.ExcelFile(excel_url)
        df_2 = archivo_excel.parse('SH', skiprows=1)
        df = df_2.iloc[:,4:]
        df.columns = df.iloc[0]
        df = df.set_index('Estado de Situación Financiera (millones de pesos corrientes)')
        Activo = df.loc['Activo'][:-4]
        Pasivo = df.loc['Pasivo'][:-4]
        Capital = df.loc['Capital Contable'][:-4]
        df_liquidez_solvencia = pd.DataFrame()
        df_liquidez_solvencia['Liquidez'] = Pasivo/Activo
        df_liquidez_solvencia['Solvencia'] = Capital/Activo 
        '''
        Anterior versión

        #Cambiando el indice del data frame
        df = df.set_index('Indicadores del Balance General (millones de pesos corrientes)')

        #Eliminando columnas innecesarias
        df = df.drop(['Unnamed: 0'], axis = 1)

        #Cambiando Columnas por filas
        df = df.transpose()

        #Data frame con sólo la info necesaria
        df_resumen = df[['Pasivo', 'Activo','Capital contable']]

        #Data frame liquidez y solvencia calculada
        df_liquidez_solvencia = pd.DataFrame()
        df_liquidez_solvencia['Liquidez'] = df_resumen['Pasivo']/df_resumen['Activo']
        df_liquidez_solvencia['Solvencia'] = df_resumen['Capital contable']/df_resumen['Activo']      
        '''

        df_liquidez_solvencia = df_liquidez_solvencia.sort_index()
        df_liquidez_solvencia.index.name = 'Fecha'
        indicador = df_liquidez_solvencia['Solvencia']
        quarterly = indicador.resample('Q').mean()
        quarterly = quarterly.reset_index()
        lista_fechas = []
        for fecha in quarterly['Fecha']:
            dias = int(fecha.strftime('%d'))-1
            fecha_nueva = fecha - datetime.timedelta(days = dias)
            lista_fechas.append(fecha_nueva)
        quarterly['Fecha'] = lista_fechas
        quarterly = quarterly.set_index('Fecha')
        columns_names = list(quarterly.columns.values)
        #quarterly.to_excel(writer, sheet_name = columns_names[0])
        quarterly = self.espisodios(quarterly, columns_names)

        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = self.episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)
        '''
        quarterly = quarterly.style.applymap(self.text_format)
        #indicador.to_excel(writer, sheet_name = columns_names[0])
        self.write_to_path(quarterly,'MX')
        driver.quit()
        
    def ex_mx_portafolio(self, driver):
        # Inicializar el navegador
        driver.get('https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CE183&locale=es')
        driver.maximize_window()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
            'button#graph_nodo_2_SE45273')))\
                .click()

        driver.switch_to.frame(driver.find_element(By.ID, 'iframeGrafica'))

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
            'button#btnDatos')))\
                .click()

        portafolio= driver.find_elements(By.XPATH ,"//table[@id = 'tableData']//tr[@data-ts]")

        #Limpieza de datos
        df = self.infoSplitDf_Mx(portafolio, 'Inversión de Portafolio')    
        indicador = self.dataCleaning(df, '%d/%m/%Y')
        quarterly = indicador.reset_index()
        lista_fechas_portafolio = []
        for fecha in quarterly['Fecha']:
            fecha_nueva_portafolio = fecha - relativedelta(months = 1)
            lista_fechas_portafolio.append(fecha_nueva_portafolio)
        quarterly['Fecha'] = lista_fechas_portafolio
        quarterly = quarterly.set_index('Fecha')
        columns_names = list(quarterly.columns.values)
        #quarterly.to_excel(writer, sheet_name = columns_names[0])
        quarterly = self.espisodios(quarterly, columns_names)

        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = self.episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)
        '''
        driver.quit()
        quarterly = quarterly.style.applymap(self.text_format)
        self.write_to_path(quarterly,'MX')
        #indicador.to_excel(writer, sheet_name = columns_names[0])

    def ex_mx_deuda(self, driver):
        # Inicializar el navegador
        driver.get('https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CG7&sector=9&locale=es')
        driver.maximize_window()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
            'input#exportarSeriesFormatoXLS')))\
                .click()

        '''
        nombre_archivo = getDownLoadedFileName(180, driver) #Se esperan 3 minutos a que se descargue
        print(nombre_archivo)   
        '''
        #OTRA OPCIÓN: BUSCAR EL NOMBRE DEL ARCHIVO EN LA CARPETA CON REGEX, ASUMIENDO QUE EMPIEZA CON CONSULTA

        #Leyendo el archivo

        patron = '/Consulta*.xlsx'
        nombre_archivo = self.getDownLoadedFileName(patron) #FALTAAAAAAAAAAAAAAA
        excel_path = nombre_archivo.replace('\\','/')

        now = time.time()
        timelapse = 0
        espera = 5 
        #Espera 5 segundos hasta que el archivo este por seguridad
        while timelapse < espera:
            try:
                archivo_excel = pd.ExcelFile(excel_path)
                break
            except:
                pass
            timelapse = time.time() - now 

        df = archivo_excel.parse('Hoja1', skiprows=17)

        #Filtrando sólo la información necesaria
        filtro = df['Fecha']>datetime.datetime.strptime("1999/12/31", "%Y/%m/%d")
        df = df[filtro]

        #Saldos a Final del Periodo
        df = df[['Fecha','SG193', 'SG199']] #SG193 = Económica Amplia, SG199 = Consolidada con Banco de México

        #Definiendo Fecha como index
        df = df.set_index('Fecha')

        #Calculo de la deuda total
        df_deuda_total = pd.DataFrame()
        df_deuda_total['Deuda Pública'] = df['SG193'] + df['SG199']
        df_deuda_total = df_deuda_total.rename(columns={'Deuda Pública':'Deuda Externa'})
        print(df_deuda_total)
        indicador = df_deuda_total.sort_index()
        quarterly = indicador.resample('Q').mean()
        quarterly = quarterly.reset_index()
        print('Quarterly')
        print(quarterly)
        lista_fechas = []
        for fecha in quarterly['Fecha']:
            dias = int(fecha.strftime('%d'))-1
            fecha_nueva = fecha - datetime.timedelta(days = dias)
            lista_fechas.append(fecha_nueva)
        quarterly['Fecha'] = lista_fechas
        quarterly = quarterly.set_index('Fecha')
        columns_names = list(quarterly.columns.values)
        #quarterly.to_excel(writer, sheet_name = columns_names[0])
        indicador = self.espisodios(quarterly, columns_names)

        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = self.episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)
        '''
        driver.quit()
        print(indicador)
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'MX')
        #indicador.to_excel(writer, sheet_name = columns_names[0])

    def ex_mx_pbi(self, driver):
        # Inicializar el navegador
        driver.get('https://www.inegi.org.mx/sistemas/bie/')
        try:
            driver.maximize_window()
        except:
            pass

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="fila_contextTopics_1000_4"]/div[1]')))\
                .click()

        time.sleep(5)

        driver.execute_script("window.scrollTo(0, 300)") #Por seguridad

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//label[contains(text(),"Producto interno")]')))\
                .click()

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//label[contains(text(),"Series Originales")]')))\
                .click()

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//label[contains(text(),"Valores a precios corrientes")]')))\
                .click()

        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//label[contains(text(),"Producto Interno Bruto")]')))\
                .click()


        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="btn_tabladivfastview"]'))).click()
        
        time.sleep(15)
        pib = pd.read_html(driver.page_source)[0]
        mapeo = {'1T':'/03','2T':'/06', '3T':'/09', '4T':'/12'}
        #Separando la info, pasando los datos a números y obteniendo data frame
        #df = self.infoSplitDf_Mx(pib, 'PIB')   Anterior versión
        #Limpieza de datos
        indicador = pd.DataFrame()
        indicador['Fecha'] = pib['Periodo'].str.split().str[0] + pib['Periodo'].str.split().str[1].replace(mapeo)
        indicador['PIB'] = pib['Millones de pesos a precios corrientes']
        lista_fechas_PIB = []
        for fecha in indicador['Fecha']:
            fecha_nueva_PIB = datetime.datetime.strptime(fecha, '%Y/%m')
            lista_fechas_PIB.append(fecha_nueva_PIB)
        indicador['Fecha'] = lista_fechas_PIB
        indicador = indicador.set_index('Fecha')
        indicador = indicador.sort_index()

        columns_names = list(indicador.columns.values)
        #quarterly.to_excel(writer, sheet_name = columns_names[0])
        indicador = self.espisodios(indicador, columns_names)

        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = self.episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)
        '''
        driver.quit()
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'MX')
        #indicador.to_excel(writer, sheet_name = columns_names[0

    def ex_mx_inflacion(self,driver):
        url = 'https://www.inegi.org.mx/temas/inpc/'
        driver.get(url)
        driver.maximize_window()
        boton_tabla = '//*[@id="btn_tablagraf_gral0"]'
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, boton_tabla))).click()  
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tableStatcontGraficagraf_gral0"]')))
        tablas = pd.read_html(driver.page_source)
        df = tablas[1]
        mapeo = {'Ene':'Jan','Abr':'Apr','Ago':'Aug','Dic':'Dec'}
        df['Año'] = df['Periodo'].str.split().str[0]
        df['Mes'] = df['Periodo'].str.split().str[1].replace(mapeo)
        df['Fecha'] = df['Año'] + ' ' + df['Mes']
        df = df.drop(['Periodo', 'Año', 'Mes'] ,axis=1)
        df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y %b')
        df.set_index('Fecha', inplace=True)
        df = pd.DataFrame(df['Porcentaje'].resample('Q').mean())
        df.index = df.index.to_series().apply(self.correccion_fecha)
        indicador = df.rename(columns = {'Porcentaje':'Inflacion'})

        #Resampleo
        quarterly = indicador.resample('Q').mean()
        quarterly = quarterly.reset_index()
        lista_fechas = []
        for fecha in quarterly['Fecha']:
            dias = int(fecha.strftime('%d'))-1
            fecha_nueva = fecha - datetime.timedelta(days = dias)
            lista_fechas.append(fecha_nueva)
        quarterly['Fecha'] = lista_fechas
        quarterly = quarterly.set_index('Fecha')
        columns_names = list(quarterly.columns.values)
        #quarterly.to_excel(writer, sheet_name = columns_names[0])

        #Episodios
        quarterly = self.espisodios(quarterly, columns_names)

        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = self.episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)
        '''
        driver.quit()
        quarterly = quarterly.style.applymap(self.text_format)
        self.write_to_path(quarterly,'MX')
        #indicador.to_excel(writer, sheet_name = columns_names[0])

##############EXTRACCIÓN JAPÓN########################
#####################################################
    
    #Funciones de extraccion
    def ex_jp_reservas(self):
        df = pd.read_csv("https://www.mof.go.jp/policy/international_policy/reference/official_reserve_assets/historical.csv", encoding = "ISO-8859-1")
        df_temp = df.iloc[18:,[2,3,5]].reset_index(drop=True)
        df_temp = df_temp.rename(columns={'Unnamed: 2':'Año', 'Unnamed: 3':'Mes', 'Unnamed: 5':'Reservas Internacionales',})
        df_temp['Año'] = df_temp['Año'].ffill()
        df_temp['Año'] = df_temp['Año'].astype(int)
        df_temp['Mes'] = df_temp['Mes'].str[:3]
        df_temp['Fecha'] = df_temp['Año'].astype(str) + ' ' + df_temp['Mes']
        df_temp['Fecha'] = pd.to_datetime(df_temp['Fecha'], format='%Y %b')
        df_temp['Reservas Internacionales'] = df_temp['Reservas Internacionales'].astype('float')
        df_temp.set_index('Fecha',  inplace=True)
        df_reservas = pd.DataFrame(df_temp['Reservas Internacionales'].resample('Q').mean())
        columns_names = list(df_reservas.columns.values)
        df_reservas = self.tasaCrecimiento(df_reservas, columns_names[-1])
        #writer = pd.ExcelWriter('episodios_indicadores_JP.xlsx')

        indicador = df_reservas
        columns_names = list(indicador.columns.values)
        indicador = self.episodios(indicador, columns_names)
        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)      
        '''
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'JP')
        #indicador.to_excel(writer, sheet_name = columns_names[0])

    def ex_jp_tipo_de_cambio(self, driver):
        driver.get('https://fred.stlouisfed.org/series/EXJPUS')
        driver.maximize_window()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="download-button"]'))).click() #Da click en el boton de descarga
        time.sleep(5)
        #Prueba por 20 segundos
        inicio = time.time()
        tiempo = 0
        while tiempo < 20:
            try:
                url = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="download-data-csv"]'))).get_attribute('href')
                print(url)
                df = pd.read_csv(url, parse_dates=['DATE'])
                break #Si funciona se detiene
            except:
                tiempo = time.time() - inicio

        df.set_index('DATE', drop=True, inplace=True)
        df.index.names = ['Fecha']
        df = df['2000':str(datetime.datetime.today().year)]
        df = df.resample('Q').mean()
        df = df.rename(columns = {"EXJPUS":'Tipo de Cambio'})

        indicador = df
        columns_names = list(indicador.columns.values)
        indicador = self.episodios(indicador, columns_names)
        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)      
        '''
        driver.quit()
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'JP')
        #indicador.to_excel(writer, sheet_name = columns_names[0])

    def ex_jp_exportaciones(self):
        df = pd.read_csv('https://www.customs.go.jp/toukei/suii/html/data/d41ma.csv', encoding="ISO-8859-1")
        df = df.iloc[1:]
        df = df.rename(columns=df.iloc[0])
        df = df.iloc[2:]
        df.dropna(inplace=True)
        df["Years/Months"] = [datetime.datetime.strptime(i, "%Y/%m") for i in df["Years/Months"]]
        df.set_index("Years/Months", inplace=True, drop=True)
        df.index.names = ['Fecha']
        df["Exp-Total"] = df["Exp-Total"].astype('int64')
        df.drop('Imp-Total', axis=1, inplace=True)
        df = df[df["Exp-Total"]!=0]
        #Recordatorio: Esto estará en millones de yen
        df = pd.DataFrame(df['Exp-Total'].resample('Q').mean())
        df = df['2000':]
        df = df.rename(columns={'Exp-Total':'Exportaciones'})

        indicador = df
        columns_names = list(indicador.columns.values)
        indicador = self.episodios(indicador, columns_names)
        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)      
        '''
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'JP')
        #indicador.to_excel(writer, sheet_name = columns_names[0])

    def ex_jp_liquidez(self):
        #Falta optimizar mucho
        fechas = pd.date_range(start='1/1/2012', end=datetime.datetime.today())
        liquidez  = {"Fecha":[],"Liquidez":[]}
        solvencia = {"Fecha":[],"Solvencia":[]}

        for fecha in fechas:
            temp = str(fecha.year)[-2:]+'0'*(1-fecha.month//10)+str(fecha.month)+'0'*(1-len(str(fecha.day))//2)+str(fecha.day)
            año = fecha.year
            query = "https://www.boj.or.jp/en/statistics/boj/other/acmai/release/" + str(año) + "/ac" + temp + ".htm/"

            try:
                tablas = pd.read_html(query)
                Activos_Totales =tablas[0].iloc[-1][1]
                Depositos = tablas[1].iloc[0:6][1].sum()
                C_Capital = tablas[1].iloc[6:-1][1].sum()

                liquidez['Fecha'].append(fecha)
                liquidez['Liquidez'].append(Depositos/Activos_Totales)
                solvencia['Fecha'].append(fecha)
                solvencia['Solvencia'].append(C_Capital/Activos_Totales)        

            except:
                continue
        
        df_liquidez = pd.DataFrame(liquidez).set_index('Fecha', drop=True).resample('Q').mean()
        #df_solvencia = pd.DataFrame(solvencia).set_index('Fecha', drop=True).resample('Q').mean()

        indicador = df_liquidez
        columns_names = list(indicador.columns.values)
        indicador = self.episodios(indicador, columns_names)
        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)      
        '''
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'JP')
        #indicador.to_excel(writer, sheet_name = columns_names[0])

    def ex_jp_solvencia(self):
        #Falta optimizar mucho
        fechas = pd.date_range(start='1/1/2012', end=datetime.datetime.today())
        liquidez  = {"Fecha":[],"Liquidez":[]}
        solvencia = {"Fecha":[],"Solvencia":[]}

        for fecha in fechas:
            temp = str(fecha.year)[-2:]+'0'*(1-fecha.month//10)+str(fecha.month)+'0'*(1-len(str(fecha.day))//2)+str(fecha.day)
            año = fecha.year
            query = "https://www.boj.or.jp/en/statistics/boj/other/acmai/release/" + str(año) + "/ac" + temp + ".htm/"

            try:
                tablas = pd.read_html(query)
                Activos_Totales =tablas[0].iloc[-1][1]
                Depositos = tablas[1].iloc[0:6][1].sum()
                C_Capital = tablas[1].iloc[6:-1][1].sum()

                liquidez['Fecha'].append(fecha)
                liquidez['Liquidez'].append(Depositos/Activos_Totales)
                solvencia['Fecha'].append(fecha)
                solvencia['Solvencia'].append(C_Capital/Activos_Totales)        

            except:
                continue
        
        #df_liquidez = pd.DataFrame(liquidez).set_index('Fecha', drop=True).resample('Q').mean()
        df_solvencia = pd.DataFrame(solvencia).set_index('Fecha', drop=True).resample('Q').mean()
        indicador = df_solvencia
        columns_names = list(indicador.columns.values)
        indicador = self.episodios(indicador, columns_names)
        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)      
        '''
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'JP')
        #indicador.to_excel(writer, sheet_name = columns_names[0])

    def ex_jp_portafolio(self):
        df = pd.read_csv('https://www.mof.go.jp/policy/international_policy/reference/balance_of_payments/bp_trend/bppi/pi/6pi-1.csv', encoding = "ISO-8859-1")
        df = df.iloc[56:,[2,3,13]].reset_index(drop=True)
        df = df.rename(columns={'Unnamed: 2':'Año', 'Unnamed: 3':'Mes', 'Unnamed: 13':'Inversión de Portafolio',})
        df['Año'] = df['Año'].ffill()
        df['Año'] = df['Año'].astype(int)
        df['Mes'] = df['Mes'].str[:3]
        df['Fecha'] = df['Año'].astype(str) + ' ' + df['Mes']
        df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y %b')
        df['Inversión de Portafolio'] = df['Inversión de Portafolio'].apply(lambda x: float(str(x).replace(',','.'))).astype('float')
        df.set_index('Fecha',  inplace=True)
        df = pd.DataFrame(df['Inversión de Portafolio'].resample('Q').mean())
        df = df['2000':]
        columns_names = list(df.columns.values)
        df = self.tasaCrecimiento(df, columns_names[-1])
        indicador = df
        columns_names = list(indicador.columns.values)
        indicador = self.episodios(indicador, columns_names)
        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)      
        '''
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'JP')
        #indicador.to_excel(writer, sheet_name = columns_names[0])

    def ex_jp_deuda(self, driver):
        driver.get('https://www.boj.or.jp/en/statistics/public/ngd/index.htm/')
        driver.maximize_window()
        xpaths = ['//*[@id="contents-skip"]/div/p/a', #Link
        '//*[@id="menuSearchTabpanel"]/div[2]/div[1]/div[2]/input',#Boton
        '//*[@id="menuSearchDataCodeList"]/tbody/tr[1]/td/label', #Checkbox National Goverment Debt
        '//*[@id="menuSearchTabpanel"]/div[2]/div[2]/div[4]/a', #Add to Search Condition 
        ]

        for xpath in xpaths:
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

        #Bajar de pagina?

        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fromYear"]')))
        element.send_keys('2000')
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="toYear"]')))
        element.send_keys(str(datetime.datetime.today().year))

        xpaths_selection = ['//*[@id="cmbFREQ"]',
        '//*[@id="cmbFREQ"]/option[6]',
        '//*[@id="cmbFREQ_OPTION"]',
        '//*[@id="cmbFREQ_OPTION"]/option[3]',
        '//*[@id="resultArea"]/div[4]/ul/li[1]/a',]

        for xpath in xpaths_selection:
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(5)
        element = driver.find_element(By.XPATH ,"//a[@class='littlelargeButton largeButton-download']")
        element.click()

        driver.switch_to.window(driver.window_handles[-1])
        url = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/table/tbody/tr/td/a'))).get_attribute('href')

        df = pd.read_csv(url)
        df = df.iloc[1:]
        df = df.rename(columns={df.columns[0]:'Fecha', df.columns[1]:'Deuda Externa'})
        df['Deuda Externa'] = df['Deuda Externa'].astype('float')
        df.set_index('Fecha',inplace=True)
        indicador = df
        columns_names = list(indicador.columns.values)
        indicador = self.episodios(indicador, columns_names)
        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)      
        '''
        driver.quit()
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'JP')
        #indicador.to_excel(writer, sheet_name = columns_names[0])

    def ex_jp_pbi(self):
        url = 'https://www.esri.cao.go.jp/jp/sna/data/data_list/sokuhou/files/2022/qe221_2/tables/gaku-mg2212.csv'
        df = pd.read_csv(url, encoding = "ISO-8859-1")
        df = df.iloc[6:,0:2].reset_index(drop=True)
        df = df.rename(columns={df.columns[0]:'Fecha', df.columns[1]:'GDP'})
        df['Año'] = [i[:4] if '/' in str(i) else np.nan for i in df['Fecha']]
        df['Año'] = df['Año'].ffill()
        df.dropna(inplace=True)
        df['Mes'] = [str(i).split('-')[-1].strip().strip('.') for i in df['Fecha']]
        df['Mes'] = ['0'*(1-int(i)//10)+i for i in df['Mes']]
        df['Fecha'] =  df['Año']+' '+df['Mes']
        df.drop(['Año','Mes'], inplace=True, axis=1)
        df['Fecha'] = [datetime.datetime.strptime(i,"%Y %m") for i in df['Fecha']]
        df.set_index('Fecha', inplace=True)
        df = df['2000':]
        df['GDP'] = df['GDP'].str.replace(',','').astype('float')
        columns_names = list(df.columns.values)
        df = self.tasaCrecimiento(df, columns_names[-1])
        df = df.rename(columns={'GDP':'PIB'})
        indicador = df
        columns_names = list(indicador.columns.values)
        indicador = self.episodios(indicador, columns_names)
        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)      
        '''
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'JP')
        #indicador.to_excel(writer, sheet_name = columns_names[0])

    def ex_jp_inflacion(self, driver):
        driver.get('https://www.stat.go.jp/english/data/cpi/1588.html#mon')
        driver.maximize_window()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="section"]/article[2]/ul[1]/li[1]/a/img'))).click() #Da click en el boton de descarga
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div[2]/section/div[2]/div/div/div[1]/section/section/div/div[2]/ul[1]/li[2]/div[last()]/a'))).click()
        url = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="stat-dl_icon stat-icon_4 stat-icon_format js-dl stat-download_icon_left"]'))).get_attribute('href')
        df = pd.read_excel(url)
        df = df.iloc[13:,7:9].dropna().reset_index(drop=True)
        df = df.rename(columns={'Unnamed: 7':'Fecha', df.columns[1]:'Inflacion'})
        df['Año'] = [i[:4] if len(i.strip()) > 2 else np.nan for i in df['Fecha']]
        df['Mes'] = ['0'*(1-(int(i)//10))+i  if len(i.strip()) <= 2 else "0"+i[-2] for i in df['Fecha']]
        df['Año'] = df['Año'].ffill()
        df = df.drop('Fecha',axis=1)
        df['Fecha'] = df['Año'] + '/' + df['Mes']
        df.drop(['Año','Mes'], axis=1,inplace=True)
        df['Fecha'] = df['Fecha'].str.strip()
        df['Fecha'] = pd.to_datetime(df['Fecha'], format="%Y/%m")
        df.set_index(df['Fecha'], drop=True, inplace=True)
        df = pd.DataFrame(df['Inflacion'].resample('Q').mean())
        df = df['2000':]   
    
        indicador = df
        columns_names = list(indicador.columns.values)
        indicador = self.episodios(indicador, columns_names)
        '''
        df_quantity = pd.DataFrame(columns= ['Indicador', 'Alertas', 'Crisis'])
        list_quantity = episode_count(indicador, columns_names[0])
        df_quantity=df_quantity.append({'Indicador' : list_quantity[0] , 'Alertas' : list_quantity[1], 'Crisis' : list_quantity[2]} , ignore_index=True)      
        '''
        driver.quit()
        indicador = indicador.style.applymap(self.text_format)
        self.write_to_path(indicador,'JP')
       #indicador.to_excel(writer, sheet_name = columns_names[0])

################### Funciones China ########################
############################################################

# Funciones de apoyo
    def isEmpty(self,variable):
        if(variable == ''):
            variable = float(0)
        else:
            variable = float(variable)
        
        return variable    
        
    def monthly_prep(self, indicador):
        quarterly = indicador.resample('Q').mean()
        quarterly = quarterly.reset_index()
        lista_fechas = []
        for fecha in quarterly['Fecha']:
            dias = int(fecha.strftime('%d'))-1
            fecha_nueva = fecha - datetime.timedelta(days = dias)
            lista_fechas.append(fecha_nueva)
        quarterly['Fecha'] = lista_fechas
        quarterly = quarterly.set_index('Fecha')
        return quarterly

    def trim_q_prep(self, indicador):
        indicador = indicador.reset_index()
        lista_fechas = []
        for fecha in indicador['Fecha']:
            if('Q1' in fecha):
                fecha = fecha[0:4]+'-03'
            elif('Q2' in fecha):
                fecha = fecha[0:4]+'-06'
            elif('Q3' in fecha):
                fecha = fecha[0:4]+'-09'
            elif('Q4' in fecha):
                fecha = fecha[0:4]+'-12'
            lista_fechas.append(fecha)
        indicador['Fecha'] = lista_fechas
        indicador['Fecha'] = pd.to_datetime(indicador['Fecha'])
        indicador = indicador.set_index('Fecha')
        indicador = indicador.drop('index', axis=1)
        return indicador
    
    def trim_num_prep(self, indicador):
        indicador = indicador.reset_index()
        lista_fechas = []
        for fecha in indicador['Fecha']:
            fecha_nueva = fecha - relativedelta(months = 1)
            lista_fechas.append(fecha_nueva)
        indicador['Fecha'] = lista_fechas
        indicador = indicador.set_index('Fecha')
        indicador = indicador.sort_index()
        return indicador

    def episodios_estilo(self, indicador):
        columns_names = list(indicador.columns.values)
        indicador = self.espisodios(indicador, columns_names)
        indicador = indicador.style.applymap(self.text_format)
        return indicador

    def ex_cn_reservas(self,driver):
        # Inicializar el navegador
        driver.get('https://www.safe.gov.cn/en/ForexReserves/index.html')

        forex_reserves = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div[2]/ul/li')

        i = 1
        dates_list = []
        values_list = []

        for element in forex_reserves:
            element = element.text.split('\n')
            if('Official Reserve Assets'in element[0]):
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.XPATH, 
                    '/html/body/div[3]/div/div[2]/div[3]/div[2]/ul/li['+str(i)+']/dt/a')))\
                        .click()       

                driver.switch_to.window(driver.window_handles[-1])                

                if('2019' in element[0]):
                    
                    dates = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[1]/div[3]/div[4]/table/tbody/tr[3]/td')
                    values = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[1]/div[3]/div[4]/table/tbody/tr[6]/td')
                
                elif('2017' in element[0]):
                    for p in range(1,6,2):
                        excel_url = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[3]/div[4]/div/div[2]/p['+ str(p) +']/a').get_attribute('href')

                        archivo_excel = pd.ExcelFile(excel_url)

                        if(p == 1):
                            df = archivo_excel.parse('Sheet1', skiprows=3)
                            data = df.iloc[3]
                        elif(p == 3):
                            df = archivo_excel.parse('Sheet1', skiprows=1)
                            data = df.iloc[1]
                        elif(p==5):
                            df = archivo_excel.parse('Sheet1', skiprows=2)
                            data = df.iloc[1]
                        
                        data2 = data.reset_index()

                        for item in data2.iloc[:,0]:
                            if ('Unnamed' in str(item)):
                                data = data.drop(item)
                        
                        data = data.reset_index()
                        data = data.drop(0)

                        for date in data['index']:
                            date = datetime.datetime.strptime(str(date), '%Y.%m')
                            dates_list.append(date)

                        if(p == 1):
                            values_list.extend(data[3])  
                        elif(p == 3 or p == 5):
                            values_list.extend(data[1])
                        
                        print('-------SE EXTRAJO LA INFO EXCEL ' + str(p))                    
                    driver.close()
                    driver.switch_to.window(driver.window_handles[-1])
                    continue
                else:
                    WebDriverWait(driver, 5)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[3]/div/div[1]/div[3]/div[4]/div/div/div[2]/p/a')))\
                            .click() 

                    if('2018' in element[0]):
                        driver.switch_to.window(driver.window_handles[-1])
                
                    dates = driver.find_elements(By.XPATH, '/html/body/div[1]/table/tbody/tr[3]/td')
                    values = driver.find_elements(By.XPATH, '/html/body/div[1]/table/tbody/tr[6]/td')   
            
                index_to_delete = list(range(0, 24, 2))

                values.pop(-1)
                dates.pop(0)

                for idx in sorted(index_to_delete, reverse = True):
                    del values[idx]

                values_text = []
                for value in values:
                    value = value.text
                    if(value == ''):
                        value = np.NaN
                    values_text.append(value)

                dates_text = []
                for date in dates:
                    date = date.text
                    date = datetime.datetime.strptime(date, '%Y.%m')
                    dates_text.append(date)           


                dates_list.extend(dates_text)
                values_list.extend(values_text)

                driver.close()

                if('2018' in element[0]):
                    driver.switch_to.window(driver.window_handles[-1])
                    driver.close()

                print('------------SE EXTRAJO-----'+ element[0])

            elif('Exchange Reserves' in element[0]):

                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.XPATH, 
                    '/html/body/div[3]/div/div[2]/div[3]/div[2]/ul/li[15]/dt/a')))\
                        .click() 

                time.sleep(5)
                
                driver.switch_to.window(driver.window_handles[-1])

                excel_url = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[3]/div[4]/p[4]/a').get_attribute('href')
                archivo_excel = pd.ExcelFile(excel_url)
                df = archivo_excel.parse('sheet1', skiprows=4)

                for date in df['Date']:
                    date = datetime.datetime.strptime(str(date), '%B %Y')
                    dates_list.append(date)

                values_list.extend(df['Amount'])

                driver.close()

                print('----------------------SE EXTRAJO LA INFO ANTES DEL 2015-----------')
            
            driver.switch_to.window(driver.window_handles[-1])
            i += 1
        
        values_float = []
        for value in values_list:
            if (value != np.NaN):
                value = float(value)
            values_float.append(value)

        data_reservas = {'Fecha': dates_list,
        'Reservas Internacionales': values_float}

        df_reservas = pd.DataFrame(data_reservas, columns=['Fecha', 'Reservas Internacionales'])

        print('--------------------SE EXTRAJO RESERVAS--------------')

        df_reservas = self.dataCleaning_EU(df_reservas)
        df_reservas = self.monthly_prep(df_reservas)
        columns_names = list(df_reservas.columns.values)
        df_reservas = self.tasaCrecimiento(df_reservas, columns_names)
        df_reservas = self.episodios_estilo(df_reservas)
        self.write_to_path(df_reservas, 'CN')

    def ex_cn_tipo_de_cambio(self, driver):
        # Inicializar el navegador
        driver.get('https://fred.stlouisfed.org/series/EXCHUS')

        WebDriverWait(driver, 60)\
        .until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="input-cosd"]')))\
            .click()

        time.sleep(5)
        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="input-cosd"]')))\
                .send_keys(Keys.CONTROL, 'a')    

        time.sleep(5)
        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="input-cosd"]')))\
                .send_keys(Keys.BACKSPACE)
        
        time.sleep(5)
        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="input-cosd"]')))\
                .send_keys('2000-01-01') 

        WebDriverWait(driver, 60)\
        .until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="download-button"]')))\
            .click()

        WebDriverWait(driver, 60)\
        .until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="download-data"]')))\
            .click()

        time.sleep(5)
        patron = '/EXCHUS*' 
        nombre = self.getDownLoadedFileName(patron)
        excel_path = nombre.replace('\\','/')

        try:
            now = time.time()
            timelapse = 0
            espera = 5 
            #Espera 5 segundos hasta que el archivo este por seguridad
            while timelapse < espera:
                try:
                    archivo_excel = pd.ExcelFile(excel_path)
                    break
                except:
                    pass
                timelapse = time.time() - now 
        except:
            print('ERROR AL EXTRAER TIPO DE CAMBIO')
            archivos = os.listdir('.')

            for archivo in archivos:
                if('EXCHUS' in archivo):
                    excel_path = archivo
            
        archivo_excel = pd.ExcelFile(excel_path)
        df_cambio = archivo_excel.parse('FRED Graph', skiprows=10)

        df_cambio.rename(columns={'observation_date':'Fecha',
                            'EXCHUS':'Tipo de Cambio'},
                inplace=True)

        print('--------------SE EXTRAJO TIPO DE CAMBIO-----------------')

        df_cambio = self.dataCleaning_EU(df_cambio)
        df_cambio = self.monthly_prep(df_cambio)
        df_cambio = self.episodios_estilo(df_cambio)
        self.write_to_path(df_cambio, 'CN')

    def ex_cn_exportaciones(self,driver):
        # Inicializar el navegador
        driver.get('https://www.safe.gov.cn/en/2019/0926/1568.html')

        excel_url = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[3]/div[4]/p/a').get_attribute('href')

        archivo_excel = pd.ExcelFile(excel_url)
        df_trade_Goods = archivo_excel.parse('In USD', skiprows=3)

        df_export = df_trade_Goods.iloc[1]

        df_export = df_export.reset_index()

        df_export = df_export.drop(0)

        df_export.rename(columns={'index':'Fecha',
                            1 :'Exportaciones'},
                inplace=True)

        wrong_dates = df_export.index[df_export['Fecha'].str.contains('Jan-Feb', na=False)].tolist()
        print(wrong_dates)

        for index in wrong_dates:
            index = index-1
            split_date = df_export.Fecha.iloc[index].split(' ')
            date_string = df_export.Fecha.iloc[index] = split_date[1] + '-02'
            df_export.Fecha.iloc[index]= datetime.datetime.strptime(str(date_string), '%Y-%m')
            value = df_export.Exportaciones.iloc[index]/2
            df_export.Exportaciones.iloc[index] = value
            df_export.Exportaciones.iloc[index-1] = value

        print('-------------------------SE EXTRAJO EXPORTACIONES---------------------')
        df_export = self.dataCleaning_EU(df_export)
        df_export = self.monthly_prep(df_export)
        df_export = self.episodios_estilo(df_export)
        self.write_to_path(df_export, 'CN')

    def ex_cn_liquidez_solvencia(self,driver):
        # Inicializar el navegador
        driver.get('http://www.pbc.gov.cn/en/3688247/3688975/index.html')
        
        data = driver.find_elements(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div[2]/div[2]/div/ul/li')

        df_liquidezSolvencia = pd.DataFrame()

        i = 1

        for element in data:

            year = driver.find_element(By.XPATH ,'/html/body/div[6]/div[2]/div[2]/div[2]/div[2]/div/ul/li['+ str(i) +']/a').text            

            # Click en el año
            WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[6]/div[2]/div[2]/div[2]/div[2]/div/ul/li['+ str(i) +']/a')))\
                .click()

            year = int(year)

            if(year > 2018):
                # Click en Assets and Liabilities...
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[3]/div/div/a')))\
                    .click()

                quarterly = driver.find_elements(By.XPATH ,'/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td')
                quarterly.pop(0)

                j = 2

                for q in quarterly:

                    quarter = driver.find_element(By.XPATH ,'/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td['+ str(j) +']/a').text
                    
                    if(not(driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td['+ str(j) +']/a').get_attribute('href'))):
                        j += 1
                        continue
                    else:

                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td['+ str(j) +']/a')))\
                            .click()        

                        driver.switch_to.window(driver.window_handles[-1])
                        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/table/tbody/tr[11]/td[6]')))
                        assets = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[11]/td[6]').text)
                        liabilities = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[15]/td[6]').text)
                        equities = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[19]/td[6]').text)

                        new_line = {'Año': str(year),'Trimestre': quarter,'Assets': assets, 'Liabilities': liabilities, 'Equities': equities}

                        df_liquidezSolvencia = df_liquidezSolvencia.append(new_line, ignore_index= True)

                        driver.close()

                        driver.switch_to.window(driver.window_handles[-1])

                        j += 1
                                
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[1]/div/div[2]/div/div/ul/li[1]/a')))\
                    .click()

                i += 1

            elif(year > 2016 and year <= 2018):
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[5]/div/div/a')))\
                    .click()
                
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table[2]/tbody/tr/td[2]/a')))\
                    .click()

                driver.switch_to.window(driver.window_handles[-1])

                WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[13]/td[9]'))) #Espera
                assets_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[13]/td[9]').text)
                assets_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[13]/td[10]').text)
                liabilities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[18]/td[9]').text)
                liabilities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[18]/td[10]').text)
                equities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[23]/td[8]').text)
                equities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[23]/td[9]').text)

                assets =  assets_uses + assets_sources
                liabilities = liabilities_uses + liabilities_sources
                equities = equities_uses + equities_sources

                assets_q = assets/4
                liabilities_q = liabilities/4
                equities_q = equities/4

                quarter = range(1,4)

                for q in quarter:
                    new_line = {'Año': str(year),'Trimestre': 'Q'+str(q),'Assets': assets_q, 'Liabilities': liabilities_q, 'Equities': equities_q}
                    df_liquidezSolvencia = df_liquidezSolvencia.append(new_line, ignore_index= True)

                print('-------------------DATA FRAME DESDE 2017----------------')

                driver.close()
                driver.switch_to.window(driver.window_handles[-1])

                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[1]/div/div[2]/div/div/ul/li[1]/a')))\
                    .click()

                i += 1

            else:

                if(year < 2008):
                    if(year == 2007):
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table[21]/tbody/tr/td[2]/a')))\
                            .click()
                    else:
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table[16]/tbody/tr/td[2]/a')))\
                            .click()
                else:
                    if(year < 2012 and year >2007):
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[4]/div/div/a')))\
                            .click()                
                    else:
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[5]/div/div/a')))\
                            .click()  
                            
                    WebDriverWait(driver, 60)\
                    .until(EC.element_to_be_clickable((By.XPATH, 
                    '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table/tbody/tr/td[2]/a')))\
                        .click()    

                driver.switch_to.window(driver.window_handles[-1])              
                
                time.sleep(5)
                WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/table/tbody/tr[14]/td[9]')))
                assets_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[14]/td[9]').text)
                assets_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[14]/td[10]').text)
                liabilities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[21]/td[9]').text)
                liabilities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[21]/td[10]').text)
                equities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[28]/td[9]').text)
                equities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[28]/td[10]').text)

                assets =  assets_uses + assets_sources
                liabilities = liabilities_uses + liabilities_sources
                equities = equities_uses + equities_sources

                assets_q = assets/4
                liabilities_q = liabilities/4
                equities_q = equities/4

                quarter = range(1,5)

                for q in quarter:
                    new_line = {'Año': str(year),'Trimestre': 'Q'+str(q),'Assets': assets_q, 'Liabilities': liabilities_q, 'Equities': equities_q}
                    df_liquidezSolvencia = df_liquidezSolvencia.append(new_line, ignore_index= True)

                print('----------------SE EXTRAJO ANTES DE 2017----------------')

                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(10) #Espera por ssegeuridad
                driver.find_element(By.TAG_NAME ,'body').send_keys(Keys.CONTROL + Keys.HOME)

                if(year != 2006):
                    time.sleep(5)
                    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/ul/li[1]/a'))).click()

                i += 1
            
        df_liquidez = pd.DataFrame()
        df_liquidez['Fecha'] = df_liquidezSolvencia['Año'] + '-' + df_liquidezSolvencia['Trimestre']
        df_liquidez['Liquidez'] = df_liquidezSolvencia['Liabilities']/df_liquidezSolvencia['Assets'] 
        
        df_solvencia =pd.DataFrame()
        df_solvencia['Fecha'] = df_liquidezSolvencia['Año'] + '-' + df_liquidezSolvencia['Trimestre']
        df_solvencia['Solvencia'] = df_liquidezSolvencia['Equities']/df_liquidezSolvencia['Assets']        
        
        df_liquidez = self.trim_q_prep(df_liquidez)
        df_solvencia = self.trim_q_prep(df_solvencia)
        df_liquidez = self.episodios_estilo(df_liquidez)
        df_solvencia = self.episodios_estilo(df_solvencia)

        time.sleep(2)
        self.write_to_path(df_liquidez, 'CN')    
        time.sleep(2)   
        self.write_to_path(df_solvencia, 'CN') 
        
    def ex_cn_liquidez(self, driver):
        # Inicializar el navegador
        driver.get('http://www.pbc.gov.cn/en/3688247/3688975/index.html')
        
        data = driver.find_elements(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div[2]/div[2]/div/ul/li')

        df_liquidezSolvencia = pd.DataFrame()

        i = 1

        for element in data:

            year = driver.find_element(By.XPATH ,'/html/body/div[6]/div[2]/div[2]/div[2]/div[2]/div/ul/li['+ str(i) +']/a').text            

            # Click en el año
            WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[6]/div[2]/div[2]/div[2]/div[2]/div/ul/li['+ str(i) +']/a')))\
                .click()

            year = int(year)

            if(year > 2018):
                # Click en Assets and Liabilities...
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[3]/div/div/a')))\
                    .click()

                quarterly = driver.find_elements(By.XPATH ,'/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td')
                quarterly.pop(0)

                j = 2

                for q in quarterly:

                    quarter = driver.find_element(By.XPATH ,'/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td['+ str(j) +']/a').text
                    
                    if(not(driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td['+ str(j) +']/a').get_attribute('href'))):
                        j += 1
                        continue
                    else:

                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td['+ str(j) +']/a')))\
                            .click()        

                        driver.switch_to.window(driver.window_handles[-1])
                        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/table/tbody/tr[11]/td[6]')))
                        assets = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[11]/td[6]').text)
                        liabilities = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[15]/td[6]').text)
                        equities = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[19]/td[6]').text)

                        new_line = {'Año': str(year),'Trimestre': quarter,'Assets': assets, 'Liabilities': liabilities, 'Equities': equities}

                        df_liquidezSolvencia = df_liquidezSolvencia.append(new_line, ignore_index= True)

                        driver.close()

                        driver.switch_to.window(driver.window_handles[-1])

                        j += 1
                                
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[1]/div/div[2]/div/div/ul/li[1]/a')))\
                    .click()

                i += 1

            elif(year > 2016 and year <= 2018):
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[5]/div/div/a')))\
                    .click()
                
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table[2]/tbody/tr/td[2]/a')))\
                    .click()

                driver.switch_to.window(driver.window_handles[-1])

                WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[13]/td[9]'))) #Espera
                assets_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[13]/td[9]').text)
                assets_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[13]/td[10]').text)
                liabilities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[18]/td[9]').text)
                liabilities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[18]/td[10]').text)
                equities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[23]/td[8]').text)
                equities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[23]/td[9]').text)

                assets =  assets_uses + assets_sources
                liabilities = liabilities_uses + liabilities_sources
                equities = equities_uses + equities_sources

                assets_q = assets/4
                liabilities_q = liabilities/4
                equities_q = equities/4

                quarter = range(1,4)

                for q in quarter:
                    new_line = {'Año': str(year),'Trimestre': 'Q'+str(q),'Assets': assets_q, 'Liabilities': liabilities_q, 'Equities': equities_q}
                    df_liquidezSolvencia = df_liquidezSolvencia.append(new_line, ignore_index= True)

                print('-------------------DATA FRAME DESDE 2017----------------')

                driver.close()
                driver.switch_to.window(driver.window_handles[-1])

                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[1]/div/div[2]/div/div/ul/li[1]/a')))\
                    .click()

                i += 1

            else:

                if(year < 2008):
                    if(year == 2007):
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table[21]/tbody/tr/td[2]/a')))\
                            .click()
                    else:
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table[16]/tbody/tr/td[2]/a')))\
                            .click()
                else:
                    if(year < 2012 and year >2007):
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[4]/div/div/a')))\
                            .click()                
                    else:
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[5]/div/div/a')))\
                            .click()  
                            
                    WebDriverWait(driver, 60)\
                    .until(EC.element_to_be_clickable((By.XPATH, 
                    '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table/tbody/tr/td[2]/a')))\
                        .click()    

                driver.switch_to.window(driver.window_handles[-1])              
                
                WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/table/tbody/tr[14]/td[9]')))
                assets_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[14]/td[9]').text)
                assets_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[14]/td[10]').text)
                liabilities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[21]/td[9]').text)
                liabilities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[21]/td[10]').text)
                equities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[28]/td[9]').text)
                equities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[28]/td[10]').text)

                assets =  assets_uses + assets_sources
                liabilities = liabilities_uses + liabilities_sources
                equities = equities_uses + equities_sources

                assets_q = assets/4
                liabilities_q = liabilities/4
                equities_q = equities/4

                quarter = range(1,5)

                for q in quarter:
                    new_line = {'Año': str(year),'Trimestre': 'Q'+str(q),'Assets': assets_q, 'Liabilities': liabilities_q, 'Equities': equities_q}
                    df_liquidezSolvencia = df_liquidezSolvencia.append(new_line, ignore_index= True)

                print('----------------SE EXTRAJO ANTES DE 2017----------------')

                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(10) #Espera por ssegeuridad
                driver.find_element(By.TAG_NAME ,'body').send_keys(Keys.CONTROL + Keys.HOME)

                if(year != 2006):

                    WebDriverWait(driver, 60)\
                    .until(EC.element_to_be_clickable((By.XPATH, 
                    '/html/body/div[6]/div[1]/div/div[2]/div/div/ul/li[1]/a')))\
                        .click()

                i += 1
            
        df_liquidez = pd.DataFrame()
        df_liquidez['Fecha'] = df_liquidezSolvencia['Año'] + '-' + df_liquidezSolvencia['Trimestre']
        df_liquidez['Liquidez'] = df_liquidezSolvencia['Liabilities']/df_liquidezSolvencia['Assets'] 
        
        #df_solvencia =pd.DataFrame()
        #df_solvencia['Fecha'] = df_liquidezSolvencia['Año'] + '-' + df_liquidezSolvencia['Trimestre']
        #df_solvencia['Solvencia'] = df_liquidezSolvencia['Equities']/df_liquidezSolvencia['Assets']        
        

        print('------------SE EXTRAJO LIQUIDEZ ---------------')

        df_liquidez = self.trim_q_prep(df_liquidez)
        #df_solvencia = self.trim_q_prep(df_solvencia)
        #df_liquidez = self.dataCleaning_EU(df_liquidez)
        #df_solvencia = self.dataCleaning_EU(df_solvencia)
        df_liquidez = self.episodios_estilo(df_liquidez)
        #df_solvencia = self.episode_count(df_solvencia)

        self.write_to_path(df_liquidez, 'CN')       
        #self.write_to_path(df_solvencia, 'CN') 

    def ex_cn_solvencia(self, driver):
        # Inicializar el navegador
        driver.get('http://www.pbc.gov.cn/en/3688247/3688975/index.html')
        
        data = driver.find_elements(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div[2]/div[2]/div/ul/li')

        df_liquidezSolvencia = pd.DataFrame()

        i = 1

        for element in data:

            year = driver.find_element(By.XPATH ,'/html/body/div[6]/div[2]/div[2]/div[2]/div[2]/div/ul/li['+ str(i) +']/a').text            

            # Click en el año
            WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '/html/body/div[6]/div[2]/div[2]/div[2]/div[2]/div/ul/li['+ str(i) +']/a')))\
                .click()

            year = int(year)

            if(year > 2018):
                # Click en Assets and Liabilities...
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[3]/div/div/a')))\
                    .click()

                quarterly = driver.find_elements(By.XPATH ,'/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td')
                quarterly.pop(0)

                j = 2

                for q in quarterly:

                    quarter = driver.find_element(By.XPATH ,'/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td['+ str(j) +']/a').text
                    
                    if(not(driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td['+ str(j) +']/a').get_attribute('href'))):
                        j += 1
                        continue
                    else:

                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/table/tbody/tr/td['+ str(j) +']/a')))\
                            .click()        

                        driver.switch_to.window(driver.window_handles[-1])
                        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/table/tbody/tr[11]/td[6]')))
                        assets = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[11]/td[6]').text)
                        liabilities = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[15]/td[6]').text)
                        equities = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[19]/td[6]').text)

                        new_line = {'Año': str(year),'Trimestre': quarter,'Assets': assets, 'Liabilities': liabilities, 'Equities': equities}

                        df_liquidezSolvencia = df_liquidezSolvencia.append(new_line, ignore_index= True)

                        driver.close()

                        driver.switch_to.window(driver.window_handles[-1])

                        j += 1
                                
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[1]/div/div[2]/div/div/ul/li[1]/a')))\
                    .click()

                i += 1

            elif(year > 2016 and year <= 2018):
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[5]/div/div/a')))\
                    .click()
                
                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table[2]/tbody/tr/td[2]/a')))\
                    .click()

                driver.switch_to.window(driver.window_handles[-1])

                WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[13]/td[9]'))) #Espera
                assets_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[13]/td[9]').text)
                assets_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[13]/td[10]').text)
                liabilities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[18]/td[9]').text)
                liabilities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[18]/td[10]').text)
                equities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[23]/td[8]').text)
                equities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/table/tbody/tr[23]/td[9]').text)

                assets =  assets_uses + assets_sources
                liabilities = liabilities_uses + liabilities_sources
                equities = equities_uses + equities_sources

                assets_q = assets/4
                liabilities_q = liabilities/4
                equities_q = equities/4

                quarter = range(1,4)

                for q in quarter:
                    new_line = {'Año': str(year),'Trimestre': 'Q'+str(q),'Assets': assets_q, 'Liabilities': liabilities_q, 'Equities': equities_q}
                    df_liquidezSolvencia = df_liquidezSolvencia.append(new_line, ignore_index= True)

                print('-------------------DATA FRAME DESDE 2017----------------')

                driver.close()
                driver.switch_to.window(driver.window_handles[-1])

                WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, 
                '/html/body/div[6]/div[1]/div/div[2]/div/div/ul/li[1]/a')))\
                    .click()

                i += 1

            else:

                if(year < 2008):
                    if(year == 2007):
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table[21]/tbody/tr/td[2]/a')))\
                            .click()
                    else:
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table[16]/tbody/tr/td[2]/a')))\
                            .click()
                else:
                    if(year < 2012 and year >2007):
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[4]/div/div/a')))\
                            .click()                
                    else:
                        WebDriverWait(driver, 60)\
                        .until(EC.element_to_be_clickable((By.XPATH, 
                        '/html/body/div[6]/div[2]/div[2]/div/div[2]/div/ul/li[5]/div/div/a')))\
                            .click()  
                            
                    WebDriverWait(driver, 60)\
                    .until(EC.element_to_be_clickable((By.XPATH, 
                    '/html/body/div[6]/div[2]/div[2]/div/div[2]/ul/table/tbody/tr/td[2]/a')))\
                        .click()    

                driver.switch_to.window(driver.window_handles[-1])              
                
                WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/table/tbody/tr[14]/td[9]')))
                assets_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[14]/td[9]').text)
                assets_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[14]/td[10]').text)
                liabilities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[21]/td[9]').text)
                liabilities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[21]/td[10]').text)
                equities_uses = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[28]/td[9]').text)
                equities_sources = self.isEmpty(driver.find_element(By.XPATH ,'/html/body/div[1]/table/tbody/tr[28]/td[10]').text)

                assets =  assets_uses + assets_sources
                liabilities = liabilities_uses + liabilities_sources
                equities = equities_uses + equities_sources

                assets_q = assets/4
                liabilities_q = liabilities/4
                equities_q = equities/4

                quarter = range(1,5)

                for q in quarter:
                    new_line = {'Año': str(year),'Trimestre': 'Q'+str(q),'Assets': assets_q, 'Liabilities': liabilities_q, 'Equities': equities_q}
                    df_liquidezSolvencia = df_liquidezSolvencia.append(new_line, ignore_index= True)

                print('----------------SE EXTRAJO ANTES DE 2017----------------')

                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(10) #Espera por ssegeuridad
                driver.find_element(By.TAG_NAME ,'body').send_keys(Keys.CONTROL + Keys.HOME)

                if(year != 2006):

                    WebDriverWait(driver, 60)\
                    .until(EC.element_to_be_clickable((By.XPATH, 
                    '/html/body/div[6]/div[1]/div/div[2]/div/div/ul/li[1]/a')))\
                        .click()

                i += 1
            
        #df_liquidez = pd.DataFrame()
        #df_liquidez['Fecha'] = df_liquidezSolvencia['Año'] + '-' + df_liquidezSolvencia['Trimestre']
        #df_liquidez['Liquidez'] = df_liquidezSolvencia['Liabilities']/df_liquidezSolvencia['Assets'] 
        
        df_solvencia =pd.DataFrame()
        df_solvencia['Fecha'] = df_liquidezSolvencia['Año'] + '-' + df_liquidezSolvencia['Trimestre']
        df_solvencia['Solvencia'] = df_liquidezSolvencia['Equities']/df_liquidezSolvencia['Assets']        
        

        print('------------SE EXTRAJO LIQUIDEZ ---------------')

        #df_liquidez = self.trim_q_prep(df_liquidez)
        df_solvencia = self.trim_q_prep(df_solvencia)
        #df_liquidez = self.dataCleaning_EU(df_liquidez)
        #df_solvencia = self.dataCleaning_EU(df_solvencia)
        #df_liquidez = self.episodios_estilo(df_liquidez)
        df_solvencia = self.episodios_estilo(df_solvencia)

        #self.write_to_path(df_liquidez, 'CN')       
        self.write_to_path(df_solvencia, 'CN') 
    

    def ex_cn_portafolio(self, driver):
        # Inicializar el navegador
        driver.get('https://www.safe.gov.cn/en/2019/0329/1496.html')

        excel_url = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[3]/div[4]/p/a').get_attribute('href')

        archivo_excel = pd.ExcelFile(excel_url)
        df_payments = archivo_excel.parse('quarterly(USD)', skiprows=3)

        df_portfolio = df_payments.iloc[99]

        df_portfolio = df_portfolio.reset_index()

        df_portfolio = df_portfolio.drop(0)

        df_portfolio.rename(columns={'index':'Fecha',
                        99 :'Inversión de Portafolio'},
                inplace=True)

        print('-------------------------SE EXTRAJO PORTAFOLIO--------------------')

        #df_portfolio = self.dataCleaning_EU(df_portfolio)
        df_portfolio = self.trim_q_prep(df_portfolio)
        columns_names = list(df_portfolio.columns.values)
        df_portfolio = self.tasaCrecimiento(df_portfolio, columns_names)
        df_portfolio = self.episodios_estilo(df_portfolio)
        self.write_to_path(df_portfolio, 'CN')


    def ex_cn_deuda(self, driver):
        # Inicializar el navegador
        driver.get('https://www.safe.gov.cn/en/2018/0329/1412.html')
        driver.maximize_window()
        time.sleep(15)
        excel_url = WebDriverWait(driver, 15)\
        .until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="content"]/p[1]/span/a')))\
            .get_attribute('href')
        archivo_excel = pd.ExcelFile(excel_url)
        df_external_debt = archivo_excel.parse('Sheet1', skiprows=1)
        df_debt = df_external_debt.iloc[58]
        df_debt = df_debt.reset_index()
        df_debt.drop([0,1], inplace = True)
        df_debt.rename(columns={'index':'Fecha',
                            58 :'Deuda Externa'},
                inplace=True)

        print('-------------------------SE EXTRAJO DEUDA EXTERNA--------------------')
        #df_debt = self.dataCleaning_EU(df_debt)   
        df_debt = self.trim_q_prep(df_debt)
        df_debt = self.episodios_estilo(df_debt)
        self.write_to_path(df_debt, 'CN')
        
    def ex_cn_pbi(self, driver):    # Inicializar el navegador
        driver.get('https://fred.stlouisfed.org/series/CHNGDPNQDSMEI')

        WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="input-cosd"]')))\
            .click()

        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="input-cosd"]')))\
                .send_keys(Keys.CONTROL, 'a')    

        time.sleep(5)
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="input-cosd"]')))\
                .send_keys(Keys.BACKSPACE)
        
        time.sleep(5)
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="input-cosd"]')))\
                .send_keys('2000-01-01') 

        WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="download-button"]')))\
            .click()

        WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="download-data"]')))\
            .click()

        time.sleep(5)
        patron = '/CHNGD*.xls' #FALTA CORREGIR EL PATRON
        nombre = self.getDownLoadedFileName(patron)
        excel_path = nombre.replace('\\','/')
        
        try:
            now = time.time()
            timelapse = 0
            espera = 5 
            #Espera 5 segundos hasta que el archivo este por seguridad
            while timelapse < espera:
                try:
                    archivo_excel = pd.ExcelFile(excel_path)
                    break
                except:
                    pass
                timelapse = time.time() - now 
        except:
            print('ERROR AL EXTRAER PIB')
            archivos = os.listdir('.')

            for archivo in archivos:
                if('CHNGDP' in archivo):
                    excel_path = archivo
                    break

        
        archivo_excel = pd.ExcelFile(excel_path)
        df_pib = archivo_excel.parse('FRED Graph', skiprows=10)

        df_pib.rename(columns={'observation_date':'Fecha',
                            'CHNGDPNQDSMEI':'PIB'},
                inplace=True)

        print('--------------SE EXTRAJO PIB-----------------')   

        df_pib = self.dataCleaning_EU(df_pib)
        df_pib = self.trim_num_prep(df_pib)
        columns_names = list(df_pib.columns.values)
        df_pib = self.tasaCrecimiento(df_pib, columns_names)
        print('--------------------')
        df_pib = self.episodios_estilo(df_pib)
        self.write_to_path(df_pib, 'CN')
            
    def ex_cn_inflacion(self, driver):
        # Inicializar el navegador
        driver.get('https://fred.stlouisfed.org/series/CHNCPIALLQINMEI')

        WebDriverWait(driver, 60)\
        .until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="input-cosd"]')))\
            .click()

        time.sleep(5)
        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="input-cosd"]')))\
                .send_keys(Keys.CONTROL, 'a')    

        time.sleep(5)
        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="input-cosd"]')))\
                .send_keys(Keys.BACKSPACE)
        
        time.sleep(5)
        WebDriverWait(driver, 60)\
            .until(EC.element_to_be_clickable((By.XPATH, 
            '//*[@id="input-cosd"]')))\
                .send_keys('2000-01-01') 

        WebDriverWait(driver, 60)\
        .until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="download-button"]')))\
            .click()

        WebDriverWait(driver, 60)\
        .until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="download-data"]')))\
            .click()
        
        time.sleep(5)
        patron = '/CHNCPI*.xls' #FALTA CORREGIR EL PATRON
        nombre = self.getDownLoadedFileName(patron)
        excel_path = nombre.replace('\\','/')

        try: 
            now = time.time()
            timelapse = 0
            espera = 5 
            #Espera 5 segundos hasta que el archivo este por seguridad
            while timelapse < espera:
                try:
                    archivo_excel = pd.ExcelFile(excel_path)
                    break
                except:
                    pass
                timelapse = time.time() - now 

        except:
            print('ERROR AL EXTRAER INFLACION')
            archivos = os.listdir('.')

            for archivo in archivos:
                if('CHNCPI' in archivo):
                    excel_path = archivo

        archivo_excel = pd.ExcelFile(excel_path)

        df_inflacion = archivo_excel.parse('FRED Graph', skiprows=10)

        df_inflacion.rename(columns={'observation_date':'Fecha',
                            'CHNCPIALLQINMEI':'Inflacion'},
                inplace=True)

        driver.close()

        print('--------------SE EXTRAJO INFLACION-----------------')  

        df_inflacion = self.dataCleaning_EU(df_inflacion)  
        df_inflacion = self.trim_num_prep(df_inflacion)
        df_inflacion = self.episodios_estilo(df_inflacion)
        self.write_to_path(df_inflacion, 'CN')
            

if __name__=="__main__":
    window=GUI()
    window.mainloop()