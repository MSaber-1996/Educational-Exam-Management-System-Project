# importing modules (the Tkinter and pyodbc the most two or ths main important libraries in this project : \
# Tkinter it is a python library that make gui and Pyodbc that allow to connect with sql server databases)

from faulthandler import disable
#import customtkinter
from cgitb import text
from random import choices
from sys import stdin
from tarfile import RECORDSIZE
from tkinter import *
from tkinter.font import BOLD
from turtle import update, width
from unicodedata import name
import pyodbc
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkinter import customtkinter

#*************************************************************************************
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green



# create the main window

root = Tk()
root.title("Exam System")
root.iconbitmap("D:/BI_ITI/project/Exam_try/iti_logo.ico")
root.geometry('500x300')
root['bg'] = "#2a3439"




# define the function of Query from database

def SQLQuery(Q):
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor = connection.cursor()
    cursor.execute(Q)
    cursor.commit()
    connection.close()




#***********************************************************************************************************************************************
# cerate the student window and all it's widgets

def openstudent_1():
  global student_1
  student_1 =  Toplevel(root)
  student_1.iconbitmap("D:/BI_ITI/project/Exam_try/iti_logo.ico")
  student_1.title("Student")
  student_1.geometry("500x300")
  student_1['bg'] = "#2a3439"
  
  #define the labels of the student_1 window

  label_hellodear = Label(student_1, text = "Hello, Dear : Student",font=('Arial 16 bold'), fg="black" , bg="#E6E6FA")
  label_hellodear.grid(row= 0, column=3, columnspan= 5, padx= 40, pady=10)
  label_info = Label(student_1, text= "Please tell Us this Information", font=('Arial', 16), fg="black", bg="#E6E6FA" )
  label_info.grid(row= 2, column=2, columnspan= 5, padx= 30, pady=10)

  label_ID = Label(student_1, text= "ID", font=('Arial 10 bold'), bg="#E6E6FA", fg="black")
  label_ID.grid(row=3, column=3)
  label_fname = Label(student_1, text= "First Name", font=('Arial 10 bold'), bg="#E6E6FA", fg="black")
  label_fname.grid(row=4, column=3)
  
  
 #define the entry widgets in student_1 window
  global e_id
  e_id = Entry(student_1, borderwidth= 2)
  e_fname = Entry(student_1, borderwidth= 2)
 
  e_id.grid(row= 3 , column=4)
  e_fname.grid(row= 4 , column=4)
 

  #define function of take the values from entry widget in student_1 window

  def store_st_values():
    StID = e_id.get()
    StFname = e_fname.get()
    
    label_helloSt = Label(student_2, text= f"Hello {StFname} ", font= ('Arial 16 bold'), fg="black" , bg="#E6E6FA")
    label_helloSt.grid(row= 1, column=0, columnspan= 5, padx= 20, pady=10 )

  btn_ok = Button (student_1, text= "Check" , font=('Arial 14 bold'), fg="blue" , bg="#E6E6FA", command= lambda : check())
  btn_ok.grid(row = 4 , column = 5, padx = 10)

  def check():
    conn_check = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cur_check = conn_check.cursor()
    cur_check.execute(f"select StID from Student")
    records = cur_check.fetchall()
    cur_check.close()
    conn_check.close()
    ids = []
    for x in records:
        ids.append(x[0])

    if int(e_id.get())  in ids:
        conn_checkname = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
        cur_checkname = conn_checkname.cursor()
        cur_checkname.execute(f"select StFname from Student WHERE StID = {e_id.get()}")
        recordname = cur_checkname.fetchall()
        cur_checkname.close()
        conn_checkname.close()

        if str(e_fname.get()) != recordname[0][0]:
          messagebox.showerror("showerror", "Invalid Student Name")
          
        else:
          
          btn_ok = Button (student_1, text= "OK" , font=('Arial 14 bold'), fg="blue" , bg="#E6E6FA",\
          command= lambda : [openstudent_2(), store_st_values()])
          btn_ok.grid(row = 6 , column = 2, columnspan = 5, padx = 10, pady = 10)

    else:
       messagebox.showerror("showerror", "Invalid ID")
        




  # define the button ok to move to the next window student_2 
   
  # btn_ok = Button (student_1, text= "OK" , font=('Arial 17 bold'), fg="blue" , bg="#000000",\
  #  command= lambda : [openstudent_2(), store_st_values()])
  # btn_ok.grid(row = 6 , column = 2, columnspan = 5, padx = 10, pady = 10)

#***********************************************************************************************************************************************
### create the Second window for student
def openstudent_2():
  global student_2
  student_2 = Toplevel(student_1)
  student_2.iconbitmap("D:/BI_ITI/project/Exam_try/iti_logo.ico")
  student_2.title("Ready To Exam")
  student_2.geometry("500x300")
  student_2['bg'] = "#2a3439"

  label_clickstart = Label(student_2, text=("If you are ready to Exam Click Start"),font= ('Arial 16 bold'), fg="black" , bg="#E6E6FA")
  label_clickstart.grid(row= 2, column= 0 , columnspan= 5, padx= 40, pady=5 )
  
  #btn_CSharp = Button(student_2, text= "C#", font=('Arial 17 bold'), fg= "black", bg= "red", command=lambda:[csharpexam()])
  btn_Start = Button(student_2, text= "Start", font=('Arial 14 bold'), fg= "blue", bg= "#E6E6FA", command=lambda:[startexam()])
  #btn_Python = Button(student_2, text= "Python", font=('Arial 17 bold'), fg= "black", bg= "red",command=lambda:[pythonexam()])

  #btn_CSharp.grid(row= 3, column=1 , pady= 20)
  btn_Start.grid(row= 3, column= 2, pady= 20)
  #btn_Python.grid(row= 3, column= 3, pady= 20)

# the sql exam *********************************************

def startexam():
    global Exam
    Exam = Toplevel(student_2)
    Exam.iconbitmap("D:/BI_ITI/project/Exam_try/iti_logo.ico")
    Exam.title("Exam")
    Exam.geometry("900x600")
    Exam['bg'] = "#2a3439"

    label_qsql = Label(Exam, text="Questions", font=('Arial 12 bold'), fg="black", bg="#E6E6FA")
    label_qsql.grid(row=0, column=0)

    label_crs = Label(Exam, text="Course" , font=('Arial 12 bold'), fg="black", bg="#E6E6FA")
    label_crs.grid(row=0, column=8)

    label_ExID = Label(Exam, text="ExID", font=('Arial 10 bold'), fg="black", bg="#E6E6FA")
    label_ExID.grid(row=0, column=2, padx=10)

    label_qid = Label(Exam, text="QID", font=('Arial 10 bold'), fg="black", bg="#E6E6FA")
    label_qid.grid(row=0, column=5, padx=10)

    e_exid = Entry(Exam, width=7, borderwidth=2)
    e_exid.grid(row=0, column=3)

    e_qid = Entry(Exam, width=5, borderwidth=2)
    e_qid.grid(row=0, column=6)

    e_Ans = Entry(Exam, width=5, borderwidth=2)
    e_Ans.grid(row=3, column=2)

    btn_viewQs = Button(Exam, text="view Questions",\
       fg="blue",bg="#E6E6FA",command=lambda:[textquestions.insert(END,querysql()), text_crs.insert(END,crsQuery())])
    btn_viewQs.grid(row=0, column=4)

    btn_viewQ = Button(Exam, text="view Question", fg="blue", bg="#E6E6FA" ,command=lambda:[textquestion.insert(END,queryQuestion()),\
       textchoices.insert(END, querychoices())])
    btn_viewQ.grid(row=0, column=7)

    btn_viewAns = Button(Exam, text="Answer", fg="blue", bg="#E6E6FA" ,command=lambda :[insertanswer()])
    btn_viewAns.grid(row=3, column=1, pady=20)

    btn_empty = Button(Exam, text="Clear", fg="blue", bg="#E6E6FA" ,command=lambda :[ClearQuestions()])
    btn_empty.grid(row=2, column=0)

    def ClearQuestions():
      textquestions.delete(1.0, END)
      e_exid.delete(0, END)
      text_crs.delete(1.0, END)
      textchoices.delete(1.0, END)
      textquestion.delete(1.0, END)
      e_qid.delete(0, END)


    textquestions = Text(Exam, width=5, height=10, font=('Arial 10 bold'), bg="#2a3439", fg="white")
    textquestions.grid(row=1, column=0)

    text_crs = Text(Exam, width=10, height=2, font=('Arial 12 bold'), bg="#2a3439", fg="white")
    text_crs.grid(row=0, column=9, pady=10)


    def crsQuery():
      conn_crs = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
      cur_crs = conn_crs.cursor()
      cur_crs.execute(f"select CrsName from Course where CrsID = (select ExCrsID from Exam where ExID = {e_exid.get()})")
      crs = cur_crs.fetchall()
      cur_crs.close()
      conn_crs.close()
      return crs[0][0]
    

    textquestion = Text(Exam, width=100, height=3, font=('Arial 10 bold'), bg="#2a3439", fg="white")
    textquestion.grid(row=1, column=1, columnspan=10)

    textchoices = Text(Exam, width=100, height=20, font=('Arial 8 bold'), bg="#2a3439", fg="white")
    textchoices.grid(row=2, column=1, columnspan=10 )

    def querysql():
      global ex_id
      ex_id = e_exid.get()
      conn_Sql = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
      cur_Sql = conn_Sql.cursor()
      cur_Sql.execute(f"SELECT QID FROM ExamQuestion WHERE ExID = {ex_id}")
      Sqlqs = cur_Sql.fetchall()
      cur_Sql.close()
      conn_Sql.close()
      print_Sqlqs = ''
      for x in Sqlqs:
        print_Sqlqs = print_Sqlqs+str(x[0])+"\n"
      return print_Sqlqs

    def queryQuestion():
      global Question
      Question = e_qid.get()
      conn_ques = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
      cur_ques = conn_ques.cursor()
      cur_ques.execute(f"SELECT QBody FROM Question WHERE QID = {Question}")
      Sqlquestion = cur_ques.fetchall()
      cur_ques.close()
      conn_ques.close()
      print_Sqlques = ''
      for x in Sqlquestion:
        print_Sqlques = print_Sqlques+str(x[0])
      return print_Sqlques

    def querychoices():
      global querychoice
      querychoice = e_qid.get()
      conn_choices = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
      cur_choices = conn_choices.cursor()
      cur_choices.execute(f"SELECT Choice FROM QMcqChoice WHERE QID = {Question}")
      qchoices = cur_choices.fetchall()
      cur_choices.close()
      conn_choices.close()
      print_qchoices = ''
      for x in qchoices:
        print_qchoices = print_qchoices+str(x[0])+"\n"
      return print_qchoices

    
    def insertanswer():
      StIDAns = e_id.get()
      ExIDAns = e_exid.get()
      QIDAns = e_qid.get()
      Ans =  e_Ans.get()
      conn_ans = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
      cursor_ans = conn_ans.cursor()
      cursor_ans.execute(f" [dbo].[ansinfo] {StIDAns},{QIDAns},{ExIDAns},{Ans}")
      cursor_ans.commit()
      conn_ans.close()

      
      conn_model = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
      cursor_model = conn_model.cursor()
      cursor_model.execute(f"select QModelAnswer from Question where QID = {QIDAns}")
      model= cursor_model.fetchall()
      
      if model[0][0] in Ans:
        conn_mark = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
        cur_mark = conn_mark.cursor()
        cur_mark.execute(f"update Answer set Mark = 1 where QID = {QIDAns}")
        cur_mark.commit()
        conn_mark.close()
      else:
        conn_notmark = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
        cur_notmark = conn_notmark.cursor()
        cur_notmark.execute(f"update Answer set Mark = 0 where QID = {QIDAns}")
        cur_notmark.commit()
        cur_notmark.close()
      cursor_model.commit()
      conn_model.close()
      e_qid.delete(0,END)
      textquestion.delete(1.0, END)
      textchoices.delete(1.0, END)
      e_Ans.delete(0,END)





