
# Prepaid 
units=int(input("Number of watts consumed: "))
if(units>0 and units<=100):
    payAmount=units*1.5
    fixedcharge=25.00
elif(units>100 and units<=200):
    payAmount=(100*1.5)+(units-100)*2.5
    fixedcharge=50.00
elif(units>200 and units<=300):
    payAmount=(100*1.5)+(200-100)*2.5+(units-200)*4
    fixedcharge=50.00
elif(units>300):
    payAmount=2500; #fixed amount
    fixedcharge=75.00
else:
    payAmount=0;
    
Total= payAmount+fixedcharge
print("\n Your Electicity bill this month= $%.2f " %Total);
