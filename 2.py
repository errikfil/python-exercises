import math
import random

fibonacci = [0, 1]   # βαζει στην λίστα fibonacci τους πρώτους 600 αριθμούς
for i in range(2, 600):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

n = int(input('εισάγετε έναν αριθμό της ακολουθίας fibonacci:'))
odd = True    # αρχικοποιηση της μεταβλητης να είναι αληθής μέχρι την στιγμή που θα γίνει ψευδής και θα γινει break
if n == 0 or n == 1 or n == 2 or n == 3:
    print("ο", n, "ος όρος είναι ο", fibonacci[n], " και δεν είναι πρώτος")
else:
    for i in range(0, 20):
        a = random.randint(1, n-1)     # δημιουργεί έναν τυχαίο αριθμό a < n

        if (a ** (n-1) - 1) % n != 0:
            odd = False
            break

    if odd:
        print("ο", n, "ος όρος είναι ο", fibonacci[n], " και είναι πρώτος")
    else:
        print("ο", n, "ος όρος είναι ο", fibonacci[n], " και δεν είναι πρώτος")