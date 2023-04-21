from django.test import TestCase
from restaurant.models import MenuItem
from serializers import MenuItemSerializer
from views import MenuItemsView
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.__str__(), "IceCream : 80")

class MenuViewTest(TestCase):
   def setUp(self):
       self.items = [MenuItem.objects.create(title="Chocolate Cake", price=7, inventory=100),
                MenuItem.objects.create(title="Cookies", price=3, inventory=200),
                MenuItem.objects.create(title="pancakes", price=8, inventory=100) ]
