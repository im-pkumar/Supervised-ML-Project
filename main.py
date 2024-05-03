#!/usr/bin/env python
# coding: utf-8

# In[17]:


import allin1_projects_new as all
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import messagebox,filedialog
from tkinter.ttk import Combobox
import os
user = os.environ.get('Username')
savepath = f"C:/Users/{user}/Desktop/"
color = {'main_bg':"#5F5B50",'text':"#29250D",'frame_bg':"#EAE3B9",'btn':"#FAD130"}
fontsize = {'title':32,'subhead':16,'text':12}
item_type = ['Baking Goods','Breads','Breakfast','Canned','Dairy','Frozen Foods','Fruits and Vegetables','Hard Drinks',
             'Health and Hygiene','Household','Meat','Seafood','Snack Foods','Soft Drinks','Other']
yr = list(np.arange(1950,2024))


# In[18]:


win = Tk()
win.state("zoomed")
win.resizable(False,False)
win.title("All in One ML Projects")
win.configure(bg=color['main_bg'])

title_f = Frame(win)
title_f.configure(bg=color['btn'],bd=1)
title_f.place(relx=0,rely=0,relheight=0.1,relwidth=1)

title = Label(title_f, text="All In One ML Projects",font=("monoscope",fontsize['title'],"bold"),fg=color['text'],bg=color['btn'])
title.pack(pady=10)

