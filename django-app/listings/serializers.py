from rest_framework import serializers
from .models import Listing
from .models import Image
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

UserModel = get_user_model()

class ListingListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = ['id','product_name', 'category', 'logo_image', 'absolute_url']

    def get_absolute_url(self, obj):
        return reverse('listings_detail', args=(obj.pk,))

class ImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ['id','image', 'image_title', 'uploded_at']
        model = Image

class ListingDetailSerializer(serializers.ModelSerializer):
    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()
    listing_images = ImageSerializer(many=True,required=False)

    class Meta:
        model = Listing
        fields = ['id', 'product_name', 'category', 'logo_image', 'details', 'created_at', 'vegetarian', 'vegan', 'update', 'delete', 'listing_images']

    def get_update(self, obj):
        return reverse('listings_update', args=(obj.pk,))

    def get_delete(self, obj):
        return reverse('listings_delete', args=(obj.pk,))

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        new_token = Token.objects.create(user=user)
        return user

    class Meta:
        model = get_user_model()
        fields = [ "username", "password"]
