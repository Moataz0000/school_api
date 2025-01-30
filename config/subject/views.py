from rest_framework import generics
from .serializers import SubjectSerializer
from .repository import SubjectRepo



class SubjectListView(generics.ListCreateAPIView):
    queryset = SubjectRepo.get_all_avaliable_subject()
    serializer_class = SubjectSerializer
    
    







