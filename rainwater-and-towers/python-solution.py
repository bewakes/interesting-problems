def find_collected_water(towers):
    if not towers: return 0
    length = len(towers)

    leftmaxs = [towers[0]]*length
    for i, x in enumerate(towers[1:]):
        if x> leftmaxs[i]:
            leftmaxs[i+1] = x
        else:
            leftmaxs[i+1] = leftmaxs[i]

    rightmaxs = [towers[-1]]*length
    for i, x in enumerate(reversed(towers[:-1])):
        if x > rightmaxs[length-1-i]:
            rightmaxs[length-2-i] = x
        else:
            rightmaxs[length-2-i] = rightmaxs[length-1-i]
    # now for each tower, find the minimum of max-right and max-left
    minimums = list(map(min, zip(leftmaxs, rightmaxs)))
    # how much a tower can hold is difference between minimum of max and its height
    diffs = list(map(lambda (x, y): x-y, zip(minimums, towers)))
    return sum(diffs)

if __name__ == '__main__':
    towers = [5,3,7,2,6,4,5,9,1,2]
    print(find_collected_water(towers))
