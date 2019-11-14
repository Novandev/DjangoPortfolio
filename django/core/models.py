from django.db import models

# Create your models here.

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


class Project(models.Model):

    name = models.CharField(
        max_length=50)

    description =models.TextField(
        max_length=650)

    languages =  models.TextField(
        max_length=350)

    technologies_used = models.TextField(
        max_length=350)

    github_link = models.URLField(max_length=350,default='http://www.github.com/novandev')

    live_link = models.URLField(max_length=350,default='http://www.github.com/novandev')

    def __str__(self):
        return 'name: {}\n description:{}\n languages: {}\n technologies_used: {}\n github_link:{}\n live_link:{} '.format(self.name, self.description, self.languages,self.technologies_used,self.github_link,self.live_link)



class Like(models.Model):
    created



# new_project = Project.objects.create(
# name="project1",
#  description="an apt description",
#  languages="all of them",
#  technologies_used="all of them",
#  github_link="http://www.github.com/novandev",
#  live_link="http://www.github.com/novandev"
#  )