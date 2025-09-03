from django.urls import path
from .views import FolderListCreateView, NoteListCreateView

urlpatterns = [
    path('folders/', FolderListCreateView.as_view(), name='folder-list-create'),
    path('folders/<int:folder_id>/notes/', NoteListCreateView.as_view(), name='note-list-create'),
]