def is_pangram(target):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    target = target.replace(" ", "").lower()
    for a in alphabets:
        if a not in target:
            return False
    return True