# the c# exam ***********************************************

# def csharpexam():
#   global CSharp
#   CSharp = Toplevel(student_2)
#   CSharp.title("C# Exam")
#   CSharp.geometry("500x300")
#   CSharp['bg'] = "#E6E6FA"

  


# the python exam *********************************************

# def pythonexam():
#   global Python
#   Python = Toplevel(student_2)
#   Python.title("Python Exam")
#   Python.geometry("500x300")
#   Python['bg'] = "#E6E6FA"

  # btntryQuery = Button(student_2, text = "Query", command= SQLQuery("select * from student"))
  # btntryQuery.grid(row)

#***********************************************************************************************************************************************
#create the instructor 1 window
def openinstructor_1():
  global ins_1
  ins_1 =  Toplevel(root)
  ins_1.iconbitmap("D:/BI_ITI/project/Exam_try/iti_logo.ico")
  ins_1.title("Instructor")
  ins_1.geometry("500x300")
  ins_1['bg'] = "#2a3439"
  label_hellodear_ins_1 = Label(ins_1, text = "Hello, Dear : Instructor",font=('Arial 17 bold'), fg="black" , bg="#E6E6FA")
  label_hellodear_ins_1.grid(row= 0, column=3, columnspan= 5, padx= 40, pady=10)
  label_info_ins_1 = Label(ins_1, text= "Please tell Us this Information", font=('Arial', 16), fg="black", bg="#E6E6FA")
  label_info_ins_1.grid(row= 2, column=2, columnspan= 5, padx= 30, pady=10)

  label_ID_ins_1 = Label(ins_1, text= "ID", font=('Arial 10 bold'), fg="black", bg="#E6E6FA")
  label_ID_ins_1.grid(row=3, column=3)
  label_fname_ins_1 = Label(ins_1, text= "First Name", font=('Arial 10 bold'), fg="black", bg="#E6E6FA")
  label_fname_ins_1.grid(row=4, column=3)
  
  e_id_ins_1 = Entry(ins_1, borderwidth= 2)
  e_fname_ins_1 = Entry(ins_1, borderwidth= 2)
  
  e_id_ins_1.grid(row= 3 , column=4)
  e_fname_ins_1.grid(row= 4 , column=4)
  

  def ins_1_values():
    InsID = e_id_ins_1.get()
    InsFname = e_fname_ins_1.get()
    
    label_helloIns = Label(ins_2, text= f"Hello Eng {InsFname}", font= ('Arial 17 bold'), fg="black" , bg="#E6E6FA")
    label_helloIns.grid(row= 0, column=0, columnspan= 3, padx= 10, pady=5 )

    

  btn_ok = Button (ins_1, text= "Check" , font=('Arial 14 bold'), fg="blue" , bg="#E6E6FA", command= lambda : checkins())
  btn_ok.grid(row = 4 , column = 5, padx = 10)

  def checkins():
    conn_checkins = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cur_checkins = conn_checkins.cursor()
    cur_checkins.execute(f"select InsID from Instructor")
    records = cur_checkins.fetchall()
    cur_checkins.close()
    conn_checkins.close()
    idsins = []
    for x in records:
        idsins.append(x[0])

    if int(e_id_ins_1.get())  in idsins:
        conn_checknameins = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
        cur_checknameins = conn_checknameins.cursor()
        cur_checknameins.execute(f"select InsFname from Instructor WHERE InsID = {e_id_ins_1.get()}")
        recordnameins = cur_checknameins.fetchall()
        cur_checknameins.close()
        conn_checknameins.close()

        if str(e_fname_ins_1.get()) != recordnameins[0][0]:
          messagebox.showerror("showerror", "Invalid Instructor Name")
          # mesage = Toplevel(ins_1)
          # whatever_you_do = "Invalid Instructor FName"
          # msg = Message(mesage, text = whatever_you_do)
          # msg.config(bg='white', font=('Arial', 10, 'bold'))
          # msg.grid(row=0,column=0)
        else:
          # mesage = Toplevel(ins_1)
          # whatever_you_do = "Correct Login"
          # msg = Message(mesage, text = whatever_you_do)
          # msg.config(bg='white', font=('Arial 10 bold'))
          # msg.grid(row=0,column=0)
          btn_ins_1_ok = Button (ins_1, text= "OK" , font=('Arial 17 bold'), fg="blue" , bg="#E6E6FA",\
           command= lambda : [openinstructor_2() , ins_1_values()])
          btn_ins_1_ok.grid(row = 6 , column = 2, columnspan = 5, padx = 10, pady = 10)
          
    else:
       messagebox.showerror("showerror", "Invalid ID")
        # mesage = Toplevel(ins_1)
        # whatever_you_do = "Invalid ID"
        # msg = Message(mesage, text = whatever_you_do)
        # msg.config(bg='white', font=('Arial 24 bold'))
        # msg.grid(row=0,column=0)    

  

#*******************************************************************************************************************************************

#create the instructor second window

def openinstructor_2():
  global ins_2
  ins_2 = Toplevel(ins_1)
  ins_2.iconbitmap("D:/BI_ITI/project/Exam_try/iti_logo.ico")
  ins_2.title("Instructor Job")
  ins_2.geometry("500x400")
  ins_2['bg'] = "#2a3439"

  label_database = Label(ins_2, text="Tabels in Our Database",font= ('Arial 14 bold'), fg="black" , bg="#E6E6FA" )
  label_database.grid(row=3, column=0, columnspan=4)

  btn_insert_st = Button(ins_2, text= "Add Student",width= 12, font=('Arial 12 bold'), fg="blue" , bg="#E6E6FA", command= lambda : [add_student()])
  btn_update_st = Button(ins_2, text= "Update Student",width= 12, font=('Arial 12 bold'), fg="blue" , bg="#E6E6FA", command= lambda : [update_student()])
  btn_delete_st = Button(ins_2, text= "Delete Student",width= 12 , font=('Arial 12 bold'), fg="blue" , bg="#E6E6FA", command= lambda : [delete_student()])
  btn_exam_creation = Button(ins_2, text= "Exam Creation",width= 12, font=('Arial 12 bold'), fg="blue" , bg="#E6E6FA", command= lambda : [create_exam()])
  btn_exam_correction = Button(ins_2, text= "Exam Correction",width= 12, font=('Arial 12 bold'), fg="blue", bg="#E6E6FA", command= lambda :[ExamCorrection()])  
  btn_reports = Button(ins_2, text="Reports",font=('Arial 12 bold'),width= 12, fg="blue", bg="#BFFF00", command=lambda: [Examreports()])
  btn_StudentTable = Button(ins_2, text="Student", font=('Arial 12 bold'),width= 12, fg="blue", bg="#ADD8E6",\
   command=lambda:studentfun())
  btn_CourseTable = Button(ins_2, text="Course", font=('Arial 12 bold'),width= 12, fg="blue", bg="#ADD8E6", command=lambda:coursefun())
  btn_AnswerTable = Button(ins_2, text="Answer", font=('Arial 12 bold'),width= 12, fg="blue", bg="#ADD8E6", command=lambda:Answerfun())
  btn_DepartmentTable = Button(ins_2, text="Department", font=('Arial 12 bold'),width= 12, fg="blue", bg="#ADD8E6", command=lambda:Depfun())
  btn_ExamTable = Button(ins_2, text="Exam", font=('Arial 12 bold'),width= 12, fg="blue", bg="#ADD8E6", command=lambda:Examfun())
  btn_ExamQuestionTable = Button(ins_2, text="ExamQuestion",width= 12, font=('Arial 12 bold'), fg="blue", bg="#ADD8E6", command=lambda:ExamQuesfun())
  btn_InstructorTable = Button(ins_2, text="Instructor",width= 12, font=('Arial 12 bold'), fg="blue", bg="#ADD8E6", command=lambda:Insfun())
  btn_QuestionTable = Button(ins_2, text="Question",width= 12, font=('Arial 12 bold'), fg="blue", bg="#ADD8E6", command=lambda:Quesfun())
  btn_QMcqChiceTable = Button(ins_2, text="QMcqChoice",width= 12, font=('Arial 12 bold'), fg="blue", bg="#ADD8E6", command=lambda:Choicefun())
  btn_StudentCourseTable = Button(ins_2, text="StudentCourse",width= 12, font=('Arial 12 bold'), fg="blue", bg="#ADD8E6", command=lambda:StCrsfun())
  btn_TopicTable = Button(ins_2, text="Topics",width= 12, font=('Arial 12 bold'), fg="blue", bg="#ADD8E6", command=lambda:Topicfun())


  btn_insert_st.grid(row= 1 , column= 0, padx=10, pady=10)
  btn_update_st.grid(row= 1 , column= 1, padx=10, pady=10)
  btn_delete_st.grid(row= 1 , column= 2,padx=10, pady=10)
  btn_exam_creation.grid(row=2, column=0,padx=10, pady=10)
  btn_exam_correction.grid(row=2, column= 1, padx=10, pady=10)
  btn_reports.grid(row=2, column=2, padx=10, pady=10)
  btn_StudentTable.grid(row=4, column=0, padx=10, pady=10)
  btn_CourseTable.grid(row=4, column=1, padx=10, pady=10)
  btn_AnswerTable.grid(row=4, column=2, padx=10, pady=10)
  btn_DepartmentTable.grid(row=5, column=0, padx=10, pady=10)
  btn_ExamTable.grid(row=5, column=1, padx=10, pady=10)
  btn_ExamQuestionTable.grid(row=5, column=2, padx=10, pady=10)
  btn_InstructorTable.grid(row=6, column=0, padx=10, pady=10)
  btn_QuestionTable.grid(row=6, column=1, padx=10, pady=10)
  btn_QMcqChiceTable.grid(row=6, column=2, padx=10, pady=10)
  btn_StudentCourseTable.grid(row=7, column=0, padx=10, pady=10)
  btn_TopicTable.grid(row=7, column=1, padx=10, pady=10)

