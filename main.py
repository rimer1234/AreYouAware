from tkinter import *
import pygame
from random import *
from twilio.rest import Client
from time import *

color = "black"

# Account Sid and Auth Token from twilio.com / console
twilio_account_sid = 'AC1d6857e4e67dedb6aa33e94cd2616291'
twilio_auth_token = 'dd701579b72c6da38e315cd0b98e710b'

client = Client(twilio_account_sid, twilio_auth_token)

pygame.init()

root = Tk()
root.title("Are You Aware?")
root.geometry('1052x652+0+0')
root.configure(background="black")

#**********Start Create Frames***********#
Base = Frame(root, bg=color)
Base.grid()

Layer1 = Frame(root, bg=color, bd=20, width=900, height=600)
Layer1.grid(row=0, column=0)
Layer2 = Frame(root, bg=color, bd=20, width=452, height=600)
Layer2.grid(row=0, column=1)

Layer1a = Frame(Layer1, bg=color, bd=20, width=900, padx=110, height=200)
Layer1a.grid(row=0, column=0)
Layer1b = Frame(Layer1, bg=color, bd=20, width=900, height=200)
Layer1b.grid(row=1, column=0)
Layer1c = Frame(Layer1, bg=color, bd=20, width=900, height=200)
Layer1c.grid(row=2, column=0)

#**********End Create Frames***********#
prompt = StringVar()
prompt.set("Choose An Answer")

avail50_50 = TRUE
availphone = TRUE
availpeople = TRUE
gameover = FALSE
numq = 1
prize = 0

Qns = [
  "Q1: Which of the following is a microaggression?",
  "Q2: Which of the following is a microaggression?",
  "Q3: Which of the following is a microaggression?",
  "Q4: Is it microaggression to say to an Asian or Latino person: \nWhy are you so quiet? We want to know what you think. Be more verbal.",
  "Q5: Which is a microaggression?",
  "Q6: Is is microaggression to say: You have a cool accent?",
  "Q7: Which of the following is a  microaggression?",
  "Q8: Is this microaggression to say :\n You're so tall that it must be difficult to find a boyfriend right?",
  "Q9: Is is microaggression to say: \nYou don’t seem gay.",
  "Q10:Is it microaggression to say: \n There is only one race, the human race."
]

Ans1 = [
  "Where are you really from?", 
  "You are a credit to your race.",
  "You have great fashion \nsense for a plus-sized girl", 
  "Yes it is",
  "As a woman, I know what it’s \nlike to be in a minority group",
  "No it is not", 
  "I love your hair today! \nDo you use styling products?", 
  "In some cases", 
  "Yes it is", 
  "In some cases"
]
Ans2 = [
  "Where were you born?", 
  "You are so articulate.", 
  "I love your dress",
  "No it is not", 
  "College admission must be easy \n because you’re Black",
  "Yes it is", 
  "That lipstick shade is so pretty! \nWhere can I buy it?", 
  "Yes it is", 
  "No it is not", 
  "No it is not"
]
Ans3 = [
  "You speak good English.", 
  "Asians are good in math. \nCan you help?",
  "Great job with the essay", 
  "Maybe", 
  "All of the above", 
  "Maybe", 
  "Your braided hair is so pretty! \nCan I touch it?",
  "No it is not", 
  "Maybe", 
  "Yes it is"
]
Ans4 = [
  "All of the above", 
  "All of the above", 
  "All of the Above", 
  "In some cases",
  "How did 'you' get this job?", 
  "In some cases", 
  "None of the above", 
  "Maybe",
  "In some cases", 
  "Maybe"
]

correctans = [4, 4, 1, 1, 3, 2, 3, 2, 1, 3]

images = [
  "Photo0.png", "Photo1.png", "Photo2.png", "Photo3.png", "Photo4.png",
  "Photo5.png", "Photo6.png", "Photo7.png", "Photo8.png", "Photo9.png"
]

prizes = [
  2000, 4000, 8000, 16000, 32000, 64000, 128000, 250000, 500000, 1000000
]

#****************Question***************#
Question1 = StringVar()
Question2 = StringVar()
Question3 = StringVar()
Question4 = StringVar()

