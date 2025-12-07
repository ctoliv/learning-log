from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # --- NEW FIELDS FOR YOUR FEATURE ---
    # When you studied
    study_date = models.DateField(null=True, blank=True)

    # Where you studied
    STUDY_LOCATION_CHOICES = [
        ('home', 'Home'),
        ('library', 'Library'),
        ('work', 'Work'),
        ('classroom', 'Classroom'),
        ('coffee', 'Coffee shop'),
        ('other', 'Other'),
    ]
    study_location = models.CharField(
        max_length=50,
        choices=STUDY_LOCATION_CHOICES,
        default='home',
    )

    # How many hours you studied
    hours_spent = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=0,
        help_text="Hours spent studying for this entry (e.g., 0.5, 1.0, 2.5).",
    )
    # -----------------------------------

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..."