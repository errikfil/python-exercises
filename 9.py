import math  # για να γινει η στρογγυλοποίηση στην γραμμη 43


def count_char(text, char):  # συναρτηση που μετράει το ποσες φορες εμφανιζεται ο char στο αρχείο
    count = 0
    for word in text.upper().split():  # κανει κεφαλαια τα γραμματα σε καθε λεξη
        for character in word:  # ελεγχει καθε γραμμα στην λεξη που πηρε πάνω
            if character == char:   # αν ο χαραστηρας είναι ίδιος με τον char που έχουμε πάρει, αυξάνει το count
                count += 1
    return count


filename = input("Enter the file name: ")
with open(filename) as file:
    text = file.read().replace(" ", "")  # στο αρχείο αντικαθηστά τα space με τίποτα

total = len(text)  # το σύνολο των γραμματων στο αρχείο
print("the total number of letters is: ", total)

list1 = []
for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':  # ελεγχει ποια γραμματα της αβ υπαρχουν στο αρχειο
    with open(filename) as file:
        if x in file.read():
            list1.append(ord(x))  # αν υπαρχει το συγκεκριμενο γραμμα το μετατρεπει στο αντιστοιχο ASCII
            # και το βαζει στην λιστα list1

odd_numbers = []
for x in list1:  # ελεγχει ποιοι αριθμοί από την list1 είναι μονοί και τους βάζει στην λίστα prime_numbers
    if (x % 2) != 0:
        odd_numbers.append(x)

print("the odd numbers (values of ASCII characters) of the file are: ", odd_numbers)

string = ""
my_letters = []
for char in odd_numbers:
    string = chr(char)
    my_letters.append(string)
#print(my_letters)

for char in my_letters:
    perc = 100 * count_char(text, char) / total  # υπολογίζει το ποσοστό του κάθε γράμματος
    #print(count_char(text, char))
    #print(perc)
    perc2 = (math.ceil(perc))  # απλοποιεί προς τα πάνω το ποσοστό perc
    #print(perc2)
    star = perc2 * "*"
    print("{0}: {1}".format(char, star))
