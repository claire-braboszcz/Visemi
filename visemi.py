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


#TRIALS_FILE = '.csv'

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
#trialList = data.importConditions(TRIALS_FILE, returnFieldNames=False)
#trials = data.TrialHandler(trialList, nReps=1, method='sequential', extraInfo=expInfo)
#trials.data.addDataType('respKey')
#trials.data.addDataType('respTime')
#trials.data.addDataType('stimOnset')
#trials.data.addDataType('scanOnset')



#----------------
# Set up logging 
#----------------

#globalClock = core.Clock()
#
#logging.console.setLevel(logging.DEBUG)
#
#if not os.path.isdir('Logdata'):
#    os.makedirs('Logdata')  # if this fails (e.g. permissions) we will get error
#filename = 'Logdata' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['session'])
#logging.setDefaultClock(globalClock)
#logFileExp = logging.LogFile(filename +'.log', level=logging.EXP)
#logging.console.setLevel(logging.INFO)  # this outputs to the screen, not a file



#--------------------------------------
#Define experiment constant 
#--------------------------------------

win = visual.Window(size=(1024, 768), 
        fullscr=True, 
        screen=0, 
        allowGUI=True, 
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
    core.wait(1)

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

#    trials.addData('movement', moveRatingScale.getRating())
#    trials.addData('similarity', simRatingScale.getRating())
#    trials.addData('effort', effRatingScale.getRating())

#-------------
# Play movie 
#-------------

def playclip(stimpath):
    fixation()
    clip = visual.MovieStim(win=win,
            name= 'clip', 
            filename= stimpath +'ani_01_clip.mp4',
            size = [800, 450],
            ori =0, 
            pos=[0,0], 
            opacity =1, 
            depth = -1.0
            )
    while clip.status != visual.FINISHED:
        clip.draw()
        win.flip()

    fixation()
    # get key press at the end of clip
   # event.waitKeys(keyList=keyStop)
    mouse.getPressed()
#------------------------
# Play visual noise
#------------------------

def playmask(stimpath):
     vismask = visual.MovieStim(win =win,
             filename= stimpath + 'ani_01_mask' + '.mp4', 
            #image = '/home/claire/Documents/Experiment/Imagery/Clips/Animal/s_frame_cat' + str(n) +'.png',
             pos = [0,0],
             size = [800,450],
             opacity =1, 
             units = 'pix'
             )
    
     while vismask.status != visual.FINISHED:
        vismask.draw()
        win.flip()



#------------------
# Show picture 
#------------------

def showpix(stimpath):
    fixation()
    pix = visual.ImageStim(win =win, 
            image = stimpath + 'ani_01_frame.png', 
            pos = [0,0], 
            size = [800, 600], 
            opacity = 1,
            units = 'pix'
            )

    pix.draw()
    win.flip()
    core.wait(1)
    #event.waitKeys(keyList=keyStop)
    mouse.getPressed()
#------------------------
# Mental Imagery trial 
#------------------------


def imagery():
    fix_cross.draw()
    win.flip()   
    event.waitKeys(keyList=keyStop)

#---------------------
# Define Movie Block 
#---------------------

def movieblock():    
    # play video clip
    playclip(stimpath)
    # play visual mask
    playmask(stimpath)
    # mental imagery trial
    imagery()
    # display phenomenological questions
    pheno()

#------------------------
# Define Picture Block 
#------------------------

def pixblock():
    showpix(stimpath)
    imagery()
    pheno()

#-----------------
# Run Experiment
#----------------

#pixblock()
movieblock()

core.quit()






