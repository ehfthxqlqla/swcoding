"""
https://vscode.dev 가서 하나 만들기
"""

import time as t
import random as rand

a = ["랜덤1", "랜덤2", "랜덤3"] # 리스트 (list)
# 예를들어 a = ["치킨", "짜장", "탕수육", "피자", "가지볶음"] 처럼 4~5개 만든다.

count = 10 # count의 숫자를 수정하여 뽑아낼 횟수를 정한다.

for x in range(1, count + 1):
    print(x,":", rand.choice(a))
