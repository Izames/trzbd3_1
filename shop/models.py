from django.db import models

class Forge(models.Model):
    name = models.CharField(max_length=50, verbose_name="название мода")
    version = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField(blank=True, verbose_name="описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    photo = models.ImageField(null=True, upload_to='image/%Y%m%d%h', blank=True)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    #OtD = models.OneToOneField(Author, on_delete=models.PROTECTED)
    #MtM = models.ManyToManyField(Author) # связь через автоматические промежуток таблиц
    Order = models.ManyToManyField('Order', through='Pos_Forge_order')
    def __str__(self):
        return f"{self.name} - {self.price}"
    def __lt__(self, other):
        if self.name < other.name:
            return True
        return False
    class Meta:
        verbose_name = "мод фордж"
        verbose_name_plural = "моды фордж"
        ordering = ['name', '-price']

class Author(models.Model):
    name = models.CharField()
    description =models.CharField(null=True)
class Order(models.Model):
    name = models.CharField()
    date_create = models.DateTimeField(auto_now_add=True)
class Pos_Forge_order(models.Model):
    chocolate = models.ForeignKey(Forge, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    count_mods = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2)

