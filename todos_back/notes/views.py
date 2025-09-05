from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Folder, Note
from .serializers import FolderSerializer, NoteSerializer

# View to list and create folders for the authenticated user

class FolderListCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Retrieve folders owned by the current user
    def get(self, request):
        folders = Folder.objects.filter(owner=request.user)
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)

# Create a new folder and assign it to the current user
    def post(self, request):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to list and create notes within a specific folder
class NoteListCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Retrieve notes in the specified folder owned by the current user
    def get(self, request, folder_id):
        notes = Note.objects.filter(folder_id=folder_id, owner=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

# Create a new note in the specified folder for the current user
    def post(self, request, folder_id):
        data = request.data.copy()
        data['folder'] = folder_id
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
