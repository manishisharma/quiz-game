print('WELCOME TO MY QUIZ GAME ')
playing=input("'do u want ot play !")
if playing.lower()!= "yes":
   quit()
print("'okay lets play'")
score=0
ans=input("what does cpu stands for?  ")
if ans.lower()=="central processing unit":
   print("hurray ! correct ")
   score=+1
else:
   print("oops ,wrong ")

ans=input("what does ram means ")
if ans.lower()=="random access memory":
   print("hurray ! correct ")
   score+=1
else:
   print("oops ,wrong ")

ans=input("what does psu means ")
if ans.lower()=="power supply":
   print("hurray ! correct ")
   score+=1
else:
   print("oops ,wrong ")

ans=input("who invented java  ")
if ans.lower()=="james gosling":
   print("hurray ! correct ")
   score+=1
else:
   print("oops ,wrong ")

ans=input("what does % means in coding  ")
if ans.lower()=="modulus":
   print("hurray ! correct ")
   score+=1
else:
   print("oops ,wrong ")

ans=input("what are the types of error in php  ")
if ans.lower()=="three":
   print("hurray ! correct ")

   score+=1
else:
   print("oops ,wrong ")

ans=input("what is javascript  ")
if ans.lower()=="both serevr and cleint side language ":
   print("hurray ! correct ")
   score+=1
else:
   print("oops ,wrong ")

print("woooooh you scored :", score)
print("you played very well ")

  