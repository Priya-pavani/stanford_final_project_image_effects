#########################################################################################################################################################################3
###################################  This is a project on different image filters ########################################################################################
"""
                                   It uses tkinter modules,Pillow,opencv,numpy  modules
""" 

from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import cv2
import numpy as np
root = Tk()

################################################################################################################################################################
############################### This code is about opening file#################################################################################################
################################################################################################################################################################

def openfile():


    global filename
    filename = filedialog.askopenfilename( 
                                      filetypes=(("jpg file","*jpg"),
                                                 ("jpeg file","*jpeg")),title = "select an image file")
    print(filename)
    print(type(filename))
    img=Image.open(filename)
    img=img.resize((500,500))
    img=ImageTk.PhotoImage(img)
    
    global label1
    label1.forget()
    global frame1
    
    label1 = Label( frame1,image=img)
    label1.image = img
    label1.pack()
    frame1.pack(side= "left",padx=30)
    global frame2
    global label2
    label2.forget()
    label2 = Label( frame2,image=img1,)
    label2.pack()

################################################################################################################################################################################################
######################### This code is about how to save the modified/altered image  ###########################################################################################################
################################################################################################################################################################################################

def savefile():
    global filename
    
    try:

        if filename is not None:

            image = label2.image
            if image:
                image = ImageTk.getimage(image)
                image = image.convert("RGB")
                save_path = filedialog.asksaveasfile( mode ="w",filetypes=(("JPG files", "*.jpg"), ("PNG files", "*.png")))
                if save_path:
                    image.save(save_path)
    except:
        messagebox.showerror("File selection error","No file is selected to save ")





######################################################################################################################################################################################
################################ This code is about displaying black and white image ####################################################################################################
############################################################################################################################################################################################

def black_and_white():
    try:
        if filename is not None:
            i=cv2.imread(filename)
            i=cv2.resize(i,(500,500))
            i=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
            #cv2.waitkey(0)
            #blue,green,red = cv2.split(i)
            #new = cv2.merge((red,green,blue))
            im=Image.fromarray(i)
            im=ImageTk.PhotoImage(im)
            global frame2
            global label2
            label2.forget()
            label2 = Label(frame2,image=im)
            label2.image=im
            label2.pack()
    except :
        messagebox.showerror("Selection error","First select the file ")


###########################################################################################################################################################
############################ This code is about creating a sketch effect on the given photo ###############################################################
###########################################################################################################################################################

def sketch():
    global filename
    
    try:
        if filename is not None:
            image = cv2.imread(filename,-1)
            image=cv2.resize(image,(500,500))
            grey_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #blurred_image = cv2.GaussianBlur(grey_image, (21, 21), 0, 0)
            #edges = cv2.Canny(blurred_image, 30, 100)
            #filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            invert = cv2.bitwise_not(grey_image)
            blur = cv2.GaussianBlur(invert ,(21,21),0)
            inverted_blur=cv2.bitwise_not(blur)
            sketch = cv2.divide(grey_image, inverted_blur,scale=200.0)
            im=Image.fromarray(sketch)
            im=ImageTk.PhotoImage(im)
            global frame2
            global label2
            label2.forget()
            label2 = Label(frame2,image=im)
            label2.image=im
            label2.pack()

    except:

        messagebox.showerror("selection error","First select the file ")


##########################################################################################################################################################
#################################### This code is about creating  oil painting effect #########################################################################
##########################################################################################################################################################

def oil_painting():
    global filename
    
    try:

        if filename is not None:
            image = cv2.imread(filename,-1)
            image=cv2.resize(image,(500,500))
            # Apply oil painting filter
            oil_radius = 1  # Adjust the radius to control the effect
            oil_intensity = 5  # Adjust the intensity to control the effect
            filtered_image = cv2.xphoto.oilPainting(image, oil_radius, oil_intensity)
            #filtered_image = oil_painting.apply(image)
            '''blue,green,red = cv2.split(filtered_image)
            new = cv2.merge((red,green,blue))'''
            im=Image.fromarray(filtered_image)
            im=ImageTk.PhotoImage(im)
            global frame2
            global label2
            label2.forget()
            label2 = Label(frame2,image=im)
            label2.image=im
            label2.pack()
    except:
        messagebox.showerror("selection error","First select the file ")


################################################################################################################################################################################
#################################################### This code is to create sepia filter ############################################################################################################
################################################################################################################################################################################

