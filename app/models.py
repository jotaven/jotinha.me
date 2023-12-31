from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/', default='portfolio/images/default.png')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Projects'
    