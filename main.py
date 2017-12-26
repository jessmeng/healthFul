####################################
# HackED Projecto
# Brandyn Amado, Jessica Meng 
####################################

from tkinter import *
import copy
import math
import random 

#########################################################
# init
#########################################################

def init(data):
    #mode of data starts at startGame
    data.mode = "startGame"
    
    #for startGame mode 
    data.timerDelay = 100
    #for positive symbol
    data.posSize = 15
    data.posX = 20
    data.posY = 20
    data.posHeadRight, data.posHeadDown = True, True
    #for negative symbol
    data.negSize = 10
    data.negX = 450
    data.negY = 20
    data.negHeadRight, data.negHeadDown = True, True
    data.pop = None
    #for playGame mode 
    data.symbols = [] 
    data.powerUps = []
    #list of positive facts
    data.posFacts = ['''Come up with a meal plan\nfor your week, so you know\nexactly what to buy at the grocery\nstore and you are more accountable\nto yourself (and less likely\nto eat out and unhealthy\nrestaurants)''', '''Go shopping for food on a full\nstomach: When you are hungry, you\nare inclined to buy far more food\nthan you need, and you will\nlikely buy unhealthy foods that you\ncrave.''', '''Spend most of your shopping time\nalong the perimeter of the\ngrocery store: This is where the\nproduce and healthier foods tend to\nbe located. Only venture inward\nif you need something specific\nand you know where it is.''', '''Hydrate Properly: Staying hydrated\nis one of the most important things\nyou can do for your health,\nand it is highly under appreciated.''', '''Use healthier oils: When cooking,\nyou should look for oils that\nhave a high smoke point, such\nas coconut and avocado oil. In\ngeneral, saturated fats are the\nmost stable under heat, so you\nshould cook with those (even\nthough this goes against much of\nwhat you may have heard).''', '''Use mustard instead of mayo,\nBBQ sauce, or ketchup on your\nsandwiches. Mayo is high in trans\nfats, and BBQ sauce and ketchup are\nloaded with high fructose corn\nsyrup. Mustard, on the other hand,\nis a good source of several\nminerals and omega-3 fatty acids.''', '''Season your food with healthy\nspices: Besides adding flavor to\nyour meals, some spices are\nincredibly nutrient dense. Of\nspecial mention are cinnamon,\nturmeric, and ginger.''', '''Take the stairs instead of the\nelevator. It only takes an extra\n2 or 3 minutes at most, and\nsometimes is even faster. Climbing\nstairs is actually great exercise,\nand if you make a habit of it,\nyou will be a far more conditioned\nperson.''', '''Whenever you can, walk: If you\nsimply can’t walk to where you need\nto go, make a point to park\nfurther away from your destination\nand walk the extra block or two.\nSimilarly, you can get off of the\nbus or subway one stop early and\nwalk the rest of the way. Even\nchange the channel on the TV\nitself instead of using the remote.\nBe creative!''', '''Warm up before and cool down after\nyour workout. Most people shrug\nthis off and consider it a waste\nof precious workout time, but it is\nvery important for reducing your\nrisk of injury as well as\nimproving your performance.''']
    #list of negative facts
    data.negFacts = ['''About 80 percent of people in\ndeveloping countries rely on local\nestablishments for health care.\nThis is often in the form of\nill-equipped clinics and local\nhealers. There are no ambulances or\nemergency help numbers. People\noften have to walk, sometimes\nfor days, to get to a ecent clinic\nor hospital.''', '''Many people don't practice\nrudimentary disease prevention\nmeasures such as keeping water\ncovered, washing vegetables,\nbrushing teeth, vaccinating\nchildren, taking the garbage\naway from the house and screening\nwindows against flies and\nmosquitos.''', '''Bringing good health care to\npoor rural areas is no easy task.\nOne doctor who travels widely from\nvillage to village told the New\nYork Times, "When we go out and try\nto inoculate babies, some peasants\nare very frightened and hide their\nkids. Or they turn their dogs on us\nto bite us and drive us away...\nWe give them injections for measles,\nand then the kid gets a cold. \nSo the parents come and complain.\nThey say, "You promised that my\nchild wouldn't get sick!"''', '''Some developing countries have a\nsocial security medical system\nthat guarantees coverage for\neveryone, but sometimes that\ncoverage is less than ideal.\nWhen patients go to a hospital,\nthey have wait to get a number,\nthen go to another window,\nand get another number and wait \nagain. To get into a hospital\nsometimes people starting lining\nup at 3 o'clock in the morning\nto squeeze through the doors.''', '''Channeling heath care money into\nbasic care is often far more\ncost effective than putting it into\nexpensive treatment. For example,\n"basic treatment for leukemia costs\nabout $5,000 and on average adds\na bit more than a month to a\npatient's life. The same $5,000,\nused to buy vitamin A supplements\nfor children, adds a total of\n10,000 years of life expectancy"\n(The New York Times).''', '''There are good clinics and\nhospitals and bad ones. Most are\nclean and neat, the doctors and\nnurses are well trained and\ndisciplined, and good records and\ncharts are kept on the patient,\nbut shortages of medicines, \nsterilized needles and supplies\nare common.''', '''A typical rural clinic is made\nof cement blocks and has unglazed\nwindows and no screens. There is\nno fan, and flies are everywhere.\nThe worst clinics have nothing\nand medical care is provided on\na day to day basis by an untrained\nvillager with some knives and\npliers and instructions to give out\nmalaria pills if someone has a\nfever. Broken bones, in spiome cases,\nare not set, and people often\ndie of easily treatable diseases\nlike flu, diarrhea and measles.''', '''It is not uncommon for hospitals\nto lose electricity because of\npower shortages, to lose radio\ncontact with the outside world\nbecause they are unable to pay\ntheir electricity bills, and to\nlose their ability to provide\nambulance service because there is\nno money for gas. The supply\nof basic medicines is variable. \nWell-stocked clinics are often\nthat way through the work of\nlucky, aggressive and\nwell-connected pharmacists.''', '''Doctors do everything from\nset bones to perform major surgery.\nNurses give treatment and medicines\nbut generally don't care for\npatients (that is done by their\nfamilies). Clinic workers with\nonly a secondary education\nroutinely pull teeth, perform\nappendectomies and deliver babies.\nPharmacists give advise and\ndispense a wide variety of drugs\nand medicines over the counter\nthat are only available with a\nprescription in the United States.''', '''Many medical personnel in\nthird-world countries are not in\nthe habit of washing hands between\npatients, as working taps existed\nat only a few points in the\nbuilding -- most of the examining\nrooms had taps, but they were\nnot connected.''']
    data.score, data.timeLeft = 0, 60
    #for the player
    data.playX = data.width/2
    data.playY = data.height - 80
    data.playSpX = 0
    data.time = 0 
    #for the power up
    data.powerSize = 20
    data.powerX = 20
    data.powerY = 20
    data.spedUp = False
    data.mult = 1
    #pauses/unpauses the game
    data.isPaused = False 
    #for the fact screen pop up with message 
    data.factOnScreen = False
    data.factIsPos = False
    data.message = 0
    
