def most_frequent(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1

    return d


string=input("Enter the String")
output=most_frequent(string)
print(output)
