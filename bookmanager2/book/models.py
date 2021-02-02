from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name=models.CharField(max_length=100)
    pub_date=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        db_table='bookinfo'


class PeopleInfo(models.Model):
    gender_list=(
        (1,'male'),
        (2,'female')
    )
    name=models.CharField(max_length=10)
    gender=models.SmallIntegerField(choices=gender_list,default=1)
    description=models.CharField(max_length=1000)
    is_delete=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        db_table='peopleinfo'


