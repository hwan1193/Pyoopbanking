import streamlit as st

# 객체지향 프로그래밍을 활용한 은행 시스템 클래스들
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} 원 입금 완료. 현재 잔액: {self.balance} 원"
        else:
            return "양수 금액만 입금 가능합니다."
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{amount} 원 출금 완료. 현재 잔액: {self.balance} 원"
        else:
            return "잔액이 부족합니다."

    def get_balance(self):
        return self.balance

class BankSystem:
    def __init__(self):
        self.accounts = {}  # 계좌 번호 -> BankAccount 객체
    
    def create_account(self, account_id, account_holder, initial_balance=0):
        if account_id in self.accounts:
            return "해당 계좌는 이미 존재합니다."
        self.accounts[account_id] = BankAccount(account_holder, initial_balance)
        return "계좌 생성 완료!"
    
    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            return self.accounts[account_id].deposit(amount)
        return "계좌를 찾을 수 없습니다."
    
    def withdraw(self, account_id, amount):
        if account_id in self.accounts:
            return self.accounts[account_id].withdraw(amount)
        return "계좌를 찾을 수 없습니다."
    
    def check_balance(self, account_id):
        if account_id in self.accounts:
            return f"계좌 {account_id}의 잔액은 {self.accounts[account_id].get_balance()} 원입니다."
        return "계좌를 찾을 수 없습니다."

# Streamlit 세션 상태에 은행 시스템 인스턴스 저장
if 'bank' not in st.session_state:
    st.session_state.bank = BankSystem()

# 제목 및 사이드바 메뉴
st.title("나만의 은행 시스템")
menu = st.sidebar.selectbox("메뉴 선택", ["계좌 생성", "입금", "출금", "잔액 조회"])

# 각 메뉴별 기능 구현
if menu == "계좌 생성":
    st.header("계좌 생성")
    account_id = st.text_input("계좌번호", key="create_acc")
    account_holder = st.text_input("이름", key="create_name")
    initial_balance = st.number_input("초기 입금액", min_value=0.0, value=0.0, key="create_init")
    if st.button("계좌 생성"):
        message = st.session_state.bank.create_account(account_id, account_holder, initial_balance)
        st.success(message)

elif menu == "입금":
    st.header("입금")
    account_id = st.text_input("계좌번호", key="deposit_acc")
    amount = st.number_input("입금액", min_value=0.0, value=0.0, key="deposit_amt")
    if st.button("입금"):
        message = st.session_state.bank.deposit(account_id, amount)
        st.success(message)

elif menu == "출금":
    st.header("출금")
    account_id = st.text_input("계좌번호", key="withdraw_acc")
    amount = st.number_input("출금액", min_value=0.0, value=0.0, key="withdraw_amt")
    if st.button("출금"):
        message = st.session_state.bank.withdraw(account_id, amount)
        st.success(message)

elif menu == "잔액 조회":
    st.header("잔액 조회")
    account_id = st.text_input("계좌번호", key="balance_acc")
    if st.button("조회"):
        message = st.session_state.bank.check_balance(account_id)
        st.info(message)