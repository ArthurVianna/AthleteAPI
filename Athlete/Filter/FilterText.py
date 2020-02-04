from .DefaultFilter import *

class FilterText(DefaultFilter):
    """docstring for FilterText"""
    def __init__(self,field):
        super().__init__(field)
        self.default_suffix.update({"_like" : "__contains" ,"_ilike" : "__icontains"})