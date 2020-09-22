def countApplesAndOranges(s, t, a, b, apples, oranges):
    app = 0
    ora = 0
    for i in apples:
        if ((a+i) >= s and (a+i) <= t):
            app += 1
    for j in oranges:
        if((b+j) <= t and (b+j) >= s):
            ora += 1
    print(app)
    print(ora)