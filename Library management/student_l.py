import pymysql

class student:
    def __init__(self):
        self.__servername="localhost"
        self.__username="root"
        self.__password=""
        self.__dbname="library1"
        try:
            self.con=pymysql.connect(self.__servername,self.__username,self.__password,self.__dbname)
            print("connection successfull")
        except:
            print("Connection Error")
    def add(self):
        self.libid=int(input("\t\t Enter library id of student :"))
        self.regno=int(input("\t\t Enter registration no of student :"))
        self.b=input ("\t\t Enter branch of student :")
        self.section=input ("\t\t Enter section of student :")
        self.sem=input ("\t\t Enter semester of student :")
        self.c=int(input("\t\t Enter contact of student :"))
        query="insert into student(libid,regno,branch,section,semester,contact) values(%s,%s,%s,%s,%s,%s)"
        val=(self.libid,self.regno,self.b,self.section,self.sem,self.c)
        cur=self.con.cursor()
        try:
            cur.execute(query,val)
        except:
            print("Error in the query")

        else:
            self.con.commit()
            print("\t\t\tRecord Insert Successfully ")
            print("")

    def show(self):
        query="select * from student"
        cur=self.con.cursor() #prepared cursor
        try:
            cur.execute(query) #run select query
            result=cur.fetchall()
            print(result)
        except:
            print("Record not found")

    def update(self):        
        self.libid=int(input ("\t\t\tEnter library id for UPDATE  : "))
        print("\t\t\t1. Update branch \n\t\t\t2. Update section \n\t\t\t3. Update semester \n\t\t\t4. Update contact \n\t\t\t5.Exit ")
        while(True):
            print("\t\t\t=====================================")
            ch=int(input("\t\t\tEnter your Choice for Updation   : "))
            print("\t\t\t=====================================")
            if(ch==1):
                self.b=input("\t\t\tEnter updated branch         :")
                query="update student set branch=%s where code=%s"
                cur=self.con.cursor()
                val=(self.bn,self.b)
                try:
                    cur.execute(query,val)
                    self.con.commit()
                    print("\t\t\t -- Branch is Updated -- ")
                except:
                    print("\t\t\t Oops ,Record Not Found !")
            if(ch==2):
                self.section=input("\t\t\tEnter updated section      : ")
                query="update student set section=%s where code=%s"
                cur=self.con.cursor()
                val=(self.a,self.section)
                try:
                    cur.execute(query,val)
                    self.con.commit()
                    print(" \t\t\t-- Section is Updated --")                              
                except:
                    print(" \t\t\tOops ,Record Not Found !")
            if(ch==3):
                self.sem=input("\t\t\tEnter updated semester  : ")
                query="update student set semester=%s where code=%s"
                cur=self.con.cursor()
                val=(self.pb,self.sem)
                try:
                    cur.execute(query,val)
                    self.con.commit()
                    print(" \t\t\t-- Semester is Updated --")
                except:
                    print("\t\t\t Oops ,Record Not Found !")
            if(ch==4):
                self.c=input("\t\t\tEnter updated contact of student  : ")
                query="update student set contact=%s where code=%s"
                cur=self.con.cursor()
                val=(self.sub,self.c)
                try:
                    cur.execute(query,val)
                    self.con.commit()
                    print("\t\t\t     -- subject is Updated -- ")
                except:
                    print("\t\t\t Oops ,Record Not Found !")

            if(ch==5):  
                print("\t\t\t           -- All Updation Done -- ")
                break
    def delete(self):
        self.libid=int(input ("\t\t\tEnter Library id for Delete  : "))
        query="Delete from student WHERE code=%s"
        cur=self.con.cursor()
        try:
            cur.execute(query,self.libid)
        except:
            print("\t\t\t Record not Found ")
        else:
            self.con.commit()
            print("\t\t\t Record Deleted Successfully")
            print("\t\t\t")
    def __del__(self):
            self.con.close()
            print("\t\t\t\tGood Day")
            print("\t\t\t *******  Thank You  ******* ")













            
