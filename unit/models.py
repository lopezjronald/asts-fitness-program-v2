from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(active_status='active')


class Airman(models.Model):
    ACTIVE_CHOICE = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    RANK_CHOICE = (
        ('AB', 'AB'),
        ('Amn', 'Amn'),
        ('A1C', 'A1C'),
        ('SrA', 'SrA'),
        ('SSgt', 'SSgt'),
        ('TSgt', 'TSgt'),
        ('MSgt', 'MSgt'),
        ('SMSgt', 'SMSgt'),
        ('CMSgt', 'CMSgt'),
        ('2nd Lt', '2nd Lt'),
        ('1st Lt', '1st Lt'),
        ('Capt', 'Capt'),
        ('Maj', 'Maj'),
        ('Lt Col', 'Lt Col'),
        ('Col', 'Col'),
        ('Brig Gen', 'Brig Gen'),
        ('Maj Gen', 'Maj Gen'),
        ('Lt Gen', 'Lt Gen'),
        ('Gen', 'General'),
    )
    FITNESS_CHOICE = (
        ('Excellent', 'EXCELLENT'),
        ('Satisfactory', 'SATISFACTORY'),
        ('Pass', 'PASS'),
        ('Unsatisfactory', 'UNSATISFACTORY'),
        ('Fail', 'FAIL'),
        ('Exemption', 'EXEMPTION'),
    )
    airman_id = models.AutoField(primary_key=True, serialize=True)
    fitness_level = models.CharField(max_length=50,
                                     choices=FITNESS_CHOICE,
                                     default='satisfactory')
    rank = models.CharField(max_length=10,
                            choices=RANK_CHOICE,
                            default='AB')
    first_name = models.CharField(max_length=20)
    middle_initial = models.CharField(max_length=5)
    last_name = models.CharField(max_length=20)
    ssn = models.IntegerField()
    airman_slug = models.SlugField(max_length=50,
                                   unique_for_date='test_date')
    test_date = models.DateField()
    ptl = models.BooleanField(default=False)
    ufpm = models.BooleanField(default=False)
    active_status = models.CharField(max_length=10,
                                     choices=ACTIVE_CHOICE,
                                     default='Active')

    class Meta:
        verbose_name = 'Airman'
        verbose_name_plural = 'AIRMEN'
        ordering = ('last_name',)

    def __str__(self):
        return f"{self.rank} {self.first_name} {self.middle_initial} {self.last_name}"

    objects = models.Manager()
    active = ActiveManager()

    def get_absolute_url(self):
        return reverse('unit:airman_detail',
                       args=[self.test_date.year,
                             self.test_date.month,
                             self.test_date.day,
                             self.airman_slug])


class Naughty(models.Model):
    NAUGHTY_CHOICE = (
        ('Fail', 'FAIL'),
        ('Unsatisfactory', 'UNSATISFACTORY'),
        ('Non-Current', 'NON-CURRENT'),
    )
    naughty_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.CASCADE, )
    failure_date = models.DateField()
    be_well_completion_date = models.DateField()
    status_level = models.CharField(max_length=50,
                                    choices=NAUGHTY_CHOICE, )

    class Meta:
        verbose_name = 'Failure, Unsatisfactory, & Non-Current'
        verbose_name_plural = 'FAILURE, UNSATISFACTORY, & NON-CURRENTS'
        ordering = ('-failure_date',)

    def clean(self):
        if self.failure_date and self.be_well_completion_date:
            if self.failure_date > self.be_well_completion_date:
                raise ValidationError('Failure Date cannot be after the Be Well Completion Date')

    def __str__(self):
        return f"{self.airman_id}"


class PhysicalTrainingLeader(models.Model):
    ptl_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.CASCADE, )
    ptl_certification_date = models.DateField()
    ptl_expiration_date = models.DateField()
    cpr_expiration_date = models.DateField()

    class Meta:
        verbose_name = 'Physical Training Leader'
        verbose_name_plural = 'PHYSICAL TRAINING LEADERS'
        ordering = ('ptl_expiration_date',)

    def clean(self):
        if self.ptl_certification_date and self.ptl_expiration_date:
            if self.ptl_certification_date >= self.ptl_expiration_date:
                raise ValidationError('Expiration Date must be later than the Certification Date')

    def __str__(self):
        return f"{self.airman_id}"


class UnitFitnessProgramManager(models.Model):
    ufpm_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.CASCADE, )
    ptl_id = models.ForeignKey(
        PhysicalTrainingLeader,
        on_delete=models.CASCADE, )
    ufpm_certification_date = models.DateField()
    ufpm_expiration_date = models.DateField()

    class Meta:
        verbose_name = 'Unit Fitness Program Manager'
        verbose_name_plural = 'UNIT FITNESS PROGRAM MANAGERS'
        ordering = ('ufpm_expiration_date',)

    def clean(self):
        if self.ufpm_certification_date and self.ufpm_expiration_date:
            if self.ufpm_certification_date >= self.ufpm_expiration_date:
                raise ValidationError('Expiration Date must be later than the Certification Date')
        if self.airman_id and self.ptl_id:
            if str(self.airman_id) != str(self.ptl_id):
                raise ValidationError("Airman ID and PTL ID Must Match")

    def __str__(self):
        return f"{self.airman_id}"


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True, serialize=True)
    airman_id = models.ForeignKey(
        Airman,
        on_delete=models.CASCADE, )
    profile_start_date = models.DateField()
    profile_expiration_date = models.DateField()
    profile_details = models.TextField()

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'PROFILES'
        ordering = ('profile_expiration_date',)

    def clean(self):
        if self.profile_start_date and self.profile_expiration_date:
            if self.profile_start_date > self.profile_expiration_date:
                raise ValidationError('Profile Start Date must be later than the Profile Expiration Date')

    def __str__(self):
        return f"{self.airman_id}"