####################################
# mode dispatcher
####################################

#goes to individual mode mousePressed functions
def mousePressed(event, data):
    if (data.mode == "startGame"): 
        startGameMousePressed(event, data)
    elif (data.mode == "playGame"):   
        playGameMousePressed(event, data)
    elif (data.mode == "instructionScreen"):   
        instructionScreenMousePressed(event, data)
    elif (data.mode == "gameOver"):   
        gameOverMousePressed(event, data)

#goes to individual mode keyPressed functions
def keyPressed(event, data):
    if (data.mode == "startGame"): 
        startGameKeyPressed(event, data)
    elif (data.mode == "playGame"):
        playGameKeyPressed(event, data)
    elif (data.mode == "instructionScreen"):   
        instructionScreenKeyPressed(event, data)
    elif (data.mode == "gameOver"):   
        gameOverKeyPressed(event, data)

#goes to individual mode timerFired functions
def timerFired(data):
    if (data.mode == "startGame"): 
        startGameTimerFired(data)
    elif (data.mode == "playGame"):   
        playGameTimerFired(data)
    elif (data.mode == "instructionScreen"):   
        instructionScreenTimerFired(data)
    elif (data.mode == "gameOver"):   
        gameOverTimerFired(data)

#goes to individual mode redrawAll functions
def redrawAll(canvas, data):
    if (data.mode == "startGame"): 
        startGameRedrawAll(canvas, data)
    elif (data.mode == "playGame"):   
        playGameRedrawAll(canvas, data)
    elif (data.mode == "instructionScreen"):   
        instructionScreenRedrawAll(canvas, data)
    elif (data.mode == "gameOver"):   
        gameOverRedrawAll(canvas, data)

