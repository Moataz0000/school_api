from rest_framework import generics
from .serializers import SubjectSerializer
from .repository import SubjectRepo
from rest_framework.response import Response
from rest_framework import status



class SubjectListView(generics.ListCreateAPIView):
    queryset = SubjectRepo.get_all_avaliable_subject()
    serializer_class = SubjectSerializer
    
    




class SubjectUpdateRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubjectRepo.get_all_avaliable_subject()
    serializer_class = SubjectSerializer
    lookup_field = 'id'
    
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": f"Subject '{instance.title}' has been successfully deleted."},
            status=status.HTTP_204_NO_CONTENT
        )
    