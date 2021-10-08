TC = int(input())
for tc in range(1,TC+1):
    bin = list(input())
    tri = list(input())
    lb = len(bin)
    lt = len(tri)
    #print(lb, lt, bin, tri)
    ans = 0
    for i in range(lb):
        tbin = bin[:]
        tbin[i] = str(1-int(tbin[i]))
        for j in range(lt):
            for k in range(3):
                if k != int(tri[j]):
                    ttri = tri[:]
                    ttri[j] = str(k)
                    nbin = int(''.join(tbin),2)
                    #print(tbin,nbin,''.join(ttri))
                    if nbin==int(''.join(ttri),3):
                        ans = nbin
            if ans:
                break
        if ans:
            break
    print(f'#{tc} {ans}')
