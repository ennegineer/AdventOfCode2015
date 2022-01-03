import hashlib

for num in range(0,100000000000):
    input = "yzbqklnj" + str(num)
    digestor = hashlib.md5(input.encode())
    guess = digestor.digest().hex()[0:6]
    # print(guess)
# digestor.update(input.encode())
    if guess == '000000':
        print(f"answer! {num}")

# answer = digestor.digest()

# print(answer)

# MD5 hash in hexadecimal starting with at least five zeroes
#   MD5 hash starts with my input and has 6 numbers after it. find lowest
# find the lowest positive number with no leading zeroes 

## encode() : Converts the string into bytes to be acceptable by hash function.
## digest() : Returns the encoded data in byte format.
## hexdigest() : Returns the encoded data in hexadecimal format.

            # newnumber = hashlib.md5(input.encode())
            # print(newnumber)
            # print(min(newnumber.hexdigest()))
            # halp = newnumber.hexdigest()
            # answer = hashlib.md5(halp.digest())


# answer is not 28E52FE8670
# answer is not 0000028E52FE8670
