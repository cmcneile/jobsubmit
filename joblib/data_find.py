#!/home/cmcneile/anaconda3/bin/python

#
# 
#

import os
import re

def get_config_list(tag, gdir) :

    clist = [] 
    print ('Searching for configurations in ' , gdir)
    for filename in os.listdir(gdir):
       if not re.search( 'info' ,   filename  ) :
           cfg = filename.replace(tag, '')
           clist.append(int(cfg))

    slist = sorted(clist)
    return slist