####################################
# startGame mode
####################################

#draws the starting board
def drawStart(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "lavender", outline = "MediumPurple1", width = 15)
    canvas.create_text(data.width/2 - 65, data.height/3, text = "health", fill = "SlateBlue3", font = "Courier 60 bold")
    canvas.create_text(data.width/2 + 105, data.height/3, text = "Ful", fill = "maroon4", font = "Courier 60 bold")
    canvas.create_text(data.width/2 + 165, data.height/3.5, text = "TM", fill = "LightSalmon4", font = "Courier 15 bold")
    canvas.create_text(data.width/2, data.height/2.3, text = "\"a healthful (helpful) game\"", fill = "IndianRed3", font = "Courier 20 bold")
    canvas.create_text(data.width/2, data.height/2.1, text = "created by Brandyn Amado and Jessica Meng", fill = "IndianRed4", font = "Courier 18 bold")
    canvas.create_text(data.width/2, data.height*2.7/4, text = "Press \'i\' for instructions!", fill = "aquamarine4", font = "Courier 25 bold")
    canvas.create_text(data.width/2, data.height*3/4, text = "Press \'p\' to play!", fill = "turquoise4", font = "Courier 25 bold")

#draws the bouncing positive symbol in the beginning
def drawPos(canvas, data):
    canvas.create_oval(data.posX - data.posSize, data.posY - data.posSize, data.posX + data.posSize, data.posY + data.posSize, outline = "light sky blue", width = 4)
    
#draws the bouncing negative symbol in the beginning
def drawNeg(canvas,data):
    canvas.create_rectangle(data.negX, data.negY, data.negX + 3*data.negSize, data.negY + data.negSize, fill = "red", width = 0)
    canvas.create_rectangle(data.negX + data.negSize, data.negY - data.negSize, data.negX + 2*data.negSize, data.negY + 2*data.negSize, fill = "red", width = 0)

#move functions for having the positive symbol animated
def movePosLeft(data):
    data.posX -= random.randint(1, 10)
def movePosRight(data):
    data.posX += random.randint(1, 10)
def movePosUp(data):
    data.posY -= random.randint(1, 10)
def movePosDown(data):
    data.posY += random.randint(1, 10)
    
#move functions for having the negative symbol animated
def moveNegLeft(data):
    data.negX -= random.randint(1, 10)
def moveNegRight(data):
    data.negX += random.randint(1, 10)
def moveNegUp(data):
    data.negY -= random.randint(1, 10)
def moveNegDown(data):
    data.negY += random.randint(1, 10)

#moves the positive symbol, allows it to bounce around
def movePos(data):
    if (data.posHeadRight == True):
        if (data.width - 40 <= data.posX + data.posSize):
            data.posHeadRight = False
        movePosRight(data)
    else:
        if (data.posX <= 40):
            data.posHeadRight = True
        movePosLeft(data)
    if (data.posHeadDown == True):
        if (data.height - 40 <= data.posY + data.posSize):
            data.posHeadDown = False
        movePosDown(data)
    else:
        if (data.posY <= 40):
            data.posHeadDown = True
        movePosUp(data)
        
#moves the negative symbol, allows it to bounce around
def moveNeg(data):
    if (data.negHeadRight == True):
        if (data.width - 40 <= data.negX + data.negSize):
            data.negHeadRight = False
        moveNegRight(data)
    else:
        if (data.negX <= 40):
            data.negHeadRight = True
        moveNegLeft(data)
    if (data.negHeadDown == True):
        if (data.height - 40 <= data.negY + data.negSize):
            data.negHeadDown = False
        moveNegDown(data)
    else:
        if (data.negY <= 40):
            data.negHeadDown = True
        moveNegUp(data)

def startGameMousePressed(event, data):
    if event.x < 500:
        data.mode = "playGame"

