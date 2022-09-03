import errno
import os
from pathlib import Path
from PIL import Image
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
from tkinter import filedialog as fd

def imgToWebP():
    filetypes = (
        ('PNG', '*.png'),
        ('JPG', '*.jpg'),
        ('JPEG', '*.jpeg'),
        ('All files', '*.*')
    )

    paths = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    qtyPath = len(paths)

    askquestion(
        title="Start converting", 
        message="Everything is ready to start work! \nYou want to convert " + str(qtyPath) +  " images to webp format. \n\nTo begin?"
    )

    iterations = 0
    iterationsErrors = 0
    Path(os.getcwd() + '/WEBP Images/').mkdir(parents=True, exist_ok=True)
    for imgPath in paths:
        im = Image.open(imgPath).convert('RGB')
        imageName = os.path.basename(imgPath)
        try:
            im.save(os.getcwd() + '/WEBP Images/' + imageName + '.webp', 'webp')
            iterations += 1
        except:
            iterationsErrors + 1
            continue
    
    showinfo(
        title='Result',
        message="Done for " + str(iterations) +  " times!\nCompleted with " + str(iterationsErrors) + " errors!\n\nCheck in 'WEBP Images' folder"
    )

    