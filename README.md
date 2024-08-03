# Silent-Auction-Project
This Python program implements a silent auction system where multiple bidders can place their bids. The program determines the winner by finding the highest bid.

Features:
- Asks each bidder for their name and bid price
- Stores bidder information in a dictionary
- Finds the winner by identifying the highest bid
- Displays the winner's name and bid price
- Allows for multiple bidders
- Clears the screen after each bid

How it works:
1. The program welcomes the user and initializes an empty dictionary bidder_data to store bidder information.
2. It asks each bidder for their name and bid price, and stores this information in the bidder_data dictionary.
3. The program asks if there are more bidders. If not, it ends the bidding process.
4. If there are more bidders, the program clears the screen and repeats the bidding process.
5. Once the bidding process is complete, the program finds the winner by identifying the highest bid in the bidder_data dictionary.
6. The program displays the winner's name and bid price.
This code demonstrates basic Python concepts such as dictionaries, loops, conditional statements, and input/output operations. It also uses the os module to clear the screen.
