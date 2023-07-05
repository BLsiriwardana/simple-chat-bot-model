import mysql.connector
import pyttsx3
engine = pyttsx3.init()
mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    password=""

)
#print(mydb)
#message = input("me :")
fruits = []
myquery = mydb.cursor()
#myquery.execute('CREATE DATABASE my_system')
myquery.execute('USE my_system')
#myquery.execute('CREATE TABLE fruits (fruit_id VARCHAR(225) PRIMARY KEY, fruits_name VARCHAR(225), price INT(10))')
#myquery.execute('CREATE TABLE votes (vote_id INT(100) auto_increment PRIMARY KEY, vote_name VARCHAR(225), num_votes INT(100))')
#myquery.execute("INSERT INTO fruits (fruit_id, fruits_name, price ) VALUES ('FF1', 'Apple', 80 ) ")
#sql_query_fruit_insert ="INSERT INTO fruits (fruit_id, fruits_name, price ) VALUES (%s, %s, %s ) "
#Val = [
 #   ('FF2', 'Banana', 100),
  #  ('FF3', 'Pinapple', 250),
   # ('FF4', 'Wood Apple', 60)

#]
#myquery.executemany(sql_query_fruit_insert, Val)
sql_query_fruit_select_1 = "SELECT fruits_name,fruit_id FROM fruits"
myquery.execute(sql_query_fruit_select_1)
result = myquery.fetchall()
message = input("Me:")
for x in result:
    fruits.append(str(x))
item_final = []
def cutting(a):
    x = 0
    while True:
        if x != len(fruits):
          item = fruits[x]
          y = 0
          while True:
             if y != len(item):
                 if item[y] == "'":
                     #print(y)
                     z = 1 + y
                     while True:
                        if item[z] == "'":
                           #print(z)
                           item_final.append(item[y+1:z])
                           break
                        else:
                           z = z + 1
                     break
                 else:
                     y = y + 1
             else:
                 break
          x = x + 1
        else:
            break

#print(fruits[1])
#name = fruits[1]
#print

mydb.commit()
cutting(fruits)
print(item_final)
#print(item_final[2])
n = 0
while n != len(item_final):
    if message.lower() == str(item_final[n]).lower():
            print("yes ! It's fruit.")
            break
    elif n == len(item_final)-1:
         print('wrong!')
         break
    else:
            print('checking.....')
            n = n + 1

