import customtkinter as ctk

defualt_value_r = 2
defualt_value_p = 20
defualt_value_n = 10
defualt_value_e = 1

window = ctk.CTk()
window.title(' ')
window.geometry('330x560')
ctk.set_appearance_mode("Dark")

#Button Function
def button_event():

   textbox_x.delete("0.0", "end")
   textbox_y.delete("0.0", "end")

   r= entry_r.get()
   p= entry_p.get()
   n=  entry_n.get()
   e=  entry_e.get()

   #Equation using Default Values
   if r=='':
      r=defualt_value_r     
   if p=='':
      p=defualt_value_p 
   if n=='':
      n=defualt_value_n
   if e=='':
      e=defualt_value_e
      
   #Parametric Equation
   textbox_x.insert("0.0", "(%s*cos(t))-(%s*cos(t+arctan(sin((1-%s)*t)/((%s/(%s*%s))-cos((1-%s)*t)))))-(%s*cos(%s*t))" % (p,r,n,p,e,n,n,e,n))
   textbox_y.insert("0.0", "(-%s*sin(t))+(%s*sin(t+arctan(sin((1-%s)*t)/((%s/(%s*%s))-cos((1-%s)*t)))))+(%s*sin(%s*t))" % (p,r,n,p,e,n,n,e,n))


window.grid_columnconfigure((0), weight=1)

#Heading
label = ctk.CTkLabel(window,text='Cycloidal Parametric Equations Generator',font=('Sans_serif',16))
label.grid(row=0, column=0, padx=15, pady=20,sticky="ew", columnspan=3)

#Setting up the button
button = ctk.CTkButton(master=window, text="Create Equation", width=150,
                                 height=32,
                                 font=('Sans_serif',14),
                                 border_width=0,
                                 corner_radius=8,
                                 command=button_event)

button.grid(row=5, column=0, padx=15, pady=5, sticky="ew", columnspan=3)

window.grid_columnconfigure((0, 1,2), weight=1)

#Roller Radius Input
label_r = ctk.CTkLabel(window,text='Roller Radius',font=('Sans_serif',14))
label_r.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew",columnspan=1)

entry_r = ctk.CTkEntry( master=window,							   
                        placeholder_text='2',
                        width=100,
                        height=30,
                        border_width=1,
                        corner_radius=10 )
entry_r.grid(row=1, column=1, padx=5, pady=(0,20),sticky="ew",columnspan=1)

label_unit_r = ctk.CTkLabel(window,text='mm',font=('Sans_serif',14))
label_unit_r.grid(row=1, column=2, padx=5, pady=(0, 20), sticky="ew")


#Pitch Circle Radius Input
label_p = ctk.CTkLabel(window,text='Pitch Circle Radius',font=('Sans_serif',14))
label_p.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew",columnspan=1)

entry_p = ctk.CTkEntry( master=window,
                        placeholder_text='20',
                        width=100,
                        height=30,
                        border_width=1,
                        corner_radius=10 )
entry_p.grid(row=2, column=1, padx=5, pady=(0,20), sticky="ew",columnspan=1)

label_unit_p = ctk.CTkLabel(window,text='mm',font=('Sans_serif',14))
label_unit_p.grid(row=2, column=2, padx=5, pady=(0, 20), sticky="ew")


#Number of Rollers Input
label_n = ctk.CTkLabel(window,text='Number of Rollers',font=('Sans_serif',14))
label_n.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="ew",columnspan=1)

entry_n = ctk.CTkEntry( master=window,
                        placeholder_text='10',      
                        width=100,
                        height=30,
                        border_width=1,
                        corner_radius=10 )
entry_n.grid(row=3, column=1, padx=5, pady=(0,20), sticky="ew",columnspan=1)

label_unit_n = ctk.CTkLabel(window,text='  ',font=('Sans_serif',14))
label_unit_n.grid(row=3, column=2, padx=5, pady=(0, 20), sticky="ew")


#Eccentricity Input
label_e = ctk.CTkLabel(window,text='Eccentricity',font=('Sans_serif',14))
label_e.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="ew",columnspan=1)

entry_e = ctk.CTkEntry( master=window,
                        placeholder_text='1',    
                        width=100,
                        height=30,
                        border_width=1,
                        corner_radius=10 )
  
entry_e.grid(row=4, column=1, padx=5, pady=(0,20), sticky="ew",columnspan=1)

label_unit3 = ctk.CTkLabel(window,text='mm',font=('Sans_serif',14))
label_unit3.grid(row=4, column=2, padx=5, pady=(0, 20), sticky="ew")

#Equations Output
textbox_x = ctk.CTkTextbox(master=window,
                           font=('Sans_serif',14),       
                           width=100,
                           height=60,
                           border_width=1,
                           corner_radius=10)
textbox_x.grid(row=6, column=0, padx=15, pady=(15,5), sticky="ew", columnspan=3)
textbox_x.insert("0.0", "Parametric Equation of X")

textbox_y = ctk.CTkTextbox(master=window,
                           font=('Sans_serif',14),                             
                           width=100,
                           height=60,
                           border_width=1,
                           corner_radius=10)
textbox_y.grid(row=8, column=0, padx=15, pady=(15,5), sticky="ew", columnspan=3)
textbox_y.insert("0.0", "Parametric Equation of Y")

def copy_select_x(): 
    window.clipboard_clear() 
    window.clipboard_append(textbox_x.get('1.0', ctk.END).rstrip())

def copy_select_y(): 
    window.clipboard_clear() 
    window.clipboard_append(textbox_y.get('1.0', ctk.END).rstrip())

copy_x=ctk.CTkButton(master=window,text='Copy X Equations',
                     command=lambda:copy_select_x(),
                     font=('Sans_serif',14),
                     width=150,
                     height=32,
                     border_width=0,
                     corner_radius=8,
                     )       
copy_x.grid(row=7, padx=15, pady=0, sticky="ew", columnspan=3)

copy_y=ctk.CTkButton(master=window,text='Copy Y Equations',
                     command=lambda:copy_select_y(),
                     font=('Sans_serif',14),
                     width=150,
                     height=32,
                     border_width=0,
                     corner_radius=8,
                     )       
copy_y.grid(row=9, padx=15, pady=0, sticky="ew", columnspan=3)
window.mainloop()