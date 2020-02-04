from .DefaultFilter import *
from .FilterNumber import *
from .FilterText import *

class FilterModel(object):
    numericFieldTypes = ["Integer","Auto","Float"]
    keyFieldTypes = ["Foreign"]
    filters = []
    prefix = ""
    def __init__(self,model,prefix=""):
        super(FilterModel, self).__init__()
        self.createFilterForModel(model,prefix)
    
    def createFilterForModel(self,model,prefix=""):
        filters = []
        for field in model._meta.fields:
            if any( numericType.lower() in str(type(field)).lower() for numericType in self.numericFieldTypes ):
                filters.append(FilterNumber(prefix + field.name))
            elif any( keyType.lower() in str(type(field)).lower() for keyType in self.keyFieldTypes):
                filters.append(FilterFK(prefix + field.name,field.remote_field.model))
            else:
                filters.append(FilterText(prefix + field.name))
        self.filters = filters

    def getKwargs(self,request):
        kwargs = {}
        for fieldFilter in self.filters:
            kwargs.update(fieldFilter.createArg(request))
        return kwargs

class FilterFK(DefaultFilter):
    
    model = None
    modelFilter = None
    def __init__(self, field,model):
        super().__init__(field)
        self.model = model
        self.modelFilter = FilterModel(self.model,field + "__")

    def createArg(self,request):
        kwargs = self.modelFilter.getKwargs(request)
        return kwargs


