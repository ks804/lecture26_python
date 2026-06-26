from .delivery import Delivery

class DeliveryService:
    deliveryId_seq = 111111

    def __init__(self, delivery_dao):
        self.__dao = delivery_dao

    def create_delivery(self, orderId, memberId, address):
        deliveryId = 'D' + str(DeliveryService.deliveryId_seq)
        DeliveryService.deliveryId_seq += 1

        delivery = Delivery(deliveryId, orderId, memberId, address, '배송준비중')
        return self.__dao.insert_delivery(delivery)

    def view_delivery(self, deliveryId):
        return self.__dao.select_delivery_by_id(deliveryId)

    def view_member_deliveries(self, memberId):
        return self.__dao.select_delivery_by_member(memberId)

    def view_all_deliveries(self):
        return self.__dao.select_all_deliveries()

    def view_delivery_by_order(self, orderId):
        return self.__dao.select_delivery_by_order(orderId)

    def change_status(self, deliveryId, status):
        delivery = self.__dao.select_delivery_by_id(deliveryId)
        if delivery:
            delivery.set_status(status)
            return self.__dao.update_delivery(deliveryId, delivery)
        return False

    def delete_delivery(self, deliveryId):
        return self.__dao.delete_delivery(deliveryId)
