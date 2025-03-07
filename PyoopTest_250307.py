class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} 원 입금 완료. 현재 잔액: {self.balance} 원")
        else:
            print("양수 금액만 입금 가능합니다.")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} 원 출금 완료. 현재 잔액: {self.balance} 원")
        else:
            print("잔액이 부족합니다.")

    def get_balance(self):
        return self.balance

class BankSystem:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_id, account_holder, initial_balance=0):
        if account_id in self.accounts:
            print("해당 계좌는 이미 존재합니다.")
        else:
            self.accounts[account_id] = BankAccount(account_holder, initial_balance)
            print("계좌 생성 완료!")
    
    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)
        else:
            print("계좌를 찾을 수 없습니다.")
    
    def withdraw(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].withdraw(amount)
        else:
            print("계좌를 찾을 수 없습니다.")
    
    def check_balance(self, account_id):
        if account_id in self.accounts:
            balance = self.accounts[account_id].get_balance()
            print(f"계좌 {account_id}의 잔액은 {balance} 원입니다.")
            return balance
        else:
            print("계좌를 찾을 수 없습니다.")
            return None

def main():
    bank = BankSystem()
    
    while True:
        print("\n=== 은행 시스템 ===")
        print("1. 계좌 생성")
        print("2. 입금")
        print("3. 출금")
        print("4. 잔액 조회")
        print("5. 종료")
        choice = input("선택: ")
        
        if choice == "1":
            account_id = input("계좌번호: ")
            name = input("이름: ")
            try:
                initial = float(input("초기 입금액: "))
            except ValueError:
                print("숫자만 입력해 주세요.")
                continue
            bank.create_account(account_id, name, initial)
        
        elif choice == "2":
            account_id = input("계좌번호: ")
            try:
                amount = float(input("입금액: "))
            except ValueError:
                print("숫자만 입력해 주세요.")
                continue
            bank.deposit(account_id, amount)
        
        elif choice == "3":
            account_id = input("계좌번호: ")
            try:
                amount = float(input("출금액: "))
            except ValueError:
                print("숫자만 입력해 주세요.")
                continue
            bank.withdraw(account_id, amount)
        
        elif choice == "4":
            account_id = input("계좌번호: ")
            bank.check_balance(account_id)
        
        elif choice == "5":
            print("시스템을 종료합니다.")
            break
        
        else:
            print("올바른 선택이 아닙니다.")

if __name__ == "__main__":
    main()