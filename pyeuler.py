def is_prime(num):
    
    if num == 1:
        return False

    elif num == 2 or num == 3:
        return True

    elif num % 2 == 0:
        return False

    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                break
        else:
            return True

        return False