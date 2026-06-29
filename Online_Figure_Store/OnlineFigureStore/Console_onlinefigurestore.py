from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Member.member_manager import MemberManager
from Figure.figure import Figure
from Figure.figure_dao import FigureDAO
from Figure.figure_service import FigureService
from Cart.cart_dao import CartDAO
from Cart.cart_item_dao import CartItemDAO
from Cart.cart_service import CartService
from Delivery.delivery_dao import DeliveryDAO
from Delivery.delivery_service import DeliveryService
from Order.order_dao import OrderDAO
from Order.order_item_dao import OrderItemDAO
from Order.order_service import OrderService


class ConsoleOnlineFigureStore:
    # ===== 시작 메뉴 =====
    start_menu = ['종료', '로그인', '회원가입', '피규어조회']

    # ===== 사용자(회원) 메뉴 =====
    member_menu = ['로그아웃', '피규어조회', '장바구니', '주문내역조회', '배송조회', '내정보']
    figure_menu = ['돌아가기', '피규어상세정보', '장바구니담기']
    cart_menu = ['돌아가기', '상품삭제', '주문하기']
    order_menu = ['돌아가기', '상세조회', '주문취소']
    order_detail_menu = ['돌아가기', '배송조회']
    my_info_menu = ['돌아가기', '내정보조회', '비밀번호수정', '회원탈퇴']

    # ===== 관리자 메뉴 =====
    admin_menu = ['로그아웃', '피규어관리', '회원관리', '주문목록조회', '배송관리']
    figure_manager_menu = ['돌아가기', '피규어목록', '피규어추가', '피규어수정', '피규어삭제']
    member_manager_menu = ['돌아가기', '회원목록', '회원정보조회', '회원삭제']
    delivery_manager_menu = ['돌아가기', '전체배송목록', '배송상태변경', '배송삭제']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.mmg = MemberManager(self.msv)
        self.fsv = FigureService(FigureDAO())
        self.csv = CartService(CartDAO(), CartItemDAO(), self.fsv)
        self.dsv = DeliveryService(DeliveryDAO())
        self.osv = OrderService(OrderDAO(), OrderItemDAO(), self.csv, self.dsv)
        self.sample_figures()

    def main(self):
        self.show_welcome()
        while True:
            if self.run_start_menu() == False:
                break
        self.say_goodbye()

    def sample_figures(self):
        # 상품명, 캐릭터, 가격, 재고
        self.fsv.add_figure('명조 플로로 1/7 스케일 피규어', '장리', 189000, 5)
        self.fsv.add_figure('명조 유노 1/7 스케일 피규어', '금석', 215000, 3)
        self.fsv.add_figure('명조 치사 1/7 스케일 피규어', '음림', 175000, 4)
        self.fsv.add_figure('명조 에이메스 1/8 스케일 피규어', '절지', 242000, 2)
        self.fsv.add_figure('명조 데니아 1/7 스케일 피규어', '베레니스', 198000, 6)

    def show_welcome(self):
        print("=========== 명조 미소녀 피규어 스토어 ===========")

    def say_goodbye(self):
        print('============ 이용해주셔서 감사합니다 ============')
        print()

    def select_menu(self, menu_list, menu_name='MENU'):
        print()
        print(f'====================== {menu_name} ======================')
        for i in range(1, len(menu_list)):
            print(f'{i}. {menu_list[i]} | ', end=' ')
        print(f'0. {menu_list[0]}')
        print('==================================================')
        print()
        try:
            menu = int(input('>>메뉴 선택 : '))
            print()
            if not (0 <= menu <= len(menu_list) - 1):
                raise Exception('ERROR : 잘못된 입력입니다')
            return menu
        except ValueError:
            print('ERROR : 숫자를 입력해주세요')
            return -1
        except Exception as e:
            print(e)
            return -1


# start_menu ==================================================================

    def run_start_menu(self):
        while True:
            menu = self.select_menu(ConsoleOnlineFigureStore.start_menu, '시작메뉴')
            if menu == 0:
                return False
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_join()
            elif menu == 3:
                self.run_figure_menu()

    def menu_login(self):
        id = input('아이디: ')
        password = input('비밀번호: ')
        print()
        if self.msv.login(id, password):
            if self.msv.current_user == MemberService.ADMIN_ID:
                print('[관리자 전용 페이지로 로그인했습니다]')
                self.run_admin_menu()
            else:
                print(f'[{self.msv.current_user}님 로그인되었습니다]')
                self.run_member_menu()
        else:
            print('ERROR : 아이디 또는 비밀번호가 잘못되었습니다')

    def menu_join(self):
        id = input('생성할 아이디: ')
        password = input('사용할 비밀번호: ')
        name = input('이름: ')
        phone = input('전화번호: ')
        email = input('이메일: ')
        print()
        member = Member(id, password, name, phone, email)
        if self.msv.join(member) == True:
            print(f'{name}님 회원가입 되었습니다')
        else:
            print('ERROR : 이미 가입된 회원입니다')


