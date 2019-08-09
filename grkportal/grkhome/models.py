from django.db import models


class MemberRegister(models.Model):
    applicant_first_name = models.CharField(max_length=50, null=True)
    applicant_last_name = models.CharField(max_length=50, null=True)
    applicant_mobile = models.IntegerField(max_length=10, null=True)
    applicant_occupation = models.CharField(max_length=25, null=True)
    applicant_company = models.CharField(max_length=25, null=True)
    # spouse_first_name = models.CharField(max_length=50, null=True)
    # spouse_last_name = models.CharField(max_length=50, null=True)
    # spouse_mobile = models.IntegerField(max_length=10, nul=True)
    # spouse_occupation = models.CharField(max_length=25, null=True)
    # spouse_company = models.CharField(max_length=25, null=True)
    applicant_ca_homeNumber = models.IntegerField(max_length=6, null=True)
    ca_street_name = models.CharField(max_length=50, null=True)
    ca_place = models.CharField(max_length=50, null=True)
    ca_pincode = models.CharField(max_length=50, null=True)
    in_homeNumber = models.IntegerField(max_length=6, null=True)
    in_street_name = models.CharField(max_length=50, null=True)
    in_place = models.CharField(max_length=50, null=True)
    in_pincode = models.CharField(max_length=50, null=True)
    in_conatctNumber = models.IntegerField(max_length=10, null=True)
