from django.db import models


# Create your models here.


class UpdateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(UpdateMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    shipping_address = models.TextField()
    product_cart = models.ForeignKey('Cart', on_delete=models.CASCADE)


class Product(UpdateMixin):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    name = models.TextField()
    description = models.TextField()


class Cart(UpdateMixin):
    id = models.AutoField(primary_key=True)
    cart_code = models.CharField(max_length=6)
    is_paid = models.BooleanField()
    products = models.ManyToManyField(Product)

    def get_total_price(self):
        sum = 0
        for product in self.products:
            sum += product
        return sum
