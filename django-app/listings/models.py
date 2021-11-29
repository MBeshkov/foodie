from django.db import models
from django.conf import settings

# Create your models here.
class Listing(models.Model):
    beverage = 'bvg'
    cereal = 'crl'
    dairy = 'dry'
    egg_product = 'egg'
    fat_oil = 'oil'
    fruit = 'frt'
    veggie = 'vgs'
    legume = 'lgm'
    nut_seed = 'nts'
    meat = 'met'
    seafood = 'sea'
    sauce_soup = 'sup'
    snack = 'snk'
    dessert = 'dst'
    miscellaneous = 'mis'
    tag_choices = [
        (beverage, 'Beverages'),
        (cereal, 'Cereal'),
        (dairy, 'Dairy products'),
        (egg_product, 'Egg products'),
        (fat_oil, 'Fats and oils'),
        (fruit, 'Fruits'),
        (veggie, 'Vegetables'),
        (legume, 'Legumes'),
        (nut_seed, 'Nuts and seeds'),
        (meat, 'Meat'),
        (seafood, 'Seafood'),
        (sauce_soup, 'Sauces and soups'),
        (snack, 'Snacks'),
        (dessert, 'Desserts'),
        (miscellaneous, 'Miscellaneous'),
    ]
    product_name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=3, choices=tag_choices, default=miscellaneous)
    logo_image = models.ImageField(upload_to='listingImages', blank=True, default="listingImages/default.jpg")
    details = models.TextField(null=True, verbose_name="Tell us more about the product")
    created_at = models.DateTimeField(auto_now_add=True)
    vegetarian = models.BooleanField(null=True)
    vegan = models.BooleanField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings', null=True)

    def __str__(self):

        return "{}. {}".format(self.product_name, self.category)

    def get_test(self):
        return self.product_name + ' which is a ' + self.category

class Image(models.Model):
	listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_images',blank=True, null=True)
	image = models.ImageField(upload_to='listingImages',blank=True)
	image_title = models.CharField(max_length=120, blank=True)
	uploded_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-uploded_at']