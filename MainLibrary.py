import pymysql as SQL
try:
    conn=SQL.connect(host='localhost',port=3306,user='root',passwd='1234',database='library',cursorclass=SQL.cursors.DictCursor)
    smt=conn.cursor()
    print("*"*148)
    print("*"*148)
    print("*"*148)
    print("\t\t\t\t\t\tWelcome To Learning Center ")
    c=int(input("\t\t1] Login as a faculty\n\t\t2] Login as a user  "))
    # q="create table user(enrollmentid int primary key,name varchar(25),year decimal(10),semester decimal(10),stream varchar(10))"
    # smt.execute(q)
    # conn.commit()
    # q2='create table libraria(libid int primary key,name varchar(25))'
    # smt.execute(q2)
    # conn.commit()
    # q3="create table book(name varchar(50),quantity decimal(3))"
    # smt.execute(q3)
    # conn.commit()
    if(c==1):
        Aid=int(input("Enter your faculty I'd  \n"))
        q="select * from librarian where libid={0}".format(Aid)
        smt.execute(q)
        rec=smt.fetchone()
        if(rec):
            if(Aid==rec['libid']):
                print("Choose what you want to perform \n")
                p=int(input("\t\t1] Show books \n\t\t2] Add a book \n\t\t3] Remove a book\n"))
                if(p==1):
                    book=input("Enter name of book  ")
                    q="select * from book where name='{0}'".format(book)
                    smt.execute(q)
                    r=smt.fetchone()
                    if(r):
                        print(r['name'],r['quantity'])
                elif(p==2):
                    book=input("Enter name of book availalble ")
                    qty=int(input("Enter number of"+ book +" you want to insert"))
                    q="insert into book values('{0}',{1})".format(book,qty)
                    smt.execute(q)
                    conn.commit()
                elif(p==3):
                    book=input("Enter name of book you want to remove ")
                    qty=int(input("Enter number of"+ book +" you want to remove"))
                    q="insert into book values('{0}',{1})".format(book,qty)
                    smt.execute(q)
                    conn.commit()
            else:
                print("Your I'd didnot match, please try again")
        else:
            print("No records match for the admin Id you inserted")
    elif(c==2):
        c1=input("\t\tAre you a new user? (y/n) \n")
        if(c1=='y' or c1=='Y'):
            c2=int(input("\t\t1] Create your account\n\t\t2] Exit"))
            if(c2==1):
                Uid=int(input("Enter your college enrollment id: "))
                un=input("Wnter your Name: ")
                uy=int(input("Enter year of study: "))
                us=int(input("Enter your semester: "))
                ust=input("Enter Stream of study in short form like(CSE,ECE...etc): ")
                q="insert into user values({0},'{1}',{2},{3},'{4}')".format(Uid,un,uy,us,ust)
                smt.execute(q)
                conn.commit()
                print("\n\n\t\tWhat task do you want to perform?")
                ch=int(input("\t\t1] Return a book \n\t\t2] Issue a book \n\t\t3] Exit"))
                if(ch==1):
                    print("You were a new user and do not have any book to return")                   
                elif(ch==2):
                    book=input("Enter the name of book you want to Issue ")
                    q="insert into book values('{0}')".format(book)
                    smt.execute(q)
                    records=smt.fetchone()
                    if(records):
                        print("You have issued ",records['name'],records['quantity'])
                    print("Enjoy your book")
                elif(ch==3):
                    print("Exiting...")
            elif(c2==2):
                print("Exiting...")
                breakpoint
        elif(c1=='n' or c1=='N'):
            c3=int(input("\t\t1] Login\n\t\t2] Exit"))
            if(c3==1):
                Uid=int(input("Enter your enrollment id "))
                q="Select * from user where enrollmentid={0}".format(Uid)
                smt.execute(q)
                records=smt.fetchone()
                if(records):
                    print("\n\t\t",records['enrollmentid'],"\n\t\t",records['name'],"\n\t\t",records['year'],"\n\t\t",records['semester'],"\n\t\t",records['stream'])
                else:
                    print("No User found")
                ch=int(input("\t\t1] Return a book \n\t\t2] Issue a book \n\t\t3] Exit"))
                if(ch==1):                  #Database connect
                    book=input("Enter the name of book you want to return ")
                    print("Book Returned succesfully")                   
                elif(ch==2):
                    book=input("Enter the name of book you want to issue ")
                    q="insert into book values('{0}')".format(book)
                    q2='select * from book where name={0}'.format(book)
                    smt.execute(q)
                    records=smt.fetchone()
                    if(records):
                        print("You Have Issued ",records['name'])
                        print("Enjoy your book")
                    else:
                        print("No book found")
                elif(ch==3):
                    print("Exiting...")
            elif(c3==2):
                print("Exitting...")
                
    conn.close()
except Exception as err:
    print("Error:",err)