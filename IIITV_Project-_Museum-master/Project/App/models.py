from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.utils.translation import ugettext_lazy as _



class Project(models.Model):
    CHOICES=(('ONE','I'),
            ('TWO','II'),
            ('THREE','III'),
            ('FOUR','IV'),
            ('FIVE','V'),
            ('SIX','VI'),
            ('SEVEN','VII'),
            ('EIGHT','VIII'),)
    semester=models.CharField(max_length=100,choices=CHOICES)
    course_name=models.CharField(max_length=100)
    project_name=models.CharField(max_length=100)
    project_description=models.TextField(max_length=100)
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    faculty_mentor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='faculty_mentor')
    student_mentor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='student_mentor')
    likes = models.ManyToManyField(User,blank=True,null=True,related_name='likes')
    file_upload = models.FileField(blank=True, null=True, verbose_name=_("file"))

    #class Meta:
    #    verbose_name = _("Project")
    #    verbose_name_plural = _("Projects")

    def __str__(self):
        return self.semester + "  " + self.course_name + " " + self.project_name

class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    kind = models.CharField(max_length=100, default="Mentor")

    class Meta:
        verbose_name = _("Relationship")
        verbose_name_plural = _("Relationships")

    def __str__(self):
        return str(
            self.from_user.name + " - " +
            self.to_user.name + " (" +
            self.kind.name + ")")
