def total(g,s,k):
    return(g*17+s)*29 + k

coins= {"g":100,"s":50,"k":25}

print(total(**coins),"Knuts")
