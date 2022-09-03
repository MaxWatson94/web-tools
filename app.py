from tkinter import *
from tkinter import ttk
from email.mime import image
from PIL import Image, ImageTk
from tkinter import messagebox
from logic.converter.imgToWebp import imgToWebP
from logic.getStatusSites.getStatus import getStatus
from logic.improveQuality.improveQuality import improveQuality
from logic.getSearchStatus.getSearchStatus import getSearchStatus
from logic.optimizeImageSize.optimizeImageSize import optimizeImageSize
from logic.optimizeVideoSize.optimizeVideoSize import optimizeVideoSize

# FINDOW SETTINGS
window = Tk()
# window.iconbitmap(r"gui/icon.ico")
window.title("Web tools")
window.geometry('1000x500')
window.resizable(False, False)
# window.wm_attributes("-transparent", True)
# window.wm_attributes("-topmost", True)

# BACKGROUND IMAGE SETTIGS
# img = Image.open('gui/bg/main-BG.jpg')
# bg = ImageTk.PhotoImage(img)
# label = Label(window, image=bg)
# label.place(x = 0, y = 0)

# FRAME SETTING
frame = Frame(
   window,
   padx = 25,
   pady = 25
)
frame.pack(expand=True)
frame.configure(bg='#070d14')

#####################################
# BLOCK WITH CONVERTER IMAGES TO WEBP
#####################################
webp_lb = Label(
   frame,
   font=("Helvetica", 22),
   fg="#FFFFFF",
   text="Images to WebP"
)
webp_lb.grid(row=0, column=0)

# open button
open_button = Button(
    frame,
    text='Choose images',
    command=imgToWebP,
    font=("Helvetica", 16),
)
open_button.grid(row=1, column=0, pady=(0,50), padx=50)


#################################
# BLOCK WITH CHECK EMLID RESURSES
#################################
checkResurses_lb = Label (
    frame,
    font=("Helvetica", 22),
    text="Check status of our sites"
)
checkResurses_lb.grid(row=0, column=1)

#button for get Status of the sites
getStatusSitesButton = Button(
    frame,
    font=("Helvetica", 16),
    text = 'Get status',
    command=getStatus
)
getStatusSitesButton.grid(row=1, column=1, pady=(0,50), padx=50)

#############################
# IMPROVE PHORO QUALITY BLOCK
#############################
improveQualityPhoto_lb = Label(
    frame,
    font=("Helvetica", 22),
    text='Improve quality photo'
)
improveQualityPhoto_lb.grid(row=0, column=2, padx=50)

# button for open photo for improve quality
improveQualityPhotoButton = Button(
    frame,
    font=("Helvetica", 16),
    text='Choose photo',
    command=improveQuality,
)
improveQualityPhotoButton.grid(row=1, column=2, pady=(0,50), padx=50)

##########################################
# CHECK VISIBILITY ON GOOGLE SEARCH ENGINE
##########################################
checkVisibilityGooelSearch_lb = Label(
    frame,
    font=("Helvetica", 22),
    text='Check visibility\nOn Google search engine'
)
checkVisibilityGooelSearch_lb.grid(row=2, column=0)

# button for get search status
getSearchStatusButton = Button(
    frame,
    font=("Helvetica", 16),
    text='Get search status',
    command=getSearchStatus
)
getSearchStatusButton.grid(row=3, column=0)

#####################
# OPTIMAZE IMAGE SIZE
#####################
optimizeImageSize_lb = Label(
    frame,
    font=("Helvetica", 22),
    text='Optimize image size'
)
optimizeImageSize_lb.grid(row=2, column=1)

# button for select images to omtimaze
optimizeImageSizeButton = Button(
    frame,
    text='Select images',
    font=("Helvetica", 16),
    command=optimizeImageSize
)
optimizeImageSizeButton.grid(row=3, column=1)

#####################
# OPTIMAZE VIDEO SIZE
#####################
optimizeVideoSize_lb = Label(
    frame,
    font=("Helvetica", 22),
    text='Optimize video size'
)
optimizeVideoSize_lb.grid(row=2, column=2)

# button for select images to omtimaze
optimizeVideoSizeButton = Button(
    frame,
    font=("Helvetica", 16),
    text='Select video file',
    command=optimizeVideoSize
)
optimizeVideoSizeButton.grid(row=3, column=2)

# EMLID STATUS
mainStatusEmlidSite_lb = Label(
    frame,
    font=("Helvetica", 12),
    text='Emlid uptime status:\n\nEmlid.COM⠀✅⠀ |⠀ Store⠀✅⠀ |⠀ Blog⠀✅⠀ |⠀ B2B Portal⠀✅⠀',
)
mainStatusEmlidSite_lb.grid(row=4, column=1, pady=(50, 0))


if __name__ == '__main__':
    # Infinity Run
    window.mainloop()