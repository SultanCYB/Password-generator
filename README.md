# pwd generator
### random python password generator
## Usage
### This function has 3 optional parameters explained respectively:

- length (1): 

length of the password, there is no max range. If no length given; the function will choose a random length between 8 and 40

- num (2): 

if False given; it will exclude digits from the password

- symbol (3): 

if False given; it will exclude symbols from the password

## Examples
    >>> from pwd_generator import pwd_generator
    
    
    >>> pwd_generator()
    y~h98'@!8bn@c.7/[%~h
    
    >>> pwd_generator(num=False)
    y;|P&B_.>&~`\[)
    
    >>> pwd_generator(symbol=False)
    kdU367Xpz9968ShZ48P4r0HYSyZRB
    
    >>> pwd_generator(num=False, symbol=False)
    bUzNSjIcGVJHYUZjf
    
    >>> pwd_generator(8)
    G317)ze2
    
    >>> pwd_generator(8, False, False)
    rPKBPKws