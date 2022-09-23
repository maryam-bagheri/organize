from abc import ABC, abstractmethod
from shutil import move
import os

class file_organizer:
    def file_mover(self,file,new_location):
        #print(file)
        try:
            move(os.path.join(file), os.path.join(new_location))
        except:
            os.replace(file, new_location)

    if __name__=='__main__':
        print('Please run from main')

