from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField()
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    # departments = models.ManyToManyField(Department),
    # grant_id = models.ForeignKey('GrantID')

    # Need revision, enum for status, something else for file
    status = models.CharField(max_length=50)
    file_link = models.CharField(max_length=200)

    # Author information
    PI_first_name = models.CharField(max_length=50)
    PI_last_name = models.CharField(max_length=50)
    PI_email = models.EmailField(max_length=100)

    author_list = models.CharField(max_length=500)

    class Meta:
        permissions = (
            ('view_document', 'View document'),
        )


# class Author(models.Model):
# 	name_first = models.CharField(max_length=50)
# 	name_middle = models.CharField(max_length=50, blank=True)
# 	name_last = models.CharField(max_length=50)
# 	email = models.EmailField(max_length=100, default='')
# 	documents = models.ManyToManyField(Document)


class Department(models.Model):
    name = models.CharField(max_length=50)
    documents = models.ManyToManyField(Document)
    # Admins or Users?

    # Possible way to represent grantIDs
    # class GrantID(models.Model):
    # 	id = models.CharField(max_length=100)
    # 	department = models.ForeignKey('Department')
    #	document = models.ManyToMany('Document')

    # User and Admin Groups
