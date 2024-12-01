'''
کاربر یک عدد ۳۲ بیتی وارد میکنید.
اگر عدد ۳۲ بیت نبود صفر برگردانده شود
درغیر این صورت عکس معکوس شود.
مثلا کاربر اگر عدد ۱۲۳ وارد کرد
خروجی ۳۲۱ شود

'''

def check_32_bite(number: int) -> bool:
    number = int(number)
    max_bit = 2 ** 31
    min_bit = 2 ** -31
    if number > max_bit or number < min_bit:
        return True
    return False


def to_list(num: str) -> list:
    if check_32_bite(number=num) == True:
        print('pom',check_32_bite(number=num))
        for item in num:
            if int(item) > 0:
                number_new = num[::-1]
                number_new[0] = item
            number_new = num[::-1]
        return number_new
    return 0


def main():
    number=input('enter your number:')
    return to_list(num=number)

a = main()
print(a)




