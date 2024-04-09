print("WELCOME TO  QUIZ")
r1 = input("DO YOU WANT TO PLAAY QUIZ ? (yes or no) ")
if r1.lower() != 'yes':
    quit()
if r1.lower() == 'yes' :
    print("OK THEN ! LET'S PLAY QUIZ :)")
score = 0
answer = input("what does CPU stand for ? ")
if answer.lower() == 'central processing unit':
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT!")
answer = input("what does GPU stand for ? ")
if answer.lower() == 'graphics processing unit':
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT!")
answer = input("what does RAM stand for ? ")
if answer.lower() == 'random access memory':
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT!")
answer = input("what does SQL stand for ? ")
if answer.lower() == 'structured query language':
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT!")
answer = input("what does DSA stand for ? ")
if answer.lower() == 'data structures and algorithms':
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT!")
print("YOU HAVE ANSWERD " + str(score) + " QUESTIONS CORRECTLY .")
print("YOU SCORED " +  str((score / 5) * 100)  + " % IN QUIZ .")