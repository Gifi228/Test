from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_("title"), max_length=100)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(_("Title"), max_length=20)

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_("title"), max_length=100)
    price = models.IntegerField(_("price"))
    short_desc = models.TextField(_("short description"))
    discount = models.IntegerField(_("discount"), default=0)
    size = models.TextField(_("size"), max_length=2)
    sku = models.TextField(_("sku"), max_length=100)
    description = models.TextField(_("short description"), max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("category"), related_name="product")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name=_("tag"), related_name="tag")

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ForeignKey('media.Media',
                              on_delete=models.CASCADE,
                              verbose_name=_("image"))
    product = models.ForeignKey(Product,
                                verbose_name=_("product"),
                                on_delete=models.CASCADE,
                                related_name="product_images")

    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")

    def __str__(self):
        return f"Image Id: {self.id} | Product: {self.product.title}"



class Characteristic(models.Model):
    title = models.CharField(_("title"), max_length=100)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name=_("product"),
                                related_name="characteristics")

    class Meta:
        verbose_name = _("characteristic")
        verbose_name_plural = _("characteristics")

    def __str__(self):
        return self.title


class CharacteristicValue(models.Model):
    title = models.CharField(_("title"), max_length=100)
    characteristic = models.ForeignKey(Characteristic,
                                       on_delete=models.CASCADE,
                                       verbose_name=_("characteristic"),
                                       related_name="values")

    class Meta:
        verbose_name = _("characteristic value")
        verbose_name_plural = _("characteristic values")

    def __str__(self):
        return self.title


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        NEW = 'new', _('new')
        ACCEPTED = 'accepted', _('accepted')
        CANCELLED = 'cancelled', _('cancelled')
        FINISHED = 'finished', _('finished')

    full_name = models.CharField(_("full name"), max_length=100)

    statuc = models.CharField(_("status"), max_length=20, choices=OrderStatus.choices,
                              default=OrderStatus.NEW)
    total_price = models.FloatField(_("total price"), default=0)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return self.full_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("quantity"), default=1)


    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")
        unique_together = ['order', 'product']

    def __str__(self):
        return f"Id: {self.id}|Q: {self.quantity}"

    @property
    def total_price(self):
        return self.product.price * self.quantity