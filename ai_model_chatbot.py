import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 140)
engine.setProperty('volume',1.0)
greetings = ["hi","helo","good morning", "good afternoon", "good evening", "good night"]
greetings_answer = ["hi","hello","good morning", "good afternoon", "good evening", "good night"]
dictionary_1 = ["what", "do"]
dictionary_2 = ["mother", "father", "sister", "brother","you"]
answers_2 = ["Thushari Gangani ", "Nimal Gunarathna ", " I haven't any sister", "my elder brother's name is Iresh malinda.my younger brother's name is Ishan pabasara",]
dictionary_3 = ["colour", "school", "go", "sport", "play", "eat", "food", "name", "old", "age", "hobbies", "hobby", "doing", "do"]
dictionary_4 = ["have", "Like"]
answers_1 = [ "my favourite colour is Black", "I got education from Methodist High school until grade 11. now I doing A/L from maths stream in mahanama college.",
           "I got education from Methodist High school until grade 11. now I doing A/L from maths stream in mahanama college.", "I most like to rugby", "I most like to rugby", "no special", "no special", "My name  is Bihan Lakshitha.", "I am 19 years old", "I am 19 years old", "I am 19 year0s old"
           , "not only reading books but only codding", "not only reading books but only codding", "not only reading books but only codding", "not only reading books but only codding"
           ]
