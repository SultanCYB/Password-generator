# Password generator
### Random python password generator
## Usage
### This function has 3 optional parameters explained respectively:

- ### length (1) [ default will be randomly in range 8-41] :

> length of the password. It has no max range. If no length given; the function will choose a random length between 8 and 40

- ### num (2) [ default is True ] :

> Include numbers. If False given; it will exclude the digits from the password

- ### symbol (3) [ default is True ] :

> Include symbols. If False given; it will exclude symbols from the password

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
