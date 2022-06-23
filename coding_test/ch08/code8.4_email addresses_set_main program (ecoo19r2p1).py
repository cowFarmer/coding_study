# Main Program

for dataset in range(10):
    n = int(input())
    addresses = set()
    for i in range(n):
        address = input()
        address = clean(address)
        addresses.add(address)

    print(len(addresses))