#if "p" is pressed, go to playGame mode
def startGameKeyPressed(event, data):
    #splash screen to instructionScreen mode
    if (event.keysym == "i"):
        data.mode = "instructionScreen"
    #splash screen to playGame mode
    elif (event.keysym == "p"):
        data.mode = "playGame"

#moves the positive and negative symbols around
def startGameTimerFired(data):
    movePos(data)
    moveNeg(data)

#draws the starting background and moving positive and negative symbols
def startGameRedrawAll(canvas, data):
    drawStart(canvas, data)
    drawPos(canvas, data)
    drawNeg(canvas, data)
    
####################################
# instructionScreen mode
####################################

#draws the instruction screen
def drawHelp(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "white smoke", outline = "powder blue", width = 15)
    canvas.create_text(data.width/2, data.height/6, text = "Instructions:", fill = "navy", font = "Courier 35 bold")
    canvas.create_oval(data.width/4 - 40, data.height*1.2/4, data.width/4 - 10, data.height*1.2/4 + 30, outline = "light sky blue", width = 4)
    canvas.create_rectangle(data.width/4 - 40, data.height*1.4/3, data.width/4 - 30, data.height*1.4/3 + 35, fill = "red", width = 0)
    canvas.create_rectangle(data.width/4 - 52, data.height*1.4/3 + 12, data.width/4 - 17, data.height*1.4/3 + 22, fill = "red", width = 0)
    canvas.create_text(data.width/2 + 40, data.height/3 - 7, text = "Positive symbol! (Retrieve)", fill = "black", font = "Courier 18 bold")
    canvas.create_text(data.width/2 + 30, data.height/3 + 15, text = "Good health practices (+10)", fill = "black", font = "Courier 15 bold")
    canvas.create_text(data.width/2 + 30, data.height/3 + 75, text = "Negative symbol! (Avoid)", fill = "black", font = "Courier 18 bold")
    canvas.create_text(data.width/2 + 40, data.height/3 + 98, text = "Health issues/bad health practices (+0)", fill = "black", font = "Courier 15 bold")
    outRad = 20
    inOut = 0.382
    inRad = (outRad * inOut)
    allPoints = []
    for point in range(2 * 5):
        angleOfPoint = math.pi/2 - (2*math.pi)*(point/(5*2))
        #if point is even, use the outer radius 
        if (point % 2 == 0):
            pointRad = outRad
        #if point is odd, use the inner radius
        if (point % 2 == 1):
            pointRad = inRad
        #point X and point Y 
        pointX = 100 + (pointRad*math.cos(angleOfPoint))
        pointY = 340 - (pointRad*math.sin(angleOfPoint))
        allPoints += (pointX, pointY)
    canvas.create_polygon(allPoints, fill = "yellow")
    canvas.create_text(data.width/2 + 30, data.height/3 + 165, text = "Power Up!", fill = "black", font = "Courier 18 bold")
    canvas.create_text(data.width/2 + 40, data.height/3 + 188, text = "2x speed for 5 seconds (+20)", fill = "black", font = "Courier 15 bold")
    canvas.create_text(data.width/2, data.height*3.75/5 + 45, text = "Press \'s\' to go back to the Start Screen", fill = "dark slate blue", font = "Courier 18 bold")
    canvas.create_text(data.width/2, data.height*4.1/5 + 45, text = "Press \'r\' to start/resume play", fill = "purple4", font = "Courier 20 bold")
    
def instructionScreenMousePressed(event, data):
    pass

#game goes back to startScreen mode or to playGame mode
def instructionScreenKeyPressed(event, data):
    #splash screen to startScreen mode
    if (event.keysym == "s"):
        data.mode = "startGame"
    #splash screen to playGame mode
    elif (event.keysym == "r"):
        data.mode = "playGame"

def instructionScreenTimerFired(data):
    pass 
    
#creates the instruction screen 
def instructionScreenRedrawAll(canvas, data):
    drawHelp(canvas, data)
    
####################################
# playGame mode
####################################

