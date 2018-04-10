from move_result_enum import *


class MoveResult(object):
    # move_result_type = None
    # value = None
    # yes = None
    # land = None

    def __init__(self, move_result_type, value, land):
        self.move_result_type = move_result_type
        self.value = value
        self.land = land
        self.yes = None
        self.msg = None

    def set_msg(self, msg):
        self.msg = msg
    def get_move_result_type(self):
        return self.move_result_type

    def get_value(self):
        return self.value

    def get_land(self):
        return self.land

    def set_decision(self, decision):
        assert self.move_result_type == MoveResultType.BUY_LAND_OPTION
        self.yes = decision

    def get_decision(self):
        assert self.move_result_type == MoveResultType.BUY_LAND_OPTION
        return self.yes

    def __str__(self):
        saying = self.msg if self.msg else ""
        saying += MoveResultType.get_description(self.move_result_type)
        ret = saying + " value:{0}, land: {1}" .format(
            self.value, self.land)
        if self.yes is not None:
            ret += " decision: {0}".format(self.yes)
        return ret
