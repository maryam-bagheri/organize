from abc import ABC, abstractmethod
from shutil import move

class file_organizer:
    def file_mover(self,file,new_location):
        #print(file)
        move(file, new_location)

    if __name__=='__main__':
        print('Please run from main')