#draw Background
def drawBackground(canvas, data):
    #side building and sky
    canvas.create_rectangle(0,0,data.width,data.height - 20,fill = "midnight blue")
    canvas.create_rectangle(30,250,200,data.height - 20, width = 5, outline = "black", fill = "honeydew")
    canvas.create_rectangle(100,375,200,data.height - 20,width = 0, fill = "honeydew2")
    canvas.create_rectangle(75,375,100,data.height - 20, width = 5, outline = "black", fill = "honeydew")
    canvas.create_rectangle(60,350,200,375, width = 5, outline = "black", fill = "honeydew")
    #main building and stairs
    canvas.create_rectangle(200,100,data.width - 35,data.height - 20, width = 5, outline = "black", fill = "honeydew")
    canvas.create_rectangle(285,360,data.width - 120,data.height - 60,fill = "cyan", width = 0)
    canvas.create_line(333,360,333,data.height - 60, fill = "black", width = 5)
    canvas.create_oval(314,396,324,406, fill = "gray29", width = 3)
    canvas.create_oval(352,396,342,406, fill = "gray29", width = 3)
    canvas.create_rectangle(230,data.height - 40,data.width - 65,data.height - 20, fill = "light gray", width = 5)
    canvas.create_rectangle(240,data.height - 60,data.width - 75,data.height - 40, fill = "light gray", width = 5)
    canvas.create_rectangle(260,360,285,data.height - 60, width = 5, outline = "black", fill = "honeydew")
    canvas.create_rectangle(data.width - 120,360,data.width - 95,data.height - 60, width = 5, outline = "black", fill = "honeydew")
    canvas.create_rectangle(240,335,data.width - 75,360, width = 5, outline = "black", fill = "honeydew")
    #grass
    canvas.create_rectangle(0,data.height - 20,data.width + 10,data.height + 10,fill = "green", width = 5)

    #windows
    for i in range(3):
        drawWindow(canvas,45 + i*50,270,40)
    canvas.create_oval(290,115,370,195,fill = "honeydew", width = 4)
    canvas.create_rectangle(300, 150, 300 + 6*data.negSize, 150 + data.negSize, fill = "red", width = 0)
    canvas.create_rectangle(295 + 3*data.negSize, 135 - data.negSize, 305 + 3*data.negSize, 175 + data.negSize, fill = "red", width = 0)
    for j in range(4):
        drawWindow(canvas,215 + j*60,205,50)
    for k in range(4):
        drawWindow(canvas,215 + k*60,270,50)
    
# draws windows
def drawWindow(canvas, x, y, w):
    sideL = w
    canvas.create_rectangle(x, y, x + sideL, y + sideL, width = 5, fill = "cyan")

#draws the Time Left, Score, and help for Instructions displayed during the game 
def drawTimeAndScore(canvas, data):
    timeLeft = "Time Left: " + str(data.timeLeft)
    canvas.create_text(100, data.height/16, text = timeLeft, fill = "white", font = "Courier 20 bold")
    score = "Score: " + str(data.score)
    canvas.create_text(75, data.height/9, text = score, fill = "white", font = "Courier 20 bold")
    canvas.create_text(data.width*3.75/5, data.height/16, text = "Press \'h\' for help", fill = "white", font = "Courier 16 bold")
    canvas.create_text(data.width*3.4/5, data.height/9, text = "Press \'p\' to pause/unpause", fill = "white", font = "Courier 16 bold")

#draws the player    
def drawPlayer(canvas,data):
    #for the head
    headR = 15
    canvas.create_oval(data.playX - headR, data.playY - headR, data.playX + headR, data.playY + headR, fill = "tan", width = 5, outline = "black")
    #for the body
    bodyL = 35
    canvas.create_line(data.playX, data.playY + headR, data.playX, data.playY + headR + bodyL, width = 5, fill = "black")
    #for the arms and legs 
    legL = 25
    canvas.create_line(data.playX, data.playY + headR + bodyL, data.playX - headR, data.playY + headR + bodyL + legL, width = 5, fill = "black")
    canvas.create_line(data.playX, data.playY + headR + bodyL, data.playX + headR, data.playY + headR + bodyL + legL, width = 5, fill = "black")
    canvas.create_line(data.playX, data.playY + headR + 10, data.playX - 2*headR, data.playY, width = 5, fill = "black")
    canvas.create_line(data.playX, data.playY + headR + 10, data.playX + 2*headR, data.playY, width = 5, fill = "black")

