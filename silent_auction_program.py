import os
print("*****welcome to the silent Auctoin program*****")
def find_winner(bidder_details):#{jenny:10000, Ram:30000, shyam:50000}
    highest_bid=0#30000
    winner=""
    for bidder in bidder_details:#jenny
        bidding_price=bidder_details[bidder]#30000
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"Here is the list of all the bidders:{bidder_details}")
    print(f"The winner is {winner} with a bid price of {highest_bid}")


bidder_data={}#empty dictonary
end_of_bidding=False
while not end_of_bidding:
    name=input("What is your name?:")
    price=int(input("What is your bid?:"))
    bidder_data[name]=price#dictionary key=name value=price
    more_bidders=input("Are there more biders? Type'Yes' or'no' :").lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=='Yes':
        os.system('cls')
































































































