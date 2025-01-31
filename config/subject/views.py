from rest_framework import generics
from .serializers import SubjectSerializer
from .repository import ManageSubject
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class SubjectListView(generics.ListCreateAPIView):
    queryset = ManageSubject.get_all_available_subjects()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class SubjectUpdateRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = ManageSubject.get_all_available_subjects()
    serializer_class = SubjectSerializer
    lookup_field = 'id'
    
    
    def destroy(self, request, *args, **kwargs):
        subject_id = self.kwargs.get('id')
        is_deleted = ManageSubject.delete_subject(subject_id)
        if is_deleted:
            return Response(
                {"message": f"Subject has been successfully deleted."},
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {"error": "Subject not found."},
                status=status.HTTP_404_NOT_FOUND
            )