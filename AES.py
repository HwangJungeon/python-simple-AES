import json
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import base64

def encrypt(data, key):
    try:
        # JSON 데이터를 문자열로 변환
        data = json.dumps(data)
        
        # 64자리 키를 bytes로 변환
        key = bytes.fromhex(key)
        
        # AES 객체 생성 (ECB 모드)
        cipher = AES.new(key, AES.MODE_ECB)
        
        # 데이터를 패딩하고 암호화
        ciphertext = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
        
        # base64로 인코딩
        encrypted_data = base64.b64encode(ciphertext).decode('utf-8')
        
        return encrypted_data
    except Exception as e:
        print(f"Encryption failed: {e}")
        return None

def decrypt(encrypted_data, key):
    try:
        # 64자리 키를 bytes로 변환
        key = bytes.fromhex(key)
        
        # base64 디코딩
        encrypted_data = base64.b64decode(encrypted_data)
        
        # AES 객체 생성 (ECB 모드)
        cipher = AES.new(key, AES.MODE_ECB)
        
        # 패딩을 제거하고 데이터 해독
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size).decode('utf-8')
        
        # 문자열을 JSON 데이터로 변환
        decrypted_data = json.loads(decrypted_data)
        
        return decrypted_data
    except Exception as e:
        print(f"Decryption failed: {e}")
        return None