import mysql.connector

 
#mysql.connector.connect(host='localhost',database='db1',user='root',password='School2009')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="School2009"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS db1")
mycursor.execute("use db1")

mycursor.execute("""    
    create table if not exists users(
    id int primary key auto_increment,
    login varchar(20) not null,
    password varchar(20),
    first_name varchar(20),
    last_name varchar(20),
    constraint uc_user unique(login)
);
""")

login = input("Enter login: ")
password = input("Enter password: ")

first_name = input("Enter ur ferst name: ")
last_name = input("Enter ur lastname: ")

status = input("Enter ur status (student / teacher): ")

mycursor.execute("""
  create table if not exists students(
      chifer varchar(16),
      student_id int references users(id)
  );
""")

mycursor.execute("""
  create table if not exists teachers(
    first_name varchar(20) references users(first_name),
    last_name varchar(20) references users(last_name),
    teacher_id int references users(id)
  );
"""
)

mycursor.execute("""
    insert into users(login, password, first_name, last_name)
    values('%s', '%s', '%s', '%s');
"""
% (login, password, first_name, last_name)
)

mydb.commit()

if status == "student":
  chifer = input("Enter your chifer: ")
  mycursor.execute(
    """
    insert into students(chifer) values('%s');
    """
  %chifer
  )

else:
  mycursor.execute("""
    insert into teachers(first_name, last_name, )
    values();
  """
)

mydb.commit()



mycursor.execute("select * from users")

