from cart import ShoppingCart
def test_prepared_cart(prepared_cart_with_cleanup):
    assert prepared_cart_with_cleanup.get_total() == 4000
    assert prepared_cart_with_cleanup.get_item_count() == 2
    prepared_cart_with_cleanup.add_item('mouse', 500)
    assert prepared_cart_with_cleanup.get_total() == 4500
    
    
class TestCartLifecycle:
    def setup_method(self):
        self.cart = ShoppingCart()
        print('Начало тестового прогона')
        
    def test_add_products(self):
        self.cart.add_item('mouse', 500, 2)
        assert self.cart.get_total() == 1000
        self.cart.add_item('keyboard', 1000)
        assert self.cart.get_total() == 2000
        assert self.cart.get_item_count() == 3
    
    def test_remove_product(self):
        self.cart.add_item('monitor', 3000)
        self.cart.remove_item('monitor')
        assert len(self.cart.items) == 0
        
    def teardown_method(self):
        self.cart.clear()
        print('Тесты завершены')
    