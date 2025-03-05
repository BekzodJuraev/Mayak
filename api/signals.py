from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import telegram
from .models import Orders,Basket,Basketproducts
from config import BOT_TOKEN,CHANEL_SUPPORT,API_KEY_GOOGLE
from googleapiclient.discovery import build
API_KEY = API_KEY_GOOGLE
SPREADSHEET_ID = "1z7CKVIOjz30amDeUlFkPZl-mSNW_gymkASNSv-Ot10E"
RANGE_NAME = "Лист1!B2:B"
service = build("sheets", "v4", developerKey=API_KEY)
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
        try:
            # Fetch data
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
            values = result.get("values", [])

            # Print the values
            if not values:
                pass
            else:
                for row in values:
                    if basket.phone in row[0]:
                       message+="Это Резидент"

        except Exception as e:
            pass
        bot.send_message(group_id,text=message)

