def Simple_Interest(principal, rate, time):
    return (principal*rate*time) / 100

def Rate_in_SI(interest,principal,time): 
    return interest / (principal*time)

def Principal_in_SI(interest,rate,time):
    return interest/ (rate*time)

def Time_in_SI(interest, principal, rate): 
    return(100*interest)/ (principal*rate)
    