def solution(digits):
    n = list(map(int ,digits))
    for i in range(len(digits)-1,0,-1):
        if n[i] > n[i-1]:
            break
    if i == 1 and n[i] <= n[i-1]:
        print (digits+"0")
        return
    val = n[i-1]
    smallest = i
    for j in range(i+1,len(digits)):
        if n[j] > val and n[j] < n[smallest]:
            smallest = j
    n[smallest],n[i-1] = n[i-1], n[smallest]
    val = 0
    for k in range(i):
        val = val * 10 + n[k]
    n = sorted(n[i:])
    for l in range(len(digits)-i):
        val = val * 10 + n[l]
    print (val)
 
 
# test above function
digits = "115"        
solution(digits)
 
digits = "8000"        
solution(digits)
