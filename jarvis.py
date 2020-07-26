# importing usefull modules
import pyttsx3  #pip install pyttsx3
import datetime 
import speech_recognition as sr #pip install speechRecognition
import pyaudio #by wheel install 
import os
import wikipedia #pip install wikipedia
import webbrowser 
import pygame  #pip install pygame
import random
import time
import pyautogui
from selenium  import webdriver  #pip install selenium
from selenium.webdriver.common.keys import Keys


pygame.mixer.init()

# def browser():
#     browser = "chrome"
#     webbrowser.open_new(browser)
    


# generating voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)

# making speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#wihsME function
def wishME():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak(" Hello Sir!  Good Morning Sir!")

    elif hour >= 12 and hour < 17:
        speak(" Hello Sir! Good Afternoon Sir!")

    else:
        speak(" Hello Sir! Good Evening Sir!")

    speak(" sir plzz tell! what can i do for you")

# function for taking user command in voice    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1500
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

# list of songs
songs = ['F:\\musics\\1.mp3',
'F:\\musics\\2.mp3',
'F:\\musics\\3.mp3',
'F:\\musics\\4.mp3',
'F:\\musics\\5.mp3',
'F:\\musics\\6.mp3',
'F:\\musics\\7.mp3',
'F:\\musics\\8.mp3',
'F:\\musics\\9.mp3',
'F:\\musics\\10.mp3',
'F:\\musics\\11.mp3',
'F:\\musics\\12.mp3',
'F:\\musics\\13.mp3',
'F:\\musics\\14.mp3',
'F:\\musics\\15.mp3',
'F:\\musics\\16.mp3',
'F:\\musics\\17.mp3',
'F:\\musics\\18.mp3',
'F:\\musics\\19.mp3',
'F:\\musics\\20.mp3',
'F:\\musics\\21.mp3',
'F:\\musics\\22.mp3',
'F:\\musics\\23.mp3',
'F:\\musics\\24.mp3',
'F:\\musics\\25.mp3',
'F:\\musics\\26.mp3',
]