# member_menu ==================================================================

    def run_member_menu(self):
        while True:
            menu = self.select_menu(ConsoleOnlineFigureStore.member_menu, '회원메뉴')
            if menu == 0:
                self.msv.logout()
                print('로그아웃되었습니다')
                return
            elif menu == 1:
                self.run_figure_menu()
            elif menu == 2:
                self.run_cart_menu()
            elif menu == 3:
                self.run_order_menu()
            elif menu == 4:
                self.menu_view_my_deliveries()
            elif menu == 5:
                self.run_my_info_menu()


# figure_menu ==================================================================

    def run_figure_menu(self):
        self.menu_list_figures()
        while True:
            menu = self.select_menu(ConsoleOnlineFigureStore.figure_menu, '피규어메뉴')
            if menu == 0:
                return
            elif menu == 1:
                self.menu_figure_detail()
                self.menu_list_figures()
            elif menu == 2:
                self.menu_add_cart()

    def menu_list_figures(self):
        figures = self.fsv.get_all_figures()
        if figures:
            for figure in figures:
                print(figure.get_list_info())
        else:
            print('등록된 피규어가 없습니다')

    def menu_figure_detail(self):
        figureId = input('피규어번호: ')
        print()
        figure = self.fsv.get_figure_detail(figureId)
        if figure:
            print(figure)
        else:
            print('ERROR : 존재하지 않는 피규어입니다')

    def menu_add_cart(self):
        if not self.msv.current_user:
            print('ERROR : 로그인 후 이용해주세요')
            return
        figureId = input('장바구니에 담을 피규어번호: ')
        try:
            quantity = int(input('담을 수량: '))
        except ValueError:
            print()
            print('ERROR : 수량은 숫자로 입력해주세요')
            self.menu_list_figures()
            return
        print()
        result = self.csv.add_item(self.msv.current_user, figureId, quantity)
        if result == True:
            print('장바구니에 담겼습니다')
            self.menu_list_figures()
        elif result == 'STOCK_ERROR':
            print('ERROR : 재고보다 많은 수량은 담을 수 없습니다')
            self.menu_list_figures()
        elif result == 'QUANTITY_ERROR':
            print('ERROR : 수량은 1개 이상 입력해주세요')
            self.menu_list_figures()
        else:
            print('ERROR : 존재하지 않는 피규어입니다')
            self.menu_list_figures()


# cart_menu ==================================================================

    def run_cart_menu(self):
        while True:
            self.menu_view_cart()
            menu = self.select_menu(ConsoleOnlineFigureStore.cart_menu, '장바구니메뉴')
            if menu == 0:
                return
            elif menu == 1:
                self.menu_remove_cart_item()
            elif menu == 2:
                self.menu_order_cart()

    def menu_view_cart(self):
        cart = self.csv.view_cart(self.msv.current_user)
        if cart:
            print(cart)
        else:
            print('장바구니가 비어있습니다')

    def menu_remove_cart_item(self):
        figureId = input('삭제할 피규어번호: ')
        try:
            quantity = int(input('삭제할 수량: '))
        except ValueError:
            print()
            print('ERROR : 수량은 숫자로 입력해주세요')
            return
        print()
        result = self.csv.remove_item(self.msv.current_user, figureId, quantity)
        if result == True:
            print('선택한 상품이 장바구니에서 삭제되었습니다')
        elif result == 'QUANTITY_ERROR':
            print('ERROR : 장바구니에 담긴 수량보다 많이 삭제할 수 없습니다')
        else:
            print('ERROR : 장바구니에 없는 피규어번호입니다')

    def menu_order_cart(self):
        address = self.osv.get_member_address(self.msv.current_user)
        if address:
            print(f'기존 배송주소로 주문합니다: {address}')
        else:
            address = input('배송주소: ')
        print()
        result = self.osv.order_cart(self.msv.current_user, address)
        if result == True:
            print('주문되었습니다')
        elif result == 'STOCK_ERROR':
            print('ERROR : 재고가 부족하여 주문할 수 없습니다')
        else:
            print('ERROR : 장바구니가 비어있습니다')


