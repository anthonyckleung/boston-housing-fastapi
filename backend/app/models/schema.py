from pydantic import BaseModel


class Item(BaseModel):
    num_rooms: int 
    pupil_teacher_ratio: float 
    l_stat: float 
    