def sum_without_smallest(v):
    index_smallest = v.index(min(v))
    sum_ = 0
    if len(v) == 1:
        sum_ = v[0]
    else:
        for i in range(len(v)):
            if i == index_smallest:
                continue
            else:
                sum_ = sum_ + v[i]

    return sum_


def main():
    v = [34, 674]
    total = sum_without_smallest(v)
    print(total)


if __name__ == '__main__':
    main()
