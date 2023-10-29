from django.db import models
from shortuuid.django_fields import ShortUUIDField  # for id generation
from django.utils.html import mark_safe
from userauths.models import User

STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("in_review", "In Review"),
    ("rejected", "Rejected"),
    ("published", "Published"),
)

RATING = (
    (1, "⭐✰✰✰✰"),
    (2, "⭐⭐✰✰✰"),
    (3, "⭐⭐⭐✰✰"),
    (4, "⭐⭐⭐⭐✰"),
    (5, "⭐⭐⭐⭐⭐"),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


# Create your models here.

class Category(models.Model):
    cId = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefghi12345")
    title = models.CharField(max_length=100, default="clothes")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Staff(models.Model):
    stId = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven", alphabet="abcdefghi67891")

    name = models.CharField(max_length=100, default="Myname")
    image = models.ImageField(upload_to=user_directory_path, default='staff.jpg')
    description = models.TextField(null=True, blank=True, default="Great team")

    adress = models.CharField(max_length=100, default="135, Main street Moscow")
    contact = models.CharField(max_length=100, default="+7(977) 657 689")
    chat_resp_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Staffs"

    def staff_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.name


class Product(models.Model):
    pId = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghi12345")

    title = models.CharField(max_length=100, default="Adidas")
    image = models.ImageField(upload_to=user_directory_path, default='product.jpg')
    description = models.TextField(null=True, blank=True, default="Best wine")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    price = models.DecimalField(max_digits=9999999, decimal_places=2, default="2.99")
    old_price = models.DecimalField(max_digits=9999999, decimal_places=2, default="3.99")

    specification = models.TextField(null=True, blank=True)

    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=20, prefix="sku", alphabet="123456789")

    date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price

# To display images of a given product
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"


# ##service

# for service provided by us
class Service(models.Model):
    sId = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghi12345")

    title = models.CharField(max_length=100, default="Adidas")
    image = models.ImageField(upload_to=user_directory_path, default='product.jpg')
    description = models.TextField(null=True, blank=True, default="The product")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    specification = models.TextField(null=True, blank=True)
    # tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    service_status = models.CharField(choices=STATUS, max_length=10, default="in_review")

    status = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=20, prefix="sku", alphabet="123456789")

    date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Services"

    def service_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

# For product review
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating




