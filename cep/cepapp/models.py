from django.db import models

# Create your models here.



class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank=True, null=True)
    editor = models.CharField(max_length=50, blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    p = models.ForeignKey('Publisher', models.DO_NOTHING, blank=True, null=True)
    s = models.ForeignKey('Staff', models.DO_NOTHING, blank=True, null=True)
    r = models.ForeignKey('Reader', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class Publisher(models.Model):
    publisher_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    year_of_publishing = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publisher'


class Reader(models.Model):
    reader_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reader'


class Reports(models.Model):
    reg_id = models.IntegerField(primary_key=True)
    issue_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    fine = models.IntegerField(blank=True, null=True)
    book_id = models.IntegerField()
    reader_id = models.IntegerField()
    reg_by = models.ForeignKey('Staff', models.DO_NOTHING, db_column='reg_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reports'


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    login = models.ForeignKey('System', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'staff'


class System(models.Model):
    login_id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'system'