p1 = "make a lot of money"
p2 = "Click on download button to download"
p3 = "share your bank detail"
p4 = "give 300 and return 500"

message = input("Enter your Comment :")
if((p1 in message ) or (p2 in message ) or (p3 in message ) or (p4 in message )):
    print("This Comment is spam")

else:
    print("This Comment is not a spam")    