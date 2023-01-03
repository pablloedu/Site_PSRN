from pyexpat import model
from tabnanny import verbose
from django.db import models
from django import forms
from tinymce.models import HTMLField
from accounts.models import UserCustom
import re


# https://acervolima.com/como-integrar-o-editor-de-texto-personalizado-ao-seu-site-django/
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    text = HTMLField()
    main_idea = models.TextField(max_length=500,verbose_name='Ideia Central do Texto')
    image = models.ImageField(blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    publiched_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.PositiveBigIntegerField(blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    attachment_id = models.ManyToManyField(
        'Attachment', verbose_name='Anexos', blank=True
    )
    user_id = models.ForeignKey(
        UserCustom, on_delete=models.CASCADE,
        verbose_name='Autor'
    )
    
    main_tag = models.ForeignKey('Tag', verbose_name='Tag Principal',on_delete=models.CASCADE, related_name='Main_Tag', default=1)


    tag = models.ManyToManyField(
        'Tag', verbose_name='Categorias', blank=True,
    )

    def __str__(self):
        return self.title

    def generate_summary(self):
        main_idea = self.main_idea[:300]
        main_idea = re.sub('<[^>]+?>', '', main_idea)
        return main_idea.strip() + '...'

    # DÁ PROBLEMA COM PALAVRAS QUE JÁ TEM UM HIFEN
    def generate_url(self):
        title = self.title.replace(' ','-').strip()
        return title
    # TESTAR OS DIFERENTES TITULOS PRA NÃO DAR MERDA DEPOIS
    def generate_title(self):
        if len(self.title) > 50:
            title = self.title[:40].strip() + '...'
            return title
        else:
            return self.title



class Attachment(models.Model):
    name = models.CharField(max_length=180)
    link = models.CharField(max_length=3000, blank=True, null=True)
    item = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name


# https://pypi.org/project/django-rgbfield/
class Tag(models.Model):
    name = models.CharField(max_length=80)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# quatidade de vizualizações da publicação
class Visualized(models.Model):
    ref_date = models.DateField()
    count = models.IntegerField(blank=True, null=True)
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, verbose_name='Postagem'
    )

    def __str__(self):
        return self.post_id.title


class Contact(models.Model):
    name = models.CharField(max_length=180)
    phone = models.PositiveBigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    instragram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=500, blank=True, null=True)
    whatsapp = models.PositiveBigIntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class HTMLForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude=()