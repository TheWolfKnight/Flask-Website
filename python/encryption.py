from sys import stdout, exit


if __name__ == "__main__":
    stdout.write("DON'T RUN ME REEEEEEEEEEEEEEE")
    stdout.flush()
    exit()


CONST_ALPNUM: str = "0123456789abcdefghijklmnopqrstuvwxyz"


def encrypt_pwd(pwd: str, key: str) -> str:
    """
    Encrypts the given password using the 
    """
    r: str = ""
    for idx, val in enumerate(pwd):
        valPos: int = CONST_ALPNUM.index(val)
        loop_key : chr = key[idx%len(key)]
        keyPos: int = CONST_ALPNUM.index(loop_key)
        r += CONST_ALPNUM[(valPos+keyPos)%len(CONST_ALPNUM)]
    return r

