#   PassingUnderWedge
#   Unix Timestamp: 1703907279

#   Author: Ausin Smith
#   ThatSmittyDude@outlook.com
#   github.com/ThatSmittyDude

#   passingunderyellow.com
#   puyinside.com

#   Variables
LF = float(input("LF corner weight: "))
LR = float(input("LR corner weight: "))
RF = float(input("RF corner weight: "))
RR = float(input("RR corner weight: "))
Total = LF + LR + RF+ RR
Wedge = ((RF + LR) / Total) * 100

# Print results
print("Total weight")
print(Total)
print("Wedge %")
print(round(Wedge), 1)