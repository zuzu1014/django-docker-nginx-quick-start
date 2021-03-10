from django.db import models

# Create your models here.

    
class Section(models.Model):
    

    section = models.CharField(max_length=30, verbose_name="section", unique=True)
    order = models.IntegerField(verbose_name='order')


    def __str__(self):
        return self.section
    
    class Meta:
        db_table = "section_table"
        verbose_name = "section"
        verbose_name_plural = "sections"

class Post(models.Model):

    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    title = models.CharField(max_length=30, verbose_name='title')
    html = models.TextField(verbose_name="html")
    order = models.IntegerField(verbose_name='order')
    hash_tag = models.TextField(verbose_name="hash_tag")

    def __str__(self):
        return self.title

