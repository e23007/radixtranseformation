def radix(target,prev,next):
    result=0
    i=0
    while target>0:
        r=target%next
        result=result+r*prev**i
        target=target//next
        i=i+1
    return result
