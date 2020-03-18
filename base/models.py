from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    title = models.CharField(max_length=100, null=True, unique=True),
    body = models.TextField(null=True)
    display = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def contains_image(self):
        return bool(self.image)

class Contact(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)

    def full_name(self):
        return f'{first_name} {last_name}'

    def __str__(self):
        return self.email

class FAQ(models.Model):
    question = models.CharField(max_length=200, null=True, help_text="Max Characters: 200", unique=True)
    answer = models.TextField(max_length=200, null=True, blank=True)
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class AboutSection(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    body_content = models.TextField(null=True)
    display = models.BooleanField(default=True)
