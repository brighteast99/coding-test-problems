def solution(phone_book):
    phone_book = set(phone_book)
    for phone_num in phone_book:
        for i in range(len(phone_num)):
            if phone_num[:i] in phone_book:
                return False
    return True
