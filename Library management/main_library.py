import pymysql
import bookt
import student_l
class login:
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
      def admin(self):
            print("\t\t ********** Library Management System  ********** ")
            print("")
            print("\t\t ********** Created By Bhavesh Bhurkud ********** ")
            print("")
            print("\t\t ---------------------   ADMIN  LOGIN    ----------------- ")
            while(True):
                  try:
                        print("")
                        self.uname=input("\t\t\tUsername : ")
                        self.passwd=input("\t\t\tPassword : ")
                        if(self.uname=="Admin") & (self.passwd=="admin@123"):
                              print("\t\t\t================================")
                              print("\t\t\t\tLogin Successful")
                              break
                        raise ValueError
                  except ValueError:
                        print("\t\t\tRe - enter Username & Password ")
            print("\t\t\t================================")
            
#main
#lo=login()
#lo.admin()
#l=bookt.library()
#l.update()
#l.show()
s=student_l.student()
s.show()