Punctuation_marks = ['.', ',']
while True:
    msg = input("You:")
    y = 0
    while True :
        if len(msg) <= y:
            print("no")
            break

        elif msg[y] == '.' or msg[y] == '?' or msg[y] == '!' :
           msg2 = msg[0:y]
           a = y + 1
           x = 0
           while True:
               if str.__contains__(str(msg2), greetings[x]):
                   print("Bihan: " + greetings_answer[x])
                   engine.say(greetings_answer[x])
                   engine.runAndWait()

               break
           while True:
               if str.__contains__(str(msg2), dictionary_1[x]):

                   #   print(dictionary_1[x])
                   if x == 0:
                       while True:
                           if str.__contains__(str(msg2), dictionary_2[x]):
                               # print(dictionary_2[x])
                               #  print(len(dictionary_2)-1 )
                               # print(x)
                               if x == len(dictionary_2) - 1:
                                   # print(len(dictionary_2)-1)
                                   x = 0
                                   while True:
                                       if str.__contains__(str(msg2), dictionary_3[x]):
                                           #  print(x)
                                           #  print(dictionary_3[9])
                                           print("Bihan:" + answers_1[x])
                                           engine.say(answers_1[x])
                                           engine.runAndWait()
                                           break
                                       elif x >= len(dictionary_3):
                                           print("sorry I can't reply ro it")
                                           break
                                       else:
                                           x = x + 1
                                   break
                               elif x == len(dictionary_2):
                                   print("sorry I can't reply ro it")
                                   break
                               else:
                                   while True:
                                       if str.__contains__(str(msg2), dictionary_2[x]):
                                           print("Bihan: " + answers_2[x])
                                           engine.say(answers_2[x])
                                           engine.runAndWait()
                                           break
                                       elif x >= len(dictionary_2):
                                           print("sorry I can't reply ro it")
                                           break
                                       else:
                                           x = x + 1
                           elif x >= len(dictionary_2):
                               print("sorry I can't reply ro it")
                               break
                           else:
                               x = x + 1
                   else:
                       print("sorry I can't reply ro it")
                       break
                   break
               elif x >= len(dictionary_1):
                   print("sorry I can't reply ro it")
                   break
               else:
                   x = x + 1
           while True:
               if len(msg) <= a:
                   #print("no")
                   break
               elif msg[a] == '.' or msg[a] == '?':
                   b = a + 1
                   msg3 = msg[y:a]
                   x = 0
                   while True:
                       if str.__contains__(str(msg3), greetings[x]):
                           print("Bihan: " + greetings_answer[x])
                           engine.say(greetings_answer[x])
                           engine.runAndWait()

                       break
                   while True:
                       if str.__contains__(str(msg3), dictionary_1[x]):

                           #   print(dictionary_1[x])
                           if x == 0:
                               while True:
                                   if str.__contains__(str(msg3), dictionary_2[x]):
                                       # print(dictionary_2[x])
                                       #  print(len(dictionary_2)-1 )
                                       # print(x)
                                       if x == len(dictionary_2) - 1:
                                           # print(len(dictionary_2)-1)
                                           x = 0
                                           while True:
                                               if str.__contains__(str(msg3), dictionary_3[x]):
                                                   #  print(x)
                                                   #  print(dictionary_3[9])
                                                   print("Bihan:" + answers_1[x])
                                                   engine.say(answers_1[x])
                                                   engine.runAndWait()
                                                   break
                                               elif x >= len(dictionary_3):
                                                   print("sorry I can't reply ro it")
                                                   break
                                               else:
                                                   x = x + 1
                                           break
                                       elif x == len(dictionary_2):
                                           print("sorry I can't reply ro it")
                                           break
                                       else:
                                           while True:
                                               if str.__contains__(str(msg3), dictionary_2[x]):
                                                   print("Bihan: " + answers_2[x])
                                                   engine.say(answers_2[x])
                                                   engine.runAndWait()
                                                   break
                                               elif x >= len(dictionary_2):
                                                   print("sorry I can't reply ro it")
                                                   break
                                               else:
                                                   x = x + 1
                                   elif x >= len(dictionary_2):
                                       print("sorry I can't reply ro it")
                                       break
                                   else:
                                       x = x + 1
                               break
                           else:
                               print("sorry I can't reply ro it")
                               break
                           break
                       else:
                           x = x + 1
                   while True:
                       if len(msg) <= b:
                           print("no")
                           break
                       elif msg[b] == '.' or msg[b] == '?':
                           msg3 = msg[a:b]
                           a = y + 1
                           x = 0
                           while True:
                               if str.__contains__(str(msg3), greetings[x]):
                                   print("Bihan: " + greetings_answer[x])
                                   engine.say(greetings_answer[x])
                                   engine.runAndWait()

                               break
                           while True:
                               if str.__contains__(str(msg3), dictionary_1[x]):

                                   #   print(dictionary_1[x])
                                   if x == 0:
                                       while True:
                                           if str.__contains__(str(msg3), dictionary_2[x]):
                                               # print(dictionary_2[x])
                                               #  print(len(dictionary_2)-1 )
                                               # print(x)
                                               if x == len(dictionary_2) - 1:
                                                   # print(len(dictionary_2)-1)
                                                   x = 0
                                                   while True:
                                                       if str.__contains__(str(msg3), dictionary_3[x]):
                                                           #  print(x)
                                                           #  print(dictionary_3[9])
                                                           print("Bihan:" + answers_1[x])
                                                           engine.say(answers_1[x])
                                                           engine.runAndWait()
                                                           break
                                                       elif x >= len(dictionary_3):
                                                           print("sorry I can't reply ro it")
                                                           break
                                                       else:
                                                           x = x + 1
                                                   break
                                               elif x == len(dictionary_2):
                                                   print("sorry I can't reply ro it")
                                                   break
                                               else:
                                                   while True:
                                                       if str.__contains__(str(msg3), dictionary_2[x]):
                                                           print("Bihan: " + answers_2[x])
                                                           engine.say(answers_2[x])
                                                           engine.runAndWait()
                                                           break
                                                       elif x >= len(dictionary_2):
                                                           print("sorry I can't reply ro it")
                                                           break
                                                       else:
                                                           x = x + 1
                                                   break
                                           elif x >= len(dictionary_2):
                                               print("sorry I can't reply ro it")
                                               break
                                           else:
                                               x = x + 1
                                   else:
                                       print("sorry I can't reply ro it")
                                       break
                                   break
                               else:
                                   x = x + 1
                       else:
                           b = b + 1
                   break
               else:
                   a = a + 1
           break
        else:
            y = y + 1
