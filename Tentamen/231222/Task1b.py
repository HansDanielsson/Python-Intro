strlst = ["one", "two", "three"]
n = len(strlst)
m = len(strlst[2])
if n == m:
    print("Equal")
elif len(strlst[0]) < m or strlst[1] == "one":
    print("different")
else:
    print("Similar")
