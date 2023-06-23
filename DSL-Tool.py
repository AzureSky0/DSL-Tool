from tkinter import*
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import numpy
from sklearn.linear_model import LinearRegression ,LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class Main:
    
    def __init__(self):
        self.start()

    
    def start(self):
        self.root = Tk()
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.s_h = int(round(screen_height,-2))
        self.s_w = int(round(screen_width,-2))
        if self.s_w>1500:
            self.s_w=1500
        if self.s_h<500:
            self.s_h=500

        self.s_h-=100

        # self.s_h,self.s_w = 700,1400 #her screen resolution

        print('system Screen resolution [w,h]: ',self.s_w,self.s_h)

        self.root.title('prototype_1')
        self.root.geometry(f"{self.s_w}x{self.s_h}")
        self.root.config(bg='lightBlue')

        self.createFrames()
        self.mainMenu()
        self.createCanvas(self.optFrame)
        self.root.update_idletasks()
        Tq.desplMessFrame(self.cFrame)
        Tq.desplOutputFrame(self.disFrame)


        self.root.mainloop()

    def createFrames(self):
        #screensize = w~1500 h~800
        # mf_w=int(self.s_w*0.98)
        self.mf_w = int(self.s_w/1.001)-28
        self.mf_h = int(self.s_h/1.2)
        self.cf_h = int(self.s_h/8)-4

        self.mFrame = Frame(master=self.root,height=self.mf_h,width=self.mf_w,bg='orange')
        self.mFrame.grid(row=0,column=0,sticky='ew',padx=15,pady=5)
        self.cFrame = Frame(master=self.root,height=self.cf_h,width=self.mf_w)
        self.cFrame.grid(row=1,column=0,sticky='ew',padx=15,pady=5)

        #Now creating 2 Frames in mframe for options and display
        self.dw = int(self.mf_w/2)-10
        self.ow = int(self.mf_w/2)-10

        print('sizeof mainFrame and subframe :',self.mf_w,self.mf_h," : ",self.dw,self.ow)
        self.optFrame = Frame(master=self.mFrame,height=self.mf_h-10,width=self.dw)
        self.optFrame.grid(row=0,column=0,padx=5,pady=5)
        self.disFrame = Frame(master=self.mFrame,height=self.mf_h-10,width=self.ow,bg='white')
        self.disFrame.grid(row=0,column=1,padx=5,pady=5)
        

    def createCanvas(self,frame):
        self.myCanvas = Canvas(frame,bg='white',height=self.mf_h-20,width=self.dw-20)
        self.myCanvas.grid(column=0,row=0,sticky=NSEW)

        self.myscrollbar = ttk.Scrollbar(frame,orient=VERTICAL, command=self.myCanvas.yview)
        self.myscrollbar.grid(column=1,row=0,sticky=NS)

        self.myCanvas.configure(yscrollcommand=self.myscrollbar.set)

        self.subframe2 = Frame(self.myCanvas)
        self.myCanvas.create_window((0,0),window=self.subframe2,anchor="nw")

        self.myCanvas.bind('<Configure>', func = lambda e: self.myCanvas.configure(scrollregion= self.myCanvas.bbox("all")))

        

    
    def mainMenu(self):
        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)
        
        #create a menu item

            #option1
        self.option1_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='Data Collection',menu=self.option1_menu)
        self.option1_menu.add_command(label='From Drive',command=self.option1_c1)
        # self.option1_menu.add_separator()
        # self.option1_menu.add_command(label='Quit',command=self.root.quit)

            #option2
        option2_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='pre-process',menu=option2_menu)
        option2_menu.add_command(label='Cleaning and preprocessing',command=self.option2_c1)
        option2_menu.add_separator()
        # option2_menu.add_command(label='op022',command=self.option1_c1)
        # option2_menu.add_separator()
        # option2_menu.add_command(label='op023',command=self.option1_c1)

        option3_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label='Supervised Learning',menu=option3_menu)
        option3_menu.add_command(label='Linear Regression',command=self.option3_c1)
        option3_menu.add_separator()
        option3_menu.add_command(label='Logestic Regression',command=self.option3_c2)
        # option3_menu.add_command(label='low-pass filters',command=self.option3_c1)
        # option3_menu.add_separator()


        # option4_menu = Menu(self.my_menu)
        # self.my_menu.add_cascade(label='Segmentation',menu=option4_menu)


        # option5_menu = Menu(self.my_menu)
        # self.my_menu.add_cascade(label='Rep & Desc',menu=option5_menu)
        
    #ckick Command
    def option1_c1(self):
        for widget in self.subframe2.winfo_children():
            widget.destroy()
        mFS.dataCollectionWigids(self.subframe2)


        # Frame2.config(height=1080,width=700,bg="lightblue")
        

    def option2_c1(self):
        for widget in self.subframe2.winfo_children():
            widget.destroy()
        mFS.preProcessingWigids(self.subframe2)
    
    def option3_c1(self):
        for widget in self.subframe2.winfo_children():
            widget.destroy()
        mFS.LinearRegWigids(self.subframe2)
    
    def option3_c2(self):
        for widget in self.subframe2.winfo_children():
            widget.destroy()
        mFS.LogesticRegWigids(self.subframe2)
    
