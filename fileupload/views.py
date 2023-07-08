# Importing rest framework packages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

# Importing serializers
from .serializers import DocumentSerializer

# Importing custom packages
from .models import Document

# Importing django modules
from django.core.files.storage import default_storage


class FileUpload(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            posts = Document.objects.filter(user=request.user)
            serializer = DocumentSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except:
            return Response("", status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        posts_serializer = DocumentSerializer(data=request.data)

        if posts_serializer.is_valid():
            posts_serializer.save(user=request.user)
            return Response("File uploaded successfully", status=status.HTTP_201_CREATED)

        else:
            print('error', posts_serializer.errors)
            return Response("File couldn't upload successfully", status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_file(request, id):
    try:
        file = Document.objects.filter(pk=id)
        file_path = file.values_list("file", flat=True)[0]
        default_storage.delete(file_path)
        file.delete()

        print(file_path)

        return Response("File deleted", status=status.HTTP_200_OK)

    except:
        return Response("File couldn't be deleted", status.HTTP_500_INTERNAL_SERVER_ERROR)
