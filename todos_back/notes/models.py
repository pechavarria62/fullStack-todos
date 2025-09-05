from django.db import models
from django.conf import settings

# container for notes
class Folder(models.Model):
    name = models.CharField(max_length=100) # Folder name
    '''
    settings.AUTH_USER_MODEL -> Link to the user who owns the folder
     on_delete=models.CASCADE, related_name='folders' -> user.folders reverse lookup
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='folders')
    # Timestamp when folder is created
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='notes')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title