#define functions of new windows to show the  Student tables STSTSSTSTTSTSSTSTSTTSTSTSTTSTSTSTSTSTTSTSTSTSTTSTSTSTSTSTSTSTSTSTTSTSTSTSTSTSTS

def studentfun():
  global studentdata
  studentdata = Toplevel(ins_2)
  studentdata.title("Student Table")

  # add some style 

  style = ttk.Style()

#pick a theme 

  style.theme_use('default')

# configure the tree view colors

  style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")

# change the selected color
  style.map('Treeview', background = [('selected', '#347083')])

# create the tree view frame
  tree_frame = Frame(studentdata)
  tree_frame.pack(pady=5)

# create the frame scrollbar

  scroll_frame = Scrollbar(tree_frame)
  scroll_frame.pack(side=RIGHT, fill = Y)

## create the tree view*****************

  my_tree = ttk.Treeview(tree_frame, yscrollcommand= scroll_frame.set, selectmode="extended")
  my_tree.pack()

# define the scrollbar

  scroll_frame.config(command=my_tree.yview)

# define our columns

  my_tree['columns'] = ("ID","FName","LName","Age","Gender","City","Email","Phone","Link","Department")
  my_tree.column("#0", width=0, stretch=NO)
  my_tree.column("ID", anchor=CENTER, width="30")
  my_tree.column("FName", anchor=W, width="100")
  my_tree.column("LName", anchor=W, width="100")
  my_tree.column("Age", anchor=CENTER, width="30")
  my_tree.column("Gender", anchor=CENTER, width="30")
  my_tree.column("City", anchor=CENTER, width="100")
  my_tree.column("Email", anchor=CENTER, width="300")
  my_tree.column("Phone", anchor=W, width="200")
  my_tree.column("Link", anchor=CENTER, width="300")
  my_tree.column("Department", anchor=CENTER, width="50")


# define the heading of this column

  my_tree.heading("#0", text="", anchor=W)
  my_tree.heading("ID", text="ID", anchor=CENTER)
  my_tree.heading("FName", text="First Name", anchor=W)
  my_tree.heading("LName", text="Last Name", anchor=W)
  my_tree.heading("Age", text="Age", anchor=CENTER)
  my_tree.heading("Gender", text="Gender", anchor=CENTER)
  my_tree.heading("City", text="City", anchor=CENTER)
  my_tree.heading("Email", text="Email", anchor=CENTER)
  my_tree.heading("Phone", text="Phone", anchor=W)
  my_tree.heading("Link", text="Link", anchor=CENTER)
  my_tree.heading("Department", text="Department", anchor=CENTER)

#  Add Data

  conn_selectST = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
  cur_selectST = conn_selectST.cursor()
  cur_selectST.execute("select * from Student")
  records = cur_selectST.fetchall()
  cur_selectST.close()
  conn_selectST.close()

#  create stripted rows

  my_tree.tag_configure('oddrow', background="white")
  my_tree.tag_configure('evenrow', background="lightblue")

# display our data on the screen

  global countt
  countt = 0
  for record in records:
      if countt % 2==0:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               record[5], record[6], record[7], record[8], record[9]), tags=('evenrow',))
      else:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               record[5], record[6], record[7], record[8], record[9]), tags=('oddnrow',))

      countt+=1


#define functions of new windows to show the database Course tables CRSCRSCRSCRSCRSCRRSCRSCRSCRSRCRSCRSCRSCRSCRCRSCRSCRSCRSCRSCRSCRSCRSCRSCRR

def coursefun():
  global coursedata
  coursedata = Toplevel(ins_2)
  coursedata.title("Course Table")

  # add some style

  style = ttk.Style()

#pick a theme 

  style.theme_use('default')

# configure the tree view colors

  style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")

# change the selected color
  style.map('Treeview', background = [('selected', '#347083')])

# create the tree view frame
  tree_frame = Frame(coursedata)
  tree_frame.pack(pady=10)

# create the frame scrollbar

  scroll_frame = Scrollbar(tree_frame)
  scroll_frame.pack(side=RIGHT, fill = Y)

## create the tree view*****************

  my_tree = ttk.Treeview(tree_frame, yscrollcommand= scroll_frame.set, selectmode="extended")
  my_tree.pack()

# define the scrollbar

  scroll_frame.config(command=my_tree.yview)

# define our columns

  my_tree['columns'] = ("CrsID","CrsName","CrsDuration","CrsInsID")
  my_tree.column("#0", width=0, stretch=NO)
  my_tree.column("CrsID", anchor=CENTER, width="50")
  my_tree.column("CrsName", anchor=W, width="100")
  my_tree.column("CrsDuration", anchor=W, width="100")
  my_tree.column("CrsInsID", anchor=CENTER, width="50")


# define the heading of this column

  my_tree.heading("#0", text="", anchor=W)
  my_tree.heading("CrsID", text="ID", anchor=CENTER)
  my_tree.heading("CrsName", text="Course Name", anchor=W)
  my_tree.heading("CrsDuration", text="Duration", anchor=W)
  my_tree.heading("CrsInsID", text="InsID", anchor=CENTER)
  

#  Add Data

  conn_selectCrs = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
  cur_selectCrs = conn_selectCrs.cursor()
  cur_selectCrs.execute("select * from Course")
  records = cur_selectCrs.fetchall()
  cur_selectCrs.close()
  conn_selectCrs.close()

#  create stripted rows

  my_tree.tag_configure('oddrow', background="white")
  my_tree.tag_configure('evenrow', background="lightblue")

# display our data on the screen

  global countt
  countt = 0
  for record in records:
      if countt % 2==0:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
      else:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3]), tags=('oddnrow',))

      countt+=1







#define functions of new windows to show the  Answer tables ANSANANSANSANSANSANSANSSANSANSANSANSANSSANSANSANSANSANSSANSANSANSANSANSSANSANSANSANSANS

def Answerfun():
  global answerdata
  answerdata = Toplevel(ins_2)
  answerdata.title("Answer Table")

  # add some style 

  style = ttk.Style()

#pick a theme 

  style.theme_use('default')

# configure the tree view colors

  style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")

# change the selected color
  style.map('Treeview', background = [('selected', '#347083')])

# create the tree view frame
  tree_frame = Frame(answerdata)
  tree_frame.pack(pady=10)

# create the frame scrollbar

  scroll_frame = Scrollbar(tree_frame)
  scroll_frame.pack(side=RIGHT, fill = Y)

## create the tree view*****************

  my_tree = ttk.Treeview(tree_frame, yscrollcommand= scroll_frame.set, selectmode="extended")
  my_tree.pack()

# define the scrollbar

  scroll_frame.config(command=my_tree.yview)

# define our columns

  my_tree['columns'] = ("StID","QID","ExID","Date","Answer","Mark")
  my_tree.column("#0", width=0, stretch=NO)
  my_tree.column("StID", anchor=CENTER, width="50")
  my_tree.column("QID", anchor=W, width="100")
  my_tree.column("ExID", anchor=W, width="100")
  my_tree.column("Date", anchor=CENTER, width="200")
  my_tree.column("Answer", anchor=CENTER, width="50")
  my_tree.column("Mark", anchor=CENTER, width="50")


# define the heading of this column

  my_tree.heading("#0", text="", anchor=W)
  my_tree.heading("StID", text="StID", anchor=CENTER)
  my_tree.heading("QID", text="QID", anchor=W)
  my_tree.heading("ExID", text="ExID", anchor=W)
  my_tree.heading("Date", text="Date", anchor=CENTER)
  my_tree.heading("Answer", text="Answer", anchor=CENTER)
  my_tree.heading("Mark", text="Mark", anchor=CENTER )


#  Add Data

  conn_selectST = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
  cur_selectST = conn_selectST.cursor()
  cur_selectST.execute("select * from Answer")
  records = cur_selectST.fetchall()
  cur_selectST.close()
  conn_selectST.close()

#  create stripted rows

  my_tree.tag_configure('oddrow', background="white")
  my_tree.tag_configure('evenrow', background="lightblue")

# display our data on the screen

  global countt
  countt = 0
  for record in records:
      if countt % 2==0:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               record[5]), tags=('evenrow',))
      else:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               record[5]), tags=('oddnrow',))

      countt+=1




