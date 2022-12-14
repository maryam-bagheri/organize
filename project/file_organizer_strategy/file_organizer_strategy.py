from file_organizer_strategy.compress_organizer import compress_organizer
from file_organizer_strategy.exec_organizer import exec_organizer
from file_organizer_strategy.pdf_organizer import pdf_organizer
from file_organizer_strategy.audio_organizer import audio_organizer
from file_organizer_strategy.video_organizer import video_organizer
from file_organizer_strategy.excel_organizer import excel_organizer
from file_organizer_strategy.word_organizer import word_organizer
from project_enum.audio_extension import audio_extension
from project_enum.compress_extension import compress_exptension
from project_enum.image_extension import image_extension
from project_enum.file_organizer_type import file_organizer_type
from file_organizer_strategy.image_organizer import image_organizer
from project_enum.pdf_extension import pdf_extension
from project_enum.exec_extension import exec_extension
from project_enum.video_extension import video_extension
from project_enum.excel_extension import excel_extension
from project_enum.word_extension import word_extension

class file_organizer_strategy:
    def choose_strategy(self,file,strategy_type,folder):
        if True in [e.name==strategy_type for e in image_extension]:
            img_organizer=image_organizer()
            img_organizer.file_mover(folder+'/'+file,folder+file_organizer_type.image.name)
        elif True in [e.name==strategy_type for e in audio_extension]:
            aud_organizer=audio_organizer()
            aud_organizer.file_mover(folder+'/'+file,folder+file_organizer_type.audio.name)
        elif True in [e.name==strategy_type for e in pdf_extension]:
            pdf_org=pdf_organizer()
            pdf_org.file_mover(folder+'/'+file,folder+file_organizer_type.pdf.name)
        elif True in [e.name==strategy_type for e in compress_exptension]:
            comp_organizer=compress_organizer()
            comp_organizer.file_mover(folder+'/'+file,folder+file_organizer_type.compress.name)
        elif True in [e.name==strategy_type for e in exec_extension]:
            exec_org=exec_organizer()
            exec_org.file_mover(folder+'/'+file,folder+file_organizer_type.exec.name)
        elif True in [e.name==strategy_type for e in video_extension]:
            video_org=video_organizer()
            video_org.file_mover(folder+'/'+file,folder+file_organizer_type.video.name)
        elif True in [e.name==strategy_type for e in excel_extension]:
            excl_org=excel_organizer()
            excl_org.file_mover(folder+'/'+file,folder+file_organizer_type.excel.name)
        elif True in [e.name==strategy_type for e in word_extension]:
            word_org=word_organizer()
            word_org.file_mover(folder+'/'+file,folder+file_organizer_type.word.name)
        pass