#function for starting JARVIS
def main():
            
    speak("say    'Hi     Jarvis'     to     Activate     -JARVIS-   ")
    while True: 
        print("say 'Hi jarvis' to Activate -JARVIS-")
        say = takeCommand().lower()  
        if ("hi jarvis" == say):
            wishME()      
            while True: 
                    
                query = takeCommand().lower() #Converting user query into lower case
                # Logic for executing tasks based on query
                if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2) 
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)


                # My Computer Handle
                elif 'go back' in query:
                    pyautogui.press('backspace')

                elif 'open my computer' in query:
                    path = 'C:\\Windows\\explorer.exe'
                    os.startfile(path)
                    
                
                elif 'maximize tab' in query:
                    pyautogui.hotkey('win','up')
                
                elif 'go to windows' in query:
                    pyautogui.moveTo(304,400,duration=0.1)
                    pyautogui.doubleClick()
                
                elif 'go to games' in query:
                    pyautogui.moveTo(831,400,duration = 0.1)
                    pyautogui.doubleClick()
                
                elif 'go to music' in query:
                    pyautogui.moveTo(1050,400,duration = 0.1)
                    pyautogui.doubleClick()
                
                elif 'go to movies' in query:
                    pyautogui.moveTo(296,450,duration = 0.1)
                    pyautogui.doubleClick()
                
                elif 'go to main' in query:
                    pyautogui.moveTo(552,457,duration=0.1)
                    pyautogui.doubleClick()

                elif 'go to downloads' in query:
                    pyautogui.moveTo(1013,267,duration=0.1)
                    pyautogui.doubleClick()


                elif 'items in start' in query:
                    pyautogui.moveTo(54,755,duration=0.2)
                    pyautogui.click()
                    speak("what do you want to search")
                    say = takeCommand()
                    pyautogui.typewrite(say,interval=0.1)
                    pyautogui.press('enter')

                elif 'system shutdown' in query:
                    pyautogui.hotkey('ctrl','esc')
                    pyautogui.moveTo(27,718,duration=0.1)
                    pyautogui.click()
                    pyautogui.moveTo(59,629,duration=0.1)
                    pyautogui.click()

                elif 'system restart' in query:
                    pyautogui.hotkey('ctrl','esc')
                    pyautogui.moveTo(27,718,duration=0.1)
                    pyautogui.click()
                    pyautogui.moveTo(57,657,duration=0.1)
                    pyautogui.click()

                elif 'go to desktop' in query:
                    pyautogui.hotkey('win','d')
                # computer handle end



                
                    
                # File Handling
                elif 'search karo' in query:
                    pyautogui.press('f3')
                    speak('search what sir!')
                    say = takeCommand()
                    pyautogui.write(say,interval=0.1)
                    pyautogui.press('down')
                    pyautogui.press('enter')

                    


                elif 'close' in query:
                    pyautogui.hotkey('ctrl' , 'w')

                elif 'create new folder' in query:
                    pyautogui.hotkey('ctrl' ,'shift' , 'n')
                    say = takeCommand()
                    if 'rename' in say:
                        speak("sir please say name for folder")
                        say = takeCommand()
                        pyautogui.write(say,interval=0.1)
                        pyautogui.press('enter')
                    else:
                        pyautogui.press('enter')
                
                elif 'maximize' in query:
                    pyautogui.hotkey('win','up')
                
                elif 'minimize' in query:
                    pyautogui.hotkey('win','up')

                elif 'copy file' in query:
                    pyautogui.hotkey('ctrl','c')

                elif 'paste file' in query:
                    pyautogui.hotkey('ctrl','v')
                
                elif 'cut file' in query:
                    pyautogui.hotkey('ctrl','x')

                elif 'open new' in query:
                    pyautogui.hotkey('ctrl','n')
                
                elif 'hold ctrl' in query:
                    pyautogui.keyDown('ctrl')

                elif 'hold shift' in query:
                    pyautogui.keyDown('shift')
                
                elif 'release ctrl' in query:
                    pyautogui.keyUp('ctrl')

                elif 'release shift' in query:
                    pyautogui.keyUp('shift')

                elif 'select all' in query:
                    pyautogui.hotkey('ctrl' ,'a')
                # file handling end

                # Notepad handle
                elif 'open notepad' in query:
                    pyautogui.moveTo(54,755,duration=0.2)
                    pyautogui.click()
                    pyautogui.write("notepad" , interval = 0.2)
                    pyautogui.press('enter')

                elif 'save this file' in query:
                    pyautogui.hotkey('ctrl','s')
                    say = takeCommand()
                    pyautogui.write(say,interval=0.2)
                    pyautogui.press('enter')
                    pyautogui.hotkey('alt','f4')

                
                # Notes end 
 

                # Start handle
                elif 'open start' in query:
                    pyautogui.hotkey('ctrl' , 'esc')

                elif 'scroll up' in query:
                    pyautogui.vscroll(343)

                elif 'scroll down' in query:
                    pyautogui.vscroll(-343)

                
                #start end

                # Wifi Handle
                elif 'connect ' in query:
                    pyautogui.moveTo(1220,756,duration = 0.1)
                    pyautogui.click()
                    time.sleep(2)
                    pyautogui.moveTo(1058,681,duration=0.1)
                    pyautogui.click()
                    time.sleep(2)
                    pyautogui.moveTo(1220,756,duration = 0.1)
                    pyautogui.click()

                elif 'disconnect ' in query:
                    pyautogui.moveTo(1220,756,duration = 0.1)
                    pyautogui.click()
                    time.sleep(2)
                    pyautogui.moveTo(1058,681,duration=0.1)
                    pyautogui.click()
                    time.sleep(2)
                    pyautogui.moveTo(1220,756,duration = 0.1)
                    pyautogui.click()
                #wifi end
                
                

                elif 'who am i' in query:
                    print(speak)
                    speak('Your name is Masoom Zaid. You are a python programmer.')

                
                elif 'kya kar sakte ho' in query:      
                    speak("Sir I can not        break        the           moon          and            stars             because         won't        be       that       logical        thing ")
                    speak("But !  Sir    i      Do     allthings      what      do       you        want!")

                elif ("jarvis" == query):
                    speak("yes sir")

                #km player automation
                elif 'forward' in query:
                    pyautogui.press('right')

                elif 'more forward' in query:
                    pyautogui.press('right' ,presses=3)

                elif 'backward' in query:
                    pyautogui.press('left')

                elif 'more backward' in query:
                    pyautogui.press('left' ,presses=3)

                elif 'pause' in query:
                    pyautogui.press('space')
                    
                elif 'play' in query:
                    pyautogui.press('space')

                elif 'full screen' in query:
                    pyautogui.hotkey('ctrl','enter')

                elif 'window screen' in query:
                    pyautogui.hotkey('ctrl','enter')


                elif 'jyada karo' in query:
                    pyautogui.press('up',presses = 5)
                
                elif 'kam karo' in query:
                    pyautogui.press('down',presses = 5)
                # KM Player End
                

                elif ("search on google" == query):
                    speak("sir can u tell me what do you want to search on Google")
                    
                    said = takeCommand()
                    text = said
                    speak("Searching google....")
                    chromedriver = "C:\\Users\\Shadab\\Desktop\\jarvis\\chromedriver.exe"
                    driver = webdriver.Chrome(chromedriver)
                    driver.get("https://www.google.co.in/")
                    driver.find_element_by_name("q").send_keys(text)
                    
                    driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()
                    

                elif ("search on youtube" == query):
                    
                    speak("sir can u tell me what do you want to search on Youtube")
                    said = takeCommand()
                    text = said
                    speak("Searching youtube....")
                    driver.get("https://www.youtube.com/")
                    driver.find_element_by_name("search_query").send_keys(text)
                    
                    driver.find_element_by_xpath("//*[@id='search-icon-legacy']/yt-icon").click()
                    

                elif ("search on gaana" == query):
                    
                    speak("sir can u tell me what do you want to search on gaana")
                    said = takeCommand()
                    text = said
                    speak("Searching gaana....")
                    chromedriver = "C:\\Users\\Shadab\\Desktop\\jarvis\\chromedriver.exe"
                    driver = webdriver.Chrome(chromedriver)
                    driver.get("https://gaana.com/")
                    driver.find_element_by_id("sb").send_keys(text)
                    
                    driver.find_element_by_xpath("//*[@id='mainarea']/div[1]/div[2]/div[1]/div[1]/a").click()


                elif 'how are you' in query:
                    speak("i am fine sir thank you for asking!")
                    speak("How can i help you sir")
                    
                elif ("open google" == query):
                    speak("opening google...")
                    webbrowser.open('google.com')

                elif ("google khol do" == query):
                    speak("opening google...")
                    webbrowser.open('google.com')

                elif 'open converter' in query:
                    speak("opening Y 3 Mate...")
                    webbrowser.open("https://www.y2mate.com/en5/download-youtube")
                    

                elif ("open youtube" == query):
                    speak("opening youtube...")
                    webbrowser.open('youtube.com')


                elif 'open gaana' in query:
                    speak("opening gaana...")
                    webbrowser.open("gaana.com")
                
                elif 'open facebook' in query:
                    speak("opening facebook....")
                    webbrowser.open("facebook.com")


                elif 'open codewithharry' in query:
                    speak("opening code with harry....")
                    webbrowser.open("codewithharry.com")

                
                

                elif 'edureka channel' in query:
                    speak("openeing edureka....")
                    webbrowser.open("https://www.youtube.com/channel/UCkw4JCwteGrDHIsyIIKo4tQ")
                     

                elif 'open programming channel' in query:
                    speak("opening sir")
                    webbrowser.open("https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")
                    
                elif 'open stackoverflow' in query:
                    speak("opening stack over flow")
                    webbrowser.open("stackoverflow.com")
                    

                

                elif 'open torrent' in query:
                    speak("opening torrent...")
                    torrent_path = "C:\\Users\\Shadab\\AppData\\Roaming\\uTorrent\\uTorrent.exe"
                    os.startfile(torrent_path)

                elif 'open photoshop' in query:
                    speak("opening photoshop...")
                    photoshop_path = "C:\\Program Files (x86)\Adobe\\Adobe Photoshop CC 2014 (32 Bit)\\Photoshop.exe"
                    os.startfile(photoshop_path)


                elif 'open vs code' in query:
                    speak("opening v s code...")
                    vs_path = "C:\\Users\\Shadab\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(vs_path)

                elif 'open pycharm' in query:
                    speak("opening pycharm...")
                    pycharm_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
                    os.startfile(pycharm_path)

                elif 'open music player' in query:
                    speak("opening  audio  player...")
                    km_path = "C:\\KMPlayer\\KMPlayer.exe"
                    os.startfile(km_path)

                elif 'open project folder' in query:
                    speak("opening projects...")
                    path_fol = "H:\\python projects"
                    os.startfile(path_fol)

                elif  'open full course' in query:
                    speak("opening courses...")
                    path_Lio = "H:\\Learn in one video"
                    os.startfile(path_Lio)

                
                elif  'programming tutorials' in query:
                    speak("opening tutorials...")
                    path_program = "H:\\Programming Videos"
                    os.startfile(path_program)


                elif 'open music folder' in query:
                    speak("opening sir...")
                    path_music = "F:\\New Songs"
                    os.startfile(path_music)

                elif 'play yalgaar song' in query:
                    speak("playing yalgaar ")
                    path_music = "F:\\musics\\15.mp3"
                    os.startfile(path_music)

                elif 'open sublime ' in query:
                    speak("opening sublime.")
                    sublime_path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                    os.startfile(sublime_path)

                elif 'open voice' in query:
                    speak("opening sir!")
                    voice_path = "C:\\Users\\Public\\Desktop\\Vocal Remover Pro.exe"
                    os.startfile(voice_path)

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}") 

                elif 'play songs' in query:
                    os.startfile(random.choice(songs))

                elif 'change song' in query:
                    os.startfile(random.choice(songs))


                elif 'quit' in query:
                    speak("ok sir! have a nice day")
                    exit()

if __name__ == "__main__":
        
    #calling main function
    main()

           
         
