def solution(phone_book):
    phone_book.sort(key=len)
    occurances = set()
    for phone_num in phone_book:
        for i in range(len(phone_num)):
            if phone_num[:i] in occurances:
                return False
            occurances.add(phone_num)
    return True
