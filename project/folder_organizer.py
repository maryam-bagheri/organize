from os import mkdir, path, walk
from pathlib import Path as pathlib
from shutil import move
from project_enum.file_organizer_type import file_organizer_type

from file_organizer_strategy.file_orgabnizer_strategy import file_organizer_strategy

class folder_organizer:
    def __init__(self) -> None:
        self.file_list=[]
        
    def __list_files(self, location):
        for (dirpath, dirnames, filenames) in walk(location):
            self.file_list.extend(filenames)
            break

    def __check_directory(self, dir_location):
        """Check if directory exists or not. If not create one."""
        if not path.exists(dir_location):
            mkdir(dir_location)

    def __file_mover(self, folder):
        """move file based on extension list to new location."""
        file_org_str=file_organizer_strategy()
        for file in self.file_list:
            ext=(path.splitext(file)[1]).lower().replace('.','')
            file_org_str.choose_strategy(file,ext,folder)

    def organize_files(self, folder):
        """Organize file list"""
        self.__list_files(folder)
        extensions=[e.name for e in file_organizer_type]
        for e in extensions:
            self.__check_directory(path.join(folder, e))
        self.__file_mover(folder)