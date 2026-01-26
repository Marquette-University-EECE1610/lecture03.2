# event_messy.py
# This program works, but it is hard to read, hard to change,
# and mixes input/output with computation.
# Your task is to refactor it into clear, reusable functions.

print("Campus Event Cost Estimator")
print("----------------------------")

# inputs
attendees = int(input("Enter number of attendees: "))
cost_per_person = float(input("Enter food cost per person: "))
room_fee = float(input("Enter room rental fee: "))

av_choice = input("Do you need AV support (yes/no)? ")

# magic numbers
tax_rate = 0.055
av_fee = 150.0

# food cost
food_total = attendees * cost_per_person

# AV cost
if av_choice == "yes":
    av_total = av_fee
else:
    av_total = 0.0

# subtotal
subtotal = food_total + room_fee + av_total

# tax
tax = subtotal * tax_rate

# total cost
total_cost = subtotal + tax

# cost per attendee
if attendees > 0:
    per_person = total_cost / attendees
else:
    per_person = 0.0

# output
print()
print("Event Cost Summary")
print("------------------")
print("Food cost:", food_total)
print("Room fee:", room_fee)
print("AV cost:", av_total)
print("Tax:", tax)
print("Total cost:", total_cost)
print("Cost per attendee:", per_person)

# quick sanity checks
if per_person > 100:
    print("Warning: This is an expensive event per person.")
elif per_person < 10:
    print("Note: This event is very inexpensive per person.")

print("Done.")