#creates new power up to list data.powerUps
def createPowerUp(data):
    x = random.randint(50, 450)
    y = 0
    data.powerUps.append([x,y])  
    
#draws the power up (star) 
def drawPowerUp(canvas, data):
    for i in range(len(data.powerUps)):
        centerX = data.powerUps[i][0]
        centerY = data.powerUps[i][1]
        outRad = data.powerSize
        inOut = 0.382
        inRad = (outRad * inOut)
        allPoints = []
        for point in range(2 * 5):
            angleOfPoint = math.pi/2 - (2*math.pi)*(point/(5*2))
            #if point is even, use the outer radius 
            if (point % 2 == 0):
                pointRad = outRad
            #if point is odd, use the inner radius
            if (point % 2 == 1):
                pointRad = inRad
            #point X and point Y 
            pointX = centerX + (pointRad*math.cos(angleOfPoint))
            pointY = centerY - (pointRad*math.sin(angleOfPoint))
            allPoints += (pointX, pointY)
        canvas.create_polygon(allPoints, fill = "yellow")

#creates new symbol to list data.symbols
def createSymbol(data):
    x = random.randint(50, 450)
    y = 0
    #s for symbol
    s = random.randint(0, 1) 
    data.symbols.append([x,y,s])   
    
#draws the symbol based on list data.symbols
def drawSymbols(canvas, data):
    for i in range(len(data.symbols)):
        x = data.symbols[i][0]
        y = data.symbols[i][1]
        s = data.symbols[i][2]
        if (s == 0):
            canvas.create_rectangle(x, y, x + 3*data.negSize, y + data.negSize, fill = "red", width = 0)
            canvas.create_rectangle(x + data.negSize, y - data.negSize, x + 2*data.negSize, y + 2*data.negSize, fill = "red", width = 0)
        elif (s == 1):
            canvas.create_oval(x - data.posSize, y - data.posSize, x + data.posSize, y + data.posSize, outline = "light sky blue", width = 4)
    
#checks for collisions between player and symbols and power ups 
def collision(data):
    #for the symbols
    for i in range(len(data.symbols)):
        x = data.symbols[i][0]
        y = data.symbols[i][1]
        s = data.symbols[i][2]
        if (s == 0):
            if ((data.playX - 15 - 10 <= x + data.negSize and data.playX + 15 + 10 >= x) and (data.playY - 15 - 9 <= y + data.negSize and data.playY + 15 - 9 >= y)):
                data.pop = i
                data.score += 0
                data.isPaused = True
                data.factOnScreen = True
                data.factIsPos = False
                data.message = random.randint(0, 9)
                break
        if (s == 1):
            if ((data.playX - 15 - 10 <= x + data.posSize and data.playX + 15 + 10 >= x) and (data.playY - 15 - 3 <= y + data.posSize and data.playY + 15 - 3 >= y)):
                data.pop = i
                data.score += 10
                data.isPaused = True
                data.factOnScreen = True
                data.factIsPos = True
                data.message = random.randint(0, 9)
                break
    #for the power ups
    for i in range(len(data.powerUps)):
        x = data.powerUps[i][0]
        y = data.powerUps[i][1]
        if ((data.playX - 15 - 10 <= x + (0.5*data.powerSize) and data.playX + 15 >= x) and (data.playY - 15 <= y + (0.5*data.powerSize) and data.playY + 15 >= y)):
            data.powerUps.pop(i)
            data.score += 20
            data.spedUp = True
            data.t1 = data.time
            break
                
#pops up a fact screen every time the player hits a symbol
def factScreen(canvas, data):
#for the negative facts
    if (not data.factIsPos):
        canvas.create_rectangle(data.width/6, data.height/6, data.width*5/6, data.height*5/6, fill = "LightSalmon2", outline = "OrangeRed4", width = 3)
        canvas.create_text(data.width/6 + 120, data.height/6 + 10, text = "Uh-Oh!", fill = "red3", anchor = "nw", font = "Courier 30 bold")
        canvas.create_text(data.width/6 + 10, data.height/6 + 50, text = "Fact:", fill = "brown", anchor = "nw", font = "Courier 20 bold")
        canvas.create_text(data.width/6 + 10, data.height/6 + 80, text = data.negFacts[data.message], fill = "black", anchor = "nw", font = "Courier 15 bold")
        canvas.create_text(data.width/6 + 22, data.height/6 + 310, text = "Press \'p\' to continue playing", fill = "brown", anchor = "nw", font = "Courier 16 bold")
