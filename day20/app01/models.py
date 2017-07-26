from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveSmallIntegerField(null=True)   #[0 ,32767]的取值范围
    authors = models.ManyToManyField("Author")   #多对多，django会默认给你创建第三张表，来放对应类型， 实现双向一对多
    publisher = models.ForeignKey("Publisher")  #关联Publisher的主键，主键就是自增的那个ID
    pub_time = models.DateField()        #时间为天

    def __str__(self):
        return self.name
'''
    models.Book.objects.create(name='py',price=66,pub_time="2017-07-11",publisher_id=3)  创建
    models.Book.objects.all() 查看所有
    b1=models.Book.objects.all()[0] 根据作者去查
    b1.authors.all()


创建的过程中是不能加ManytoMany的关系的，必须把这个对象创建完成，在加
例如:
    b4=models.Book.objects.create(name='New',price=299,pub_time="2017-03-21",publisher_id=2)
    b4.authors.add(1,2,3) 这里的1,2 分别是作者id,多加几个也行
    b4.save() 保存后才会提交
    b4.authors.remove(1,2)  b4.save()  也是同样道理
    b4.authors.all()  查看多对多关系

###FK
外键查询  b4.publisher.name  就行，因为b4是book表的对象，而且book表做了publisher的外键，所以这样就可以直接查到
'''
'''
###CRUD
##写多了你会发现， 跨表操作就是用双下划线，不同表之间关联就用ForeKey， 要通过foreKey查询,就用这张表的对象.另外一张表的字段即可
    创建
        object.create
    修改
        object.update
    查询
        object.filter 返回的列表
        object.get    返回对象或错误，有就返回，没有就报错
             models.Book.objects.get(id=11)
        models.Book.objects.get_or_create(name='Haddop',publisher_id=2,pub_time="2016-10-10")  如果没有就创建
        models.Book.objects.filter(name__contains = 'py')    查询py的名称
        models.Book.objects.filter(name__icontains = 'py') 查询的时候忽略大小写
        models.Book.objects.filter(name__startswith = 'p') 查询开头是p的
        models.Book.objects.filter(name__endswith = 'p')    查询结尾是p的
        models.Book.objects.filter(pub_time__range=('2016-01-01','2017-11-11')) 查询这段日期内的书
        models.Book.objects.filter(pub_time__year=2015) 查询2015年的
        models.Book.objects.filter(pub_time__year__gte=2015)
        models.Book.objects.filter(pub_time__day=3)  查询3月的
        models.Book.objects.filter(pub_time__week_day=3) 查询第三天的

        models.Book.objects.values('name','price')  只查看书名和价格
        models.Book.objects.exclude(price=None) 反查询 查询price为none的

        p1 =models.Publisher.objects.last()
        p1.book_set.all()    多个图书馆关联同一个出版社,通过出版社反向查询出版了多少书
    删除
    object.delete


##aggregate聚合
from django.db.models import Avg,Max，Min，Sum,Count
from django.db.models import Avg
models.Book.objects.all().aggregate(Avg('price'))       算平均价格
models.Book.objects.values('name').count() 统计书的个数
from django.db.models import Sum
models.Book.objects.all().aggregate(Sum('price'))       算总数

models.Book.objects.values('publisher__name').annotate(Count('id')) 查看每个出版社，总共出了多少书
models.Book.objects.values('publisher__name').annotate(Avg('price'))  每个出版社出的书。平均多少钱


models.Book.objects.filter(name__contains='H',pub_time__year='2016')  and语句 filter匹配2个条件

 result = models.UserInfo.objects.aggregate(k=Count('u_id', distinct=True), n=Count('nid'))     distinct去重  先去重在聚合
Q语句
    Q方法 组合使用，多方法使用
    from django.db.models import Q
    这是一个条件
     Q(pub_time__year='2017')
    <Q: (AND: ('pub_time__year', '2017'))>

    设置or条件
    Q(pub_time__year='2017') | Q(pub_time_year='2016')
    <Q: (OR: ('pub_time__year', '2017'), ('pub_time_year', '2016'))>
    >>> q = Q(pub_time__year='2017') | Q(pub_time__year='2016')
    >>models.Book.objects.filter(q)

    设置and条件
    q2 = Q(pub_time__year=2017),Q(pub_time__year=2016)
    >>> q2
    (<Q: (AND: ('pub_time__year', 2017))>, <Q: (AND: ('pub_time__year', 2016))>)
    这样查询的时候会出错

    >>AttributeError: 'Q' object has no attribute 'split'
F语句
from django.db.models import F
models.Book.objects.update(price=F('price')+10)   给price赋值，然后拿出来在+10  这样所以的price都会加10
models.Book.objects.update(memo=F('name'))       把所有name的值赋给memo


当你新增了表的字段后,你需要python manager.py makemigrations的时候就会提醒你设置一个值
所以你需要 memo =modles.CharField(null=True)


06-18
'''''
class Author(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(unique=True)      #email字段
    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=128,unique=True)
    website = models.URLField(unique=True)      #URL 字段
    def __str__(self):
        return self.name

#出版社是唯一的，所以把出版社定位外键，，那么在添加book的时候，就需要指定这个外键ID
