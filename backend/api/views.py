# removed Author
from api.models import Document, Department
# removed AuthorSerializer
from api.serializers import DocumentSerializer, DepartmentSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from api.serializers import UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'documents': reverse('document-list', request=request, format=format),
        # 'authors': reverse('author-list', request=request, format=format),
        'departments': reverse('department-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    })


class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


# class AuthorList(generics.ListCreateAPIView):
# 	queryset = Author.objects.all()
# 	serializer_class = AuthorSerializer

# class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Author.objects.all()
# 	serializer_class = AuthorSerializer


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
