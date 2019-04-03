# from django.db import models
#
#
# class Items(models.Model):
#     type = models.CharField(max_length=250)
#     title = models.CharField(max_length=250)
#     description = models.TextField(max_length=2000)
#     price = models.DecimalField(max_digits=6, de)
#     image = models.ImageField()
#     video = models.FileField()


# class Image(models.Model):
#     post = models.ForeignKey(Items, related_name='images')
#     file = models.ImageField(upload_to='upload')
#     position = models.PositiveSmallIntegerField(default=0)
#
#     class Meta:
#         ordering = ['position']
#
#     def __str__(self):
#         return '%s - %s ' % (self.post, self.file)
