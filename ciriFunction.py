def CIRI(active,a,n):
    Rzero = 3.28 #average R0 estimate by Liu et al, 2020 - https://academic.oup.com/jtm/article/27/2/taaa021/5735319
    k = 4 #k is how many connections does the place have.
    #I am assuming a constant value because of the lack of this information, for now.
#     normCIRI = (x-min(x))/(max(x)-min(x))
    try:
        goelSharma = (Rzero * ((1 + (1+a*k)*n)/(1+n))) 
    except:
        goelSharma = 0
    #Based on equation by Goel and Sharma, 2020 - https://arxiv.org/pdf/2004.13015.pdf
    normGS = goelSharma / 1761.36     #We are diving CIRI by the highest possible value to get an index from 0:1
    
    CIRI = active * normGS/active
    
    return CIRI

#CIRI(70, 45)