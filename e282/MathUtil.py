
'''
param: string
return: true if integer, false otherwise
'''
def isInteger(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

'''
param: String
return: integer if valid int, None otherwise
'''
def parseInt(x):
    try:
        return int(x)
    except ValueError:
        return None
