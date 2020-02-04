class DefaultFilter(object):
    """docstring for Filter"""
    def __init__(self, field):
        super(DefaultFilter, self).__init__()
        self.field = field
        self.default_suffix = {"" : "","_null" :"__isnull"}
    
    field = ""
    default_suffix = None

    def checkField(self,fieldName,append,queryParams):
        fieldValue = queryParams.get(fieldName,None)
        if fieldValue is not None:
            return { self.field + append : fieldValue}

    def createArg(self,request):
        kwargs = {}
        for key,value in self.default_suffix.items():
            tempArg = self.checkField(self.field + key,value,request.query_params)
            if tempArg is not None:
                kwargs.update(tempArg)
        return kwargs