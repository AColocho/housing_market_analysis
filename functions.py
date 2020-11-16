def counter(x):
    count = {}
    for item in x:
        dictKeys = count.keys()
        if item in dictKeys:
            value = count.get(item)
            value += 1
            count.update({item:value})
        else:
            if item == item:
                count.update({item:1})

    return {k: v for k, v in sorted(count.items(), key=lambda item: item[1],reverse= True)}

def countDF(DF):
    columns = list(DF.columns)
    count = []
    
    for i in columns:
        column = DF[i]
        count.append(counter(column))
        
    return count

def cleanReasons(x):
    if x == 'Passive income and property management ':
        return 'investing'
    elif x == 'I wanna get out this bitch ':
        return 'move to new place'
    elif x == 'Purchased a property June 2020':
        return 'already purchased property'
    else:
        return x
    
def changeToStateCode(x):
    if (x == 'Virginia') or (x== 'Virginia '):
        return 'VA'
    elif x == 'Maryland ':
        return 'MD'
    elif x == 'New York':
        return 'NY'
    elif x == 'North Carolina ':
        return 'NC'
    elif x == 'California':
        return 'CA'
    elif x == 'Centreville':
        return 'VA'
    else:
        return x