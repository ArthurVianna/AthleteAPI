from .DefaultFilter import *

class FilterNumber(DefaultFilter):
    """docstring for FilterNumber"""
    def __init__(self,field):
        super().__init__(field)
        self.default_suffix.update({"" : "","_gt" : "__gt" ,"_lt" : "__lt","_lte" : "__lte","_gte" : "__gte"})

    def checkField(self,fieldName,append,queryParams):
        
        fieldValue = queryParams.get(fieldName,None)
        if fieldValue is not None:
            if "_null" not in fieldName:
                if not fieldValue.isnumeric():
                    return
            else:
                if fieldValue.lower() in ["true","t"] :
                    fieldValue = True
                elif fieldValue.lower() in ["false","f"]:
                    fieldValue = False
                else:
                    fieldValue = None
            return { self.field + append : fieldValue}