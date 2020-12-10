from django.db import models
# Create your models here.


class Loaner(models.Model):
    class Meta:
        db_table = 'loaner'
    # loaner唯一ID（主键）
    loaner_id = models.AutoField(primary_key=True)  # AutoField 自增长字段 int型
    # SN
    loaner_sn = models.TextField(verbose_name='SN')
    # 请求人
    loaner_request = models.TextField(verbose_name='外借人')
    # 借出时间
    request_time = models.DateTimeField(auto_now=True,verbose_name='外借时间')
    # 是否归还
    loaner_status = models.BooleanField(verbose_name='是否归还')