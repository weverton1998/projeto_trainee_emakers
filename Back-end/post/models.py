from django.db import models
from accounts.models import User
from ckeditor.fields  import  RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    tittle = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tittle
