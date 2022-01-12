# GeneratePattern

### Demo

```python
from GeneratePattern import GeneratePattern

obj = GeneratePattern([1,2,3,4,5,6,7,8,9,10], 9)
input_, output = obj.generate()

print("Input Sequences")
print(*input_, sep="\n")
print("\nCorresponding Outputs")
print(output)
```

### Result

```powershell
Input Sequences
[0, 0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2]
[0, 0, 0, 0, 0, 0, 1, 2, 3]
[0, 0, 0, 0, 0, 1, 2, 3, 4]
[0, 0, 0, 0, 1, 2, 3, 4, 5]
[0, 0, 0, 1, 2, 3, 4, 5, 6]
[0, 0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

Corresponding Outputs
[2, 3, 4, 5, 6, 7, 8, 9, 10]
```
