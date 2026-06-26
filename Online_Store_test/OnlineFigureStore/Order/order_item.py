class OrderItem:
    def __init__(self, orderItemId, orderId, figure, quantity, price):
        self.__orderItemId = orderItemId
        self.__orderId = orderId
        self.__figure = figure
        self.__quantity = quantity
        self.__price = price

    def get_orderItemId(self):
        return self.__orderItemId

    def get_orderId(self):
        return self.__orderId

    def get_figure(self):
        return self.__figure

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def set_orderItemId(self, orderItemId):
        self.__orderItemId = orderItemId

    def set_orderId(self, orderId):
        self.__orderId = orderId

    def set_figure(self, figure):
        self.__figure = figure

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_price(self, price):
        self.__price = price

    def get_subtotal(self):
        return self.__price * self.__quantity

    def __str__(self):
        return (f'주문상품번호 : {self.__orderItemId} | 피규어번호 : {self.__figure.get_figureId()} | '
                f'상품명 : {self.__figure.get_name()} | 가격 : {self.__price}원 | '
                f'수량 : {self.__quantity} | 소계 : {self.get_subtotal()}원')
