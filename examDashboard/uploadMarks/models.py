from django.db import models

# Create your models here.
class exam_data(models.Model):
    name = models.CharField('Name',max_length=190,null=True,blank=True)
    roll = models.CharField('Roll',max_length=190,null=True,blank=True)
    gender = models.CharField('Gender',max_length=190,null=True,blank=True)
    physics = models.IntegerField('Physics',null=True,blank=True)
    chemistry = models.IntegerField('Chemistry',null=True,blank=True)
    maths = models.IntegerField('Maths',null=True,blank=True)

    class Meta():
        verbose_name,verbose_name_plural = 'Exam data','Exam Data'