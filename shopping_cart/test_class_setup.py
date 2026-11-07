from cart import ShoppingCart


class TestShoppingCart:
    def setup_method(self):
        self.cart = ShoppingCart()
        print('SETUP: new cart') 
        
    def test_empty_cart(self):
        assert len(self.cart.items) == 0
        assert self.cart.get_total() == 0
        
    def test_add_item(self):
        self.cart.add_item('mouse', 500, 2)
        assert self.cart.get_item_count() == 2
        assert self.cart.get_total() == 1000
        
    def teardown_method(self):
        self.cart.clear()
        print('TEARDOWN: cart cleared')

