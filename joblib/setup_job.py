
import os


def update_file(filename_in,filename_out, cfg):

  print ("Loading template  " , filename_in)
  f = open(filename_in, 'r')
  ff = open(filename_out,'w') 
 
  for line in f:
    
    ll  = line.rstrip('\n')
    lll = ll.replace('CFGX', cfg)
    ff.write(lll + '\n')

  f.close
  ff.close()


  return 



def create_work(path):
  """
     Create work directory
  """
  try:  
    os.mkdir(path)
  except OSError:  
    print ("Creation of the directory %s failed" % path)
  else:  
    print ("Successfully created the directory %s " % path)

