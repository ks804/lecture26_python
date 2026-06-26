from .cart import Cart

class CartDAO:
    def __init__(self):
        self.__cartDB = {}  # 회원아이디 : Cart 객체

    def insert_cart(self, memberId, cart):
        if not self.select_cart_by_member(memberId):
            self.__cartDB[memberId] = cart
            return True
        else:
            return False

    def select_cart_by_member(self, memberId):
        if memberId in self.__cartDB:
            return self.__cartDB[memberId]
        else:
            return None

    def update_cart(self, memberId, cart):
        if memberId in self.__cartDB:
            self.__cartDB[memberId] = cart
            return True
        else:
            return False

    def delete_cart(self, memberId):
        if memberId in self.__cartDB:
            self.__cartDB.pop(memberId)
            return True
        else:
            return False
