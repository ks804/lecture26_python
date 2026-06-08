from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService

class MemberManager:
    start_menu = ['종료', '로그인', '회원가입']
    admin_menu = ['로그아웃', '회원목록', '회원정보조회', '회원강퇴']
    member_menu = ['로그아웃', '내정보조회', '내정보수정', '회원탈퇴']
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '1234'

    def __init__(self):
        self.current_user = None
        self.ms = MemberService(MemberDAO())

    def main(self):
        self.show_welcome()
        while True:
            menu = self.select_menu(MemberManager.start_menu)
            if menu == 0:
                break
            elif menu == 1:  # 로그인
                id = input('>> id : ')
                pw = input('>> pw : ')
                if self.ms.login(id, pw):
                    self.current_user = id
                    if self.current_user == MemberManager.ADMIN_ID:
                        self.start_admin_menu()
                    else:
                        self.start_member_menu()
                else:
                    print('로그인에 실패하였습니다.')
            elif menu == 2:  # 회원가입
                id = input('>> id : ')
                pw = input('>> pw : ')
                name = input('>> name : ')
                member = Member(id, pw, name)
                if self.ms.join(member):
                    print('회원가입이 완료되었습니다.')
                else:
                    print('회원가입에 실패하였습니다.')
            else:
                print('없는 메뉴입니다.')
        self.say_goodbye()

    def start_admin_menu(self):
        print('---------- 관리자 메뉴 ----------')
        while True:
            menu = self.select_menu(MemberManager.admin_menu)
            if menu == 0:  # 로그아웃
                self.ms.logout()
                self.current_user = None
                break
            elif menu == 1:  # 회원목록
                self.list_all_member()
            elif menu == 2:  # 회원정보조회
                id = input('>> 조회할 id : ')
                info = self.ms.view_member_info(id)
                print(info if info else '존재하지 않는 회원입니다.')
            elif menu == 3:  # 회원강퇴
                id = input('>> 강퇴할 id : ')
                if self.ms.remove_member(id):
                    print('회원이 강퇴되었습니다.')
                else:
                    print('존재하지 않는 회원입니다.')
            else:
                print('없는 메뉴입니다.')

    def list_all_member(self):
        if self.current_user != MemberManager.ADMIN_ID:
            print('사용 권한이 없습니다.')
            return
        member_list = self.ms.list_members()
        if not member_list or len(member_list) <= 1:
            print('가입한 회원이 없습니다.')
        else:
            for member in member_list[1:]:
                print(member)

    def start_member_menu(self):
        print('---------- 회원 메뉴 ----------')
        while True:
            menu = self.select_menu(MemberManager.member_menu)
            if menu == 0:  # 로그아웃
                self.menu_logout()
                return
            elif menu == 1:
                self.menu_view_my_info()
            elif menu == 2:
                self.menu_update_my_info()
            elif menu == 3:
                self.menu_remove_member()
            else:
                print('없는 메뉴입니다')

    def menu_view_my_info(self):
        info = self.ms.view_member_info(self.current_user)
        print(info)

    def menu_update_my_info(self):
        org_pw = input('>> 현재 비밀번호 : ')
        new_pw = input('>> 새 비밀번호 : ')
        if self.ms.update_member_pw(self.current_user, org_pw, new_pw):
            print('비밀번호가 변경되었습니다.')
        else:
            print('비밀번호 변경에 실패하였습니다.')
    def menu_remove_member(self):
        pw = input('>> 비밀번호 확인 : ')
        member = self.ms.view_member_info(self.current_user)
        if member and member.get_pw() == pw:
            if self.ms.remove_member(self.current_user):
                self.menu_logout()
                print('회원탈퇴가 완료되었습니다.')
                return
        print('비밀번호가 일치하지 않습니다.')

    def menu_logout(self):
        self.ms.logout()
        self.current_user = None
        print('로그아웃되었습니다.')

    def show_welcome(self):
        print('=' * 50)
        title = 'Member Manager'
        print(f'{title:^50}')
        print('=' * 50)

    def say_goodbye(self):
        print('안녕히 가세요')

    def print_menu(self, menu_list):
        print('-' * 40)
        for i in range(1, len(menu_list)):
            print(f'{i}. {menu_list[i]}')
        print(f'0. {menu_list[0]}')
        print('-' * 40)

    def select_menu(self, menu_list):
        self.print_menu(menu_list)
        try:
            menu = int(input('메뉴 선택 : '))
            return menu
        except ValueError:
            return -1


if __name__ == '__main__':
    app = MemberManager()
    app.main()
