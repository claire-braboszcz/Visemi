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
# Set up parallel port
#---------------------------------------

pparallel = None
try:
    from psychopy import parallel

    pparallel = parallel.ParallelPort(address = 0x378) #888
except ImportError:

    class DummyParallel:
        def setData(self, val):
            print("Port parallele: setData %s" % val)
    pparallel = DummyParallel()


trigger_stim = int("00000011",2)
trigger_mask = int("00000101",2)
trigger_space = int("00010100", 2)
trigger_fixation = int("10100000",2)




#---------------------------------------
# Store info about the experiment session
#---------------------------------------
expName = 'Visemi'  
expInfo = {'participant':'', 'session': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel  
expInfo['date'] = data.getDateStr()  # add a simple timestamp  
expInfo['expName'] = expName



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
#------------------------------------
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


#-----------------
# Fixation cross 
#-----------------
def fixation():
    pparallel.setData(0) # sets all pin low
    fix_cross.draw()
    win.flip()
    pparallel.setData(trigger_fixation)
    core.wait(0.005)
    pparallel.setData(0)
#    core.wait(1)


for i in range(1,10):
    fixation()
    core.wait(1)
    win.flip()
    core.wait(1)
   
 
core.quit()






