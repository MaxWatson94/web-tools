from cgitb import text
import requests
from tkinter.messagebox import showinfo
from tkinter import scrolledtext
from tkinter import messagebox
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *

def getStatus():
    # Open file with sites and write to array all sites
    with open(f'logic/getStatusSites/siteList.txt') as file:
        url = [row.strip() for row in file]
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    for check in url:
        try:
            # send requsts to site
            r = requests.get(check, headers=headers)
            # check response code from the site
            if r.status_code == 200:
                print(str(check) + '- Good')
            else:
                print(str(check) + '- bad response!!!')
        except:
            print(str(check) + '- Invalid URL or bad response!!!')
