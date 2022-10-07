from django.db.models.signals import pre_save,post_save #! presave kaydetmeden önce işlem yap
from django.dispatch import receiver 
from .models import Transaction,Product

#! Bir modelde bir işlem olduğundan diğer modeli tetiklemesini istiyorsak

#? total price_total kendimiz signal ile Transaction modeli izleyerek oluşturuyor.
@receiver(pre_save, sender=Transaction)
def calculate_total_price(sender, instance, **kwargs):
    if not instance.price_total:
        instance.price_total = instance.quantity * instance.price


#! Signalin active olması için aşağıda kodu eklemeyi unutma
    """app.py

    def ready(self):
        import stock.signals
    
    """
#? Burada product içerisinde bulunan stock_quantity artırıp azaltmak için
#? Transactionda gönderilen IN ve OUT işlemine göre  product modelinde stock_quantity
#? güncellemek istiyoruz.

@receiver(post_save, sender=Transaction)
def update_stock(sender, instance, **kwargs):
    product=Product.objects.get(id=instance.product_id) # Hangi productı update edeceğimizi belirlememiz gerek!
    if instance.transaction == 1 : # IN==>>stoğa ekleme 
        if not product.stock_quantity: # product stoğu yoksa
            product.stock_quantity = instance.quantity
        else: # product stoğu varsa
             product.stock_quantity += instance.quantity
    else: # OUT==> stocktan çıkarma
       product.stock_quantity -=instance.quantity

       # Stoğun eksiye düşmesini engellenen handle serializer içerisinde
      # belirttik.

    product.save()