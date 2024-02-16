# Who Pays For Coffee?

DESCRIPTION
- This is my solution to Bertram Labs' SWE Internship Challenge

USAGE
- Collect all of the files in the same folder then open a terminal in that folder
- Run the program using the command "python3 mainGUI.py"
- Running this command will bring up the GUI after a second which the user can interact with to add the members of the coffee group
- Additionally, the program comes preprogrammed with a short list of drinks (Latte for $7, Espresso for $5, and Black Coffee for $3) but more options can be added with the "+ Add Drink" button
- Once the members have been added and their drinks have been selected, select the "GO" button to choose who should pay for this round of coffee

ASSUMPTIONS
- The first assumption I made in creating this program was that every user would show up to every coffee session (and was therefore available to pay)
- The second assumption I made was that the program would be left running in between uses as I didn't have time to fully flesh out the save features

THE ALGORITHM
- Everyone has a balance attached to them
  - This represents the monetary value of coffee that they have consumed but not paid for if positive, and paid for but not consumed if negative
- When a member pays for coffee, the amount they pay is subtracted from their balance
- The person with the highest balance pays

NOTES
- Any entry fields have been protected so that only proper input can be accepted
- To account for the "everyone has their favorite coffee" note in the challenge, I added a feature where the drop down menu defaults to the last coffee a person bought
  - No extraneous drop down menu selections are necessary if people are buying the same coffees over and over
- Each person's balance can be seen in the terminal after each group coffee purchase is made
