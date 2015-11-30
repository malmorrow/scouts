import datetime

from django.db import models
from django.utils import timezone

class Province(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province)

    def __str__(self):
        return self.name

class Group(models.Model):
    district = models.ForeignKey(District)
    name = models.CharField(max_length=200)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=None, blank=True, null=True)
    mal = models.CharField(max_length=2)

    def is_active(self):
        return self.end_date is None or self.end_date < timezone.now()

    is_active.admin_order_field = 'start_date'
    is_active.boolean = True
    is_active.short_description = 'Group active?'

    def __str__(self):
        return self.name

class Branch(models.Model):
    BROWNIE = 'BR'
    CUB = 'CU'
    GUIDE = 'GU'
    SCOUT = 'SC'
    BRANCH_CHOICES = (
        (BROWNIE, 'Brownie'),
        (CUB, 'Cub'),
        (GUIDE, 'Guide'),
        (SCOUT, 'Scout'),
    )

class Ward(models.Model):
    group = models.ForeignKey(Group)
    first_names = models.CharField(max_length=200)
    surname = models.CharField(max_length=50)
    branch = models.CharField(max_length=2, choices=Branch.BRANCH_CHOICES, default=Branch.CUB)
    application_date = models.DateField(default=datetime.date.today)
    sa_id_number = models.CharField(max_length=10)
    date_of_birth = models.DateField(default=datetime.date.today)
    email = models.EmailField()
    """
    signatory_parent # FK onto either parent_1 or parent_2 below
    residential_address # research good types for this, includes postcode
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
