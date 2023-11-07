def Solution(nums, target):
    integers = nums.split()
    twosum = []
    for i in range(len(integers)):
        for j in range(i+1, len(integers)):
            if int(integers[i])+int(integers[j]) == target:
                twosum.append(i)
                twosum.append(j)
                print(twosum)
                exit()
    # print(integers)
    return twosum


def main():
    nums = input("")
    target = int(input(''))
    Solution(nums, target)

if __name__ == '__main__':
    main()
