def textNumbers(string):
    if "one" in string:
        return '1'
    if "two" in string:
        return '2'
    if "three" in string:
        return '3'
    if "four" in string:
        return '4'
    if "five" in string:
        return '5'
    if "six" in string:
        return '6'
    if "seven" in string:
        return '7'
    if "eight" in string:
        return '8'
    if "nine" in string:
        return '9'
    else:
        return 'A'

def star1(lines):
    calibration_total = 0
    for line in lines:
        startString = ""
        for digitS in line:
            startString = startString + digitS
            if digitS.isnumeric():
                first = str(digitS)
                break
        endString = ""
        for digitE in reversed(line):
            endString = digitE + endString
            if digitE.isnumeric():
                second = str(digitE)
                break
        calibration_total += int(first + second)
    return calibration_total

def star2(lines):
    calibration_total = 0
    for line in lines:
        startString = ""
        for digitS in line:
            startString = startString + digitS
            if digitS.isnumeric():
                first = str(digitS)
                break
            elif textNumbers(startString).isnumeric():
                first = textNumbers(startString)
                break
        endString = ""
        for digitE in reversed(line):
            endString = digitE + endString
            if digitE.isnumeric():
                second = str(digitE)
                break
            elif textNumbers(endString).isnumeric():
                second = textNumbers(endString)
                break
        calibration_total += int(first + second)
    return calibration_total

if __name__ == "__main__":
    with open('inputs/day01.txt') as f:
        lines = f.readlines()
    print(star1(lines))
    print(star2(lines))
