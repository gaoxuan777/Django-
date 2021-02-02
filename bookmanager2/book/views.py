from django.shortcuts import render

# Create your views here.
from book.models import BookInfo
BookInfo(
    name='Django',
    pub_date='2020-1-2',
    readcount=0,
    commentcount=10

)
BookInfo.objects.filter(pk=1).update(name='gao')
BookInfo.objects.filter(pk=4).delete()
BookInfo.objects.filter(name__contains='天')
BookInfo.objects.filter(name__endswith='部')
BookInfo.objects.filter(name__isnull=True)
BookInfo.objects.filter(pk__in=[1,3,5])
BookInfo.objects.filter(pk__gt=3)
BookInfo.objects.filter(pub_date__year__gt=1980)
from django.db.models import F
BookInfo.objects.filter(commentcount__gt=F('readcount'))
from django.db.models import Q
BookInfo.objects.filter(~Q(id=3))
BookInfo.objects.filter(Q(id=1)|Q(id=3))
BookInfo.objects.aggregate(Sum('commentcount'))
from django.db.models import Sum