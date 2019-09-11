from django import forms
import re
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
# Create your models here.


class TestForm(forms.Form):
    testAct = forms.CharField()
    testPwd = forms.CharField()


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


is_male_female = (
    ("true", "男"),
    ("false", "女"),
)


class ConsumerForm(forms.Form):
    # 账号
    Account = forms.CharField()
    # 密码
    Password = forms.CharField(widget=forms.PasswordInput())
    # 密码
    RePassword = forms.CharField(widget=forms.PasswordInput())
    # 用户名
    Name = forms.CharField()
    # 性别 True-男  False-女
    Gender = forms.CharField(widget=forms.widgets.Select(choices=is_male_female))
    # 出生日期
    BirthDay = forms.DateField(widget=forms.DateTimeInput(attrs={"type": "date"}))
    # 用户电话
    Phone = forms.CharField(validators=[mobile_validate, ], error_messages={"required": "手机不能为空"},
                            widget=forms.TextInput(attrs={"class": "form-control",
                                                          "placeholder": "手机号码"}))
    # 用户邮箱
    Email = forms.CharField()
    # 创建时间
    # CreTime = forms.DateField()
    # 验证码
    Captcha = CaptchaField(error_messages={'invalid': "验证码错误"})


class LoginForm(forms.Form):
    # 账号
    Account = forms.CharField()
    # 密码
    Password = forms.CharField(widget=forms.PasswordInput())
    # 验证码
    Captcha = CaptchaField(error_messages={'invalid': "验证码错误"})
