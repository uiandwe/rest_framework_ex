from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)

    def __repr__(self):
        return "{} {}".format(self.name, self.price)


class Order(models.Model):
    order_state = (
        (0, "cancel"),
        (1, "ready"),
        (2, "completed_order"),
        (3, "shipping"),
        (4, "completed_shipping")
    )

    order_name = models.CharField(max_length=100)
    total_amount = models.IntegerField(default=0)
    state = models.IntegerField(choices=order_state, default=1)
    products = models.ManyToManyField(Product)

    def __repr__(self):
        return "{} {} {}".format(self.order_name, self.total_amount, self.state)
