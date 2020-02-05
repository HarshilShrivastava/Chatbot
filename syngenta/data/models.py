from django.db import models

# Create your models here.
class Data(models.Model):
    ThreatName=models.CharField( max_length=255,null=True)
    WhatItIs=models.TextField(null=True)
    WhyItOccurs2=models.TextField(null=True)
    WhyItOccurs=models.TextField(null=True)
    Others=models.TextField(null=True)
    WhenItOccurs=models.TextField(null=True)
    ImagePath=models.ImageField(upload_to="image",null=True)
    ProductName=models.CharField( max_length=250,null=True)
    Dosage=models.CharField(max_length=50,null=True)
    WhenToApply=models.ImageField(upload_to="image",null=True)
    WhenToApplyText=models.TextField(null=True)
    MethodOfApplication=models.TextField(null=True)
    ActiveIngredients=models.TextField(null=True)
    AlsoApplicableCrop=models.TextField(null=True)
    def __str__(self):
        return self.ThreatName
class query(models.Model):
    query=models.TextField()


class DataHindi(models.Model):
    ThreatName=models.CharField( max_length=255,null=True)
    WhatItIs=models.TextField(null=True)
    WhyItOccurs=models.TextField(null=True)
    HowToIdentify=models.TextField(null=True)
    Others=models.TextField(null=True)
    WhenItOccurs=models.TextField(null=True)
    ImagePath=models.ImageField(upload_to="image",null=True)
    ProductName=models.CharField( max_length=250,null=True)
    BrandLogoImgPath=models.ImageField( upload_to="image",null=True)
    ProductImgPath=models.ImageField( upload_to="image", null=True)
    BrandCommunicationImgPath=models.ImageField( upload_to="image",null=True)
    BrandCommunicationVedioURL=models.FileField( upload_to="image",null=True)
    Dosage=models.CharField(max_length=50,null=True)
    WhenToApply=models.ImageField(upload_to="image",null=True)
    WhenToApplyText=models.TextField(null=True)
    MethodOfApplication=models.TextField(null=True)
    ActiveIngredients=models.TextField(null=True)
    AlsoApplicableCrop=models.TextField(null=True)
    def __str__(self):
        return self.ThreatName
class query(models.Model):
    query=models.TextField()