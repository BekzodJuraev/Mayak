from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import telegram
from .models import Orders,Basket,Basketproducts
from config import BOT_TOKEN,CHANEL_SUPPORT

bot=telegram.Bot(BOT_TOKEN)
group_id=CHANEL_SUPPORT

@receiver(post_save,sender=Orders)
def send_message(sender,instance,created,*args,**kwargs):
    if created:
        bot.send_message(group_id,f'Имя:{instance.name}\nТелефон:{instance.phone}\nПочта:{instance.email}\nСообщение:{instance.message}')


@receiver(post_save,sender=Basketproducts)
def basket_message(sender,instance,created,*args,**kwargs):
    if created:
        basket = instance.basket
        products = basket.products.all()


        product_list = "\n".join([f"🔹 {item.items} (Кол-во: {item.count})" for item in products])

        # Формируем итоговый текст
        message = (
            f" Имя: {basket.name}\n"
            f"📞 Телефон: {basket.phone}\n"
            f"📦 Товары:\n{product_list}"
        )
        bot.send_message(group_id,text=message)

