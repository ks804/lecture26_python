from member import Member, MemberDAO, MemberService

class MemberManager:
    start_menu = ['종료','로그인','회원가입']
    admin_menu = ['로그아웃', '회원목록','회원정보조회','회원탈퇴']
    member_menu = ['로그아웃','내정보조회','내정보수정','회원탈퇴']
    ADMIN_ID = 'admin'
    ADMIN_pw = '1234'
    
    def __init__(self):
        self.current_user = None
        self.ms = MemberService(MemberDAO())
    
    def main(self):
        self.show_welcome()
        self.ms.join(Member(MemberManager.ADMIN_ID,MemberManager.ADMIN_pw,MemberManager.ADMIN_ID))
        while True:
            menu = self.select_menu(MemberManager.start_menu)
            if menu == 0: break
            elif menu == 1:
                id = input('>> id : ')
                pw = input('>> pw : ')
                self.current_user = self.ms.login(id, pw)
                if self.current_user:
                    if self.current_user == MemberManager.ADMIN_ID:
                        self.start_admin_menu()
                    else:
                        self.current_user = id
                        self.start_member_menu()
                else:
                    print('로그인에 실패하였습니다.')

            elif menu == 2:
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
        title = '관리자메뉴'
        print(self.print_title(title))
        while True:
            menu = self.select_menu(self.admin_menu)
            if menu == 0:
                print(self.ms.logout())
                break
            elif menu == 1:
                self.list_all_member()
            elif menu == 2: 
                id = input('>> id : ')
                member_info = self.ms.list_member_info(id)
                if member_info:
                    print(f'{member_info.get_id()}\t{member_info.get_name()}')
                else:
                    print('없는 회원입니다.')
            elif menu == 3:
                id = input('>> id : ')
                if self.ms.remove_member(id):
                    print('회원강퇴가 완료되었습니다.')
                else:
                    print('없는 회원입니다.')
            else:
                print('없는 메뉴입니다.')

    def start_member_menu(self):
        title = '회원메뉴'
        print(self.print_title(title))
        while True:
            menu = self.select_menu(self.member_menu)
            if menu == 0:
                print(self.ms.logout())
                break
            elif menu == 1:
                member_info = self.ms.list_member_info(self.current_user)
                if member_info:
                    print(member_info)
                else:
                    print('없는 회원입니다.')
            elif menu == 2:
                member_info = self.ms.list_member_info(self.current_user)
                if member_info:
                    pw = input('>> pw : ')
                    member_info.set_pw(pw)
                    if self.ms.update_member_info(self.current_user,member_info):
                        print('회원수정이 완료되었습니다.')
                    else:
                        print('회원수정에 실패하였습니다.')
            elif menu == 3:
                self.ms.remove_member(self.current_user)
                self.current_user = None
                print('회원탈퇴가 완료되었습니다.')
                break
            else:
                print('없는 메뉴입니다.')


    def list_all_member(self):
            print(self.current_user)
            if self.current_user != MemberManager.ADMIN_ID:
                print('사용권한이 없습니다.')
                return
            
            member_list = self.ms.list_members()
            if len(member_list) <= 1:
                print('가입한 회원이 없습니다.')
            else:
                for member in member_list[1:]:
                    print(member) 

    def show_welcome(self):
        title = 'Member Manager'
        print(self.show_title(title))

    def print_title(self, title):
        return f"{'=' * 50}\n{title:^50}\n{'='*50}"

    def say_goodbye(self):
        print('안녕히 가세요.')

    def print_menu(self, menu_list):
        print('-' * 50)
        for i in range(1, len(menu_list)):
            print(f'{i}. {menu_list[i]}')
        print(f'0. {menu_list[0]}')
        print('-' * 50)

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
