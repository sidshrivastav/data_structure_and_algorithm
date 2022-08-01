def counting_bit(n):
    return n

if __name__ == "__main__":
    # print(counting_bit(5))
    a = 6
    x = 0
    while(a):
        print("----------------------------")
        print(a)
        x += a & 1
        a >>= 1

    print("\n\nans")
    print(x)