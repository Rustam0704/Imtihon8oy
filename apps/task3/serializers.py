from rest_framework import serializers
from .models import Product
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # AES encryption
        data = str(representation).encode()
        key = get_random_bytes(16)  # 16 bytes key
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return {"ciphertext": ciphertext, "tag": tag, "nonce": cipher.nonce, "key": key}
