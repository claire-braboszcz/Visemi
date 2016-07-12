'''
Generate trial list for Visemi experiment: present pictures and videos with associated visual masks
'''

import random
import os
import csv
import numpy
import pdb
from moviepy.editor import VideoFileClip



def is_clip(stim):
    return True if stim[7] in ['c'] else False

def is_mask(stim):
    return True if stim[7] in ['m'] else False

def is_pict(stim):
    return True if stim[7] in ['f'] else False



stim_path = '/home/claire/Documents/Experiment/Imagery/Stimuli/'

#---------------------------------
# read filenames in folder
#--------------------------------

for root, dirs, files in os.walk('/home/claire/Documents/Experiment/Imagery/Stimuli'):

    clip_list = [stim for stim in files if is_clip(stim)]
    mask_list = [stim for stim in files if is_mask(stim)]
    pict_list = [stim for stim in files if is_pict(stim)]

random.shuffle(clip_list)
random.shuffle(mask_list)
random.shuffle(pict_list)


## video block
list_stim_movies = csv.writer(open('movie_block.csv','wb'), delimiter = ',', quotechar = '"')
header = ['Run', 'Stim','Stim_Duration', 'Mask', 'Mask_Duration', 'Condition']
list_stim_movies.writerow(header)
        
list_stim_pict = csv.writer(open('picture_block.csv','wb'), delimiter = ',', quotechar = '"')
list_stim_pict.writerow(header)
 

for stim in range (0, len(clip_list)):
    clip = clip_list[stim]
    ind = clip[:6]
    mask = [m for m in mask_list if ind in m]
    
    video =VideoFileClip(os.path.join(stim_path, clip))
    len_clip = video.duration
    
    video_m =VideoFileClip(os.path.join(stim_path, mask[0]))
    len_mask = video_m.duration

    m_trial = ['movie', clip, str(len_clip), mask, str(len_mask), clip[:3]] 

    list_stim_movies.writerow(m_trial)

for pic in range (0, len(pict_list)):
    pict = pict_list[pic]
    ind = pict[:6]
    mask = [m for m in mask_list if ind in m]
    
    video_m =VideoFileClip(os.path.join(stim_path, mask[0]))
    len_mask = video_m.duration

    p_trial = ['picture', pict, 'NA', mask, str(len_mask), pict[:3]] 

    list_stim_pict.writerow(p_trial)

   




