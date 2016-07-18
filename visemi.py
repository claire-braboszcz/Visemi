from psychopy import visual, core, event, logging, gui, data
import os, time
import csv

stimpath= '/home/claire/Documents/Experiment/Imagery/Stimuli/' 
#vismaskpath = '/home/claire/Documents/Experiment/Imagery/Clips/Animal/'
#pixpath = '/home/claire/Documents/Experiment/Imagery/Frames/Animals/cat_frame.png' 

if not os.path.exists(stimpath):
        raise RuntimeError("Video File could not be found:"+stimpath)

#if not os.path.exists(vismaskpath):
#        raise RuntimeError("Video File could not be found:"+vismaskpath)

#if not os.path.exists(pixpath):
#        raise RuntimeError("Video File could not be found:"+pixpath)


TRIALS_FILE = 'movie_block.csv'

#---------------------------------------
# Store info about the experiment session
#---------------------------------------

expName = 'Visemi'  
expInfo = {'participant':'', 'session': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel  
expInfo['date'] = data.getDateStr()  # add a simple timestamp  
expInfo['expName'] = expName



# Experiment handler
thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
	originPath=None,
	savePickle=False, 
	saveWideText=False) #prevent the experiment handler to write expe data upon termination (and overwriting our files)
	

#--------------------------------------
# Load trial files 
#---------------------------------------

# read from csv file
trialList = data.importConditions(TRIALS_FILE, returnFieldNames=False)
trials = data.TrialHandler(trialList, nReps=1, method='sequential', extraInfo=expInfo)
trials.data.addDataType('respKey')
trials.data.addDataType('respTime')
trials.data.addDataType('stimOnset')
trials.data.addDataType('maskOnset')
trials.data.addDataType('imOnset')
trials.data.addDataType('imStop')
trials.data.addDataType('scale1')
trials.data.addDataType('RTscale1')
trials.data.addDataType('scale2')
trials.data.addDataType('RTscale2')
trials.data.addDataType('scale3')
trials.data.addDataType('RTscale3')
#----------------
# Set up logging 
#----------------

globalClock = core.Clock()
respTime= core.Clock()
trialClock=core.Clock()

logging.console.setLevel(logging.DEBUG)
#
if not os.path.isdir('Logdata'):
    os.makedirs('Logdata')  # if this fails (e.g. permissions) we will get error
filename = 'Logdata' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['session'])
logging.setDefaultClock(globalClock)
logFileExp = logging.LogFile(filename +'.log', level=logging.EXP)
logging.console.setLevel(logging.DEBUG)  # this outputs to the screen, not a file

saveFilePrefix = expInfo['participant'] + '_' + expInfo['session']

saveFile = "data/" + str(saveFilePrefix) + ' (' + time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()) +').csv'  # Filename for csv. E.g. "myFolder/subj1_cond2 (2013-12-28 09-53-04).csv"




#--------------------------------------
#Define experiment constant 
#--------------------------------------

win = visual.Window(size=(1024, 768), 
        fullscr=True, 
        screen=0, 
        allowGUI=False, 
        allowStencil=False, 
        monitor='testMonitor', 
        color=[0,0,0], 
        colorSpace='rgb', 
        blendMode='avg', 
        useFBO=True,)



fix_cross = visual.TextStim(win =win, 
        ori =0, 
        name='fix_cross', 
        text= '+',
        font= 'Arial', 
        pos=[0,0],
        height = 0.06, 
        color='black'
        )


circle = visual.TextStim(win =win, 
        ori =0, 
        name='fix_cross', 
        text= 'o',
        font= 'Arial', 
        pos=[0,0],
        height = 0.06, 
        color='black'
        )






