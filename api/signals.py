from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import telegram
from .models import Orders

bot=telegram.Bot("7990952348:AAHho7QK_-J_WIQkoG54HIZ5w5iUDhYj4d4")
group_id=-4780572548
@receiver(post_save,sender=Orders)
def send_message(sender,instance,created,*args,**kwargs):
    if created:
        bot.send_message(group_id,f'Имя:{instance.name}\nТелефон:{instance.phone}\nПочта:{instance.email}\nСообщение:{instance.message}')