class mFrameSetup:
    def __init__(self) -> None:
        pass
    def dataCollectionWigids(self,frame):
        uploadDataLabel = Label(frame,text='Data from Device : ')
        upload = Button(frame,text='Upload data',command=Tq.collectData,width=10,height=13)
        uploadDataLabel.grid(row=0,column=0)
        upload.grid(row=0,column=1)

    def preProcessingWigids(self,frame):

        #creating Frames
        DcheckvaluesFrame = LabelFrame(frame,text='Data checking tools')
        HMvaluesFrame = LabelFrame(frame,text='Handling missing values')
        removOtlnFrame = LabelFrame(frame,text='Removing Outliners')
        dataNormFrame = LabelFrame(frame,text='Data normalization')
        dataTransFrame = LabelFrame(frame,text='Data transformation')
        fSelectFrame = LabelFrame(frame,text='Feature selection')
        DsplitFrame = LabelFrame(frame,text='Data splitting')
        
        DcheckvaluesFrame.grid(row=0,column=0,sticky=NSEW,padx=1,pady=1)
        HMvaluesFrame.grid(row=1,column=0,sticky=NSEW,padx=1,pady=1)
        removOtlnFrame.grid(row=2,column=0,sticky=NSEW,padx=1,pady=1)
        dataNormFrame.grid(row=3,column=0,sticky=NSEW,padx=1,pady=1)
        dataTransFrame.grid(row=4,column=0,sticky=NSEW,padx=1,pady=1)
        fSelectFrame.grid(row=5,column=0,sticky=NSEW,padx=1,pady=1)
        DsplitFrame.grid(row=6,column=0,sticky=NSEW,padx=1,pady=1)

        def isNull():
            nulldatacount = dsDetails.data.isnull().sum()
            Tq.desplOutPutMessage(f'Null count :\n{nulldatacount}')
        
        def isNullTol():
            nulldatacount = dsDetails.data.isnull().sum().sum()
            Tq.desplOutPutMessage(f'Total Null count : {nulldatacount}')
        
        def RepNull():
            val = self.FvalueBox.get()
            typ = self.FvalueTypeBox.get()
            if typ == 'string / object':
                pass
            if typ == 'integer':
                val = int(val)
            if typ == 'double':
                val = float(val)
            dsDetails.data = dsDetails.data.fillna(value = val)
            nulldatacount = dsDetails.data.isnull().sum()
            Tq.desplOutPutMessage(f'Total Null count : {nulldatacount}')

      #checking
        descButton = Button(DcheckvaluesFrame,text='Describe Data',command=Tq.DescData)
        descButton.grid(row=0,column=0)
        fTypeButton = Button(DcheckvaluesFrame,text='Find Data types',command=Tq.fTypeData)
        fTypeButton.grid(row=0,column=1)

      #HMvalues
        #Finding null values
        FindNullLabel = Label(HMvaluesFrame,text='Finding Null values : ')
        isNullLabel = Label(HMvaluesFrame,text='Null count : ')
        isNullButton = Button(HMvaluesFrame,text=' =>',command=isNull)
        isNullTolLabel = Label(HMvaluesFrame,text='Total null values : ')
        isNullTolButton = Button(HMvaluesFrame,text=' =>',command=isNullTol)

        FindNullLabel.grid(row=0,column=0,columnspan=2,sticky=W)
        isNullTolLabel.grid(row=1,column=0)
        isNullTolButton.grid(row=1,column=1)
        isNullLabel.grid(row=1,column=2)
        isNullButton.grid(row=1,column=3)

        #Filling Null Values
        FillNullLabel = Label(HMvaluesFrame,text='Fill Null values : ')
        FvalueLabel = Label(HMvaluesFrame,text='value to replace with : ')
        FvalueType = Label(HMvaluesFrame,text='value Type : ')
        self.FvalueBox = Entry(HMvaluesFrame)
        self.FvalueTypeBox = ttk.Combobox(HMvaluesFrame,values=['string','integer','double'])
        repNullButton = Button(HMvaluesFrame,text=' =>',command=RepNull)

        FillNullLabel.grid(row=2,column=0,columnspan=2,sticky=W)
        FvalueLabel.grid(row=3,column=0)
        FvalueType.grid(row=3,column=1)
        self.FvalueBox.grid(row=4,column=0)
        self.FvalueTypeBox.grid(row=4,column=1)
        repNullButton.grid(row=5,column=1)







        pass

    def LinearRegWigids(self,frame):
        
        defineField = LabelFrame(frame,text='Define Data')
        targetFeatureLabel =  Label(defineField,text="Dependent variable : ")
        self.TfeatureBox = ttk.Combobox(defineField,values=dsDetails.Features)

        IndiFeatureLabel =  Label(defineField,text="independent variable : ")
        self.IndifeatureBox = ttk.Combobox(defineField,values=dsDetails.Features)

        self.TfeatureBox.grid(row=0,column=1,pady=10,padx=10)
        targetFeatureLabel.grid(row=0,column=0,pady=10,padx=10)
        self.IndifeatureBox.grid(row=1,column=1,pady=10,padx=10)
        IndiFeatureLabel.grid(row=1,column=0,pady=10,padx=10)

        defineField.grid(row=0,column=0,pady=10,padx=10)
        submitButton = Button(frame,text='Model Generate',bg='lightgreen',command=Tq.defineData)
        submitButton.grid(row=1,column=0,sticky='e')


        testField = LabelFrame(frame,text='Model Testing')
        predLabel = Label(testField,text="Predict value : ")
        self.testval = Entry(testField,width=4)

        predSubmitButton  = Button(frame,text='Predict',bg='lightgreen',command=Tq.runModel)

        self.testval.grid(row=0,column=1,pady=10,padx=10)
        predLabel.grid(row=0,column=0,pady=10,padx=10)

        testField.grid(row=2,column=0,sticky='w',pady=10,padx=10)
        predSubmitButton.grid(row=3,column=0,sticky='e')

    def LogesticRegWigids(self,frame):
        defineField = LabelFrame(frame,text='Define Data')
        targetFeatureLabel =  Label(defineField,text="Dependent variable : ")
        self.LTfeatureBox = ttk.Combobox(defineField,values=dsDetails.Features)

        IndiFeatureLabel =  Label(defineField,text="independent variable : ")
        self.LIndifeatureBox = ttk.Combobox(defineField,values=dsDetails.Features)

        self.LTfeatureBox.grid(row=0,column=1,pady=10,padx=10)
        targetFeatureLabel.grid(row=0,column=0,pady=10,padx=10)
        self.LIndifeatureBox.grid(row=1,column=1,pady=10,padx=10)
        IndiFeatureLabel.grid(row=1,column=0,pady=10,padx=10)

        defineField.grid(row=0,column=0,pady=10,padx=10)
        submitButton = Button(frame,text='Model Generate',bg='lightgreen',command=Tq.defineLData)
        submitButton.grid(row=1,column=0,sticky='e')


        testField = LabelFrame(frame,text='Model Testing')
        predLabel = Label(testField,text="Predict value : ")
        self.Ltestval = Entry(testField,width=4)

        predSubmitButton  = Button(frame,text='Predict',bg='lightgreen',command=Tq.runModelL)

        self.Ltestval.grid(row=0,column=1,pady=10,padx=10)
        predLabel.grid(row=0,column=0,pady=10,padx=10)

        testField.grid(row=2,column=0,sticky='w',pady=10,padx=10)
        predSubmitButton.grid(row=3,column=0,sticky='e')


        
        


