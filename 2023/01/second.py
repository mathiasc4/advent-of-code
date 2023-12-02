digits = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def findCalibrationValue(line: str):
    firstDigit: int = 0
    lastDigit: int = 0

    firstDigitIndex: int = len(line)
    lastDigitIndex: int = -1

    for digit in digits.keys():
        firstFoundDigitIndex = line.find(digit)
        lastFoundDigitIndex = line.rfind(digit)

        if firstFoundDigitIndex > -1 and firstFoundDigitIndex < firstDigitIndex:
            firstDigitIndex = firstFoundDigitIndex
            firstDigit = digits[digit]

        if lastFoundDigitIndex > -1 and lastFoundDigitIndex > lastDigitIndex:
            lastDigitIndex = lastFoundDigitIndex
            lastDigit = digits[digit]

    return (firstDigit * 10) + lastDigit


findCalibrationValue("fourbsqr7bktkbqbdlpfour")

with open("./input", "r") as input:
    sum: int = 0

    for line in input:
        calibrationValue = findCalibrationValue(line)
        print(line[:-1] + " : " + str(calibrationValue))
        sum += calibrationValue

    print(sum)