#---------------------------------------
# Setup end message
#--------------------------------------- 
#instrPracticeClock = core.Clock()
theEnd = visual.TextStim(win=win, ori=0, name='theEnd',
    text="End of the experiment, thank you !", font='Arial',
    pos=[0, 0], height=0.04, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

pause = visual.TextStim(win=win, ori=0, name='pause',
    text="End of the first part of the experiment", font='Arial',
    pos=[0, 0], height=0.04, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)



#-------------------------------------------
# Set Keys for response and experiment flow 
#-------------------------------------------

keyStop = ['space'] # indicate stop of movie clip and stop of mental imagery


mouse= event.Mouse()

#-------------------------------------------------------------
# Define rating scale and questionnaire after each MI trial 
#-------------------------------------------------------------
move_quest = visual.TextStim(win, 
        name = 'movequest', 
        text = 'Was your mental image moving or still ?',
        height= 0.07, 
        units= 'norm'
        )

moveRatingScale= visual.RatingScale (win, 
        choices= ['still image','don''t know', 'moving image'], 
       )


sim_quest = visual.TextStim(win, 
        name = 'simquest', 
        text = 'Was your mental image similar or different from the stimuli ?',
        height= 0.07, 
        units= 'norm'
        )

simRatingScale= visual.RatingScale (win, 
        choices= ['different','don''t know', 'similar'], 
       )

eff_quest = visual.TextStim(win, 
        name = 'effquest', 
        text = 'How effortful was it to generate the mental image ?',
        height= 0.07, 
        units= 'norm'
        )

effRatingScale= visual.RatingScale (win, 
        choices= ['easy','don''t know', 'difficult'], 
       )

#-----------------
# Fixation cross 
#-----------------

def fixation():
    fix_cross.draw()
    win.flip()
#    core.wait(1)

#------------------
# Questionnaire 
#------------------

def pheno():
    #event.clear(Events)
    while moveRatingScale.noResponse: 
        move_quest.draw()
        moveRatingScale.draw()
        win.flip()

    while simRatingScale.noResponse: 
        sim_quest.draw()
        simRatingScale.draw()
        win.flip()



    while effRatingScale.noResponse: 
        eff_quest.draw()
        effRatingScale.draw()
        win.flip()


    #event.clear(Events)

    trials.addData('scale1', moveRatingScale.getRating())
    trials.addData('RTscale1', moveRatingScale.getRT())
    trials.addData('scale2', simRatingScale.getRating())
    trials.addData('RTscale2',  simRatingScale.getRT())
    trials.addData('scale3', effRatingScale.getRating())
    trials.addData('RTscale3', effRatingScale.getRT())

    moveRatingScale.reset()
    simRatingScale.reset()
    effRatingScale.reset()

#-------------
# Play movie 
#-------------

def playclip(stimpath, stim):
    fixation()
    core.wait(1)
    clip = visual.MovieStim(win=win,
            name= 'clip', 
            filename= stimpath + stim,
            size = [800, 450],
            ori =0, 
            pos=[0,0], 
            opacity =1, 
            depth = -1.0
            )
    while clip.status != visual.FINISHED:
        clip.draw()
        stimOnset= trialClock.getTime()
        win.flip()

    fixation()
    # get key press at the end of clip
    event.waitKeys(keyList=keyStop)
    respTime= trialClock.getTime()
    #mouse.clickReset()
    #button, time = mouse.getPressed(getTime=True)
    #print('mouse: ', button)
    
    #event.waitKeys(keyList= button)
    trials.addData('stimOnset', stimOnset)
    trials.addData('respTime',respTime)  
#------------------------
# Play visual noise
#------------------------

def playmask(stimpath, stim):
    vismask = visual.MovieStim(win =win,
             filename= stimpath + stim, 
            #image = '/home/claire/Documents/Experiment/Imagery/Clips/Animal/s_frame_cat' + str(n) +'.png',
             pos = [0,0],
             size = [800,450],
             opacity =1, 
             units = 'pix'
             )
    
    while vismask.status != visual.FINISHED:
        vismask.draw()
        maskOnset= trialClock.getTime()
        win.flip()

    trials.addData('maskOnset', maskOnset)  

#------------------
# Show picture 
#------------------

def showpix(stimpath, stim):
    fixation()
    pix = visual.ImageStim(win =win, 
            image = stimpath + stim, 
            pos = [0,0], 
            size = [800, 450], 
            opacity = 1,
            units = 'pix'
            )

    pix.draw()    
    stimOnset= trialClock.getTime()
    win.flip()
    core.wait(1)
    event.waitKeys(keyList=keyStop)
    #mouse.getPressed()


    trials.addData('stimOnset', stimOnset)
    trials.addData('respTime',respTime)  



#------------------------
# Mental Imagery trial 
#------------------------


def imagery():
    circle.draw()
    imOnset = trialClock.getTime()
    win.flip()   
    event.waitKeys(keyList=keyStop)
    imStop = trialClock.getTime()


    trials.addData('imOnset', imOnset)
    trials.addData('imStop', imStop)  



#---------------------
# Define Movie Block 
#---------------------

def movieblock(stim, mask):    
    # play video clip
    playclip(stimpath, stim)
    # play visual mask
    playmask(stimpath, mask)
    # mental imagery trial
    imagery()
    # display phenomenological questions
    pheno()

    

#------------------------
# Define Picture Block 
#------------------------

def pixblock(stim, mask):
    showpix(stimpath, stim)
    playmask(stimpath, mask)
    imagery()
    pheno()

#-----------------
# Run Experiment
#----------------




for thisTrial in trials:
    if thisTrial['Run'] == 'movie':
        movieblock(thisTrial['Stim'], thisTrial['Mask'])
    elif thisTrial['Run'] == 'picture':
        pixblock(thisTrial['Stim'], thisTrial['Mask'])
    elif thisTrial['Run'] == 'break':
        pause.draw(win)
        win.flip()



theEnd.draw(win)
win.flip()
core.wait(5)

trials.saveAsWideText(expInfo["participant"] + "_" + expInfo["session"]  +".csv")
core.quit()