class techniques:
    def __init__(self) -> None:
        pass
    

    def defineData(self):
            self.target = mFS.TfeatureBox.get()
            feature = mFS.IndifeatureBox.get()
            targetvalueT = dsDetails.data[self.target]
            targetvalue = targetvalueT.values.reshape(-1, 1)
            featureValueT = dsDetails.data[feature]
            self.featureValue = featureValueT.values.reshape(-1, 1)
            Tq.desplOutPutMessage(f'target value :\n{targetvalueT}\n\n{featureValueT}')
            Tq.desplMessage(f'Generating model')
            self.model = LinearRegression()
            
            X_train, X_test, y_train, y_test = train_test_split(targetvalue, self.featureValue, test_size=0.2, random_state=42)
            self.model.fit(X_train, y_train)

            y_pred = self.model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            inetrscept =self.model.intercept_
            cofficent =self.model.coef_
            
            Tq.desplMessage(f'Model is build\nmodel accuracy (mean squared error) : {mse}\nIntercept = {inetrscept}\nCofficent =  {cofficent}')

    def defineLData(self):
        self.Ltarget = mFS.LTfeatureBox.get()
        feature = mFS.LIndifeatureBox.get()
        targetvalueT = dsDetails.data[self.Ltarget]
        targetvalue = targetvalueT.values.reshape(-1, 1)
        featureValueT = dsDetails.data[feature]
        self.LfeatureValue = featureValueT.values.reshape(-1, 1)
        Tq.desplOutPutMessage(f'target value :\n{targetvalueT}\n\n{featureValueT}')
        Tq.desplMessage(f'Generating model')
        self.Lmodel = LogisticRegression()
        
        X_train, X_test, y_train, y_test = train_test_split(targetvalue, self.LfeatureValue, test_size=0.2, random_state=42)
        self.Lmodel.fit(X_train, y_train)

        y_pred = self.Lmodel.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        inetrscept =self.Lmodel.intercept_
        cofficent =self.Lmodel.coef_
        score = self.Lmodel.score(X_test,y_test)
        
        Tq.desplMessage(f'Model is build\nModel Score : {score}\nmodel accuracy (mean squared error) : {mse}\nIntercept = {inetrscept}\nCofficent =  {cofficent}')


    def runModel(self):
        val = mFS.testval.get()
        if val != '':
            val = numpy.array(float(val)).reshape(-1, 1)
            y_pred = Tq.model.predict(val)
            Tq.desplOutPutMessage(f'prediction\n {self.target} = {y_pred}')
        else:
            Tq.desplOutPutMessage(f'enter the value for prediction')
    
    def runModelL(self):
        val = mFS.Ltestval.get()
        if val != '':
            val = numpy.array(float(val)).reshape(-1, 1)
            y_pred = Tq.Lmodel.predict(val)
            Tq.desplOutPutMessage(f'prediction\n {self.Ltarget} = {y_pred}')
        else:
            Tq.desplOutPutMessage(f'enter the value for prediction')


    def collectData(self):
        path= filedialog.askopenfilename(title="Select an file", initialdir='\practice',filetypes=[('csv File','*.csv'),("Excel files", "*.xlsx,.xls"),('XML File','*.xml')])
        if path:
            if '.xls' in path or '.xlsx' in path:
                data = pd.read_excel(path)
            if '.csv' in path:
                data = pd.read_csv(path)
            if '.xml' in path:
                data = pd.read_xml(path)
            else:
                self.desplMessage('Data uploaded Successfully !\npath : '+path)
            shape = data.shape
            Features = []
            for Feature in data.columns:
                Features.append(Feature)
            dsDetails.data = data
            dsDetails.Features = Features
            self.desplMessage(f'Data uploaded Successfully !\npath : {path}')
            self.desplOutPutMessage(f'Size : {shape}\n\ninfo:\n{dsDetails.data}')
   
        else:
            self.desplMessage('Data uploaded unsuccessfull')

    def DescData(self):
            data = pd.DataFrame(dsDetails.data)
            dataDesc = data.describe()
            self.desplOutPutMessage(f'Describe :\n{dataDesc}')
        
        
    def fTypeData(self):
            data = pd.DataFrame(dsDetails.data)
            dataDesc = data.dtypes
            self.desplOutPutMessage(f'Data Types :\n{dataDesc}')
            

    def desplMessFrame(self,frame):
        
        h=frame.winfo_height()
        w=frame.winfo_width()
        print(h,w)
        h,w=frame.winfo_height(),frame.winfo_width()
        self.myLabelMes = Label(frame,bg='blue')
        self.myLabelMes.grid(row=0,column=0)
        print(h,w)
        self.text0 = Text(self.myLabelMes,width=int(w*0.1235),height=int(h*0.055),wrap=NONE)
        self.text0.grid(row=0,column=0)

        self.myScrollbary = Scrollbar(self.myLabelMes,command=self.text0.yview)
        self.myScrollbary.grid(row=0,column=1,sticky=NS)

        self.myScrollbarx = Scrollbar(self.myLabelMes,command=self.text0.xview,orient='horizontal')
        self.myScrollbarx.grid(row=1,column=0,columnspan=2,sticky=EW)

        self.text0.config(yscrollcommand=self.myScrollbary.set,xscrollcommand=self.myScrollbarx.set)
        self.desplMessage('First Upload Data to create datasets')

    def desplOutputFrame(self,frame):
        #height=670,width=700
        h=frame.winfo_height()
        w=frame.winfo_width()
        print(h,w)
        self.myLabelOutPutMes = Label(frame,bg='blue')
        self.myLabelOutPutMes.grid(row=0,column=0)
        self.text1 = Text(self.myLabelOutPutMes,width=int(w*0.1215),height=int(h*0.06),wrap=NONE)
        self.text1.grid(row=0,column=0)

        self.Scrollbary = Scrollbar(self.myLabelOutPutMes,command=self.text1.yview)
        self.Scrollbary.grid(row=0,column=1,sticky=NS)

        self.Scrollbarx = Scrollbar(self.myLabelOutPutMes,command=self.text1.xview,orient='horizontal')
        self.Scrollbarx.grid(row=1,column=0,columnspan=2,sticky=EW)

        self.text1.config(yscrollcommand=self.Scrollbary.set,xscrollcommand=self.Scrollbarx.set)
        self.desplOutPutMessage('Output will display here')

    def desplMessage(self,message):
        self.text0.delete(1.0,END)
        self.text0.insert(1.0,message)

    def desplOutPutMessage(self,message):
        self.text1.delete(1.0,END)
        self.text1.insert(1.0,message)

class DataSetDetails:
    data = NONE
    Features = []
    def __init__(self) -> None:
        pass

mFS = mFrameSetup()
Tq = techniques()
dsDetails = DataSetDetails()

main = Main()
