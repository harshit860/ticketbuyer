SERVICE_CHARGE=2
TICKET_PRICE = 10
tickets_remaining =  100

#THIS FUNCTION CAN BE USED WHERE YOU WANT ITEMS AND FIXED PRICE FOR A THING
def calculate_price(number_of_tickets):
    return number_of_tickets*TICKET_PRICE+2

while tickets_remaining>=1:
    print("tickets remaining is{} ".format(tickets_remaining))
    name=input("what is your name ")#ENTERING THE NAME OF USER
    num_of_tickets=input("how many tickets you want to buy")#THE NUMBER OF ITEMS USER WANTS TO BUY
    try:
        num_of_tickets=int(num_of_tickets)
        if num_of_tickets>tickets_remaining:
            raise ValueError("There are only{} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("oh no we ran into a issue {}please try again".format(err))
    else:
        amount_due=calculate_price(num_of_tickets)

        print("The final price to be paid is {}".format(amount_due))

        should_proceed = input("Do you want to proceed? Y/N")

        if should_proceed.lower() == "y":
            print("Sold")
            tickets_remaining = tickets_remaining-num_of_tickets
        else:
            print("thank you anyways {}".format(name))

print("Sorry tickets sold out:(")
