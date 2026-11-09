score = float (input("Enter your score "))

if score < 0 and score > 100:
    print ("INVALID SCORE")
    
elif score > 50:
    print ("YOU PASSED!!")

else:
    print ("YOU FAILED!!")
