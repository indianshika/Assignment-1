
def NumGen(n):

    for j in range(1, n+1):
        if j % 7 == 0:
            yield j

if __name__ == "__main__":
    N = 50
    for j in NumGen(N):
        print(j, end = " ")
