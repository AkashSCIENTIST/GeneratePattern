from GeneratePattern import GeneratePattern

obj = GeneratePattern([1,2,3,4,5,6,7,8,9,10], 9)
input_, output = obj.generate()

print("Input Sequences")
print(*input_, sep="\n")
print("\nCorresponding Outputs")
print(output)
