from rest_framework import viewsets

from .Pagination.CustomPagination import *
from .serializers import *
from .models import *
from .Filter.FilterModel import *

class CustomModelViewSet(viewsets.ModelViewSet):
    model = None
    filters = None
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.model = kwargs["model"]
        self.pagination_class = CustomPagination
        self.filters = FilterModel(self.model)

    def get_queryset(self):
        if('pk' in self.kwargs):
            return self.model.objects.filter(id=self.kwargs["pk"])
        
        kwargs = self.filters.getKwargs(self.request)

        listOrder = self.get_order(self.request)

        if listOrder == None or not listOrder:
            secondAttribute = self.model._meta.fields[1].name
            #Looks for the second attribute because the first will always be the id
            listOrder = [secondAttribute]

        return self.model.objects.filter(**kwargs).order_by(*listOrder)

    def get_order(self,request):
        listOrder = None
        order = self.request.query_params.get("order_by",None)
        if order:
            order = order.strip()
            listOrder = order.split(',')
            for orderRequested in listOrder:
                if not any(field.name in orderRequested for field in self.model._meta.fields ):
                    listOrder.remove(orderRequested)
        return listOrder


class AthleteViewSet(CustomModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    def __init__(self,**kwargs):
        kwargs["model"] = Athlete
        super().__init__(**kwargs)

class NocViewSet(CustomModelViewSet):
    queryset = NOC.objects.all()
    serializer_class = NocSerializer

    def __init__(self,**kwargs):
        kwargs["model"] = NOC
        super().__init__(**kwargs)

class OlympicsViewSet(CustomModelViewSet):
    queryset = Olympics.objects.all()
    serializer_class = OlympicsSerializer

    def __init__(self,**kwargs):
        kwargs["model"] = Olympics
        super().__init__(**kwargs)

class SportViewSet(CustomModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

    def __init__(self,**kwargs):
        kwargs["model"] = Sport
        super().__init__(**kwargs)

class EventViewSet(CustomModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def __init__(self,**kwargs):
        kwargs["model"] = Event
        super().__init__(**kwargs)

class CityViewSet(CustomModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def __init__(self,**kwargs):
        kwargs["model"] = City
        super().__init__(**kwargs)

class ParticipationViewSet(CustomModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer

    def __init__(self,**kwargs):
        kwargs["model"] = Participation
        super().__init__(**kwargs)
