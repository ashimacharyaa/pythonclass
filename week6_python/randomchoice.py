import random

random.seed(42)

friends = ["Ramesh","Sunita","Bikash","Anjali","Dipak"]
total_bill = 3750

def split_bill(friends, total):
    return total / len(friends)

def pick_luck(friends):
    return random.choice(friends)

def final_summary(friends, total):
    share = split_bill(friends, total)
    lucky_person = pick_luck(friends)

    print("Bill Summary")
    print("=" * 20)

    for friend in friends:
        if friend == lucky_person:
            total_payment = share + 50
            print(f"{friend} pays NPR {total_payment} (lucky +50)")
        else:
            print(f"{friend} pays NPR {share}")

    print("\nLucky Person:", lucky_person)

final_summary(friends, total_bill)