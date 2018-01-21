#usr/bin/python3

# => Dinesh Singh
# => Hackerrank

# Function input() Takes the input n and q, where each element is a string. The map function maps the elements
# as int and the result thus obtained is stored in n and q;
# Here n => Number of sequences in the list
# and q => Number of Queries
n, q = map(int, input().split());

seqList = [[] for i in range(n)];
lastAnswer = 0;

while (q):
    q -= 1;
    query, x, y = map(int, input().split());

    # Find the sequence which is to be manipulated
    indexSeq = (x^lastAnswer)%n
    seq = seqList[indexSeq]

    # Append y to extracted sequence if query is 1
    # else change the lastAnswer varible
    if query == 1:    
        seq.append(y)

    else:
        seqLength = len(seq)
        lastAnswer = seq[y%seqLength]
        print(lastAnswer)

