#!/home/cmcneile/anaconda3/bin/python


nojob = 5 


f_template = "template/ks_spectrum_in"
j_template = "template/job.sh"
input = "ks_spectrum_in"
j_input = 'job.sh' 

gdir = '/home/cmcneile/configs/hisq/l1648f211b580m013m065m838a-coul-v5' 
tag = 'l1648f211b580m013m065m838a-coul-v5.'


############################
import os
import re
from pathlib import Path
import sys
import subprocess




###import data_find from joblib
##import joblib
sys.path.append('./joblib')
import data_find
import setup_job


cfg_list = data_find.get_config_list(tag, gdir) 

count = 0 
for cfg in cfg_list :
   print("Working on ", cfg)

   wdir = "work/" + str(cfg) 
  
   p = Path(wdir)
   if p.exists() : 
     print (wdir , 'exists, so do nothing')
   else:
     setup_job.create_work(wdir)
     setup_job.update_file(f_template ,wdir + "/" + input, str(cfg))
     setup_job.update_file(j_template ,wdir + "/" + j_input, str(cfg))
     os.chdir(wdir)
     completed = subprocess.run(['/usr/bin/sbatch', j_input ])
     os.chdir("../../")



   count = count + 1
   if count == nojob :
     break
