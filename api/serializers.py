from rest_framework import serializers
from .models import Staff,Parnters,Items,Orders,Basket,Basketproducts,Category
from googleapiclient.discovery import build
from config import BOT_TOKEN,CHANEL_SUPPORT,API_KEY_GOOGLE
import telegram

SPREADSHEET_ID = "1z7CKVIOjz30amDeUlFkPZl-mSNW_gymkASNSv-Ot10E"
RANGE_NAME = "Лист1!B2:B"
service = build("sheets", "v4", developerKey=API_KEY_GOOGLE)

bot=telegram.Bot(BOT_TOKEN)

class Staffserizzers(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields=['photo','status','name','description']

class Partnerserizzers(serializers.ModelSerializer):
    class Meta:
        model=Parnters
        fields=['pictures']


class OrderSer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=['name','phone','email','message']

class BasketproductsSer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        queryset=Items.objects.all(),
        slug_field='name'
    )
    class Meta:
        model=Basketproducts
        fields=['items','count']

class BasketSer(serializers.ModelSerializer):
    products=BasketproductsSer(many=True)
    class Meta:
        model=Basket
        fields=['name','phone','products']

    def create(self, validated_data):
        products = validated_data.pop('products')
        basket = Basket.objects.create(**validated_data)
        Basketproducts.objects.bulk_create([
            Basketproducts(basket=basket, items=item['items'], count=item['count'])
            for item in products
        ])

        product_list = "\n".join([
            f"🔹 {item['items']} (Кол-во: {item['count']})" for item in products
        ])

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
                    phone = basket.phone.replace("+", "")
                    if phone in row[0]:
                        message += "\nЭто Резидент"


        except Exception as e:
            pass

        bot.send_message(CHANEL_SUPPORT, text=message)



        return basket


class ItemsSer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(many=True,
        queryset=Category.objects.all(),
        slug_field='name'
    )
    class Meta:
        model=Items
        fields=['name','pictures','categories']
