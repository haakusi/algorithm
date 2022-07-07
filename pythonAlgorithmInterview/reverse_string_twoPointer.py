# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
# 예제 1)
# 입력 - ["h", "e", "l", "l", "o"]
# 출력 - ["o", "l", "l", "e", "h"]
# 예제 2)
# 입력 - ["H", "a", "n", "n", "a", "h"]
# 출력 - ["h", "a", "n", "n", "a", "H"]
from typing import List

def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

if __name__ == '__main__':
    result = reverseString(["h","e","l","l","o"])
    print(result)



