from django.db import models
import hashlib
# Create your models here.


class Admin(models.Model):
    class Meta:
        db_table = 'Admin'
#    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=32, unique=True, null=False)
    password = models.CharField(max_length=200, null=False)

    def save(self, *args, **kwargs):
        self.password = hashlib.md5(self.password.encode('utf-8')).hexdigest()
        super(Admin, self).save(*args, **kwargs)


class Patient(models.Model):
    class Meta:
        db_table = 'Patient'
#    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, null=False)
    createTime = models.DateTimeField(auto_now_add=True)
    plan = models.BooleanField(null=False)


class ApiInvoke(models.Model):
    class Meta:
        db_table = 'ApiInvoke'
    # id = models.IntegerField(primary_key=True)
    api = models.CharField(max_length=60, null=False)
    available_count = models.IntegerField(null=True)
    count = models.IntegerField(null=True)




