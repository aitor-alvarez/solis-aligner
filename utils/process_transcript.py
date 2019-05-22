#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Aitor Alvarez'
import sys
from textgrid import TextGrid
import os
import codecs


def read_files(path, tier):
    replace={u'Q:': u'ā', u'e:': u'ē', u'i:': u'ī', u'o:' : u'ō', u'u:' : u'ū', u'A:':u'Ā', u'E:' : u'Ē', u'I:' : u'Ī', u'O:': u'Ō', u'U:':u'Ū',
         u'.':'', u'-':'', u';': '', u':': '', u'hh': ''}
    directory = os.listdir(path)
    for f in directory:
        if '.TextGrid' in f:
            grid_file = file(os.path.join(path, f), 'r+').readlines()
            grid_data = ''.join(grid_file)
            text_grid = TextGrid(grid_data)
            if text_grid.tiers[1].nameid == 'transcript':
                i=0
                for t in text_grid.tiers[1].simple_transcript:
                    word = replace_stopwords(t[2], replace)
                    text_grid.tiers[1].simple_transcript[i]= (t[0], t[1], word)
                    i+=1
                write_textgrid(path, 'new_'+f, text_grid)

def replace_stopwords(word, dic):
    for i, j in dic.iteritems():
        word = word.replace(i, j)
    return word

def write_textgrid(path, filename, textgrid_object):
    header='File type = '+ textgrid_object._check_type()+'\n'+'Object class = "TextGrid"'+'\n'+'\n'+'xmin = '+ str(textgrid_object.xmin)+'\n'+'xmax = '+str(textgrid_object.tiers[0].tier_info[3])+'\n'+'tiers? <exists>'\
           +'\n'+'size = '+ str(textgrid_object.size)+'\n'
    items = 'item []:\n'
    for i in range(0, len(textgrid_object.tiers)):
        items+= '\t item ['+str(i)+']:\n'
        for j in range(0, len(textgrid_object.tiers[i].tier_info)):
            if j == 0:
                items+= '\t \t class = "'+str(textgrid_object.tiers[i].tier_info[j])+' "\n'
            elif j == 1:
                items += '\t \t name = "'+str(textgrid_object.tiers[i].tier_info[j])+' "\n'
            elif j == 2:
                items += '\t \t xmin = '+str(textgrid_object.tiers[i].tier_info[j])+'\n'
            elif j == 3:
                items += '\t \t xmax = '+str(textgrid_object.tiers[i].tier_info[j])+'\n'
            elif j == 4:
                items += '\t \t intervals: size = '+str(textgrid_object.tiers[i].tier_info[j])+'\n'
            elif j == 5:
                l =1
                for k in textgrid_object.tiers[i].simple_transcript:
                    items += '\t \t'+'intervals['+str(l)+']:'+'\n'
                    items += '\t \t \t xmin = '+k[0]+'\n'
                    items += '\t \t \t xmax = ' +k[1]+'\n'
                    items += '\t \t \t text = "'+k[2]+'"\n'
                    l+=1

    with codecs.open(path+filename, 'w', 'UTF-8', errors='ignore') as f:
        f.write(header+items)

if __name__ == "__main__":
    path = str(sys.argv[1])
    tier = str(sys.argv[2])
    read_files(path, tier)























