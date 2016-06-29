from psychopy import visual, core, event, logging, gui
import os, time

######## Define experiment constant #####################################

clippath= '/home/claire/Documents/Experiment/Imagery/Clips/Animal/cat.mp4' 
vismaskpath = '/home/claire/Documents/Experiment/Scripts/ExpeImagery/Video_processing/Scramb/'
pixpath = '/home/claire/Documents/Experiment/Imagery/Frames/Animals/cat_frame.png' 

if not os.path.exists(clippath):
        raise RuntimeError("Video File could not be found:"+clippath)
        

if not os.path.exists(vismaskpath):
        raise RuntimeError("Video File could not be found:"+vismaskpath)



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
        height = 0.09, 
        color='white'
        )

######### Set Keys for response and experiment flow ##################
keyStop = ['space'] # indicate stop of movie clip and stop of mental imagery

######## Define rating scale and questionnaire after each MI trial ################

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


######## Fixation cross ##############

def fixation():
    fix_cross.draw()
    win.flip()
    core.wait(1)


######## Questionnaire ###################

def pheno():
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

####### Play movie #####################

def playclip(clippath):
    fixation()
    clip = visual.MovieStim(win=win,
            name= 'clip', 
            filename= clippath,
            size = [800,600],
            ori =0, 
            pos=[0,0], 
            opacity =1, 
            depth = -1.0
            )
    while clip.status != visual.FINISHED:
        clip.draw()
        win.flip()

    # get key press at the end of clip
    event.waitKeys(keyList=keyStop)


######## Play visual noise ##############

def playmask(vismaskpath):
    for n in range (1,3):
        vismask = visual.ImageStim(win =win, 
            image = vismaskpath + 's_' + str(n) + '.png', 
            pos = [0,0],
            size = [800,600],
            opacity =1, 
            units = 'pix'
            )

        vismask.draw()
        win.flip()
        core.wait(0.5)


####### Show picture ############

def showpix(pixpath):
    fixation()
    pix = visual.ImageStim(win =win, 
            image = pixpath, 
            pos = [0,0], 
            size = [800, 600], 
            opacity = 1,
            units = 'pix'
            )

    pix.draw()
    win.flip()
    core.wait(1)
    event.waitKeys(keyList=keyStop)

######### Mental Imagery trial ##############


def imagery():
    fix_cross.draw()
    win.flip()   
    event.waitKeys(keyList=keyStop)


######### Define Movie Block #############################
def movieblock():    
    # play video clip
    playclip(clippath)

    # play visual mask
    playmask(vismaskpath)

    # mental imagery trial
    imagery()

    # display phenomenological questions
    pheno()


######## Define Picture Block ##############

def pixblock():
    showpix(pixpath)
    imagery()
    pheno()

###############

pixblock()
movieblock()

core.quit()