#for the positive facts 
    elif(data.factIsPos):
        canvas.create_rectangle(data.width/6, data.height/6, data.width*5/6, data.height*5/6, fill = "DarkSlateGray2", outline = "RoyalBlue4", width = 3)
        canvas.create_text(data.width/6 + 80, data.height/6 + 10, text = "Good work!", fill = "blue2", anchor = "nw", font = "Courier 30 bold")
        canvas.create_text(data.width/6 + 10, data.height/6 + 50, text = "Tip:", fill = "DodgerBlue4", anchor = "nw", font = "Courier 20 bold")
        canvas.create_text(data.width/6 + 10, data.height/6 + 80, text = data.posFacts[data.message], fill = "black", anchor = "nw", font = "Courier 15 bold")
        canvas.create_text(data.width/6 + 22, data.height/6 + 310, text = "Press \'p\' to continue playing", fill = "DodgerBlue4", anchor = "nw", font = "Courier 16 bold")
        
def spedUpText(canvas, data):
    canvas.create_text(data.width/5, data.height/4, text = "Power Up!", fill = "yellow", anchor = "center", font = "Courier 30 bold") 
        
def playGameMousePressed(event, data):
    pass
    
#moves player based on key pressed 
def playGameKeyPressed(event, data):
    if(not data.isPaused) and (event.keysym == "Left"):
        data.playSpX = -10*data.mult
    elif(not data.isPaused) and (event.keysym == "Right"):
        data.playSpX = 10*data.mult
    elif (event.keysym == "h"):
        data.mode = "instructionScreen"
    elif (event.keysym == "p"):
        data.isPaused = not data.isPaused
        if (data.factOnScreen):
            data.factOnScreen = False
            data.symbols.pop(data.pop)

#makes player stop when key is released
def playGameKeyReleased(event,data):
    if(event.keysym == "Left"):
        data.playSpX = 0
    elif(event.keysym == "Right"):
        data.playSpX = 0

#when timer starts, timeLeft decreases by 1 until it gets to 0
def playGameTimerFired(data):
    data.timerDelay = 50
    if (not data.isPaused):
        data.time += 1
        if(data.time % 20 == 0):
            data.timeLeft -= 1
        if (data.timeLeft == 0):
            data.mode = "gameOver"
        data.playX += data.playSpX
        #adds new symbol every half second
        if (data.time % 50 == 0):
            createSymbol(data)
        if (data.time % 200 == 0):
            createPowerUp(data)
        if (data.time % 2 == 0):
            for i in range(len(data.symbols)):
                data.symbols[i][1] += 10
            for i in range(len(data.powerUps)):
                data.powerUps[i][1] += 10
        #bounds
        if (data.playX <= 45):
            data.playSpX = 0
            data.playX = 45
        if (data.playX >= data.width - 45):
            data.playSpX = 0
            data.playX = data.width - 45
        collision(data)
        #power up
        if(data.spedUp):
            if(data.time - data.t1 < 100):
                data.mult = 2
            else:
                data.mult = 1
                data.spedUp = False

#draws the border, random negs within the border, and the timeLeft and Score
#in the upper left and bottom left corner
def playGameRedrawAll(canvas, data):
    drawBackground(canvas, data)
    drawTimeAndScore(canvas, data)
    drawPlayer(canvas,data)
    drawSymbols(canvas, data)
    drawPowerUp(canvas, data)
    if(data.spedUp):
        spedUpText(canvas, data)
    if(data.factOnScreen):
        factScreen(canvas, data)

####################################
# gameOver mode
####################################

