"""
Find Empty Room
"""
import json
import os
import time
from UHE.utils import this_course, this_term, this_week, this_year
import os.path as op
# from flask import current_app

class EmptyRoom():
    def __init__(self,classroom_dict):
        self.classroom_dict = classroom_dict
    def get_room_schedule(self,room):
        """
        return a schedule of a given room in this semster
        """
        return self.classroom_dict.get(room)


    def is_room_empty(self,room, week, day, course):
        """
        confirm weather the room is empty at the time
        """
        return self.classroom_dict[room][week - 1][day - 1][course - 1] == 1


    def get_emptyroom_now(self):
        """
        uses present time to get a list contain all free rooms
        """
        week = this_week()
        day = int(time.strftime("%w"))
        course = this_course()
        return get_emptyroom(week, day, course)


    def get_emptyroom(self,week, day, course):
        """
        use custom time to get a list contain all free rooms
        """
        emptyroom_list = []
        if course == 0 or day == 0 or day == 6:
            return emptyroom_list
        for classroom in self.classroom_dict.keys():
            if self.classroom_dict[classroom][week - 1][day - 1][course - 1] == 1:
                emptyroom_list.append(classroom)
        return sorted(emptyroom_list)
