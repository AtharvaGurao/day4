#file handaling
f = open(file="sample.txt", mode="w")
f.write("aash chooses pikachu")
f.write("\n")
f.write("misty chooes psyduck")
f.close()

#input number of lines from user. example if user chooes 5,write allthe pokemons to the file

#n = int(input("Number of Pokemon: "))
#f = open(file="sample.txt", mode="w")

#for i in range(n):
 #   f.write(input("Pokemon:"))
  #  f.write("\n")
#f.close()


# 1.make two files:
# QUESTIONS.TXT that contains same questions 
# ANSWER.TXT that contains the answer

#def make_questions(n,*questions):
 # f = open(file="QUESTIONS.TXT", mode="w")
  #for questions in questions: 
   # f.write("questions")
    #f.write("/n")
  #f.close()

#def write_answers(n,*answers):
 # f = open(file="ANSWER.TXT", mode="w")
  #for answer in answers: 
 #   f.write("answer")
  #  f.write("/n")
  #f.close()

  #make_questions("capital of india")
  #write_answers()

  #main program
  #openthe files in resding mode
#try:
 # q=open("QUESTIONS.TXT","r")
 # a=open("ANSWER.TXT","r")

  # correct,wrong =0,0

  #for questions,answer in zip(q,a):
   # user_answer =input(question)
  #  if user_answer == answer:
   #   correct+=1
   # else: wrong-=1

#except FileNotFoundError as e:
 # print(e)


#finally:
#  q.close()
#  a.close()
  
   
