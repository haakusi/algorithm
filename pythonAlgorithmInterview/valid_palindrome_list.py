# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# 예제 1)
# 입력 - "A man, a plan, a canal: Panama"
# 출력 - True
# 예제 2)
# 입력 - "race a car"
# 출력 - False

def isValidPalindrome(str):
    strs = []
    for char in str:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if(strs.pop(0) != strs.pop()):
            return False
    return True

if __name__ == '__main__':
    result = isValidPalindrome("A man, a plan, a canal: Panama")
    print(result)