Answer1 = StringVar()
Answer2 = StringVar()
Answer3 = StringVar()
Answer4 = StringVar()

Question1.set(Qns[numq - 1])
Answer1.set(Ans1[numq - 1])
Answer2.set(Ans2[numq - 1])
Answer3.set(Ans3[numq - 1])
Answer4.set(Ans4[numq - 1])
canvas = Canvas(Layer2, bg=color, width=146, height=431)
canvas.grid(row=0, column=0)
canvas.delete("all")
image1 = PhotoImage(file="Photo0.png")
canvas.create_image(73, 215, image=image1)
canvas.image = image1


def Change50_50():
  global avail50_50
  global prompt
  global gameover
  if (gameover != TRUE and avail50_50 == TRUE):
    canvas = Canvas(Layer1a, bg=color, width=140, height=90)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file='5050b.png')
    canvas.create_image(70, 45, image=image1)
    canvas.image = image1
    if (correctans[numq - 1] == 1):
      Answer2.set("")
      Answer3.set("")
    elif (correctans[numq - 1] == 2):
      Answer1.set("")
      Answer3.set("")
    elif (correctans[numq - 1] == 3):
      Answer2.set("")
      Answer1.set("")
    elif (correctans[numq - 1] == 4):
      Answer2.set("")
      Answer3.set("")
    prompt.set("Two incorrect answers eliminated. Choose your answer.")


def ChangePeople():
  global prompt
  global availpeople
  if (gameover != TRUE and availpeople == TRUE):
    canvas = Canvas(Layer1a, bg=color, width=139, height=89)
    canvas.grid(row=0, column=1)
    canvas.delete("all")
    image1 = PhotoImage(file='peopleb.png')
    canvas.create_image(70, 45, image=image1)
    canvas.image = image1
    list1 = ['A', 'B', 'C', 'D']
    choice = randint(0, 3)
    prompt.set("The audience chose " + list1[choice] + ". Choose Your Answer.")


def ChangePhone():
  global prompt
  global availphone
  if (gameover != TRUE and availphone == TRUE):
    canvas = Canvas(Layer1a, bg=color, width=139, height=89)
    canvas.grid(row=0, column=2)
    canvas.delete("all")
    image1 = PhotoImage(file='phoneb.png')
    canvas.create_image(70, 45, image=image1)
    canvas.image = image1
    msg = Question1.get() + "A." + Answer1.get() + "B." + Answer2.get(
    ) + "C." + Answer3.get() + "D." + Answer4.get()
    message = client.messages.create(from_='+18563861068',
                                     body=msg,
                                     to='+12014173378')

    list1 = ['A', 'B', 'C', 'D']
    choice = correctans[numq-1]-1
    prompt.set("Sent Message to Friend on Twilio. \nYour friend says " +
               list1[choice] + ". Choose Your Answer.")


CenterImage = PhotoImage(file='center.png')
LogoCenter = Button(Layer1b,
                    image=CenterImage,
                    bg=color,
                    width=300,
                    height=200)
LogoCenter.grid(row=0, column=0)

Image50_50 = PhotoImage(file='5050.png')
Live50_50 = Button(Layer1a,
                   image=Image50_50,
                   bg=color,
                   width=140,
                   height=90,
                   command=Change50_50)
Live50_50.grid(row=0, column=0)

ImagePeople = PhotoImage(file='people.png')
LivePeople = Button(Layer1a,
                    image=ImagePeople,
                    bg=color,
                    width=139,
                    height=89,
                    command=ChangePeople)
LivePeople.grid(row=0, column=1)

ImagePhone = PhotoImage(file='phone.png')
LivePhone = Button(Layer1a,
                   image=ImagePhone,
                   bg=color,
                   width=139,
                   height=89,
                   command=ChangePhone)
LivePhone.grid(row=0, column=2)