# order_menu ==================================================================

    def run_order_menu(self):
        self.menu_list_my_orders()
        while True:
            menu = self.select_menu(ConsoleOnlineFigureStore.order_menu, '주문내역메뉴')
            if menu == 0:
                return
            elif menu == 1:
                self.menu_order_detail()
            elif menu == 2:
                self.menu_cancel_order()

    def menu_list_my_orders(self):
        orders = self.osv.get_member_orders(self.msv.current_user)
        if orders:
            for order in orders:
                print(order)
                delivery = self.dsv.view_delivery_by_order(order.get_orderId())
                if delivery:
                    print(f'배송상태 : {delivery.get_status()}')
                print()
        else:
            print('주문내역이 없습니다')

    def menu_order_detail(self):
        orderId = input('주문번호: ')
        print()
        order = self.osv.get_order_detail(orderId)
        if order:
            print(order)
            self.run_order_detail_menu(orderId)
        else:
            print('ERROR : 존재하지 않는 주문입니다')

    def run_order_detail_menu(self, orderId):
        while True:
            menu = self.select_menu(ConsoleOnlineFigureStore.order_detail_menu, '주문상세메뉴')
            if menu == 0:
                return
            elif menu == 1:
                self.menu_view_delivery(orderId)

    def menu_view_delivery(self, orderId):
        deliveries = self.dsv.view_member_deliveries(self.msv.current_user)
        if deliveries:
            for delivery in deliveries:
                if delivery.get_orderId() == orderId:
                    print(delivery)
                    return
        print('배송정보가 없습니다')

    def menu_cancel_order(self):
        orderId = input('취소할 주문번호: ')
        print()
        if self.osv.cancel_order(orderId) == True:
            print('주문이 취소되었습니다')
        else:
            print('ERROR : 취소할 수 없는 주문입니다 (존재하지 않거나 이미 배송이 시작됨)')


# delivery (member) ==================================================================

    def menu_view_my_deliveries(self):
        deliveries = self.dsv.view_member_deliveries(self.msv.current_user)
        if deliveries:
            for delivery in deliveries:
                print(delivery)
        else:
            print('배송정보가 없습니다')


# my_info_menu ==================================================================

    def run_my_info_menu(self):
        while True:
            menu = self.select_menu(ConsoleOnlineFigureStore.my_info_menu, '내정보메뉴')
            if menu == 0:
                print('회원메뉴로 돌아갑니다')
                return
            elif menu == 1:
                self.menu_view_myinfo()
            elif menu == 2:
                self.menu_update_password()
            elif menu == 3:
                self.menu_delete_membership()
                return

    def menu_view_myinfo(self):
        myinfo = self.msv.view_member_info(self.msv.current_user)
        print(myinfo)

    def menu_update_password(self):
        print('[현재 회원 정보]')
        print(self.msv.view_member_info(self.msv.current_user))
        id = input('아이디: ')
        org_password = input('현재 비밀번호: ')
        new_password = input('새 비밀번호: ')
        print()
        if self.msv.update_member_password(id, org_password, new_password) == True:
            print('비밀번호가 바뀌었습니다')
        else:
            print('ERROR : 아이디나 비밀번호가 일치하지 않습니다')

    def menu_delete_membership(self):
        id = input('아이디: ')
        print()
        if id != self.msv.current_user:
            print('ERROR : 로그인된 아이디와 일치하지 않습니다')
            return
        if self.msv.remove_member(id) == True:
            self.msv.logout()
            print('계정이 삭제되었습니다')
        else:
            print('ERROR : 아이디가 일치하지 않습니다')


# admin_menu ==================================================================

    def run_admin_menu(self):
        while True:
            menu = self.select_menu(ConsoleOnlineFigureStore.admin_menu, '관리자메뉴')
            if menu == 0:
                self.msv.logout()
                print('로그아웃되었습니다')
                return
            elif menu == 1:
                self.run_figure_manager_menu()
            elif menu == 2:
                self.run_member_manager_menu()
            elif menu == 3:
                self.menu_list_all_orders()
            elif menu == 4:
                self.run_delivery_manager_menu()


