from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    Campus_Name = models.CharField(max_length=100, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input values from Campus Name and State
        # fields to display in the browser, under University Campus list
        display_campus = '{0.Campus_Name}: {0.State}'
        return display_campus.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"