def NextQn():
  global numq
  if (numq < 10):
    numq = numq + 1
    Question1.set(Qns[numq - 1])
    Answer1.set(Ans1[numq - 1])
    Answer2.set(Ans2[numq - 1])
    Answer3.set(Ans3[numq - 1])
    Answer4.set(Ans4[numq - 1])
    canvas = Canvas(Layer2, bg=color, width=146, height=431)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file=images[numq - 1])
    canvas.create_image(73, 215, image=image1)
    canvas.image = image1
    prompt.set("Correct Answer!! You won $" + str(prize) + "!\nOn to the next one...")


def setAnswer(ans):
  global numq
  global prize
  global gameover
  if (gameover == TRUE):
    return
  if (ans == correctans[numq - 1]):
    prize = prizes[numq - 1]
  if (numq < 10 and ans == correctans[numq - 1]):
    NextQn()
  else:
    gameover = TRUE
    list1 = ['A', 'B', 'C', 'D']
    if (ans != correctans[numq - 1]):
         prompt.set("Sorry, Correct Answer is " +
                    list1[correctans[numq - 1] - 1] + "\nGame Over! You won $" + str(prize) + "!")
    else:
        prompt.set("Game Over! Congratulations! You won $" + str(prize) + "!")

#****************Question***************#

txtQuestion = Label(Layer1c,
                    font=('arial', 10, 'bold'),
                    bg='blue4',
                    fg='white',
                    bd=5,
                    width=66,
                    justify=CENTER,
                    borderwidth=10,
                    textvariable=Question1)
txtQuestion.grid(row=0, column=0, columnspan=4, pady=4)

lblQuestionA = Label(Layer1c,
                     font=('arial', 10, 'bold'),
                     text="A: ",
                     bg=color,
                     fg='white',
                     bd=5,
                     justify=CENTER)
lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

txtQuestion1 = Button(Layer1c,
                      font=('arial', 10, 'bold'),
                      bg='blue4',
                      fg='white',
                      bd=1,
                      width=25,
                      height=2,
                      justify=CENTER,
                      textvariable=Answer1,
                      command=lambda: setAnswer(1))
txtQuestion1.grid(row=1, column=1, pady=4)

lblQuestionB = Label(Layer1c,
                     font=('arial', 10, 'bold'),
                     text="B: ",
                     bg=color,
                     fg='white',
                     justify=LEFT)
lblQuestionB.grid(row=1, column=2, sticky=W)

txtQuestion2 = Button(Layer1c,
                      font=('arial', 10, 'bold'),
                      bg='blue4',
                      fg='white',
                      bd=1,
                      width=25,
                      height=2,
                      justify=CENTER,
                      textvariable=Answer2,
                      command=lambda: setAnswer(2))
txtQuestion2.grid(row=1, column=3, pady=4)

lblQuestionC = Label(Layer1c,
                     font=('arial', 10, 'bold'),
                     text="C: ",
                     bg=color,
                     fg='white',
                     bd=5,
                     justify=LEFT)
lblQuestionC.grid(row=2, column=0, sticky=W)

txtQuestion3 = Button(Layer1c,
                      font=('arial', 10, 'bold'),
                      bg='blue4',
                      fg='white',
                      bd=1,
                      width=25,
                      height=2,
                      justify=CENTER,
                      textvariable=Answer3,
                      command=lambda: setAnswer(3))
txtQuestion3.grid(row=2, column=1, pady=4)

lblQuestionD = Label(Layer1c,
                     font=('arial', 10, 'bold'),
                     text="D: ",
                     bg=color,
                     fg='white',
                     bd=5,
                     justify=CENTER)
lblQuestionD.grid(row=2, column=2, stick=W)

txtQuestion4 = Button(Layer1c,
                      font=('arial', 10, 'bold'),
                      bg='blue4',
                      fg='white',
                      bd=1,
                      width=25,
                      height=2,
                      justify=CENTER,
                      textvariable=Answer4,
                      command=lambda: setAnswer(4))
txtQuestion4.grid(row=2, column=3, pady=4)

#************************************#
lblQuestionE = Label(Layer1b,
                     font=('arial', 10, 'bold'),
                     textvariable=prompt,
                     bg='orange',
                     fg='black',
                     bd=10,
                     justify=CENTER)
lblQuestionE.grid(row=1, column=0, stick=S)

root.mainloop()
