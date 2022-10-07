from rest_framework import serializers
from .models import (
    Category,
    Brand,
    Product,
    Transaction,
    Firm
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=(
            "id",
            "name"
        )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
       model=Brand
       fields=(
            "id",
            "name"
        )

class ProductSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    category_id=serializers.IntegerField(write_only=True)
    brand=serializers.StringRelatedField()
    brand_id=serializers.IntegerField(write_only=True)

    class Meta:
        model=Product
        fields=(
            "id",
            "name",
            "category",
            "category_id",
            "brand",
            "brand_id",
            "stock_quantity"
        )
        read_only_fields = ('stock_quantity',)


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            'id',
            'name',
            'phone_number',
            'address'
        )



class TransactionSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    firm=serializers.StringRelatedField()
    firm_id=serializers.IntegerField()  # get,post
    product=serializers.StringRelatedField()
    product_id=serializers.IntegerField()

    class Meta:
        model=Transaction
        fields=(
            "id",
            "user",
            "firm",
            "firm_id",
            "product",
            "product_id",
            "price_total",
            "quantity",
            "price",
            "transaction"
        )
        read_only_fields = ('price_total',)

    def validate(self,data):
            if data.get("transaction") ==0:
                product=Product.objects.get(id=data.get( "product_id"))
                if data.get("quantity") > product.stock_quantity:
                    raise serializers.ValidationError(
                        f"Dont have enough stock.Current stock is {product.stock_quantity}"
                    )
            return data