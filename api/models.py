from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


def get_business_year_default():
    return datetime.today().date().year


class Installer(models.Model):
    user = models.OneToOneField(User, db_index=True, on_delete=models.CASCADE, verbose_name='인스톨 연결된 아이디',
                                limit_choices_to={'groups__name': '인스톨'}, related_name='installer')

    business_year = models.TextField('사업년도', blank=True, default=get_business_year_default)
    teams = models.CharField('인스톨 목록', max_length=100, default='', blank=True)

    # 대여사업자였다가 활성화가 안된 시공사는 따로 관리한다.
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')

    def __unicode__(self):
        return "%s" % self.user

    def __str__(self):
        return "{} {}".format(self.business_year, self.teams)

    class Meta:
        verbose_name_plural = u'인스톨 목록'
        verbose_name = u'인스톨'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    subtitle = models.CharField(max_length=144, blank=True)
    content = models.TextField()
    installer = models.ForeignKey(Installer, db_index=True, null=True, blank=True, verbose_name='인스톨',
                                  on_delete=models.SET_NULL, help_text='인스톨')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[{}] {}'.format(self.user.username, self.title)

    def temp(self):
        return self.title + '-temp'
