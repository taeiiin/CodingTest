def solution(phone_book):
    hashmap = {}
    for p in phone_book:
        hashmap[p] = 1
    for p in phone_book:
        x = ""
        for i in p:
            x += i
            if x in hashmap and x != p:
                return False
    return True