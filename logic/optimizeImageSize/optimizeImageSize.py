from tkinter import filedialog as fd

def optimizeImageSize():
    filetypes = (
        ('text files', '*.mp4'),
        ('All files', '*.*')
    )

    path = fd.askopenfilenames(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)