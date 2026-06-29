class CartItem:
    def __init__(self, cartItemId, cartId, figure, quantity):
        self.__cartItemId = cartItemId
        self.__cartId = cartId
        self.__figure = figure
        self.__quantity = quantity

    def get_cartItemId(self):
        return self.__cartItemId

    def get_cartId(self):
        return self.__cartId

    def get_figure(self):
        return self.__figure

    def get_quantity(self):
        return self.__quantity

    def set_cartItemId(self, cartItemId):
        self.__cartItemId = cartItemId

    def set_cartId(self, cartId):
        self.__cartId = cartId

    def set_figure(self, figure):
        self.__figure = figure

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def add_quantity(self, quantity=1):
        self.__quantity += quantity

    def get_subtotal(self):
        return self.__figure.get_price() * self.__quantity

    def __str__(self):
        return (f'장바구니상품번호 : {self.__cartItemId} | 피규어번호 : {self.__figure.get_figureId()} | '
                f'상품명 : {self.__figure.get_name()} | 캐릭터 : {self.__figure.get_character()} | '
                f'가격 : {self.__figure.get_price()}원 | 수량 : {self.__quantity} | '
                f'소계 : {self.get_subtotal()}원')