def sepia_filter():
    global filename

    try:

        if filename is not None:
            image = cv2.imread(filename,-1)

            
            image = cv2.resize(image, (500, 500))
            """sepia_tone_image = np.zeros_like(image, dtype=np.float32)
            sepia_tone_image[:,:,0] = 0.189 * image[:,:,2] + 0.769 * image[:,:,1] + 0.393 * image[:,:,0]  # Blue channel
            sepia_tone_image[:,:,1] = 0.168 * image[:,:,2] + 0.686 * image[:,:,1] + 0.349 * image[:,:,0]  # Green channel
            sepia_tone_image[:,:,2] = 0.131 * image[:,:,2] + 0.534 * image[:,:,1] + 0.272 * image[:,:,0]  # Red channel

            sepia_tone_image = np.clip(sepia_tone_image, 0, 255).astype(np.uint8)"""

            # Define the sepia tone transformation matrix
            sepia_matrix = np.array([[0.189, 0.769, 0.393],
                                    [0.168, 0.686, 0.349],
                                    [0.131, 0.534, 0.272]])

            # Apply the sepia tone transformation
            sepia_tone_image = cv2.transform(image, sepia_matrix)

            """blue,green,red = cv2.split(sepia_tone_image)
            new = cv2.merge((red,green,blue))"""
            im=Image.fromarray(sepia_tone_image)
            
            im=ImageTk.PhotoImage(im)
            global frame2
            global label2
            label2.forget()
            label2 = Label(frame2,image=im)
            label2.image=im
            label2.pack()


    except:
        messagebox.showerror("selection error","First select the file ")

####################################################################################################################################################################
############################# This code is about to cartoon filter  #############################################################################
###############################################################################################################################################################################


def cartoon_filter():
    global filename
    try:

        if filename is not None:

            image = cv2.imread(filename,-1)
            resized_image=cv2.resize(image,(500,500))
            cartoon_image = cv2.stylization(resized_image, sigma_s=1, sigma_r=1)
            blue,green,red = cv2.split(cartoon_image)
            new = cv2.merge((red,green,blue))
            im=Image.fromarray(new)
            im=ImageTk.PhotoImage(im)
            global frame2
            global label2
            label2.forget()
            label2 = Label(frame2,image=im)
            label2.image=im
            label2.pack()


    except:
        messagebox.showerror("selection error","First select the file ")

##################################################################################################################################################
################################## This code is about creating vintage filter  ###################################################################
##################################################################################################################################################
 

def vintage_filter():

    global filename
    try:


        if filename is not None:

            image = cv2.imread(filename,-1)
            image = cv2.resize(image,((500,500)))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert image to RGB
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # Convert image to grayscale
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)  # Convert image back to RGB
            noise = np.zeros(image.shape, np.uint8)
            cv2.randn(noise, 50, 20)  # Adjust the parameters (mean and standard deviation) to control the amount of noise
            image = cv2.add(image, noise)
            contrast = 1.2  # Adjust the contrast value as per your preference
            brightness = 10  # Adjust the brightness value as per your preference
            image = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
            height, width = image.shape[:2]
            center = (width//2, height // 2)
            radius = width  # Adjust the radius value to control the size of the vignette
            mask = np.zeros((height, width), dtype=np.uint8)
            cv2.circle(mask, center, radius, (255, 255, 255), -1)
            image = cv2.bitwise_and(image, cv2.merge([mask, mask, mask]))
            im=Image.fromarray(image)
            im=ImageTk.PhotoImage(im)
            global frame2
            global label2
            label2.forget()
            label2 = Label(frame2,image=im)
            label2.image=im
            label2.pack()
    except:
        messagebox.showerror("selection error","First select the file ")


#####################################################################################################################################################################3
############################## This code is about brighteness filter  ################################################################################################
#######################################################################################################################################################################

def brightness():
    global filename
    try:

        if filename is not None:
                image = cv2.imread(filename,-1)
                image = cv2.resize(image,((500,500)))   
                brightness_factor = 1.5  # Adjust the factor for desired brightness
                adjusted_image = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=1)
                blue,green,red = cv2.split(adjusted_image)
                new = cv2.merge((red,green,blue)) 
                im=Image.fromarray(new)
                im=ImageTk.PhotoImage(im)
                global frame2
                global label2
                label2.forget()
                label2 = Label(frame2,image=im)
                label2.image=im
                label2.pack()
    except:
        messagebox.showerror("selection error","First select the file ")

############################################################################################################################################################
#########################   THIS CODE IS ABOUT THE INFRARED EFFECT #########################################################################################
############################################################################################################################################################

def infrared_filter():

    global filename

    try:

        if filename is not None:
                image = cv2.imread(filename,-1)
                image = cv2.resize(image,((500,500)))  
                
                # Convert the image to grayscale
                grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # Invert the grayscale image
                negative_image = cv2.bitwise_not(grayscale_image)

                # Apply color mapping to create the infrared effect
                infrared_image = cv2.applyColorMap(negative_image, cv2.COLORMAP_JET) 
                blue,green,red = cv2.split(infrared_image)
                new = cv2.merge((red,green,blue)) 
                im=Image.fromarray(new)
                im=ImageTk.PhotoImage(im)
                global frame2
                global label2
                label2.forget()
                label2 = Label(frame2,image=im)
                label2.image=im
                label2.pack()     
    except:
        messagebox.showerror("selection error","First select the file ")


##########################################################################################################################################################
######################### This cod e code is for resetting the application  ###############################################################################
###########################################################################################################################################################