#define functions of new windows to show the  Department tables Dep Dep Dep Dep Dep Dep Dep Dep Dep Dep Dep Dep Dep Dep Dep Dep Dep Dep 

def Depfun():
  global depdata
  depdata = Toplevel(ins_2)
  depdata.title("Department Table")

  # add some style 

  style = ttk.Style()

#pick a theme 

  style.theme_use('default')

# configure the tree view colors

  style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")

# change the selected color
  style.map('Treeview', background = [('selected', '#347083')])

# create the tree view frame
  tree_frame = Frame(depdata)
  tree_frame.pack(pady=10)

# create the frame scrollbar

  scroll_frame = Scrollbar(tree_frame)
  scroll_frame.pack(side=RIGHT, fill = Y)

## create the tree view*****************

  my_tree = ttk.Treeview(tree_frame, yscrollcommand= scroll_frame.set, selectmode="extended")
  my_tree.pack()

# define the scrollbar

  scroll_frame.config(command=my_tree.yview)

# define our columns

  my_tree['columns'] = ("DeptID","DeptName","DeptDesc","DeptLocation","DeptInsID")
  my_tree.column("#0", width=0, stretch=NO)
  my_tree.column("DeptID", anchor=CENTER, width="50")
  my_tree.column("DeptName", anchor=W, width="100")
  my_tree.column("DeptDesc", anchor=W, width="100")
  my_tree.column("DeptLocation", anchor=CENTER, width="100")
  my_tree.column("DeptInsID", anchor=CENTER, width="50")
  


# define the heading of this column

  my_tree.heading("#0", text="", anchor=W)
  my_tree.heading("DeptID", text="ID", anchor=CENTER)
  my_tree.heading("DeptName", text="Name", anchor=W)
  my_tree.heading("DeptDesc", text="Description", anchor=W)
  my_tree.heading("DeptLocation", text="Location", anchor=CENTER)
  my_tree.heading("DeptInsID", text="InsID", anchor=CENTER)
  

#  Add Data

  conn_selectST = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
  cur_selectST = conn_selectST.cursor()
  cur_selectST.execute("select * from Department")
  records = cur_selectST.fetchall()
  cur_selectST.close()
  conn_selectST.close()

#  create stripted rows

  my_tree.tag_configure('oddrow', background="white")
  my_tree.tag_configure('evenrow', background="lightblue")

# display our data on the screen

  global countt
  countt = 0
  for record in records:
      if countt % 2==0:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               ), tags=('evenrow',))
      else:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               ), tags=('oddnrow',))

      countt+=1





#define functions of new windows to show the  Exam tables ExamExamExamExamExamExamExamExamExamExamExamExamExamExamExamExamExamExamExamExam

def Examfun():
  global examdata
  examdata = Toplevel(ins_2)
  examdata.title("Exam Table")

  # add some style 

  style = ttk.Style()

#pick a theme 

  style.theme_use('default')

# configure the tree view colors

  style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")

# change the selected color
  style.map('Treeview', background = [('selected', '#347083')])

# create the tree view frame
  tree_frame = Frame(examdata)
  tree_frame.pack(pady=10)

# create the frame scrollbar

  scroll_frame = Scrollbar(tree_frame)
  scroll_frame.pack(side=RIGHT, fill = Y)

## create the tree view*****************

  my_tree = ttk.Treeview(tree_frame, yscrollcommand= scroll_frame.set, selectmode="extended")
  my_tree.pack()

# define the scrollbar

  scroll_frame.config(command=my_tree.yview)

# define our columns

  my_tree['columns'] = ("ExID","ExTfNo","ExMcqNo","ExDate","ExInsID","ExCrsID")
  my_tree.column("#0", width=0, stretch=NO)
  my_tree.column("ExID", anchor=CENTER, width="50")
  my_tree.column("ExTfNo", anchor=W, width="50")
  my_tree.column("ExMcqNo", anchor=W, width="50")
  my_tree.column("ExDate", anchor=CENTER, width="200")
  my_tree.column("ExInsID", anchor=CENTER, width="50")
  my_tree.column("ExCrsID", anchor=CENTER, width="50")
  


# define the heading of this column

  my_tree.heading("#0", text="", anchor=W)
  my_tree.heading("ExID", text="ID", anchor=CENTER)
  my_tree.heading("ExTfNo", text="TfNo", anchor=W)
  my_tree.heading("ExMcqNo", text="McqNo", anchor=W)
  my_tree.heading("ExDate", text="Date", anchor=CENTER)
  my_tree.heading("ExInsID", text="InsID", anchor=CENTER)
  my_tree.heading("ExCrsID", text="CrsID", anchor=CENTER)

#  Add Data

  conn_selectST = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
  cur_selectST = conn_selectST.cursor()
  cur_selectST.execute("select * from Exam")
  records = cur_selectST.fetchall()
  cur_selectST.close()
  conn_selectST.close()

#  create stripted rows

  my_tree.tag_configure('oddrow', background="white")
  my_tree.tag_configure('evenrow', background="lightblue")

# display our data on the screen

  global countt
  countt = 0
  for record in records:
      if countt % 2==0:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               record[5]), tags=('evenrow',))
      else:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               record[5]), tags=('oddnrow',))

      countt+=1


#define functions of new windows to show the  ExamQuestion tables ExQuesExQuesExQuesExQuesExQuesExQuesExQuesExQuesExQuesExQuesExQuesExQues

def ExamQuesfun():
  global exquesdata
  exquesdata = Toplevel(ins_2)
  exquesdata.title("ExamQuestion Table")

  # add some style 

  style = ttk.Style()

#pick a theme 

  style.theme_use('default')

# configure the tree view colors

  style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")

# change the selected color
  style.map('Treeview', background = [('selected', '#347083')])

# create the tree view frame
  tree_frame = Frame(exquesdata)
  tree_frame.pack(pady=10)

# create the frame scrollbar

  scroll_frame = Scrollbar(tree_frame)
  scroll_frame.pack(side=RIGHT, fill = Y)

## create the tree view*****************

  my_tree = ttk.Treeview(tree_frame, yscrollcommand= scroll_frame.set, selectmode="extended")
  my_tree.pack()

# define the scrollbar

  scroll_frame.config(command=my_tree.yview)

# define our columns

  my_tree['columns'] = ("ExID","QID")
  my_tree.column("#0", width=0, stretch=NO)
  my_tree.column("ExID", anchor=CENTER, width="50")
  my_tree.column("QID", anchor=W, width="50")

# define the heading of this column

  my_tree.heading("#0", text="", anchor=W)
  my_tree.heading("ExID", text="EXID", anchor=CENTER)
  my_tree.heading("QID", text="QID", anchor=W)

#  Add Data

  conn_selectST = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
  cur_selectST = conn_selectST.cursor()
  cur_selectST.execute("select * from ExamQuestion")
  records = cur_selectST.fetchall()
  cur_selectST.close()
  conn_selectST.close()

#  create stripted rows

  my_tree.tag_configure('oddrow', background="white")
  my_tree.tag_configure('evenrow', background="lightblue")

# display our data on the screen

  global countt
  countt = 0
  for record in records:
      if countt % 2==0:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1]), tags=('evenrow',))
      else:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1]), tags=('oddnrow',))

      countt+=1


#define functions of new windows to show the  Instructor tables Ins Ins Ins Ins Ins Ins Ins Ins Ins Ins Ins Ins Ins Ins Ins Ins Ins Ins Ins 

def Insfun():
  global insdata
  insdata = Toplevel(ins_2)
  insdata.title("Instructor Table")

  # add some style 

  style = ttk.Style()

#pick a theme 

  style.theme_use('default')

# configure the tree view colors

  style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")

# change the selected color
  style.map('Treeview', background = [('selected', '#347083')])

# create the tree view frame
  tree_frame = Frame(insdata)
  tree_frame.pack(pady=10)

# create the frame scrollbar

  scroll_frame = Scrollbar(tree_frame)
  scroll_frame.pack(side=RIGHT, fill = Y)

## create the tree view*****************

  my_tree = ttk.Treeview(tree_frame, yscrollcommand= scroll_frame.set, selectmode="extended")
  my_tree.pack()

# define the scrollbar

  scroll_frame.config(command=my_tree.yview)

# define our columns

  my_tree['columns'] = ("InsID","InsFName","InsLName","InsCity","InsGender","InsPhone","InsEmail","InsDeptID")
  my_tree.column("#0", width=0, stretch=NO)
  my_tree.column("InsID", anchor=CENTER, width="50")
  my_tree.column("InsFName", anchor=W, width="100")
  my_tree.column("InsLName", anchor=W, width="100")
  my_tree.column("InsCity", anchor=CENTER, width="100")
  my_tree.column("InsGender", anchor=CENTER, width="50")
  my_tree.column("InsPhone", anchor=W, width="200")
  my_tree.column("InsEmail", anchor=CENTER, width="300")
  my_tree.column("InsDeptID", anchor=CENTER, width="50")


# define the heading of this column

  my_tree.heading("#0", text="", anchor=W)
  my_tree.heading("InsID", text="ID", anchor=CENTER)
  my_tree.heading("InsFName", text="First Name", anchor=W)
  my_tree.heading("InsLName", text="Last Name", anchor=W)
  my_tree.heading("InsCity", text="City", anchor=CENTER)
  my_tree.heading("InsGender", text="Gender", anchor=CENTER)
  my_tree.heading("InsPhone", text="Phone", anchor=W)
  my_tree.heading("InsEmail", text="Email", anchor=CENTER)
  my_tree.heading("InsDeptID", text="DeptID", anchor=CENTER)

#  Add Data

  conn_selectST = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
  cur_selectST = conn_selectST.cursor()
  cur_selectST.execute("select * from Instructor")
  records = cur_selectST.fetchall()
  cur_selectST.close()
  conn_selectST.close()

#  create stripted rows

  my_tree.tag_configure('oddrow', background="white")
  my_tree.tag_configure('evenrow', background="lightblue")

# display our data on the screen

  global countt
  countt = 0
  for record in records:
      if countt % 2==0:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               record[5], record[6], record[7]), tags=('evenrow',))
      else:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               record[5], record[6], record[7]), tags=('oddnrow',))

      countt+=1




