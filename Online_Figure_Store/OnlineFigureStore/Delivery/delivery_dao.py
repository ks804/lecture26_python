from .delivery import Delivery

class DeliveryDAO:
    def __init__(self):
        self.__deliveryDB = {}

    def insert_delivery(self, delivery):
        deliveryId = delivery.get_deliveryId()
        if deliveryId not in self.__deliveryDB:
            self.__deliveryDB[deliveryId] = delivery
            return True
        return False

    def select_delivery_by_id(self, deliveryId):
        return self.__deliveryDB.get(deliveryId)

    def select_delivery_by_order(self, orderId):
        for delivery in self.__deliveryDB.values():
            if delivery.get_orderId() == orderId:
                return delivery
        return None

    def select_delivery_by_member(self, memberId):
        result = []
        for delivery in self.__deliveryDB.values():
            if delivery.get_memberId() == memberId:
                result.append(delivery)
        return result

    def select_all_deliveries(self):
        delivery_list = list(self.__deliveryDB.values())
        if len(delivery_list):
            return delivery_list
        else:
            return None

    def update_delivery(self, deliveryId, delivery):
        if deliveryId in self.__deliveryDB:
            self.__deliveryDB[deliveryId] = delivery
            return True
        return False

    def delete_delivery(self, deliveryId):
        if deliveryId in self.__deliveryDB:
            self.__deliveryDB.pop(deliveryId)
            return True
        return False
