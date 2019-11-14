from django.db import models



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