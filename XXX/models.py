from django.db import models


# Create your models here.


class LoginUser(models.Model):
    email = models.CharField('邮箱', primary_key=True, max_length=30)
    pwd = models.CharField('密码', max_length=20)

    class Meta:
        verbose_name = "登陆用户表"
        verbose_name_plural = "登陆用户表"
        managed = True
        db_table = 'login_user'

    def __str__(self):
        return str(self.email)


class UserInfo(models.Model):
    email = models.ForeignKey(verbose_name='邮箱', to="LoginUser", to_field="email", on_delete=models.CASCADE,
                              primary_key=True)
    account = models.CharField('昵称', max_length=20, default='一只小XX')
    head_img = models.ImageField('头像', upload_to='head_img/', default='/static/images/1.jpg')
    credit = models.IntegerField('信誉值', default=100)

    class Meta:
        verbose_name = "用户基本信息表"
        verbose_name_plural = "用户基本信息表"
        managed = True
        db_table = 'user_info'

    def __str__(self):
        return str(self.email)


class RealName(models.Model):
    rnid = models.AutoField('id', primary_key=True)
    email = models.ForeignKey(to="LoginUser", to_field="email", on_delete=models.CASCADE)
    name = models.CharField('真实姓名', max_length=10)
    sex = models.CharField('性别', max_length=4)
    age = models.IntegerField('年龄')
    phone = models.CharField('电话号码', max_length=11)
    idnumber = models.CharField('身份证号', max_length=18)
    idfront = models.ImageField('身份证正面照片', upload_to='id_img/front/')
    idbehind = models.ImageField('身份证背面照片', upload_to='id_img/behind/')
    date = models.DateTimeField('上传时间', )
    status = models.IntegerField('是否通过认证', default=0)

    class Meta:
        verbose_name = "用户实名认证表"
        verbose_name_plural = "用户实名认证表"
        managed = True
        db_table = 'real_name'

    def __str__(self):
        return str(self.rnid)


class UserHome(models.Model):
    hid = models.AutoField('id', primary_key=True)
    email = models.ForeignKey(to="LoginUser", to_field="email", on_delete=models.CASCADE)
    name = models.CharField('住屋名称', max_length=20)
    location = models.CharField('住屋详细地址', max_length=50)
    area = models.IntegerField('住屋面积/平方米')
    type = models.CharField('住屋类型', max_length=8)
    prove = models.ImageField('住屋证明照片', upload_to='home_prove/')
    prove_date = models.DateTimeField('通过认证时间', blank=True, null=True)
    status = models.IntegerField('是否通过认证', default=0)

    class Meta:
        verbose_name = "用户住屋表"
        verbose_name_plural = "用户住屋表"
        managed = True
        db_table = 'user_home'

    def __str__(self):
        return str(self.hid)


class UserPublish(models.Model):
    pid = models.AutoField('id', primary_key=True)
    email = models.ForeignKey(to="LoginUser", to_field="email", on_delete=models.CASCADE)
    home_name = models.CharField('房屋名称', max_length=20)
    title = models.CharField('标题', max_length=50)
    role = models.CharField('房屋准则', max_length=100, blank=True, null=True)
    price = models.IntegerField('价格/元每晚')
    start_date = models.DateField('闲屋开始时间')
    end_date = models.DateField('闲屋结束时间')
    situation_desc = models.CharField('住房附近交通情况', max_length=200, blank=True, null=True)
    facilities = models.CharField('住房家具设施', max_length=100, blank=True, null=True)
    image_num = models.IntegerField('住房照片数量', default=0)
    status = models.IntegerField('发布是否过期', default=0)
    date = models.DateField('发布日期', blank=True, null=True)

    class Meta:
        verbose_name = "用户发布房屋表"
        verbose_name_plural = "用户发布房屋表"
        managed = True
        db_table = 'user_publish'

    def __str__(self):
        return str(self.pid)


class HomeImage(models.Model):
    pid = models.ForeignKey(to="UserPublish", to_field="pid", on_delete=models.CASCADE)
    image_id = models.IntegerField('照片ID')
    image = models.ImageField('照片', upload_to='home_img/')

    class Meta:
        verbose_name = "住屋照片表"
        verbose_name_plural = "住屋照片表"
        unique_together = ("pid", "image_id")
        managed = True
        db_table = 'home_image'

    def __str__(self):
        return str(self.pid)


class BannerImage(models.Model):
    bid = models.AutoField('id', primary_key=True)
    image = models.ImageField('轮播图片', upload_to='banner/')
    text_desc = models.CharField('文字描述',max_length=100,blank=True,null=True)
    status = models.BooleanField('是否显示')

    class Meta:
        verbose_name = "首页轮播图"
        verbose_name_plural = "首页轮播图"
        managed = True
        db_table = 'banner_image'

    def __str__(self):
        return str(self.bid)