#draws the end board
def drawEnd(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "azure", outline = "pale green", width = 15)
    canvas.create_text(data.width/2, data.height/3, text = "GAME OVER!", fill = "steel blue", font = "Courier 60 bold")
    finalScore = "Final Score: " + str(data.score)
    canvas.create_text(data.width/2, data.height/2 - 20, text = finalScore, fill = "maroon", font = "Courier 35 bold")
    canvas.create_text(data.width/2, data.height*2/3 - 10, text="Take care of yourself!", fill = "dark green", font = "Courier 25 bold")
    canvas.create_text(data.width/2, data.height*4/5 - 30, text="Press \'space\' to play again!", fill = "dark violet", font = "Courier 20 bold")
    canvas.create_text(data.width/2 - 35, data.height*4/5 + 40, text = "health", fill = "SlateBlue3", font = "Courier 30 bold")
    canvas.create_text(data.width/2 + 50, data.height*4/5 + 40, text = "Ful", fill = "maroon4", font = "Courier 30 bold")
    canvas.create_text(data.width/2 + 83, data.height*4/5 + 30, text = "TM", fill = "LightSalmon4", font = "Courier 10 bold")
    
#draws the bouncing positive symbol in the end
def drawPos(canvas, data):
    canvas.create_oval(data.posX - data.posSize, data.posY - data.posSize, data.posX + data.posSize, data.posY + data.posSize, outline = "light sky blue", width = 4)
    
#draws the bouncing negative symbol in the end
def drawNeg(canvas,data):
    canvas.create_rectangle(data.negX, data.negY, data.negX + 3*data.negSize, data.negY + data.negSize, fill = "red", width = 0)
    canvas.create_rectangle(data.negX + data.negSize, data.negY - data.negSize, data.negX + 2*data.negSize, data.negY + 2*data.negSize, fill = "red", width = 0)

#move functions for having the positive symbol animated
def movePosLeft(data):
    data.posX -= random.randint(1, 10)
def movePosRight(data):
    data.posX += random.randint(1, 10)
def movePosUp(data):
    data.posY -= random.randint(1, 10)
def movePosDown(data):
    data.posY += random.randint(1, 10)
    
#move functions for having the negative symbol animated
def moveNegLeft(data):
    data.negX -= random.randint(1, 10)
def moveNegRight(data):
    data.negX += random.randint(1, 10)
def moveNegUp(data):
    data.negY -= random.randint(1, 10)
def moveNegDown(data):
    data.negY += random.randint(1, 10)

#moves the positive symbol, allows it to bounce around
def movePos(data):
    if (data.posHeadRight == True):
        if (data.width - 40 <= data.posX + data.posSize):
            data.posHeadRight = False
        movePosRight(data)
    else:
        if (data.posX <= 40):
            data.posHeadRight = True
        movePosLeft(data)
    if (data.posHeadDown == True):
        if (data.height - 40 <= data.posY + data.posSize):
            data.posHeadDown = False
        movePosDown(data)
    else:
        if (data.posY <= 40):
            data.posHeadDown = True
        movePosUp(data)
        
#moves the negative symbol, allows it to bounce around
def moveNeg(data):
    if (data.negHeadRight == True):
        if (data.width - 40 <= data.negX + data.negSize):
            data.negHeadRight = False
        moveNegRight(data)
    else:
        if (data.negX <= 40):
            data.negHeadRight = True
        moveNegLeft(data)
    if (data.negHeadDown == True):
        if (data.height - 40 <= data.negY + data.negSize):
            data.negHeadDown = False
        moveNegDown(data)
    else:
        if (data.negY <= 40):
            data.negHeadDown = True
        moveNegUp(data)
        
def gameOverMousePressed(event, data):
    pass

#game starts again from startGame mode
def gameOverKeyPressed(event, data):
    #splash screen to startGame mode
    if (event.keysym == "space"):
        #sets everything back to init function
        init(data)

#to move positive and negative symbols
def gameOverTimerFired(data):
    movePos(data)
    moveNeg(data)
    
#creates the end screen (with "GAME OVER" text, etc.) and symbols
def gameOverRedrawAll(canvas, data):
    drawEnd(canvas, data)
    drawPos(canvas, data)
    drawNeg(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)
        
    def keyReleasedWrapper(event, canvas, data):
        playGameKeyReleased(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    root.title("healthFul")
    root.resizable(False, False)
    canvas = Canvas(root, width=data.width, height=data.height)
    data.canvas = canvas
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<KeyPress>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<KeyRelease>", lambda event:
                            keyReleasedWrapper(event,canvas,data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("Go healthy living!")

def main():
    run(500, 500)

if __name__ == '__main__':
    main()