# figure_manager_menu ==================================================================

    def run_figure_manager_menu(self):
        while True:
            menu = self.select_menu(ConsoleOnlineFigureStore.figure_manager_menu, '피규어관리메뉴')
            if menu == 0:
                return
            elif menu == 1:
                self.menu_list_figures()
            elif menu == 2:
                self.menu_add_figure()
            elif menu == 3:
                self.menu_edit_figure()
            elif menu == 4:
                self.menu_delete_figure()

    def menu_add_figure(self):
        name = input('상품명: ')
        character = input('캐릭터: ')
        try:
            price = int(input('가격: '))
            stock = int(input('재고: '))
        except ValueError:
            print('ERROR : 가격과 재고는 숫자로 입력해주세요')
            return
        print()
        if self.fsv.add_figure(name, character, price, stock) == True:
            print('피규어가 추가되었습니다')
        else:
            print('ERROR : 피규어 추가에 실패했습니다')

    def menu_edit_figure(self):
        figureId = input('수정할 피규어번호: ')
        name = input('상품명: ')
        character = input('캐릭터: ')
        try:
            price = int(input('가격: '))
            stock = int(input('재고: '))
        except ValueError:
            print('ERROR : 가격과 재고는 숫자로 입력해주세요')
            return
        print()
        figure = Figure(figureId, name, character, price, stock)
        if self.fsv.edit_figure(figureId, figure) == True:
            print('피규어가 수정되었습니다')
        else:
            print('ERROR : 존재하지 않는 피규어입니다')

    def menu_delete_figure(self):
        figureId = input('삭제할 피규어번호: ')
        print()
        if self.fsv.remove_figure(figureId) == True:
            print('피규어가 삭제되었습니다')
        else:
            print('ERROR : 존재하지 않는 피규어입니다')


# member_manager_menu ==================================================================

    def run_member_manager_menu(self):
        while True:
            menu = self.select_menu(ConsoleOnlineFigureStore.member_manager_menu, '회원관리메뉴')
            if menu == 0:
                return
            elif menu == 1:
                self.menu_list_members()
            elif menu == 2:
                self.menu_view_member_info()
            elif menu == 3:
                self.menu_delete_member()

    def menu_list_members(self):
        members = self.mmg.list_members()
        if members:
            for member in members:
                print(member.get_list_info())
        else:
            print('가입된 회원이 없습니다')

    def menu_view_member_info(self):
        id = input('확인할 회원 아이디: ')
        print()
        member = self.mmg.view_member_info(id)
        if member:
            print(member)
        else:
            print('ERROR : 존재하지 않는 회원입니다')

    def menu_delete_member(self):
        id = input('삭제할 회원 아이디: ')
        print()
        if self.mmg.remove_member(id) == True:
            print('회원이 삭제되었습니다')
        else:
            print('ERROR : 존재하지 않는 회원이거나 관리자입니다')


# list_all_orders ==================================================================

    def menu_list_all_orders(self):
        orders = self.osv.get_all_orders()
        if orders:
            for order in orders:
                print(order)
                delivery = self.dsv.view_delivery_by_order(order.get_orderId())
                if delivery:
                    print(f'배송번호 : {delivery.get_deliveryId()}')
                    print(f'배송상태 : {delivery.get_status()}')
                print()
        else:
            print('주문내역이 없습니다')


# delivery_manager_menu (admin) ==================================================================

    def run_delivery_manager_menu(self):
        while True:
            menu = self.select_menu(ConsoleOnlineFigureStore.delivery_manager_menu, '배송관리메뉴')
            if menu == 0:
                return
            elif menu == 1:
                self.menu_list_all_deliveries()
            elif menu == 2:
                self.menu_change_delivery_status()
            elif menu == 3:
                self.menu_delete_delivery()

    def menu_list_all_deliveries(self):
        deliveries = self.dsv.view_all_deliveries()
        if deliveries:
            for delivery in deliveries:
                print(delivery)
        else:
            print('등록된 배송정보가 없습니다')

    def menu_change_delivery_status(self):
        deliveryId = input('배송번호: ')
        status = input('변경할 배송상태(예: 배송준비중/배송중/배송완료): ')
        print()
        if self.dsv.change_status(deliveryId, status) == True:
            print('배송상태가 변경되었습니다')
        else:
            print('ERROR : 존재하지 않는 배송입니다')

    def menu_delete_delivery(self):
        deliveryId = input('삭제할 배송번호: ')
        print()
        if self.dsv.delete_delivery(deliveryId) == True:
            print('배송정보가 삭제되었습니다')
        else:
            print('ERROR : 존재하지 않는 배송입니다')


if __name__ == '__main__':
    app = ConsoleOnlineFigureStore()
    app.main()
