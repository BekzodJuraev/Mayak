from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import telegram
from .models import Orders
from config import BOT_TOKEN,CHANEL_SUPPORT

bot=telegram.Bot(BOT_TOKEN)
group_id=CHANEL_SUPPORT

@receiver(post_save,sender=Orders)
def send_message(sender,instance,created,*args,**kwargs):
    if created:
        bot.send_message(group_id,f'Имя:{instance.name}\nТелефон:{instance.phone}\nПочта:{instance.email}\nСообщение:{instance.message}')

