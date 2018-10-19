#!/home/cmcneile/anaconda3/bin/python

import os
import re


##/home/cmcneile/configs/hisq/l1648f211b580m013m065m838a-coul-v5/l1648f211b580m013m065m838a-coul-v5.4195

gdir = '/home/cmcneile/configs/hisq/l1648f211b580m013m065m838a-coul-v5' 
tag = 'l1648f211b580m013m065m838a-coul-v5.'





def get_config_list(tag, gdir) :

    clist = [] 
    print ('Searching for configurations in ' , gdir)
    for filename in os.listdir(gdir):
       if not re.search( 'info' ,   filename  ) :
           cfg = filename.replace(tag, '')
           clist.append(int(cfg))

    slist = sorted(clist)
    return slist


##cfg_list = get_config_list(tag, gdir) 
##for cfg in cfg_list :
##   print(cfg)

