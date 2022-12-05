from tkinter import *
import random
import time

n1 = 0    
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
n0 = 0

root = Tk()
root.geometry('300x430')
root.title('Game')
root.resizable(width=False, height=False)

options = [random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]

player_answer = Entry(root, bg='#C9C9C9')
player_answer.place(y=260, x=90)
mistakescore = 0
bot_score = Label(root, text=f'{mistakescore}', font='Arial, 50')
bot_score.pack()
txt2 = Label(root, text='5 ошибок и проиграешь!', font='Arial, 13')
txt2.place(x=67, y=400)
txt1 = Label(root, text='"Виселица" Угадай числа от 0 до 9\nВсего 5 цифр', font='Arial, 13')
txt1.pack()



def guessnum():
    global mistakescore
    valsymbols = player_answer.get()
    sym = 'qwertyuiopasdfghjklzxcvbbmQWERTYUIOPASDFGHJKLZXCVBNM'
    for i in sym:
        print(i)
        if not i in valsymbols:
            pass
        else:
            txt2['text'] = 'Буквы вводить нельзя!'
            txt2['bg'] ='yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '5 ошибок и проиграешь'
            txt2['bg'] = 'white'
            return 'xyinya'
    val = int(valsymbols)
    print(options[0:5])

    global n1    
    global n2
    global n3
    global n4
    global n5
    global n6
    global n7
    global n8
    global n9
    global n0

    if val != 0:
        if val != 1:
            if val != 2:
                if val != 3:
                    if val != 4:
                        if val != 5:
                            if val != 6:
                                if val != 7:
                                    if val != 8:
                                        if val != 9:
                                            txt2['text'] = 'Числа только от 0 до 9'
                                            txt2['bg'] = 'yellow'
                                            root.update()
                                            time.sleep(1)
                                            txt2['text'] = '5 ошибок и проиграешь'
                                            txt2['bg'] = 'white'
                                            return 'xyinya'
                                            
    if val == 0:
        if n0 == 0:
            n0 += 1
            print(n0)
        elif n0 > 0:
            txt2['text'] = '0 уже было'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '5 ошибок и проиграешь'
            txt2['bg'] = 'white'
            if val != options[0]:    
                if val != options[1]:
                    if val != options[2]:
                        if val != options[3]:
                            if val != options[4]:
                                mistakescore -= 1
    

    elif val == 1:
        if n1 == 0:
            n1 += 1
        elif n1 > 0:
            txt2['text'] = '1 уже было'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '5 ошибок и проиграешь'
            txt2['bg'] = 'white'
            if val != options[0]:    
                if val != options[1]:
                    if val != options[2]:
                        if val != options[3]:
                            if val != options[4]:
                                mistakescore -= 1


    elif val == 2:
        if n2 == 0:
            n2 += 1
        elif n2 > 0:
            txt2['text'] = '2 уже было'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '5 ошибок и проиграешь'
            txt2['bg'] = 'white'
            if val != options[0]:    
                if val != options[1]:
                    if val != options[2]:
                        if val != options[3]:
                            if val != options[4]:
                                mistakescore -= 1


    elif val == 3:
        if n3 == 0:
            n3 += 1
        elif n3 > 0:
            txt2['text'] = '3 уже было'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '5 ошибок и проиграешь'
            txt2['bg'] = 'white'
            if val != options[0]:    
                if val != options[1]:
                    if val != options[2]:
                        if val != options[3]:
                            if val != options[4]:
                                mistakescore -= 1


    elif val == 4:
        if n4 == 0:
            n4 += 1
        elif n4 > 0:
            txt2['text'] = '4 уже было'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '5 ошибок и проиграешь'
            txt2['bg'] = 'white'
            if val != options[0]:    
                if val != options[1]:
                    if val != options[2]:
                        if val != options[3]:
                            if val != options[4]:
                                mistakescore -= 1


    elif val == 5:
        if n5 == 0:
            n5 += 1
        elif n5 > 0:
            txt2['text'] = '5 уже было'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '5 ошибок и проиграешь'
            txt2['bg'] = 'white'
            if val != options[0]:    
                if val != options[1]:
                    if val != options[2]:
                        if val != options[3]:
                            if val != options[4]:
                                mistakescore -= 1


    elif val == 6:
        if n6 == 0:
            n6 += 1
        elif n6 > 0:
            txt2['text'] = '6 уже было'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '5 ошибок и проиграешь'
            txt2['bg'] = 'white'
            if val != options[0]:    
                if val != options[1]:
                    if val != options[2]:
                        if val != options[3]:
                            if val != options[4]:
                                mistakescore -= 1


    elif val == 7:
        if n7 == 0:
            n7 += 1
        elif n7 > 0:
            txt2['text'] = '7 уже было'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '5 ошибок и проиграешь'
            txt2['bg'] = 'white'
            if val != options[0]:    
                if val != options[1]:
                    if val != options[2]:
                        if val != options[3]:
                            if val != options[4]:
                                mistakescore -= 1


    elif val == 8:
        if n8 == 0:
            n8 += 1
        elif n8 > 0:
            txt2['text'] = '8 уже было'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '5 ошибок и проиграешь'
            txt2['bg'] = 'white'
            if val != options[0]:    
                if val != options[1]:
                    if val != options[2]:
                        if val != options[3]:
                            if val != options[4]:
                                mistakescore -= 1

    elif val == 9:
        if n9 == 0:
            n9 += 1
        elif n9 > 0:
            txt2['text'] = '9 уже было'
            txt2['bg'] = 'yellow'
            root.update()
            time.sleep(1)
            txt2['text'] = '5 ошибок и проиграешь'
            txt2['bg'] = 'white'
            if val != options[0]:    
                if val != options[1]:
                    if val != options[2]:
                        if val != options[3]:
                            if val != options[4]:
                                mistakescore -= 1


    if mistakescore < 5:
        if num1['text'] == '_':
            mistakescore += 1
            bot_score['text'] = mistakescore
            bot_score['bg'] = 'red'
        elif num2['text'] == '_':
            mistakescore += 1
            bot_score['text'] = mistakescore
            bot_score['bg'] = 'red'
        elif num3['text'] == '_':    
            mistakescore += 1
            bot_score['text'] = mistakescore
            bot_score['bg'] = 'red'
        
        elif num4['text'] == '_':
            mistakescore += 1
            bot_score['text'] = mistakescore
            bot_score['bg'] = 'red'
        elif num5['text'] == '_':
            mistakescore += 1
            bot_score['text'] = mistakescore
            bot_score['bg'] = 'red'
        
        if val == options[0]:
            mistakescore -= 1
            bot_score['text'] = mistakescore
            if mistakescore == 0:
                bot_score['bg'] = 'white'
                
        elif val == options[1]:
            mistakescore -= 1
            bot_score['text'] = mistakescore
            if mistakescore == 0:
                bot_score['bg'] = 'white'
                bot_score['text'] = mistakescore

        elif val == options[2]:
            mistakescore -= 1
            bot_score['text'] = mistakescore
            if mistakescore == 0:
                bot_score['bg'] = 'white' 

        elif val == options[3]:
            mistakescore -= 1
            bot_score['text'] = mistakescore
            if mistakescore == 0:
                bot_score['bg'] = 'white'           
            
        elif val == options[4]:
            mistakescore -= 1
            bot_score['text'] = mistakescore
            if mistakescore == 0:
                bot_score['bg'] = 'white'
                

        if val == options[0]:
            num1['text'] = val
        if val == options[1]:
            num2['text'] = val
        if val == options[2]:
            num3['text'] = val 
        if val == options[3]:
            num4['text'] = val
        if val == options[4]:      
            num5['text'] = val
    

    if mistakescore == 5:
        txt2['text'] = 'Ты проиграл!'
        txt2['bg'] = 'red'
        entry_button['state'] = DISABLED
    try:
        val1 = int(num1.cget('text'))
        val2 = int(num2.cget('text'))
        val3 = int(num3.cget('text'))
        val4 = int(num4.cget('text'))
        val5 = int(num5.cget('text'))
        if val1 == options[0]:
            if val2 == options[1]:
                if val3 == options[2]:
                    if val4 == options[3]:
                        if val5 == options[4]:
                            print('yes')
                            txt2['text'] = 'Ты выиграл!!!'
                            txt2['bg'] = 'blue'
                            entry_button['state'] = DISABLED
    except:
        print('no')


entry_button = Button(root,command=guessnum, text='Ввести',font='Arial, 20')
entry_button.place(x=80, y=300, width=150)
num1 = Label(root, text='_', font='Arial, 50')
num1.place(x=5, y=130)
num2 = Label(root, text='_', font='Arial, 50')
num2.place(x=65, y=130)
num3 = Label(root, text='_', font='Arial, 50')
num3.place(x=125, y=130)
num4 = Label(root, text='_', font='Arial, 50')
num4.place(x=185, y=130)
num5 = Label(root, text='_', font='Arial, 50')
num5.place(x=245, y=130)

root.mainloop()