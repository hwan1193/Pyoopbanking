# 간단한 설명

>BankAccount 클래스: 
>한 계좌의 소유자, 잔액 및 입금/출금 기능을 구현합니다.

>BankSystem 클래스: 
>여러 계좌를 관리하며, 계좌 생성, 입금, 출금, 잔액 조회 기능을 제공합니다.

>main 함수: 
>사용자와 상호작용하는 CLI 인터페이스로, 메뉴를 통해 기능을 선택할 수 있습니다.

>Streamlit 기능을 사용하여 배포 해보았습니다.

![Pyoopbanking_250307](https://github.com/user-attachments/assets/7631444b-6f7a-4600-87f1-8da9d517b526)

>이 코드는 객체지향 프로그래밍을 활용해 간단한 은행 시스템을 구축한 예제입니다. 디자인 패턴 측면에서 보면 다음과 같이 분류할 수 있습니다:

>Facade 패턴

BankSystem 클래스는 여러 개의 BankAccount 객체를 관리하며, 계좌 생성, 입금, 출금, 잔액 조회와 같은 여러 작업을 하나의 단순한 인터페이스로 제공하고 있습니다.
즉, 복잡한 내부 로직(여러 계좌 관리)을 감추고 단순한 메서드 호출만으로 외부에서 기능을 사용할 수 있게 하는 Facade 패턴의 특징이 있습니다.

>Singleton 패턴 (유사)

Streamlit의 st.session_state에 BankSystem 인스턴스를 한 번만 생성해 저장하고, 애플리케이션 전체에서 공유하는 구조는 사실상 Singleton 패턴과 유사합니다.
이를 통해 하나의 전역 BankSystem 인스턴스가 유지되어 여러 요청에서도 동일한 상태를 관리할 수 있습니다.

