def num2word(num):
    under_20 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    above_100 = {100: "hundred", 1000: "thousand", 1000000: "million", 1000000000: "billion"}
    if num < 20 :
        return under_20[num]
    if num < 100 :
        return tens[int(num/10)-2] + ('' if num % 10 == 0 else ' ' + under_20[num%10])
    pivot = max([key for key in above_100.keys() if key <= num])
    return num2word(int(num/pivot)) + ' ' + above_100[pivot] + ('' if num % pivot == 0 else ' ' + num2word(num % pivot))