def reset():
    
    global filename
    filename = None
    global frame1
    global label1
    global label2
    global frame2
    img=Image.open(r"assets\Upload-PNG-Pic.png")
    img=img.resize((550,550))
    img=ImageTk.PhotoImage(img)

    label1.forget()
    label1 = Label( frame1,image=img,)
    label1.image = img
    label1.pack()
    frame1.pack(side="left",fill = "x")

    label2.forget()
    img1=Image.open(r"assets\R.jpg")
    img1=img1.resize((500,500))
    img1=ImageTk.PhotoImage(img1)
    

    label2 = Label( frame2,image=img1,)
    label2.image = img1
    label2.pack()




##########################################################################################################################################################
############################ This code is about creating frame and buttons regarding effects #############################################################
##########################################################################################################################################################
title_frame = Frame(root)

title = Label( title_frame,text=" Different Image Filters",font=("calibri",19),background="medium violet red",padx=480)
title.pack(side="left",fill="x")
button = Button(title_frame,text = "Exit", bg="red", fg="white", font = ("calibri",15),relief="raised",command=root.quit)
button.pack(side="right",fill="x")
title_frame.config(background="medium violet red")

title_frame.pack(side="top",fill = "x")
########### BACKGROUND COLOR FOR BUTTONS IS:LightBlue1 #############################################################

global filename
root.attributes("-fullscreen",True)
frame3 = Frame(root)
select_label = Label(frame3, text = "Select one of the below effects to change image as you desired", font =("Arial",19), fg="black", bg="medium violet red")
select_label.pack(side="top",pady=5,fill ="x")

######################################################    black and white button   ############################################################################################

button1 = Button(frame3,text = "balck and white", bg="LightBlue1", fg="black", font = ("calibri",15),relief="raised",command = black_and_white)
button1.pack(side="left",fill = "x",padx=10,pady=5)

##########################################################      sketch button        ###########################################################################################

button2 = Button(frame3,text = "sketch", bg="LightBlue1", fg="black", font = ("calibri",15),relief="raised",command=sketch)
button2.pack(side="left",fill = "x", padx=10,pady=5)

############################################################   oil painting button ##############################################################################################

button3 = Button(frame3,text = " Inverted Oil Painting", bg="LightBlue1", fg="black", font = ("calibri",15),relief="raised",command=oil_painting)
button3.pack(side="left",fill = "x",pady=5)

###########################################################   cartoon filter button  ##############################################################################################

button4 = Button(frame3,text = " Cartoon Filter Painting", bg="LightBlue1", fg="black", font = ("calibri",15),relief="raised",command=cartoon_filter)
button4.pack(side="left",fill = "x",padx=10,pady=5)


###########################################################  sepia-tone filter button  ################################################################################################

button5 = Button(frame3,text = "sepia filter  ", bg="LightBlue1", fg="black", font = ("calibri",15),relief="raised",command=sepia_filter)
button5.pack(side="left",fill = "x",padx=10,pady=5)

###################################################### vintage filter button ######################################################################################################################

button6 = Button(frame3,text = "vintage filter  ", bg="LightBlue1", fg="black", font = ("calibri",15),relief="raised",command=vintage_filter)
button6.pack(side="left",fill = "x",padx=10,pady=5)

######################################################### BRIGHTNESS BUTTON #######################################################################################################################

button7 = Button(frame3,text = "brightness filter  ", bg="LightBlue1", fg="black", font = ("calibri",15),relief="raised",command=brightness)
button7.pack(side="left",fill = "x",padx=10,pady=5)


############################################### INFRARED IMAGE  #####################################################################################################################################

button8 = Button(frame3,text = "Infrared  ", bg="LightBlue1", fg="black", font = ("calibri",15),relief="raised",command=infrared_filter)
button8.pack(side="left",fill = "x",padx=10,pady=5)

frame3.config(background="medium violet red")
frame3.pack(side="bottom",fill = "x")


#####################################################################################################################################################################################################
####################################### The remaining code is all about creating and packing frames which consists of uploading an image and altered image###########################################
#####################################################################################################################################################################################################


frame = Frame(root)

open_button = Button(frame,text = "open file", bg = "white", fg = "black",font = ("calibri",14) ,command = openfile )
open_button.pack(padx=10,pady=60)
save_button = Button(frame,text = "save file", bg = "white", fg = "black",font = ("calibri",14) ,command = savefile )
save_button.pack(padx=10,pady=60) 
reset_button = Button(frame,text = "Reset", bg = "white", fg = "black",font = ("calibri",14) ,command = reset )
reset_button.pack(padx=10,pady=60)
frame.config(background="medium violet red")
frame.pack(side="left",fill = "y",padx=0)
#frame.pack()


frame1 = Frame(root)
img=Image.open(r"assets\Upload-PNG-Pic.png")
img=img.resize((550,550))
img=ImageTk.PhotoImage(img)

label1 = Label( frame1,image=img,)
label1.pack()
frame1.pack(side="left",fill = "x")


img1=Image.open(r"assets\R.jpg")
img1=img1.resize((500,500))
img1=ImageTk.PhotoImage(img1)
frame2 = Frame(root)

label2 = Label( frame2,image=img1,)
label2.pack()

frame2.pack(side="left",fill = "x")

root.mainloop()