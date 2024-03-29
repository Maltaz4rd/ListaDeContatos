from tkinter import *

root = Tk()
azul = '#20B2AA'
silver = '#C0C0C0'

class application():
    def __init__(self):
        self.root = root
        self.window()
        self.Frames()
        self.widgetsFrame1()
        root.mainloop()

    
    def window(self):
        root.title('Agenda de contatos')
        root.configure(background=azul)
        
        width = 700
        height = 700
        maxWidth = root.winfo_screenwidth()
        maxHeight = root.winfo_screenheight()
        minWidth = 600
        minHeight = 440

        windowWidth = root.winfo_screenwidth()
        root.minsize(minWidth, minHeight)
        root.maxsize(maxWidth, maxHeight)
        center = int(windowWidth/2 - width/2)

        root.geometry(f'{width}x{height}+{center}+200')

    def Frames(self):
        self.frame_1 = Frame(root, highlightthickness=4, highlightbackground= silver)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.48)

        self.frame_2 = Frame(root, highlightthickness= 4, highlightbackground= silver)
        self.frame_2.place(relx= 0.02, rely= 0.52, relwidth= 0.96, relheight= 0.46)

    def widgetsFrame1(self):

        #-------------------- BUTTONS ---------------------------------
        yButtons = 0.07
        self.clearButton = Button(self.frame_1, text= "Clear")
        self.clearButton.place(relx= 0.15, rely= yButtons, relwidth= 0.1, relheight= 0.1)
        self.newButton = Button(self.frame_1, text= "New")
        self.newButton.place(relx= 0.27, rely= yButtons, relwidth= 0.1, relheight= 0.1)
        self.searchButton = Button(self.frame_1, text= "Search")
        self.searchButton.place(relx= 0.6, rely= yButtons, relwidth= 0.1, relheight= 0.1)
        self.updateButton = Button(self.frame_1, text= "update")
        self.updateButton.place(relx= 0.72, rely= yButtons, relwidth= 0.1, relheight= 0.1)
        self.deleteButton =Button(self.frame_1, text= "Delete")
        self.deleteButton.place(relx= 0.84, rely= yButtons, relwidth= 0.1, relheight= 0.1)

        #------------------- LABELS AND ENTRYES -------------------------
        ## CODIGO
        self.codeLabel = Label(self.frame_1, text="cod:")
        self.codeLabel.place(relx= 0.01, rely= 0.02)
        self.codeEntry = Entry(self.frame_1)
        self.codeEntry.place(relx= 0.01, rely= 0.1, relwidth= 0.1, relheight= 0.07)

        ## NOME
        self.nameLabel = Label(self.frame_1, text= "Name:")
        self.nameLabel.place(relx= 0.01, rely= 0.22)
        self.nameEntry = Entry(self.frame_1)
        self.nameEntry.place(relx= 0.01, rely= 0.31, relwidth= 0.5, relheight= 0.07)

        ## NUMERO TELEFONICO
        self.numberLabel = Label(self.frame_1, text= "Phone Number:")
        self.numberLabel.place(relx= 0.01, rely= 0.42)
        self.numberEntry = Entry(self.frame_1)
        self.numberEntry.place(relx= 0.01, rely= 0.51, relwidth= 0.4, relheight= 0.07)

        ## EMAIL
        self.emailLabel = Label(self.frame_1, text= "Email:")
        self.emailLabel.place(relx= 0.51, rely= 0.42)
        self.emailEntry = Entry(self.frame_1)
        self.emailEntry.place(relx= 0.51, rely= 0.51, relwidth= 0.4, relheight= 0.07)

        ## descrição do contato
        self.description = Label(self.frame_1, text= "Selecione a descrição do contato:")
        self.description.place(relx= 0.01, rely= 0.62)
        self.descriptionSelButton01 = Radiobutton(self.frame_1, text= "Meu contato", value= "Meu contato")
        self.descriptionSelButton01.place(relx= 0.01, rely= 0.72)
        self.descriptionSelButton01 = Radiobutton(self.frame_1, text= "Familia", value= "Familia")
        self.descriptionSelButton01.place(relx= 0.01, rely= 0.82)
        self.descriptionSelButton01 = Radiobutton(self.frame_1, text= "Amigo", value= "Amigo")
        self.descriptionSelButton01.place(relx= 0.51, rely= 0.72)
        self.descriptionSelButton01 = Radiobutton(self.frame_1, text= "Trabalho", value= "Trabalho")
        self.descriptionSelButton01.place(relx= 0.51, rely= 0.82)
    
application()