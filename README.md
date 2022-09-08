# pwd_generator
### random python password generator
## Usage
### This function has 3 optional parameters explained respectively:

- length (1): 

length of the password must be at least 8 characters, there is no max range,
if no length given; the function will choose a random length between 8 and 40

- num (2): 

if False given; it will exclude digits from the password

- symbol (3): 

if False given; it will exclude symbols from the password

## Examples
    >>> from pwd_generator import pwd_generator
    
    
    >>> pwd_generator()
    m7zt0"9xtd3R7]6\Q:Z4(u-MUqGo"67B
    
    >>> pwd_generator(num=False)
    DWM&f]V/PtV]k)U[VXLu:F|zRkn
    
    >>> pwd_generator(symbol=False)
    Jm01F6tIq2v012Mf3E62150w
    
    >>> pwd_generator(num=False, symbol=False)
    uykJfVmJIbjDScVzTvTeLrwFsLZAiZN
    
    >>> pwd_generator(8)
    C3^91j\Z
    
    >>> pwd_generator(8, False, False)
    PCdKjbdG
