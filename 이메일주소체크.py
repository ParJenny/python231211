import re

def check_email(email):
    # 이메일 주소를 검증하는 정규표현식
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # re.search() 함수를 사용하여 정규표현식과 매치되는지 확인
    match = re.search(pattern, email)
    
    # 매치 결과 출력
    if match:
        print(f"{email}은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"{email}은(는) 유효하지 않은 이메일 주소입니다.")

# 샘플 이메일 주소 10개
sample_emails = [
    "user@example.com",
    "john.doe123@company.net",
    "invalid-email",
    "noatsign.com",
    "user@.com",
    "user@company",
    "user@company.",
    "user@company..com",
    "@company.com",
    "user@company_com"
]

# 각각의 이메일 주소에 대해 검증
for email in sample_emails:
    check_email(email)
