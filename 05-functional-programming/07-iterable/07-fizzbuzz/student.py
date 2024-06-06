def fizzbuzz():
    num = 1
    while True:
        result = ''
        if num % 3 == 0:
            result += 'fizz'
        if num % 5 == 0:
            result += 'buzz'
        result = result or str(num)
        yield result
        num += 1