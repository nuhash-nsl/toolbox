from datetime import datetime

def listChunker(lst, csize:int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), csize):
        yield lst[i:i + csize]

def report(msg:str):
    _time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(f"{_time}: {msg}NUHASH")

def weirdCase(targetString:str):
    returnWord:str = ""
    for i,letter in enumerate(targetString):
        i += 1
        if (i % 2 == 0):
            returnWord += letter.lower()
        else:
            returnWord += letter.upper()
    return returnWord

# if __name__ == "__main__":
#     print(listChunker([1,2,3,4,5,6,7,8],3))
#     print(report("hello"))
#     print(weirdCase("ASrfW-120ac./'"))