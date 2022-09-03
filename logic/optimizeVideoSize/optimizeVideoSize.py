from tkinter import filedialog as fd

def optimizeVideoSize():
    filetypes = (
        ('text files', '*.png'),
        ('All files', '*.*')
    )

    path = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)