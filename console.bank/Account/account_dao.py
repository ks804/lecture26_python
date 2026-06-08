from Account.account import Account

class AccountDAO:
    def __init__(self):
        self.__accountDB = {}
    
    def insert_account(self, account):
        account_no = str(account.get_account_no())
        if account_no not in self.__accountDB:
            self.__accountDB[account_no] = account
            return True
        return False

    def select_account_by_account_no(self, account_no):
        account_no = str(account_no)
        if account_no in self.__accountDB:
            return self.__accountDB[account_no]
        return None

    def select_accounts_by_member_id(self, member_id):
        account_list = []
        for account in self.__accountDB.values():
            if account.get_owner() == member_id:
                account_list.append(account)
        if account_list:
            return account_list
        return None

    def select_all_accounts(self):
        account_list = list(self.__accountDB.values())
        if account_list:
            return account_list
        return None

    def update_account(self, account_no, account):
        account_no = str(account_no)
        if account_no in self.__accountDB:
            self.__accountDB[account_no] = account
            return True
        return False

    def delete_account(self, account_no):
        account_no = str(account_no)
        if account_no in self.__accountDB:
            self.__accountDB.pop(account_no)
            return True
        return False
