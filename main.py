import time

while True:
    print("Welcome to the Tip Calculator!")

    amount = float(input("Enter total amount:"))

    print(f"The amount you put is {amount}")

    try:
        tip_percent = float(input("How many Percent should the tip be?"))

        total = ((amount / 100) * tip_percent) + amount
        tip = (amount / 100) * tip_percent

        print(f"The total payement would be {total}")
        print(f"The tip is {tip}")

        restart = input("continue? enter q to quit").lower()

        if restart == "q":
            print("**quitting**")
            quit()
        else:
            print("continuing")
            continue
    except:
        print("The value you entered cannot be calculated")
        print("**Restarting program**")
        time.sleep(0.5)
        continue







