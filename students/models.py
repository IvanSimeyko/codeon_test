from django.db import models
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):
    """Student Model"""

    class Meta(object):
        verbose_name = _(u"Student")
        verbose_name_plural = _(u"Students")

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"First Name")
    )

    last_name = models.CharField(
        # help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
        max_length=256,
        blank=False,
        verbose_name=_(u"Last Name")
    )

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=_(u"Middle Name"),
        default=''
    )

    birthday = models.DateField(
        blank=False,
        verbose_name=_(u"Birthday"),
        null=True
    )

    photo = models.ImageField(
        blank=True,
        verbose_name=_(u"Photo"),
        null=True
    )

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"Ticket")
    )

    notes = models.TextField(
        blank=True,
        verbose_name=_(u"Notes"))

    student_group = models.ForeignKey('Group',
        verbose_name=_(u"Group"),
        blank=False,
        null=True,
        on_delete=models.PROTECT
    )

    def __unicode__(self):
        return u"%s %s" % (self.first_name,self.last_name)


class Group(models.Model):
    """Group Model"""

    class Meta(object):
        verbose_name = _(u"Group")
        verbose_name_plural = _(u"Groups")

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"Title")
    )

    starosta = models.OneToOneField(
        'Student',
        verbose_name=_(u"Leader"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    notes = models.TextField(
        blank=True,
        verbose_name= _(u"Notes")
    )

    def __unicode__(self):
        if self.starosta:
            return u"%s ( %s %s)" % (self.title, self.starosta.first_name, self.starosta.last_name)
        else:
            return u"%s" % (self.title,)