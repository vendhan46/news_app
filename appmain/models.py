from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=50, unique=True, default=0)  # <- fixed here
    phone = models.BigIntegerField(default=0)  # Use BigIntegerField for 10-digit numbers
    address = models.CharField(max_length=100, default='')
    interested_field = models.CharField(max_length=50, default='')
    image=models.ImageField(upload_to='images/',default='')

    def __str__(self):
        return self.username



# Main Opinion/Editorials Model
class Opinion(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Reader's Opinions (Letters to the Editor)
class ReaderOpinion(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.message[:30]}"


# Opinion Poll
class Poll(models.Model):
    question = models.CharField(max_length=255)
    yes_votes = models.IntegerField()
    no_votes = models.IntegerField()

    def __str__(self):
        return self.question


class video(models.Model):
    category_choices={
        ('news', 'News'),
        ('sport', 'Sports'),
        ('technology', 'Technology'),
        ('science','Science'),
        ('entertainment', 'Entertainment'),
        ('bussiness', 'bussiness')
    }
    title=models.CharField(max_length=100, default='')
    description=models.CharField(max_length=100, default='')
    category=models.CharField(max_length=30,choices=category_choices, default='')
    youtube_url=models.URLField(blank=True, null=True)
    video_file=models.FileField(upload_to='videos/', blank=True, null=True)
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class bookmark(models.Model):
    image_url=models.URLField(blank=False,null=False)
    url=models.URLField(blank=False,null=False)
    title=models.CharField(max_length=100,default="")
    description=models.CharField(max_length=255,default="")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    



