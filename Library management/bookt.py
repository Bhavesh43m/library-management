import pymysql

class library:
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
        self.c=int(input("\t\t Enter book code :"))
        self.bn=input("\t\t Enter book name :")
        self.a=input ("\t\t Enter book auther name :")
        self.pb=input ("\t\t Enter book publication :")
        self.sub=input ("\t\t Enter subject :")
        self.cn=int(input("\t\t Enter book copy numbers :"))
        query="insert into books(code,bookname,auther,publication,subject,copy_no) values(%s,%s,%s,%s,%s,%s)"
        val=(self.c,self.bn,self.a,self.pb,self.sub,self.cn)
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
        query="select * from books"
        cur=self.con.cursor() #prepared cursor
        try:
            cur.execute(query) #run select query
            result=cur.fetchall()
            print(result)
        except:
            print("Record not found")

    def update(self):        
        self.c=int(input ("\t\t\tEnter Book Code for UPDATE  : "))
        print("\t\t\t1. Update Book name \n\t\t\t2. Update Auther name\n\t\t\t3. Update publication \n\t\t\t4. Update subject \n\t\t\t5.Update number of copies\n\t\t\t6.Exit ")
        while(True):
            print("\t\t\t=====================================")
            ch=int(input("\t\t\tEnter your Choice for Updation   : "))
            print("\t\t\t=====================================")
            if(ch==1):
                self.bn=input("\t\t\tEnter updated book name         :")
                query="update books set bookname=%s where code=%s"
                cur=self.con.cursor()
                val=(self.bn,self.c)
                try:
                    cur.execute(query,val)
                    self.con.commit()
                    print("\t\t\t -- Book name is Updated -- ")
                except:
                    print("\t\t\t Oops ,Record Not Found !")
            if(ch==2):
                self.a=input("\t\t\tEnter updated auther name      : ")
                query="update books set auther=%s where code=%s"
                cur=self.con.cursor()
                val=(self.a,self.c)
                try:
                    cur.execute(query,val)
                    self.con.commit()
                    print(" \t\t\t-- Auther is Updated --")                              
                except:
                    print(" \t\t\tOops ,Record Not Found !")
            if(ch==3):
                self.pb=input("\t\t\tEnter updated book publication  : ")
                query="update books set publication=%s where code=%s"
                cur=self.con.cursor()
                val=(self.pb,self.c)
                try:
                    cur.execute(query,val)
                    self.con.commit()
                    print(" \t\t\t-- Publication is Updated --")
                except:
                    print("\t\t\t Oops ,Record Not Found !")
            if(ch==4):
                self.adr=input("\t\t\tEnter updated subject of book  : ")
                query="update books set subject=%s where code=%s"
                cur=self.con.cursor()
                val=(self.sub,self.c)
                try:
                    cur.execute(query,val)
                    self.con.commit()
                    print("\t\t\t     -- subject is Updated -- ")
                except:
                    print("\t\t\t Oops ,Record Not Found !")
            if(ch==5):
                self.cn=int(input("\t\t\tEnter New count of Copies  : "))
                query="update studentadm set copy_no=%s where code=%s"
                cur=self.con.cursor()
                val=(self.cn,self.c)
                try:
                    cur.execute(query,val)
                    self.con.commit()
                    print("\t\t\t     -- count of books  is Updated -- ")
                except:
                    print("\t\t\t Oops ,Record Not Found !")
            if(ch==6):  
                print("\t\t\t           -- All Updation Done -- ")
                break
    def delete(self):
        self.c=int(input ("\t\t\tEnter Book Code for Delete  : "))
        query="Delete from books WHERE code=%s"
        cur=self.con.cursor()
        try:
            cur.execute(query,self.c)
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













            
