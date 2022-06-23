# Main Program

for dataset in range(10):
    n = int(input())
    addresses = []
    for i in range(n):
        address = input()
        address = clean(address)
        if not address in addresses:
            addresses.append(address)

    print(len(addresses))
