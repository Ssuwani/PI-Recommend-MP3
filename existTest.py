import os

def existTest(title):
  os.chdir('mp3')
  if os.path.isfile(title+'.mp3'):
    print("Yes. it is a file")
    os.chdir('../')
    return True
  else:
    os.chdir('../')
    return False
