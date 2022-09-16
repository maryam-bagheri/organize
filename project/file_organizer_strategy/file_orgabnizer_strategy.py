from file_organizer_strategy.pdf_organizer import pdf_organizer
from project_enum.audio_extension import audio_extension
from project_enum.image_extension import image_extension
from project_enum.file_organizer_type import file_organizer_type
from file_organizer_strategy.image_organizer import image_organizer
from project_enum.pdf_extension import pdf_extension

class file_organizer_strategy:
    def choose_strategy(self,file,strategy_type,folder):
        if True in [e.name==strategy_type for e in image_extension]:
            img_organizer=image_organizer()
            img_organizer.file_mover(folder+'/'+file,folder+'image')
        elif True in [e.name==strategy_type for e in audio_extension]:
            aud_organizer=aud_organizer()
            aud_organizer.file_mover(folder+'/'+file,folder+'audio')
        elif True in [e.name==strategy_type for e in pdf_extension]:
            pdf_org=pdf_organizer()
            pdf_org.file_mover(folder+'/'+file,folder+'pdf')
        pass
