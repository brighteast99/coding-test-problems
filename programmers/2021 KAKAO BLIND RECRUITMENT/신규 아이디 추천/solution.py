import re

def solution(new_id):
    ALLOWED_LETTERS = 'abcdefghijklmnopqrstuvwxyz-_.0123456789'

    new_id = new_id.lower()
    new_id = ''.join([letter for letter in new_id if letter in ALLOWED_LETTERS])
    new_id = re.sub('\.+', '.', new_id)
    new_id = new_id[1 if new_id[0] == '.' else 0 : -1 if new_id[-1] =='.' else None]
    if new_id == '':
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id[: -1 if new_id[-1] =='.' else None]
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))

    return new_id
