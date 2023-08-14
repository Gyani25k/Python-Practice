'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

'''


def defaminganIPaddress(strings):
    return  strings.replace('.','[.]')

strings="1.1.1.1"
res=defaminganIPaddress(strings)
print(res)