#define functions of new windows to show the  QMcqChoice tables ChoiceChoiceChoiceChoiceChoiceChoiceChoiceChoiceChoiceChoiceChoiceChoice

def Choicefun():
  global choicedata
  choicedata = Toplevel(ins_2)
  choicedata.title("Choices Table")

  # add some style 

  style = ttk.Style()

#pick a theme 

  style.theme_use('default')

# configure the tree view colors

  style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")

# change the selected color
  style.map('Treeview', background = [('selected', '#347083')])

# create the tree view frame
  tree_frame = Frame(choicedata)
  tree_frame.pack(pady=10)

# create the frame scrollbar

  scroll_frame = Scrollbar(tree_frame)
  scroll_frame.pack(side=RIGHT, fill = Y)

## create the tree view*****************

  my_tree = ttk.Treeview(tree_frame, yscrollcommand= scroll_frame.set, selectmode="extended")
  my_tree.pack()

# define the scrollbar

  scroll_frame.config(command=my_tree.yview)

# define our columns

  my_tree['columns'] = ("QID","Choice")
  my_tree.column("#0", width=0, stretch=NO)
  my_tree.column("QID", anchor=CENTER, width="50")
  my_tree.column("Choice", anchor=W, width="300")
  

# define the heading of this column

  my_tree.heading("#0", text="", anchor=W)
  my_tree.heading("QID", text="QID", anchor=CENTER)
  my_tree.heading("Choice", text="Choices", anchor=W)
 
#  Add Data

  conn_selectST = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
  cur_selectST = conn_selectST.cursor()
  cur_selectST.execute("select * from QMcqChoice")
  records = cur_selectST.fetchall()
  cur_selectST.close()
  conn_selectST.close()

#  create stripted rows

  my_tree.tag_configure('oddrow', background="white")
  my_tree.tag_configure('evenrow', background="lightblue")

# display our data on the screen

  global countt
  countt = 0
  for record in records:
      if countt % 2==0:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1]), tags=('evenrow',))
      else:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1]), tags=('oddnrow',))

      countt+=1



#define functions of new windows to show the  Question table  Ques Ques Ques Ques Ques Ques Ques Ques Ques Ques Ques Ques Ques Ques Ques  
def Quesfun():
  global quesdata
  quesdata = Toplevel(ins_2)
  quesdata.title("Questions Table")

  # add some style 

  style = ttk.Style()

#pick a theme 

  style.theme_use('default')

# configure the tree view colors

  style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")

# change the selected color
  style.map('Treeview', background = [('selected', '#347083')])

# create the tree view frame
  tree_frame = Frame(quesdata)
  tree_frame.pack(pady=10)

# create the frame scrollbar

  scroll_frame = Scrollbar(tree_frame)
  scroll_frame.pack(side=RIGHT, fill = Y)

## create the tree view*****************

  my_tree = ttk.Treeview(tree_frame, yscrollcommand= scroll_frame.set, selectmode="extended")
  my_tree.pack()

# define the scrollbar

  scroll_frame.config(command=my_tree.yview)

# define our columns

  my_tree['columns'] = ("QID","QBody","QType","QModelAnswer","QCrsID")
  my_tree.column("#0", width=0, stretch=NO)
  my_tree.column("QID", anchor=CENTER, width="50")
  my_tree.column("QBody", anchor=W, width="300")
  my_tree.column("QType", anchor=W, width="100")
  my_tree.column("QModelAnswer", anchor=CENTER, width="50")
  my_tree.column("QCrsID", anchor=CENTER, width="50")
  


# define the heading of this column

  my_tree.heading("#0", text="", anchor=W)
  my_tree.heading("QID", text="ID", anchor=CENTER)
  my_tree.heading("QBody", text="Body", anchor=W)
  my_tree.heading("QType", text="Type", anchor=W)
  my_tree.heading("QModelAnswer", text="ModelAnswer", anchor=CENTER)
  my_tree.heading("QCrsID", text="CrsID", anchor=CENTER)
 

#  Add Data

  conn_selectST = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
  cur_selectST = conn_selectST.cursor()
  cur_selectST.execute("select * from Question")
  records = cur_selectST.fetchall()
  cur_selectST.close()
  conn_selectST.close()

#  create stripted rows

  my_tree.tag_configure('oddrow', background="white")
  my_tree.tag_configure('evenrow', background="lightblue")

# display our data on the screen

  global countt
  countt = 0
  for record in records:
      if countt % 2==0:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               ), tags=('evenrow',))
      else:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2], record[3], record[4],\
               ), tags=('oddnrow',))

      countt+=1




#define functions of new windows to show the  StudentCourse table StCrs StCrs StCrs StCrs StCrs StCrs StCrs StCrs StCrs StCrs StCrs StCrs 

def StCrsfun():
  global stcrsdata
  stcrsdata = Toplevel(ins_2)
  stcrsdata.title("StCrouse Table")

  # add some style 

  style = ttk.Style()

#pick a theme 

  style.theme_use('default')

# configure the tree view colors

  style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")

# change the selected color
  style.map('Treeview', background = [('selected', '#347083')])

# create the tree view frame
  tree_frame = Frame(stcrsdata)
  tree_frame.pack(pady=10)

# create the frame scrollbar

  scroll_frame = Scrollbar(tree_frame)
  scroll_frame.pack(side=RIGHT, fill = Y)

## create the tree view*****************

  my_tree = ttk.Treeview(tree_frame, yscrollcommand= scroll_frame.set, selectmode="extended")
  my_tree.pack()

# define the scrollbar

  scroll_frame.config(command=my_tree.yview)

# define our columns

  my_tree['columns'] = ("StID","CrsID","Grade")
  my_tree.column("#0", width=0, stretch=NO)
  my_tree.column("StID", anchor=CENTER, width="50")
  my_tree.column("CrsID", anchor=W, width="50")
  my_tree.column("Grade", anchor=W, width="100")
  


# define the heading of this column

  my_tree.heading("#0", text="", anchor=W)
  my_tree.heading("StID", text="StID", anchor=CENTER)
  my_tree.heading("CrsID", text="CrsID", anchor=W)
  my_tree.heading("Grade", text="Grade", anchor=W)
  

#  Add Data

  conn_selectST = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
  cur_selectST = conn_selectST.cursor()
  cur_selectST.execute("select * from StudentCourse")
  records = cur_selectST.fetchall()
  cur_selectST.close()
  conn_selectST.close()

#  create stripted rows

  my_tree.tag_configure('oddrow', background="white")
  my_tree.tag_configure('evenrow', background="lightblue")

# display our data on the screen

  global countt
  countt = 0
  for record in records:
      if countt % 2==0:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
      else:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2]), tags=('oddnrow',))

      countt+=1


#define functions of new windows to show the  Topics table  Topics Topics Topics Topics Topics Topics Topics Topics Topics Topics Topics

def Topicfun():
  global topicdata
  topicdata = Toplevel(ins_2)
  topicdata.title("Topics Table")

  # add some style 

  style = ttk.Style()

#pick a theme 

  style.theme_use('default')

# configure the tree view colors

  style.configure("Treeview", background = "#D3D3D3", foreground = "black", rowheight = 25, fieldbackground = "#D3D3D3")

# change the selected color
  style.map('Treeview', background = [('selected', '#347083')])

# create the tree view frame
  tree_frame = Frame(topicdata)
  tree_frame.pack(pady=10)

# create the frame scrollbar

  scroll_frame = Scrollbar(tree_frame)
  scroll_frame.pack(side=RIGHT, fill = Y)

## create the tree view*****************

  my_tree = ttk.Treeview(tree_frame, yscrollcommand= scroll_frame.set, selectmode="extended")
  my_tree.pack()

# define the scrollbar

  scroll_frame.config(command=my_tree.yview)

# define our columns

  my_tree['columns'] = ("TopID","TopName","TopCrsID")
  my_tree.column("#0", width=0, stretch=NO)
  my_tree.column("TopID", anchor=CENTER, width="50")
  my_tree.column("TopName", anchor=W, width="100")
  my_tree.column("TopCrsID", anchor=W, width="50")
  


# define the heading of this column

  my_tree.heading("#0", text="", anchor=W)
  my_tree.heading("TopID", text="ID", anchor=CENTER)
  my_tree.heading("TopName", text="Name", anchor=W)
  my_tree.heading("TopCrsID", text="CrsID", anchor=W)
  

#  Add Data

  conn_selectST = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
  cur_selectST = conn_selectST.cursor()
  cur_selectST.execute("select * from Topic")
  records = cur_selectST.fetchall()
  cur_selectST.close()
  conn_selectST.close()

#  create stripted rows

  my_tree.tag_configure('oddrow', background="white")
  my_tree.tag_configure('evenrow', background="lightblue")

# display our data on the screen

  global countt
  countt = 0
  for record in records:
      if countt % 2==0:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
      else:
          my_tree.insert(parent='', index='end', iid=countt, text='', values=(record[0], record[1], record[2]), tags=('oddnrow',))

      countt+=1


 






#><>>><><><><><><><><><><><><><><><><><><><><><><><><><><><><><<><><<><><<><><><><<>><>><><><><><><<>><>><><<><>><<<><>><<>><><><><><><<><><<>

# create the -----add----- student window

