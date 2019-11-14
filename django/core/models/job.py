from django.db import models


class Job(models.Model):


    company_name = models.CharField(
        max_length=50)

    location = models.CharField(
        max_length=50)

    job_title = models.CharField(
        max_length=50)

    job_description =models.TextField(
        max_length=650)

    dates_employed =  models.CharField(
        max_length=50)

    languages =  models.TextField(
        max_length=350)

    technologies_used = models.TextField(
        max_length=350)


    def __str__(self):
            return 'job_title: {}\n location:{}\n job_title:{}\n job_description:{}\n dates_employed:{}\n languages: {}\n technologies_used: {}'.format(
                self.company_name,self.job_title, self.location, self.job_title, self.job_description,self.dates_employed,self.languages, self.technologies_used )