def bbc():
    global main_f
    main_f = Frame(win)
    main_f.configure(bg=color['frame_bg'],bd=4)
    main_f.place(relx=0.225,rely=0.12,relwidth=0.75,relheight=0.85)

    def browse():
        print("File browsing....")
        loc = filedialog.askopenfile(title="Open Documents",filetypes=[("Documents", "*.txt *.xlsx *.csv *.tsv")])
        file = loc.name
        print(file)
        loc_e.insert(0,file)
        global details,bulk_flag
        if file.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.endswith(".xlsx"):
            df = pd.read_excel(file)
        elif file.endswith(".txt"):
            df = pd.read_csv(file,delimiter="\t")
        bulk_flag = True
        print(bulk_flag)
        details = df.iloc[:,1].values

    def predict():
        all.bbcnews()
        global bulk_flag
        print(bulk_flag)
        if bulk_flag:
            global details
            p = all.pred_bbcnews(details)
            result = pd.DataFrame(p,columns=['Predicted Category'])
            result.to_csv(f"{savepath}Predicted.csv")
            bulk_flag = False
            messagebox.showinfo("Message","File Saved in Desktop!")
            cat_l = Label(main_f,text="Done! & Saved".upper(),font=("monoscope",fontsize['subhead'],"bold"),bg=color['main_bg'],fg=color['btn'],width=12)
            cat_l.place(relx=0.275,rely=0.815)
        else:
            news = news_e.get("1.0", "end-1c")
            p = all.pred_bbcnews([news])
            result_l = Label(main_f,text="Category:",font=("monoscope",fontsize['subhead'],"bold","underline"),bg=color['frame_bg'],fg=color['text'])
            result_l.place(relx=0.155,rely=0.83)
            cat_l = Label(main_f,text=p[0].upper(),font=("monoscope",fontsize['title'],"bold"),bg=color['main_bg'],fg=color['btn'],width=12)
            cat_l.place(relx=0.275,rely=0.815)

    subhead_l = Label(main_f,text="BBC News Category Prediction",font=("monoscope",fontsize['subhead'],"bold","underline"),bg=color['frame_bg'],fg=color['text'])
    subhead_l.place(relx=0.335,rely=0.01)
    news_l = Label(main_f,text="News Description",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    news_l.place(relx=0.155,rely=0.2)
    news_e = Text(main_f,font=("monoscope",fontsize['text'],"normal"),fg=color['text'],width=80,height=10)
    news_e.place(relx=0.15,rely=0.25)
    bulknews_l = Label(main_f,text="Want to get News Category in Bulk?? Click -->",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    bulknews_l.place(relx=0.155,rely=0.615)
    loc_e = Entry(main_f,font=("monoscope",fontsize['text'],"normal"),fg=color['text'],width=60)
    loc_e.place(relx=0.15,rely=0.66)
    browse_btn = Button(main_f,text="Browse",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=browse)
    browse_btn.place(relx=0.7,rely=0.645)

    pred_btn = Button(main_f,text="Predict",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=predict)
    pred_btn.place(relx=0.7,rely=0.84)


     
def imdb():
    global main_f
    main_f = Frame(win)
    main_f.configure(bg=color['frame_bg'],bd=4)
    main_f.place(relx=0.225,rely=0.12,relwidth=0.75,relheight=0.85)
    subhead_l = Label(main_f,text="IMDb Review Sentiment Prediction",font=("monoscope",fontsize['subhead'],"bold","underline"),bg=color['frame_bg'],fg=color['text'])
    subhead_l.place(relx=0.325,rely=0.01)

    def browse():
        print("File browsing....")
        loc = filedialog.askopenfile(title="Open Documents",filetypes=[("Documents", "*.txt *.xlsx *.csv *.tsv")])
        file = loc.name
        loc_e.insert(0,file)
        global details,bulk_flag
        if file.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.endswith(".xlsx"):
            df = pd.read_excel(file)
        elif file.endswith(".txt"):
            df = pd.read_csv(file,delimiter="\t")
        bulk_flag = True
        details = df.iloc[:,1].values

    def predict():
        all.imdb()
        global bulk_flag
        if bulk_flag:
            global details
            p=all.pred_imdb(details)
            result = pd.DataFrame(p,column=['Predicted Sentiment'])
            result.to_csv(f"{savepath}Predicted.csv")
            bulk_flag = False
            messagebox.info("Message","File Saved in Desktop!")
            cat_l = Label(main_f,text="Done! & Saved".upper(),font=("monoscope",fontsize['subhead'],"bold"),bg=color['main_bg'],fg=color['btn'],width=12)
            cat_l.place(relx=0.275,rely=0.815)
        else:
            review = review_e.get("1.0", "end-1c")
            p = all.pred_imdb([review])
            result_l = Label(main_f,text="Sentiment:",font=("monoscope",fontsize['subhead'],"bold","underline"),bg=color['frame_bg'],fg=color['text'])
            result_l.place(relx=0.155,rely=0.83)
            cat_l = Label(main_f,text=p[0].upper(),font=("monoscope",fontsize['title'],"bold"),bg=color['main_bg'],fg=color['btn'],width=12)
            cat_l.place(relx=0.275,rely=0.815)

    review_l = Label(main_f,text="Your IMDb Review",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    review_l.place(relx=0.155,rely=0.2)
    review_e = Text(main_f,font=("monoscope",fontsize['text'],"normal"),fg=color['text'],width=80,height=10)
    review_e.place(relx=0.15,rely=0.25)
    bulkrev_l = Label(main_f,text="Want to get Reviews Analysis in Bulk?? Click -->",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    bulkrev_l.place(relx=0.155,rely=0.625)
    loc_e = Entry(main_f,font=("monoscope",fontsize['text'],"normal"),fg=color['text'],width=60)
    loc_e.place(relx=0.15,rely=0.66)
    browse_btn = Button(main_f,text="Browse",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=browse)
    browse_btn.place(relx=0.7,rely=0.645)

    pred_btn = Button(main_f,text="Predict",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=predict)
    pred_btn.place(relx=0.7,rely=0.84)

def rt():
    global main_f
    main_f = Frame(win)
    main_f.configure(bg=color['frame_bg'],bd=4)
    main_f.place(relx=0.225,rely=0.12,relwidth=0.75,relheight=0.85)
    subhead_l = Label(main_f,text="Rotten Tomatoes Sentiment Prediction",font=("monoscope",fontsize['subhead'],"bold","underline"),bg=color['frame_bg'],fg=color['text'])
    subhead_l.place(relx=0.32,rely=0.01)

    def browse():
        print("File browsing....")
        loc = filedialog.askopenfile(title="Open Documents",filetypes=[("Documents", "*.txt *.xlsx *.csv *.tsv")])
        file = loc.name
        loc_e.insert(0,file)
        global details,bulk_flag
        if file.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.endswith(".xlsx"):
            df = pd.read_excel(file)
        elif file.endswith(".txt"):
            df = pd.read_csv(file,delimiter="\t")
        bulk_flag = True
        details = df.iloc[:,1].values

    def predict():
        all.rt()
        global bulk_flag,details
        if bulk_flag:
            all.pred_rt(details)
            result = pd.DataFrame(p,column=['Predicted Sentiment'])
            result.to_csv(f"{savepath}Predicted.csv")
            bulk_flag = False
            messagebox.info("Message","File Saved in Desktop!")
            cat_l = Label(main_f,text="Done! & Saved".upper(),font=("monoscope",fontsize['subhead'],"bold"),bg=color['main_bg'],fg=color['btn'],width=12)
            cat_l.place(relx=0.275,rely=0.815)
        else:
            review = review_e.get("1.0", "end-1c")
            p = all.pred_rt([review])
            result_l = Label(main_f,text="Sentiment:",font=("monoscope",fontsize['subhead'],"bold","underline"),bg=color['frame_bg'],fg=color['text'])
            result_l.place(relx=0.155,rely=0.83)
            cat_l = Label(main_f,text=p[0],font=("monoscope",fontsize['title'],"bold"),bg=color['main_bg'],fg=color['btn'],width=8)
            cat_l.place(relx=0.25,rely=0.815)

    review_l = Label(main_f,text="Rotten Tomatoes Review",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    review_l.place(relx=0.155,rely=0.2)
    review_e = Text(main_f,font=("monoscope",fontsize['text'],"normal"),fg=color['text'],width=80,height=10)
    review_e.place(relx=0.15,rely=0.25)
    bulkrev_l = Label(main_f,text="Want to get Reviews Analysis in Bulk?? Click -->",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    bulkrev_l.place(relx=0.155,rely=0.625)
    loc_e = Entry(main_f,font=("monoscope",fontsize['text'],"normal"),fg=color['text'],width=60)
    loc_e.place(relx=0.15,rely=0.66)
    browse_btn = Button(main_f,text="Browse",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=browse)
    browse_btn.place(relx=0.7,rely=0.645)

    pred_btn = Button(main_f,text="Predict",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=predict)
    pred_btn.place(relx=0.7,rely=0.84)

def loanapprv():
    global main_f
    main_f = Frame(win)
    main_f.configure(bg=color['frame_bg'],bd=4)
    main_f.place(relx=0.225,rely=0.12,relwidth=0.75,relheight=0.85)

    def browse():
        print("File browsing....")
        loc = filedialog.askopenfile(title="Open Documents",filetypes=[("Documents", "*.txt *.xlsx *.csv *.tsv")])
        file = loc.name
        loc_e.insert(0,file)
        global details,bulk_flag
        if file.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.endswith(".xlsx"):
            df = pd.read_excel(file)
        elif file.endswith(".txt"):
            df = pd.read_csv(file,delimiter="\t")
        bulk_flag = True
        details = df.iloc[:,:].values

    def predict():
        all.loan_apprv()
        global bulk_flag,details
        if bulk_flag:
            p = all.pred_loan_apprv(details)
            result = pd.DataFrame(p,column=['Predicted Approval'])
            result.to_csv(f"{savepath}Predicted.csv")
            bulk_flag = False
            messagebox.info("Message","File Saved in Desktop!")
            cat_l = Label(main_f,text="Done! & Saved".upper(),font=("monoscope",fontsize['subhead'],"bold"),bg=color['main_bg'],fg=color['btn'],width=12)
            cat_l.place(relx=0.275,rely=0.815)
        else:
            details = []
            id = lid_e.get()
            details.append(gender_e.get())
            details.append(marrd_e.get())
            details.append(dep_e.get())
            details.append(edu_e.get())
            details.append(slfemp_e.get())
            details.append(incm_e.get())
            details.append(coincm_e.get())
            details.append(amt_e.get())
            t = term_e.get()
            details.append(ch_e.get())
            details.append(area_e.get())
            p = all.pred_loan_apprv(details)
            res_l = Label(main_f,text="Approved",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
            res_l.place(relx=0.155,rely=0.75)
            res = Label(main_f,text=p[0],font=("monoscope",fontsize['title'],"bold"),bg=color['main_bg'],fg=color['btn'])
            res.place(relx=0.25,rely=0.74)


    subhead_l = Label(main_f,text="Loan Approval Prediction",font=("monoscope",fontsize['subhead'],"bold","underline"),bg=color['frame_bg'],fg=color['text'])
    subhead_l.place(relx=0.37,rely=0.01)
    details_l = Label(main_f,text="Your Loan Details:",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    details_l.place(relx=0.155,rely=0.1)

    dt_f = Canvas(main_f,bg=color['frame_bg'])
    dt_f.place(relx=0.1,rely=0.15,relheight=0.4,relwidth=0.85)
    lid_l = Label(dt_f,text="Loan Id",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                  width=15,anchor=W)
    lid_l.grid(row=0,column=0,pady=5,padx=5)
    lid_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20)
    lid_e.grid(row=0,column=1,pady=5,padx=5)
    gender_l = Label(dt_f,text="Gender",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                     width=15,anchor=W)
    gender_l.grid(row=0,column=2,pady=5,padx=5)
    gender_e = Combobox(dt_f,values=['Female','Male','Other'],font=("monoscope",fontsize['text'],"normal"),width=25)
    gender_e.grid(row=0,column=3,pady=5,padx=5)
    gender_e.current(0)
    married_l = Label(dt_f,text="Married",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                      anchor=W,width=15)
    married_l.grid(row=1,column=0,pady=5,padx=5)
    marrd_e = Combobox(dt_f,values=['No','Yes'],font=("monoscope",fontsize['text'],"normal"),width=25)
    marrd_e.grid(row=1,column=1,pady=5,padx=5)
    marrd_e.current(0)
    dep_l = Label(dt_f,text="Dependent",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                  width=15,anchor=W)
    dep_l.grid(row=1,column=2,pady=5,padx=5)
    dep_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20)
    dep_e.grid(row=1,column=3,pady=5,padx=5)
    edu_l = Label(dt_f,text="Education",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                  width=15,anchor=W)
    edu_l.grid(row=2,column=0,pady=5,padx=5)
    edu_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20)
    edu_e.grid(row=2,column=1,pady=5,padx=5)
    slfemp_l = Label(dt_f,text="Self Employed",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                     width=15,anchor=W)
    slfemp_l.grid(row=2,column=2,pady=5,padx=5)
    slfemp_e = Combobox(dt_f,values=['No','Yes'],font=("monoscope",fontsize['text'],"normal"),width=25)
    slfemp_e.grid(row=2,column=3,pady=5,padx=5)
    incm_l = Label(dt_f,text="Applicant Income",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                   width=15,anchor=W)
    incm_l.grid(row=3,column=0,pady=5,padx=5)
    incm_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20)
    incm_e.grid(row=3,column=1,pady=5,padx=5)
    coincm_l = Label(dt_f,text="CoApplicant Income",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                     width=15,anchor=W)
    coincm_l.grid(row=3,column=2,pady=5,padx=5)
    coincm_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20)
    coincm_e.grid(row=3,column=3,pady=5,padx=5)

    amt_l = Label(dt_f,text="Loan Amount",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                  anchor=W,width=15)
    amt_l.grid(row=4,column=0,pady=5,padx=5)
    amt_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20)
    amt_e.grid(row=4,column=1,pady=5,padx=5)
    term_l = Label(dt_f,text="Loan Term",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                   anchor=W,width=15)
    term_l.grid(row=4,column=2,pady=5,padx=5)
    term_e = Combobox(dt_f,values=[12,24,36,60,84,120,180,240,300,360,480],font=("monoscope",fontsize['text'],"normal"),width=25)
    term_e.grid(row=4,column=3,pady=5,padx=5)
    ch_l = Label(dt_f,text="Credit History",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                 width=15,anchor=W)
    ch_l.grid(row=5,column=0,pady=5,padx=5)
    ch_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20)
    ch_e.grid(row=5,column=1,pady=5,padx=5)
    area_l = Label(dt_f,text="Property Area",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                   width=15,anchor=W)
    area_l.grid(row=5,column=2,pady=5,padx=5)
    area_e = Combobox(dt_f,values=['Rural','Semi-Urban','Urban'],font=("monoscope",fontsize['text'],"normal"),width=25)
    area_e.grid(row=5,column=3,pady=5,padx=5)
    
    bulkht_l = Label(main_f,text="Want to predict in Bulk?? Click -->",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    bulkht_l.place(relx=0.155,rely=0.62)
    loc_e = Entry(main_f,font=("monoscope",fontsize['text'],"normal"),fg=color['text'],width=60)
    loc_e.place(relx=0.15,rely=0.66)
    browse_btn = Button(main_f,text="Browse",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=browse)
    browse_btn.place(relx=0.7,rely=0.645)

    pred_btn = Button(main_f,text="Predict",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=predict)
    pred_btn.place(relx=0.7,rely=0.84)


def bigmart():
    global main_f
    main_f = Frame(win)
    main_f.configure(bg=color['frame_bg'],bd=4)
    main_f.place(relx=0.225,rely=0.12,relwidth=0.75,relheight=0.85)
    subhead_l = Label(main_f,text="BigMart Sales Prediction",font=("monoscope",fontsize['subhead'],"bold","underline"),bg=color['frame_bg'],fg=color['text'])
    subhead_l.place(relx=0.37,rely=0.01)

    def browse():
        print("File browsing....")
        loc = filedialog.askopenfile(title="Open Documents",filetypes=[("Documents", "*.txt *.xlsx *.csv *.tsv")])
        file = loc.name
        loc_e.insert(0,file)
        global details,bulk_flag
        if file.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.endswith(".xlsx"):
            df = pd.read_excel(file)
        elif file.endswith(".txt"):
            df = pd.read_csv(file,delimiter="\t")
        bulk_flag = True
        details = df.iloc[:,:].values

    def predict():
        all.bigmrt()
        global bulk_flag,details
        if bulk_flag:
            all.pred_bigmrt(details)
            result = pd.DataFrame(p,column=['Predicted Sales'])
            result.to_csv(f"{savepath}Predicted.csv")
            bulk_flag = False
            messagebox.info("Message","File Saved in Desktop!")
            cat_l = Label(main_f,text="Done! & Saved".upper(),font=("monoscope",fontsize['subhead'],"bold"),bg=color['main_bg'],fg=color['btn'],width=12)
            cat_l.place(relx=0.275,rely=0.815)
        else:
            details = []
            id = id_e.get()
            details.append(wt_e.get())
            details.append(fat_e.get())
            details.append(visibl_e.get())
            details.append(type_e.get())
            details.append(mrp_e.get())
            details.append(outlet_e.get())
            t = estb_e.get()
            sz = olsize_e.get()
            details.append(olloc_e.get())
            details.append(oltype_e.get())
            p = all.pred_bigmrt(details)
            wt_l = Label(main_f,text="Approved",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
            wt_l.place(relx=0.155,rely=0.75)
            wt = Label(main_f,text=p[0],font=("monoscope",fontsize['title'],"bold"),bg=color['main_bg'],fg=color['btn'])
            wt.place(relx=0.25,rely=0.74)

    details_l = Label(main_f,text="Your BigMart Details:",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    details_l.place(relx=0.155,rely=0.1)

    dt_f = Canvas(main_f,bg=color['frame_bg'])
    dt_f.place(relx=0.1,rely=0.15,relheight=0.4,relwidth=0.85)
    id_l = Label(dt_f,text="Item Id",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                  width=15,anchor=W)
    id_l.grid(row=0,column=0,pady=5,padx=5)
    id_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20)
    id_e.grid(row=0,column=1,pady=5,padx=5)
    wt_l = Label(dt_f,text="Item Weight",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                     width=15,anchor=W)
    wt_l.grid(row=0,column=2,pady=5,padx=5)
    wt_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20)
    wt_e.grid(row=0,column=3,pady=5,padx=5)
    fat_l = Label(dt_f,text="Fat Content",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                      anchor=W,width=15)
    fat_l.grid(row=1,column=0,pady=5,padx=5)
    fat_e = Combobox(dt_f,values=['Low Fat','Regular','High Fat'],font=("monoscope",fontsize['text'],"normal"),width=25)
    fat_e.grid(row=1,column=1,pady=5,padx=5)
    fat_e.current(0)
    visibl_l = Label(dt_f,text="Item Visibility",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                  width=15,anchor=W)
    visibl_l.grid(row=1,column=2,pady=5,padx=5)
    visibl_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20)
    visibl_e.grid(row=1,column=3,pady=5,padx=5)
    type_l = Label(dt_f,text="Item Type",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                  width=15,anchor=W)
    type_l.grid(row=2,column=0,pady=5,padx=5)
    type_e = Combobox(dt_f,values=item_type,font=("monoscope",fontsize['text'],"normal"),width=25)
    type_e.grid(row=2,column=1,pady=5,padx=5)
    mrp_l = Label(dt_f,text="Item MRP",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                     width=15,anchor=W)
    mrp_l.grid(row=2,column=2,pady=5,padx=5)
    mrp_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20) 
    mrp_e.grid(row=2,column=3,pady=5,padx=5)
    outlet_l = Label(dt_f,text="Outlet Identifier",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                   width=15,anchor=W)
    outlet_l.grid(row=3,column=0,pady=5,padx=5)
    outlet_e = Entry(dt_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=20)
    outlet_e.grid(row=3,column=1,pady=5,padx=5)
    estb_l = Label(dt_f,text="Outlet Establisted",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                     width=15,anchor=W)
    estb_l.grid(row=3,column=2,pady=5,padx=5)
    estb_e = Combobox(dt_f,values=yr,font=("monoscope",fontsize['text'],"normal"),width=25)
    estb_e.grid(row=3,column=3,pady=5,padx=5)
    estb_e.current(0)
    olsize_l = Label(dt_f,text="Outlet Size",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                  anchor=W,width=15)
    olsize_l.grid(row=4,column=0,pady=5,padx=5)
    olsize_e = Combobox(dt_f,values=['Small','Medium','High'],font=("monoscope",fontsize['text'],"normal"),width=25)
    olsize_e.grid(row=4,column=1,pady=5,padx=5)
    olsize_e.current(0)
    olloc_l = Label(dt_f,text="Outlet Location",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                   anchor=W,width=15)
    olloc_l.grid(row=4,column=2,pady=5,padx=5)
    olloc_e = Combobox(dt_f,values=['Tier 1','Tier 2','Tier 3'],font=("monoscope",fontsize['text'],"normal"),width=25)
    olloc_e.grid(row=4,column=3,pady=5,padx=5)
    olloc_e.current(0)
    oltype_l = Label(dt_f,text="Credit History",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'],
                 width=15,anchor=W)
    oltype_l.grid(row=5,column=0,pady=5,padx=5)
    oltype_e = Combobox(dt_f,values=['Grocery Store','Supermarket Type1''Supermarket Type2','Supermarket Type3'],font=("monoscope",fontsize['text'],"normal"),width=25)
    oltype_e.grid(row=5,column=1,pady=5,padx=5)
    oltype_e.current(0)


    bulkht_l = Label(main_f,text="Want to predict Sales in Bulk?? Click -->",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    bulkht_l.place(relx=0.155,rely=0.62)
    loc_e = Entry(main_f,font=("monoscope",fontsize['text'],"normal"),fg=color['text'],width=60)
    loc_e.place(relx=0.15,rely=0.66)
    browse_btn = Button(main_f,text="Browse",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=browse)
    browse_btn.place(relx=0.7,rely=0.645)

    pred_btn = Button(main_f,text="Predict",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=predict)
    pred_btn.place(relx=0.7,rely=0.84)

def hnw():
    global main_f
    main_f = Frame(win)
    main_f.configure(bg=color['frame_bg'],bd=4)
    main_f.place(relx=0.225,rely=0.12,relwidth=0.75,relheight=0.85)
    subhead_l = Label(main_f,text="Height to Weight Prediction",font=("monoscope",fontsize['subhead'],"bold","underline"),bg=color['frame_bg'],fg=color['text'])
    subhead_l.place(relx=0.37,rely=0.01)

    def browse():
        print("File browsing....")
        loc = filedialog.askopenfile(title="Open Documents",filetypes=[("Documents", "*.txt *.xlsx *.csv *.tsv")])
        file = loc.name
        loc_e.insert(0,file)
        global details,bulk_flag
        if file.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.endswith(".xlsx"):
            df = pd.read_excel(file)
        elif file.endswith(".txt"):
            df = pd.read_csv(file,delimiter="\t")
        bulk_flag = True
        details = df.iloc[:,1].values

    def predict():
        global bulk_flag,details
        if bulk_flag:
            p = all.htnwt(details)
            result = pd.DataFrame(p,column=['Predicted Weight'])
            result.to_csv(f"{savepath}Predicted.csv")
            bulk_flag = False
            messagebox.info("Message","File Saved in Desktop!")
            cat_l = Label(main_f,text="Done! & Saved".upper(),font=("monoscope",fontsize['subhead'],"bold"),bg=color['main_bg'],fg=color['btn'],width=12)
            cat_l.place(relx=0.275,rely=0.815)
        else:
            h = ht_e.get()
            p = all.htnwt([[h]])
            wt_l = Label(main_f,text="Weight",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
            wt_l.place(relx=0.155,rely=0.84)
            wt = Label(main_f,text=round(p[0],2),font=("monoscope",fontsize['title'],"bold"),bg=color['main_bg'],fg=color['btn'])
            wt.place(relx=0.25,rely=0.84)

    ht_l = Label(main_f,text="Enter your Height:",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    ht_l.place(relx=0.155,rely=0.2)
    ht_e = Entry(main_f,font=("monoscope",fontsize['subhead'],"normal"),fg=color['text'],width=30)
    ht_e.place(relx=0.15,rely=0.25)
    bulkht_l = Label(main_f,text="Want to predict Weight in Bulk?? Click -->",font=("monoscope",fontsize['text'],"bold"),bg=color['frame_bg'],fg=color['text'])
    bulkht_l.place(relx=0.155,rely=0.615)
    loc_e = Entry(main_f,font=("monoscope",fontsize['text'],"normal"),fg=color['text'],width=60)
    loc_e.place(relx=0.15,rely=0.66)
    browse_btn = Button(main_f,text="Browse",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=browse)
    browse_btn.place(relx=0.7,rely=0.645)

    pred_btn = Button(main_f,text="Predict",width=15,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=predict)
    pred_btn.place(relx=0.7,rely=0.84)



sidebar_f = Frame(win)
sidebar_f.configure(bg=color['main_bg'],bd=2)
sidebar_f.place(relx=0.005,rely=0.2,relheight=0.85,relwidth=0.25)

bbcnews_btn = Button(sidebar_f,text="BBC News",width=20,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=bbc)
bbcnews_btn.grid(row=0,column=0,padx=5,pady=20)
imdb_btn = Button(sidebar_f,text="IMDb Reviews",width=20,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=imdb)
imdb_btn.grid(row=1,column=0,padx=5,pady=20)
rt_btn = Button(sidebar_f,text="Rotten Tomatoes",width=20,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=rt)
rt_btn.grid(row=2,column=0,padx=5,pady=20)
loanapp_btn = Button(sidebar_f,text="Loan Approval",width=20,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=loanapprv)
loanapp_btn.grid(row=3,column=0,padx=5,pady=20)
bigmrt_btn = Button(sidebar_f,text="BigMart Sales",width=20,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=bigmart)
bigmrt_btn.grid(row=4,column=0,padx=5,pady=20)
hnw_btn = Button(sidebar_f,text="Height and Weight ",width=20,font=("monoscope",fontsize['subhead'],"normal"),bg=color['btn'],fg=color['text'],bd=2,command=hnw)
hnw_btn.grid(row=5,column=0,padx=5,pady=20)




win.mainloop()