def add_student():
  global addst
  addst = Toplevel(ins_2)
  addst.iconbitmap("D:/BI_ITI/project/Exam_try/iti_logo.ico")
  addst.title("Add Student")
  addst.geometry("400x350")
  addst['bg'] = "#2a3439"
  #define the labels of the entry boxes
  StID_label = Label(addst, text = "ID", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StID_label.grid(row=0, column= 0)
  StFname_label = Label(addst, text = "Fname", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StFname_label.grid(row=1, column=0 )
  StLname_label = Label(addst, text = "Lname", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StLname_label.grid(row=2, column= 0)
  StAge_label = Label(addst, text = "Age", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StAge_label.grid(row=3, column= 0)
  StGender_label = Label(addst, text="Gender", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StGender_label.grid(row=4 , column=0)
  StCity_label = Label(addst, text = "City", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StCity_label.grid(row=5, column= 0)
  StEmail_label = Label(addst, text = "Email", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StEmail_label.grid(row=6, column=0 )
  StPhone_label = Label(addst, text = "Phone", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StPhone_label.grid(row=7, column= 0)
  StLink_label = Label(addst, text="Link",  font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StLink_label.grid(row=8, column=0)
  DepID_label = Label(addst, text = "DepID", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  DepID_label.grid(row=9, column= 0)

  #define the entry text box

  StID_ent = Entry(addst, width= 50, borderwidth= 5)
  StID_ent.grid(row= 0, column=1 )
  StFname_ent = Entry(addst, width= 50, borderwidth= 5)
  StFname_ent.grid(row= 1, column=1 )
  StLname_ent = Entry(addst, width= 50, borderwidth= 5)
  StLname_ent.grid(row= 2, column=1 )
  StAge_ent = Entry(addst, width= 50, borderwidth= 5)
  StAge_ent.grid(row= 3, column= 1)
  StGender_ent = Entry(addst, width= 50, borderwidth= 5)
  StGender_ent.grid(row= 4, column= 1)
  StCity_ent = Entry(addst, width= 50, borderwidth= 5)
  StCity_ent.grid(row= 5, column= 1)
  StEmail_ent = Entry(addst, width= 50, borderwidth= 5)
  StEmail_ent.grid(row= 6, column= 1)
  StPhone_ent = Entry(addst, width= 50, borderwidth= 5)
  StPhone_ent.grid(row= 7, column= 1)
  StLink_ent = Entry(addst, width= 50, borderwidth= 5)
  StLink_ent.grid(row= 8, column= 1)
  DepID_ent = Entry(addst, width= 50, borderwidth= 5)
  DepID_ent.grid(row= 9, column= 1)
  
  #Define a function take values about student
  def TakeValues():
    stid = StID_ent.get()
    global StID
    StID = stid
    stfname = StFname_ent.get()
    global StFname
    StFname = stfname
    stlname = StLname_ent.get()
    global StLname
    StLname = stlname
    stage = StAge_ent.get()
    global StAge
    StAge = stage
    stgender = StGender_ent.get()
    global StGender
    StGender = stgender
    stcity = StCity_ent.get()
    global StCity
    StCity = stcity
    stemail = StEmail_ent.get()
    global StEmail
    StEmail = stemail
    stphone = StPhone_ent.get()
    global StPhone
    StPhone = stphone
    stlink = StLink_ent.get()
    global StLink
    StLink = stlink
    depid = DepID_ent.get()
    global DepID
    DepID = depid  


  def submit():
    StID_ent.delete(0, END)
    StFname_ent.delete(0, END)
    StLname_ent.delete(0, END)
    StAge_ent.delete(0, END)
    StGender_ent.delete(0, END)
    StCity_ent.delete(0, END)
    StEmail_ent.delete(0, END)
    StPhone_ent.delete(0, END)
    StLink_ent.delete(0, END)
    DepID_ent.delete(0, END)

  def Queryfun():
    conn_insert = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_insert = conn_insert.cursor()
    cursor_insert.execute(f"INSERT INTO student VALUES ({StID}, {StFname}, {StLname}, {StAge}, {StGender}, {StCity}, {StEmail}, {StPhone}, {StLink}, {DepID})")
    cursor_insert.commit()
    conn_insert.close()

  btn_submit = Button(addst, text = "Submit", font=('Arial 12 bold'),fg="black", bg="#E6E6FA",command = lambda : [TakeValues(), Queryfun(), submit()])
  btn_submit.grid(row= 10, column= 1 ,pady= 15)

#><>>><><><><><><><><><><><><><><><><><><><><><><><><><><><><><<><><<><><<><><><><<>><>><><><><><><<>><>><><<><>><<<><>><<>><><><><><><<><><<>


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#create the ---update---- student window
def update_student():
  global updatest
  updatest = Toplevel(ins_2)
  updatest.iconbitmap("D:/BI_ITI/project/Exam_try/iti_logo.ico")
  updatest.title("Updete Student")
  updatest.geometry("700x500")
  updatest['bg'] = "#2a3439"

  label_enter_id = Label(updatest, text="Enter StudentID", font=('Arial 12 bold'), fg='White', bg="#2a3439")
  label_enter_id.grid(row=0, column=1)

  e_stid_update = Entry(updatest, borderwidth=10)
  e_stid_update.grid(row= 0, column=2)

  StID_label = Label(updatest, text = "StID", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StID_label.grid(row=2, column= 0)
  StFname_label = Label(updatest, text = "StFname", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StFname_label.grid(row=3, column=0 )
  StLname_label = Label(updatest, text = "StLname", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StLname_label.grid(row=4, column= 0)
  StAge_label = Label(updatest, text = "StAge", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StAge_label.grid(row=5, column= 0)
  StGender_label = Label(updatest, text = "StGender", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StGender_label.grid(row=6, column= 0)
  StCity_label = Label(updatest, text = "StCity", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StCity_label.grid(row=7, column= 0)
  StEmail_label = Label(updatest, text = "StEmail", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StEmail_label.grid(row=8, column=0 )
  StPhone_label = Label(updatest, text = "StPhone", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StPhone_label.grid(row=9, column= 0)
  StLink_label = Label(updatest, text = "StLink", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StLink_label.grid(row=10, column= 0)
  DepID_label = Label(updatest, text = "DepID", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  DepID_label.grid(row=11, column= 0)

  btn_view_old = Button(updatest, text= "view", font=('Arial 12 bold'), fg="blue", bg="#E6E6FA", command =lambda: [textid.insert(END,StID_values()),\
     textfname.insert(END,StFname_values()), textlname.insert(END,StLname_values()), textage.insert(END,StAge_values()),\
       textgender.insert(END,StGender_values()), textcity.insert(END,StCity_values()),textemail.insert(END,StEmail_values()),\
         textphone.insert(END,StPhone_values()), textlink.insert(END,StLink_values()), textdep.insert(END,DepID_values())])
  btn_view_old.grid(row=1, column=0)
  
  textid = Text(updatest, width=25, height=1)
  textid.grid(row=2, column=1)
  
  def StID_values():
    global St_up_ID
    St_up_ID = e_stid_update.get()
    conn_old = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_old = conn_old.cursor()
    cursor_old.execute(f"SELECT StID FROM Student WHERE StID = {St_up_ID}")
    recordid = cursor_old.fetchall()
    conn_old.close()
    print_recordid = ''
    for x in recordid:
      print_recordid = print_recordid+str(x[0])+" "
    return print_recordid

  textfname = Text(updatest, width=25, height=1)
  textfname.grid(row=3, column=1)

  def StFname_values():
    conn_old = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_old = conn_old.cursor()
    cursor_old.execute(f"SELECT StFname FROM Student WHERE StID = {St_up_ID}")
    recordfname = cursor_old.fetchall()
    conn_old.close()
    print_recordfname = ''
    for x in recordfname:
      print_recordfname = print_recordfname+str(x[0])+" "
    global stfnameup
    stfnameup =str(print_recordfname)
    return print_recordfname
    

  
  textlname = Text(updatest, width=25, height=1)
  textlname.grid(row=4, column=1)

  def StLname_values():
    conn_old = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_old = conn_old.cursor()
    cursor_old.execute(f"SELECT StLname FROM Student WHERE StID = {St_up_ID}")
    recordlname = cursor_old.fetchall()
    conn_old.close()
    print_recordlname = ''
    for x in recordlname:
      print_recordlname = print_recordlname+str(x[0])+" "
    return print_recordlname
    

  textage = Text(updatest, width=25, height=1)
  textage.grid(row=5, column=1)

  def StAge_values():
    global St_up_ID
    St_up_ID = e_stid_update.get()
    conn_old = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_old = conn_old.cursor()
    cursor_old.execute(f"SELECT StAge FROM Student WHERE StID = {St_up_ID}")
    recordage = cursor_old.fetchall()
    conn_old.close()
    print_recordage = ''
    for x in recordage:
      print_recordage = print_recordage+str(x[0])+" "
    return print_recordage
    
  
  textgender = Text(updatest, width=25, height=1)
  textgender.grid(row=6, column=1)

  def StGender_values():
    global St_up_ID
    St_up_ID = e_stid_update.get()
    conn_old = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_old = conn_old.cursor()
    cursor_old.execute(f"SELECT StGender FROM Student WHERE StID = {St_up_ID}")
    recordgender = cursor_old.fetchall()
    conn_old.close()
    print_recordgender = ''
    for x in recordgender:
      print_recordgender = print_recordgender+str(x[0])+" "
    return print_recordgender
    


  textcity = Text(updatest, width=25, height=1)
  textcity.grid(row=7, column=1)

  def StCity_values():
    global St_up_ID
    St_up_ID = e_stid_update.get()
    conn_old = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_old = conn_old.cursor()
    cursor_old.execute(f"SELECT StCity FROM Student WHERE StID = {St_up_ID}")
    recordcity = cursor_old.fetchall()
    conn_old.close()
    print_recordcity = ''
    for x in recordcity:
      print_recordcity = print_recordcity+str(x[0])+" "
    return print_recordcity
    
  
  textemail = Text(updatest, width=25, height=1)
  textemail.grid(row=8, column=1)


  def StEmail_values():
    global St_up_ID
    St_up_ID = e_stid_update.get()
    conn_old = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_old = conn_old.cursor()
    cursor_old.execute(f"SELECT StEmail FROM Student WHERE StID = {St_up_ID}")
    recordemail = cursor_old.fetchall()
    conn_old.close()
    print_recordemail = ''
    for x in recordemail:
      print_recordemail = print_recordemail+str(x[0])+" "
    return print_recordemail
   
  
  textphone = Text(updatest, width=25, height=1)
  textphone.grid(row=9, column=1)

  def StPhone_values():
    global St_up_ID
    St_up_ID = e_stid_update.get()
    conn_old = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_old = conn_old.cursor()
    cursor_old.execute(f"SELECT StPhone FROM Student WHERE StID = {St_up_ID}")
    recordphone = cursor_old.fetchall()
    conn_old.close()
    print_recordphone = ''
    for x in recordphone:
      print_recordphone = print_recordphone+str(x[0])+" "
    return print_recordphone
    
  
  textlink = Text(updatest, width=25, height=1)
  textlink.grid(row=10, column=1)

  def StLink_values():
    global St_up_ID
    St_up_ID = e_stid_update.get()
    conn_old = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_old = conn_old.cursor()
    cursor_old.execute(f"SELECT StLink FROM Student WHERE StID = {St_up_ID}")
    recordlink = cursor_old.fetchall()
    conn_old.close()
    print_recordlink = ''
    for s in recordlink:
      print_recordlink = print_recordlink+str(s[0])
    return print_recordlink
    

  
  
  textdep = Text(updatest, width=25, height=1)
  textdep.grid(row=11, column=1)
  
  def DepID_values():
    conn_old = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_old = conn_old.cursor()
    cursor_old.execute(f"SELECT StDeptID FROM Student WHERE StID = {St_up_ID}")
    record8 = cursor_old.fetchall()
    conn_old.close()
    print_record = ''
    for y in record8:
      print_record = print_record+str(y[0])+" "
    return print_record
  
  

  label_updateto = Label(updatest, text="Update to ->", font=('Arial 8 bold') ,  fg="black", bg="#E6E6FA")
  label_updateto.grid(row=2, column=2)
  label_updateto = Label(updatest, text="Update to ->", font=('Arial 8 bold'),  fg="black", bg="#E6E6FA")
  label_updateto.grid(row=3, column=2)
  label_updateto = Label(updatest, text="Update to ->", font=('Arial 8 bold'),  fg="black", bg="#E6E6FA")
  label_updateto.grid(row=4, column=2)
  label_updateto = Label(updatest, text="Update to ->", font=('Arial 8 bold'),  fg="black", bg="#E6E6FA")
  label_updateto.grid(row=5, column=2)
  label_updateto = Label(updatest, text="Update to ->", font=('Arial 8 bold'),  fg="black", bg="#E6E6FA")
  label_updateto.grid(row=6, column=2)
  label_updateto = Label(updatest, text="Update to ->", font=('Arial 8 bold'),  fg="black", bg="#E6E6FA")
  label_updateto.grid(row=7, column=2)
  label_updateto = Label(updatest, text="Update to ->", font=('Arial 8 bold'),  fg="black", bg="#E6E6FA")
  label_updateto.grid(row=8, column=2)
  label_updateto = Label(updatest, text="Update to ->", font=('Arial 8 bold'),  fg="black", bg="#E6E6FA")
  label_updateto.grid(row=9, column=2)
  label_updateto = Label(updatest, text="Update to ->", font=('Arial 8 bold'),  fg="black", bg="#E6E6FA")
  label_updateto.grid(row=10, column=2)
  label_updateto = Label(updatest, text="Update to ->", font=('Arial 8 bold'),  fg="black", bg="#E6E6FA")
  label_updateto.grid(row=11, column=2)


  StID_label = Label(updatest, text = "StID", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StID_label.grid(row=2, column= 3)
  StFname_label = Label(updatest, text = "StFname", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StFname_label.grid(row=3, column=3 )
  StLname_label = Label(updatest, text = "StLname", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StLname_label.grid(row=4, column= 3)
  StAge_label = Label(updatest, text = "StAge", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StAge_label.grid(row=5, column= 3)
  StGender_label = Label(updatest, text = "StGender", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StGender_label.grid(row=6, column= 3)
  StCity_label = Label(updatest, text = "StCity", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StCity_label.grid(row=7, column= 3)
  StEmail_label = Label(updatest, text = "StEmail", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StEmail_label.grid(row=8, column=3 )
  StPhone_label = Label(updatest, text = "StPhone", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StPhone_label.grid(row=9, column= 3)
  StLink_label = Label(updatest, text = "StLink", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  StLink_label.grid(row=10, column= 3)
  DepID_label = Label(updatest, text = "DepID", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  DepID_label.grid(row=11, column= 3)




  StID_entup = Entry(updatest, width= 30, borderwidth= 5)
  StID_entup.grid(row= 2, column=4 )
  StFname_entup = Entry(updatest, width= 30, borderwidth= 5)
  StFname_entup.grid(row= 3, column=4 )
  StLname_entup = Entry(updatest, width= 30, borderwidth= 5)
  StLname_entup.grid(row= 4, column=4 )
  StAge_entup = Entry(updatest, width= 30, borderwidth= 5)
  StAge_entup.grid(row= 5, column= 4)
  StGender_entup = Entry(updatest, width= 30, borderwidth= 5)
  StGender_entup.grid(row= 6, column= 4)
  StCity_entup = Entry(updatest, width= 30, borderwidth= 5)
  StCity_entup.grid(row= 7, column= 4)
  StEmail_entup = Entry(updatest, width= 30, borderwidth= 5)
  StEmail_entup.grid(row= 8, column= 4)
  StPhone_entup = Entry(updatest, width= 30, borderwidth= 5)
  StPhone_entup.grid(row= 9, column= 4)
  StLink_entup = Entry(updatest, width= 30, borderwidth= 5)
  StLink_entup.grid(row= 10, column= 4)
  DepID_entup = Entry(updatest, width= 30, borderwidth= 5)
  DepID_entup.grid(row= 11, column= 4)

  def updatestid():
    global stidup
    stidup = StID_entup.get()
    conn_new = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_new = conn_new.cursor()
    cursor_new.execute(f"UPDATE Student SET StID = {stidup} WHERE StID = {St_up_ID}")
    cursor_new.commit()
    conn_new.close()
    
  
  def updatestfname():
    stfnameup = StFname_entup.get()
    conn_new = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_new = conn_new.cursor()
    cursor_new.execute(f"UPDATE Student SET StFname = {stfnameup} WHERE StID = {St_up_ID}")
    cursor_new.commit()
    conn_new.close()

  def updatestlname():
    global stlnameup
    stlnameup = StLname_entup.get()
    conn_new = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_new = conn_new.cursor()
    cursor_new.execute(f"UPDATE Student SET StLname = {stlnameup} WHERE StID = {St_up_ID}")
    cursor_new.commit()
    conn_new.close()

  def updatestage():
    global stageup
    stageup = StAge_entup.get()
    conn_new = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_new = conn_new.cursor()
    cursor_new.execute(f"UPDATE Student SET StAge = {stageup} WHERE StID = {St_up_ID}")
    cursor_new.commit()
    conn_new.close()

  def updatestgender():
    global stgenderup
    stgenderup = StGender_entup.get()
    conn_new = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_new = conn_new.cursor()
    cursor_new.execute(f"UPDATE Student SET StGender = {stgenderup} WHERE StID = {St_up_ID}")
    cursor_new.commit()
    conn_new.close()
  

  def updatestcity():
    global stcityup
    stcityup = StCity_entup.get()
    conn_new = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_new = conn_new.cursor()
    cursor_new.execute(f"UPDATE Student SET StCity = {stcityup} WHERE StID = {St_up_ID}")
    cursor_new.commit()
    conn_new.close()

  def updatestemail():
    global stemailup
    stemailup = StEmail_entup.get()
    conn_new = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_new = conn_new.cursor()
    cursor_new.execute(f"UPDATE Student SET StEmail = {stemailup} WHERE StID = {St_up_ID}")
    cursor_new.commit()
    conn_new.close()

  def updatestphone():
    global stphoneup
    stphoneup = StPhone_entup.get()
    conn_new = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_new = conn_new.cursor()
    cursor_new.execute(f"UPDATE Student SET StPhone = {stphoneup} WHERE StID = {St_up_ID}")
    cursor_new.commit()
    conn_new.close()

  def updatestLink():
    global stlinkup
    stlinkup = StLink_entup.get()
    conn_new = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_new = conn_new.cursor()
    cursor_new.execute(f"UPDATE Student SET StLink = {stlinkup} WHERE StID = {St_up_ID}")
    cursor_new.commit()
    conn_new.close()

  def updatedepid():
    global depidup
    depidup = DepID_entup.get()
    conn_new = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_new = conn_new.cursor()
    cursor_new.execute(f"UPDATE Student SET StDeptID = {depidup} WHERE StID = {St_up_ID}")
    cursor_new.commit()
    conn_new.close()

  def emptyup():
    StID_entup.delete(0, END)
    StFname_entup.delete(0, END)
    StLname_entup.delete(0, END)
    StAge_entup.delete(0, END)
    StGender_entup.delete(0, END)
    StCity_entup.delete(0, END)
    StEmail_entup.delete(0, END)
    StPhone_entup.delete(0, END)
    StLink_entup.delete(0, END)
    DepID_entup.delete(0, END)
    textid.delete(1.0,END)
    textfname.delete(1.0,END)
    textlname.delete(1.0,END)
    textage.delete(1.0,END)
    textgender.delete(1.0,END)
    textcity.delete(1.0,END)
    textemail.delete(1.0,END)
    textphone.delete(1.0,END)
    textlink.delete(1.0,END)
    textdep.delete(1.0,END)
    e_stid_update.delete(0,END)



  btn_update = Button(updatest, text= "Update", font=('Arial 14 bold'),  fg="blue", bg="#E6E6FA", command=lambda\
     :[updatestfname(), updatestlname(), updatestage()\
      , updatestgender(), updatestcity(), updatestemail(), updatestphone(), updatestLink(), updatedepid(), updatestid(), emptyup()])
  btn_update.grid(row= 12, column=4, pady=20)
  



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#create the ---delete--- student window

def delete_student():
  global deletest
  deletest = Toplevel(ins_2)
  deletest.iconbitmap("D:/BI_ITI/project/Exam_try/iti_logo.ico")
  deletest.title("Delete Student")
  deletest.geometry("620x250")
  deletest['bg'] = "#2a3439"

  label_message = Label(deletest, text= "Please, Enter the Student ID", font=('Arial 14 bold'),  fg="black", bg="#E6E6FA")
  label_message.grid(row= 0 , column= 1, padx= 20 , pady= 10)
  label_stid = Label(deletest, text= "StID", font=('Arial 12 bold'), fg='White', bg="#2a3439")
  label_stid.grid(row= 1, column= 0, padx= 30, pady=10)
  
  e_stid = Entry(deletest, borderwidth=5, width=50)
  e_stid.grid(row=1, column=1, pady=10)
  
  def stidfun():
    global StID_deleted
    StID_deleted = e_stid.get()

  btn_view = Button(deletest, text= "View", fg="blue", bg="#E6E6FA", font=('Arial 14 bold'), command= lambda : [stidfun(), textst.insert(END,stwilldeleted())])
  btn_view.grid(row= 2, column= 1, pady=10)
  
  textst = Text(deletest, height=1, width=110,font=('Arial 8'), bg="#2a3439", fg="white")
  textst.grid(row=3, column=0,columnspan=6,padx=5, pady=10)

  def stwilldeleted():
    conn_insert = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_insert = conn_insert.cursor()
    cursor_insert.execute(f"SELECT * FROM Student WHERE StID = {StID_deleted}")
    records = cursor_insert.fetchall()
    cursor_insert.close()
    conn_insert.close()
    print_records = ''
    for record in records[0]:
      print_records += str(record) + " | "
    return print_records

    # label_view = Label(deletest, text= print_records )
    # label_view.grid(row= 3, column= 0, columnspan= 3, padx= 20, pady=20)
  
  def deletefun():
    conn_delete = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_delete = conn_delete.cursor()
    cursor_delete.execute(f"DELETE FROM Student WHERE StID = {StID_deleted}")
    cursor_delete.commit()
    conn_delete.close()
    e_stid.delete(0, END)
    textst.delete(1.0,END)
    


  btn_delete = Button(deletest, text= "Delete", fg="blue", bg="#E6E6FA", font=('Arial 14 bold'), command=lambda :[deletefun()])
  btn_delete.grid(row= 4 ,column= 1)




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#create the window of create exam

def create_exam():
  global CreateExam
  CreateExam = Toplevel(ins_2)
  CreateExam.iconbitmap("D:/BI_ITI/project/Exam_try/iti_logo.ico")
  CreateExam.title("Create Exam")
  CreateExam.geometry("500x300")
  CreateExam['bg'] = "#2a3439"
  
  label_exinfo = Label(CreateExam, text="Enter the New Exam Info.", font=('Arial 14 bold'), fg="black", bg="#E6E6FA")
  label_exinfo.grid(row=0, column=0, columnspan= 2, pady=10)

  label_exmcq = Label(CreateExam, text="MCQ_Num", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  label_exmcq.grid(row=1, column=0)

  label_extfq = Label(CreateExam, text="TFQ_Num", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  label_extfq.grid(row=2, column=0)

  label_crsname = Label(CreateExam, text="Course_Name", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  label_crsname.grid(row=3, column=0)


  e_exmcq = Entry(CreateExam, width=10, borderwidth=5)
  e_exmcq.grid(row=1, column=1)

  e_extfq = Entry(CreateExam, width=10, borderwidth=5)
  e_extfq.grid(row=2, column=1)

  e_crsname = Entry(CreateExam, width=10, borderwidth=5)
  e_crsname.grid(row=3, column=1)

  btn_createEx = Button(CreateExam, text="Create", font=('Arial 14 bold'), fg="blue", bg="#E6E6FA", command= lambda :[createfun(), emptycreate(),text_newex.insert(END, ExamCreated())])
  btn_createEx.grid(row= 2 , column=2, padx=20)

  text_newex = Text(CreateExam, width=60, height=1,  bg="#2a3439", fg="white", font=('Arial 10 bold'))
  text_newex.grid(row=4, column=0, columnspan=3, padx=10, pady=10)


  def createfun():
    mcqNum = e_exmcq.get()
    tfqNum = e_extfq.get()
    crsName = e_crsname.get()
    conn_create = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_create = conn_create.cursor()
    cursor_create.execute(f"createExam {mcqNum},{tfqNum},{crsName}")
    cursor_create.commit()
    conn_create.close()

  def ExamCreated():
    conn_created = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cursor_created = conn_created.cursor()
    cursor_created.execute("select top(1) * from Exam order by ExID desc")
    records = cursor_created.fetchall()
    cursor_created.close()
    conn_created.close()
    print_records = ''
    for record in records[0]:
      print_records += str(record) + "   |   "
    return print_records

  def emptycreate():
    e_exmcq.delete(0, END)
    e_extfq.delete(0, END)
    e_crsname.delete(0, END)



#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Exam correction :
def ExamCorrection():
  global CorrectExam
  CorrectExam = Toplevel(ins_2)
  CorrectExam.iconbitmap("D:/BI_ITI/project/Exam_try/iti_logo.ico")
  CorrectExam.title("Exam Correction")
  CorrectExam.geometry("500x300")
  CorrectExam['bg'] = "#2a3439"
  

  label_enter = Label(CorrectExam, text="Enter the : ", font=('Arial 14 bold'), fg="black", bg="#E6E6FA")
  label_enter.grid(row=0, column=0, columnspan= 2, pady=10)

  label_stid = Label(CorrectExam, text="StID", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  label_stid.grid(row=1, column=0)

  label_exid = Label(CorrectExam, text="ExID", font=('Arial 10 bold'), fg='White', bg="#2a3439")
  label_exid.grid(row=2, column=0)

  e_stid = Entry(CorrectExam, width=10, borderwidth=5)
  e_stid.grid(row=1, column=1)

  e_exid = Entry(CorrectExam, width=10, borderwidth=5)
  e_exid.grid(row=2, column=1)
  
  textco = Text(CorrectExam, height=2, width=10,  font=('Arial 10 bold'))
  textco.grid(row= 2, column=3, columnspan=2)

  btn_correctEx = Button(CorrectExam, text="Grade", font=('Arial 14 bold'), fg="blue", bg="#E6E6FA", command= lambda : textco.insert(END,getgradefun()))
  btn_correctEx.grid(row= 2 , column=2, padx=20)

  

   
  
  def getgradefun():
    global StID_Correct
    StID_Correct = e_stid.get()
    global ExID_Correct
    ExID_Correct = e_exid.get()
    
    conn_cor = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6FGK6F0;DATABASE=ExamSystem;Trusted_connection=yes;')
    cur_cor = conn_cor.cursor()
    cur_cor.execute(f"ExamCorrection {StID_Correct}, {ExID_Correct}")
    grades = cur_cor.fetchall()
    cur_cor.close()
    conn_cor.close()
    output = ''
    for x in grades:
      output = output+str(grades[0][0])+' '+'%'
    return output
 
# make function to but mark

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# create window to display reports images

def Examreports():
  reportat = Toplevel(ins_2)
  reportat.title("Reports")
  #reportat.geometry("900x700")
  
  my_img1 = ImageTk.PhotoImage(Image.open("H:/Exam_try/reports_images/1.JPG"))
  my_img2 = ImageTk.PhotoImage(Image.open("H:/Exam_try/reports_images/2.JPG"))
  my_img3 = ImageTk.PhotoImage(Image.open("H:/Exam_try/reports_images/3.JPG"))
  my_img4 = ImageTk.PhotoImage(Image.open("H:/Exam_try/reports_images/4.JPG"))

  img_list = [my_img1, my_img2, my_img3, my_img4]

  global img_label
  global btn_back
  global btn_next

  img_label = Label(reportat, image=my_img1)
  img_label.image = my_img1
  img_label.grid(row=0, column=0, columnspan=3)

  def next(img_num):
    global img_label
    global btn_back
    global btn_next
    
    img_label.grid_forget()

    img_label = Label(reportat, image=img_list[img_num])

    btn_next = Button(reportat, text=">>",bg="black", fg="blue", command=lambda:next(img_num+1))
    
    btn_back = Button(reportat, text="<<", bg="black", fg="blue", command=lambda: back(img_num-1))
     
    
    img_label.grid(row=0, column=0, columnspan=3)
    btn_next.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)






  def back(img_num):
    global img_label
    global btn_back
    global btn_next
  

    img_label.grid_forget()

    img_label = Label(reportat, image=img_list[img_num])

    btn_next = Button(reportat, text=">>",bg="black", fg="blue", command=lambda:next(img_num+1))
    if img_num == 3:
      btn_next = Button(reportat, text=">>",bg="black", fg="blue", state=DISABLED)
      btn_next.grid(row=1, column=2)
    btn_back = Button(reportat, text="<<", bg="black", fg="blue", command=lambda: back(img_num-1))
     
    

    img_label.grid(row=0, column=0, columnspan=3)
    btn_next.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)



 





  btn_back = Button(reportat, text="<<", bg="black", fg="blue", command= back) 
  btn_exit = Button(reportat, text="Exit",bg="black", fg="blue", command=reportat.quit) 
  btn_next = Button(reportat, text=">>",bg="black", fg="blue", command=lambda:next(1)) 
  btn_back.grid(row=1, column=0)
  btn_exit.grid(row=1, column=1)
  btn_next.grid(row=1, column=2)

#*****************************************************************************************************************************

# create the main window widgets 

label_welcome = Label(root, text="Welcome to you in our Exam System", font=('Arial 17 bold'), fg= "black", bg="#E6E6FA")
label_welcome.grid(row= 1, column=1, columnspan= 5, padx= 40, pady=30)

label_tell = Label(root, text= "Please; Tell Us Are you a :",font=('Arial 16 bold'), fg="black",bg="#E6E6FA")
label_tell.grid(row= 3, column= 1 , columnspan= 5, padx= 30, pady=20)

btn_instructor = Button(root, text= "Instructor", font=('Arial', 16), fg="blue", bg="#E6E6FA", command= openinstructor_1)
btn_instructor.grid(row=5, column= 1, columnspan= 5)

btn_student = Button(root, text= "Student", font=('Arial', 16), fg="blue" , bg="#E6E6FA", command=lambda :[ openstudent_1()])
btn_student.grid(row=6, column= 1, columnspan= 5)



root.mainloop()
