
#!/usr/bin/env python
# Author: mohamedkdidi@gmail.com 
# Convert symbolic permission notation to numeric notation.

def perm_to_num(symbolic):

    perms = {
            '---': '0',
            '--x': '1',
            '-w-': '2',
            '-wx': '3',
            'r--': '4',
            'r-x': '5',
            'rw-': '6',
            'rwx': '7'
        }

    # Trim Lead If It Exists
    if len(symbolic) > 10 | len(symbolic) < 9:
        print("Err format")
        
    if len(symbolic) == 10:
        if(symbolic[0] == "d"):
            print("directory")
        elif(symbolic[0] == "l"):
            print("symbolic link")
        elif(symbolic[0] == "s"):
            print("socket")
        elif(symbolic[0] == "b"):
            print("block device")
        elif(symbolic[0] == "p"):
            print("pipeline")
        elif(symbolic[0] == "D"):
            print("Door")
        else:
            print("Err format")
        # Trim Lead If It Exists
        symbolic = symbolic[1:]

    # Parse Symbolic to Numeric
    x = (symbolic[:-6], symbolic[3:-3], symbolic[6:])
    if  ( (not x[0] in perms) | (not x[1] in perms) | (not x[2] in perms)):
        return ("Err format")
    numeric = perms[x[0]] + perms[x[1]] + perms[x[2]]
    return numeric
    


if __name__ == "__main__":
   print(perm_to_num ('dr--r--r--'))