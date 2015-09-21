# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Student(models.Model):  
    name=models.CharField(max_length=20,verbose_name="实验用品") 
    unit = models.CharField(max_length = 128,verbose_name="单位") 
    #age=models.IntegerField(max_length=3)
    number = models.IntegerField(verbose_name="数量")
    location = models.CharField(max_length = 128,verbose_name="存放地点")
    custodian = models.CharField(max_length = 128,verbose_name="管理人")
    remark = models.CharField(max_length = 128,verbose_name='备注')

	
	
    
    def __unicode__(self):
        return self.name                          
                          
class Subject(models.Model):  
    student=models.ForeignKey(Student)  
    sub_name=models.CharField(max_length=20)  
    sub_num=models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.sub_name
