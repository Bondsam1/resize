import os
from PIL import Image
def resize(rootdir,width,height,des_dir):
    list=os.listdir(rootdir)
    for item in list:
      try:
        im=Image.open(rootdir+'/'+item)
        w,h=im.size
        new_im=im.resize((width,height))
        des_dir+=item
        new_im.save(des_dir)
      except IOError:
        list.remove(item)
