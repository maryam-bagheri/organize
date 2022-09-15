from project_enum.image_extension import image_extension
from project_enum.file_organizer_type import file_organizer_type
from file_organizer_strategy.image_organizer import image_organizer

class file_organizer_strategy:
    def choose_strategy(self,file,strategy_type,folder):
        if True in [e.name==strategy_type for e in image_extension]:
            print([e.name==strategy_type for e in image_extension])
            img_organizer=image_organizer()
            img_organizer.file_mover(folder+'/'+file,folder+'image')
        pass
