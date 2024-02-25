import secrets

def generate_random_key():
    # 16바이트(128비트)의 랜덤 키 생성
    random_key = secrets.token_bytes(16)
    
    # 생성된 키를 16진수 문자열로 변환
    hex_key = random_key.hex()
    
    return hex_key

# 랜덤 키 생성
random_key = generate_random_key()
print(f"Random Key: {random_key}")
