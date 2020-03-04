# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Bigsmall(models.Model):
    companyid = models.ForeignKey('Companyodds', db_column='CompanyId')  # Field name made lowercase.
    gameinfo = models.ForeignKey('Gameinfo', db_column='GameinfoId', blank=True, null=True)
    handicap = models.FloatField(db_column='Handicap', blank=True,
                                default='0')  # Field name made lowercase.
    big = models.FloatField(db_column='Big', blank=True, null=True)  # Field name made lowercase.
    small = models.FloatField(db_column='Small', blank=True, null=True)  # Field name made lowercase.
    is_half = models.BooleanField(db_column='is_half',default=0)

    class Meta:
        verbose_name_plural = '大小表'
        verbose_name = '大小表'

    def __str__(self):
        return self.gameinfo.homename + '&' + self.gameinfo.visitname


class Companyodds(models.Model):
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    updatetime = models.BigIntegerField(db_column='Updatetime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name_plural = '赔率表'
        verbose_name = '赔率表'

    def __str__(self):
        return self.name


# class CompanyGameinfo(models.Model):
#     company_id = models.ForeignKey('Companyodds',db_column='Company_Id')  # Field name made lowercase.
#     gameinfo_id = models.ForeignKey('Gameinfo',db_column='Gameinfo_Id')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Company_Gameinfo'
#

class Eventinfo(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(max_length=255, default='')
    class Meta:
        verbose_name_plural = '联赛'
        verbose_name = '联赛'

    def __str__(self):
        return self.name


class Gameinfo(models.Model):
    eventid = models.ForeignKey('Eventinfo', db_column='EventId')  # Field name made lowercase.
    homename = models.CharField(db_column='HomeName', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    gametime = models.DateTimeField(db_column='GameTime')  # Field name made lowercase.
    visitname = models.CharField(db_column='VisitName', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    Companyodds = models.ManyToManyField(to='Companyodds', verbose_name='比赛的开注公司', blank=True)

    class Meta:
        verbose_name_plural = '比赛信息'
        verbose_name = '比赛信息'

    def __str__(self):
        return self.homename + '&' + self.visitname


class Letball(models.Model):
    companyid = models.ForeignKey('Companyodds', db_column='CompanyId', blank=True,
                                  null=True)  # Field name made lowercase.
    gameinfo = models.ForeignKey('Gameinfo', db_column='GameinfoId', blank=True, null=True)
    left = models.FloatField(db_column='left',default=0)
    right = models.FloatField(default=0)
    Handicap = models.FloatField(default='0')  # 盘口
    is_half = models.BooleanField(db_column='is_half',default=0)

    class Meta:
        verbose_name_plural = '让球赔率'
        verbose_name = '让球赔率'

    def __str__(self):
        return self.gameinfo.homename + '&' + self.gameinfo.visitname


class Teaminfo(models.Model):
    name = models.CharField(unique=True, max_length=100)
    eventid = models.ForeignKey('Eventinfo', db_column='EventId', default=1)
    detail = models.TextField(max_length=255, default='')

    class Meta:
        verbose_name_plural = '队伍信息'
        verbose_name = '队伍信息'

    def __str__(self):
        return self.name


class Winalone(models.Model):
    companyid = models.ForeignKey('Companyodds', db_column='CompanyId')  # Field name made lowercase.
    gameinfo = models.ForeignKey('Gameinfo', db_column='GameinfoId', blank=True, null=True)
    win = models.FloatField(db_column='win',default=0)  # Field name made lowercase.
    lose = models.FloatField(db_column='lose',default=0)  # Field name made lowercase.
    draw = models.FloatField(db_column='draw',default=0)  # Field name made lowercase.
    is_half = models.BooleanField(db_column='is_half',default=0)

    class Meta:
        verbose_name_plural = '独赢赔率'
        verbose_name = '独赢赔率'

    def __str__(self):
        return self.gameinfo.homename + '&' + self.gameinfo.visitname
