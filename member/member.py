class Member:
    def __init__(self, id, pw, name):
        self.__id = id
        self.__pw = pw
        self.__name = name

    def get_id(self):
        return self.__id
    def get_pw(self):
        return self.__pw
    def get_name(self):
        return self.__name
    def set_pw(self, pw):
        self.__pw = pw

    def __str__(self):
        return f'{self.__id}\t{self.__name}\t{self.__pw}'

class MemberService:
    def __init__(self, memberDao):
        self.__dao = memberDao

    def join(self, member):
        if self.__dao.is_exist(member.get_id()):
            return False
        self.__dao.insert_member(member)
        return True
    
    def login(self, id, pw):
        member = self.__dao.get_member_info(id)
        if member:
            if pw == member.get_pw():
                return id
        return None
    
    def logout(self):
        return '로그아웃 하셨습니다.'
    
    def list_members(self):
        member_list = self.__dao.get_all_members()
        if member_list:
            return member_list
        return False
    
    def list_member_info(self, id):
        member_info = self.__dao.get_member_info(id)
        return member_info
    
    def remove_member(self, id):
        return self.__dao.remove_member(id)
    
    def update_member_info(self, id, member):
        member_info = self.__dao.update_member_info(id, member)
        return member_info


class MemberDAO:
    def __init__(self):
        self.__memberDB = {}

    def insert_member(self, member):
        self.__memberDB[member.get_id()] = member

    def is_exist(self, id):
        if id in self.__memberDB.keys():
            return True
        return False

    def get_all_members(self):
        if self.__memberDB:
            return list(self.__memberDB.values())
        
    def get_member_info(self, id):
        if self.is_exist(id):
            return self.__memberDB[id]
        else:
            return None
    
    def remove_member(self, id):
        if self.is_exist(id):
            del self.__memberDB[id]
            return True
        else:
            return False
        
    def update_member_info(self, id, member):
        if self.is_exist(id):
            self.__memberDB[id] = member
            return True
        return False