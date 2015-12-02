import datetime

from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField

class Province(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Group(models.Model):
    district = models.ForeignKey(District)
    name = models.CharField(max_length=200)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=None, blank=True, null=True)
    branches = models.ManyToManyField(Branch)

    def is_active(self):
        return self.end_date is None or self.end_date < timezone.now()

    is_active.admin_order_field = 'start_date'
    is_active.boolean = True
    is_active.short_description = 'Group active?'

    def __str__(self):
        return self.name

class Person:
    FEMALE = 'F'
    MALE = 'M'
    SEX_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )

    SINGLE = 'SI'
    MARRIED = 'MA'
    PARTNERSHIP = 'PA'
    CIVIL_UNION = 'CI'
    DIVORCED = 'DI'
    SEPARATED = 'SE'
    WIDOWED = 'WI'
    MARITAL_CHOICES = (
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (PARTNERSHIP, 'Partnership'),
        (CIVIL_UNION, 'Civil union'),
        (DIVORCED, 'Divorced'),
        (SEPARATED, 'Separated'),
        (WIDOWED, 'Widowed'),
    )

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    work_phone = PhoneNumberField()

class Parent(models.Model):
    first_names = models.CharField(max_length=200)
    surname = models.CharField(max_length=50)
    sa_id_number = models.CharField(max_length=13)
    date_of_birth = models.DateField()
    postal_address = models.CharField(max_length=200)
    work_phone = PhoneNumberField()
    cell_phone = PhoneNumberField()
    email = models.EmailField()
    sex = models.CharField(max_length=1, choices=Person.SEX_CHOICES, default=Person.FEMALE)
    marital_status = models.CharField(max_length=2, choices=Person.MARITAL_CHOICES, default=Person.SINGLE)
    occupation = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)

    def get_absolute_url(self):
        return "/parent/%i/" % self.id

class Ward(models.Model):
    group = models.ForeignKey(Group)
    first_names = models.CharField(max_length=200)
    surname = models.CharField(max_length=50)
    # Filters to be provided that restrict Ward's branch to those available via the Group
    branch = models.ForeignKey(Branch)
    application_date = models.DateField(default=datetime.date.today)
    sa_id_number = models.CharField(max_length=13)
    date_of_birth = models.DateField(default=datetime.date.today)
    email = models.EmailField()
    sex = models.CharField(max_length=1, choices=Person.SEX_CHOICES, default=Person.FEMALE)
    # research good types for this, includes postcode
    residential_address = models.CharField(max_length=200)
    home_phone = PhoneNumberField()
    cell_phone = PhoneNumberField()
    religious_denomination = models.CharField(max_length=100)
    special_conditions = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor)
    medical_aid_scheme = models.CharField(max_length=50)
    medical_aid_number = models.CharField(max_length=20)
    medical_aid_principal_member = models.CharField(max_length=200)
    parent1 = models.ForeignKey(Parent, related_name='%(class)s_parent1')
    parent2 = models.ForeignKey(Parent, related_name='%(class)s_parent2')
    """
    signatory_parent # FK onto either parent_1 or parent_2 below
    home_phone # if not provided, mobile_phone must be provided
    mobile_phone # if not provided, home_phone must be provided
    sex # male or female enum
    religious_denomination
    special_conditions # handicap, disability, special health conditions, not permitted activity, etc
    doctor # might be an FK onto known doctors, but must make extension of that list easy
    doctor_phone # if doctor is an FK, then this can be autopopulated quite easily
    medical_aid_scheme
    medical_aid_number
    medical_aid_principal_member_name
    parent_1 # FK onto parent
    parent_2 # FK onto parent
    """
    def first_name(self):
        return hasattr(self, 'preferred_first_name') and self.preferred_first_name or self.first_names.split()[:1]
    first_name.admin_order_field = 'first_names'

    def initials(self):
        pass

    def __str__(self):
        return self.first_names + ' ' + self.surname
