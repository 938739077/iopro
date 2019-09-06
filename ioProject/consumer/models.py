from django.db import models

# Create your models here.


class Consumer(models.Model):
    # 账号
    Account = models.CharField(max_length=20, blank=False, primary_key=True)
    # 密码
    Password = models.CharField(max_length=20, blank=False)
    # 用户名
    Name = models.CharField(max_length=15, blank=True)
    # 性别 True-男  False-女
    Gender = models.BooleanField(default=True)
    # gender = models.CharField(max_length=2, choices=Gender)
    # 出生日期
    BirthDay = models.DateField(auto_now_add=False, default=None, auto_now=False, blank=True)
    # 用户电话
    Phone = models.CharField(max_length=15, blank=False)
    # 用户邮箱
    Email = models.CharField(max_length=25, blank=True)
    # 创建时间
    CreTime = models.DateField(auto_now_add=True)
    # 最后一次登录时间
    LastUseTime = models.DateField(auto_now=True)

    def create_self(self, option_set):
        self.Account = option_set["Account"]
        self.Password = option_set["Password"]
        self.Name = option_set["Name"]
        self.Gender = True if option_set["Gender"] == "男" else False
        self.BirthDay = option_set["BirthDay"]
        self.Phone = option_set["Phone"]
        self.Email = option_set["Email"]

    class Meta:
        ordering = ['-CreTime']
