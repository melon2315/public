# hello world 출력 프로그램 만들어줘 파이썬으로
def hello_world():
    print("hello world") 


#입력받은 첫번째 숫자부터 두번째 숫자까지 더하는 함수
def sum_two(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += i
    return sum

#Splunk 매크로 함수 만들기  (Splunk에서 사용할 수 있는 함수)   
def splunk_macro(a,b):
    return sum_two(a,b) 

#생년월일 정보를 받아서 현재 년도 기준 성인인지 판별하는 함수
# 아래 코드의 문제점을 찾아줘
def is_adult(birth_year):
    import datetime
    current_year = datetime.datetime.now().year
    age = current_year - birth_year + 1
    if age >= 20:
        return True
    else:
        return False


# 메인함수
if __name__ == "__main__":
    hello_world()

    age = is_adult(1990)

