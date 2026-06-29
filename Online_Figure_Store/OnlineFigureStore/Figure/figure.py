class Figure:
    def __init__(self, figureId, name, character, price, stock):
        self.__figureId = figureId
        self.__name = name
        self.__character = character
        self.__price = price
        self.__stock = stock

    def get_figureId(self):
        return self.__figureId
    def get_name(self):
        return self.__name
    def get_character(self):
        return self.__character
    def get_price(self):
        return self.__price
    def get_stock(self):
        return self.__stock

    def set_figureId(self, figureId):
        self.__figureId = figureId
    def set_stock(self, stock):
        self.__stock = stock

    def get_list_info(self):
        return f'피규어번호: {self.__figureId} 상품명 : {self.__name} 캐릭터 : {self.__character}'

    def __str__(self):
        return f'피규어번호 : {self.__figureId} 상품명 : {self.__name} 캐릭터 : {self.__character} 가격 : {self.__price} 재고 : {self.__stock}'
