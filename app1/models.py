from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя автора')
    surname = models.CharField(max_length=255, verbose_name='фамилия  автора')
    date_birth = models.DateField()
    photo = models.ImageField(upload_to='authors_photo/', blank=True,
                              null=True, default='')

    def __str__(self):
        return '{} {} {}'.format(self.name, self.surname, self.date_birth)

    def author_to_string(self):
        return 'Имя  - {} Фамилия - {}'.format(self.name, self.surname)


class Book(models.Model):
    # title price author full_text file
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=0, blank=True, null=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    img = models.ImageField(upload_to='img_book/', blank=True, null=True, default='')
    description = models.TextField(max_length=1000)
    file = models.FileField(upload_to='files_book/', blank=True, null=True, default='')
    books_read_with = models.ManyToManyField('self', default='', blank=True, null=True)

    def __str__(self):
        return '{} {} $'.format(self.title, self.price)

    # pass

# id=1 a

# id=3 c
# ....
# ....
# ....
# ....
# ....
# ....
# ....
# ....
# id = 999
