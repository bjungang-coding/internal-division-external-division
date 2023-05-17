A_ = list(map(int, input().split()))
B_ = list(map(int, input().split()))

ratio = list(map(int, input().split()))

def internal_division(A: int, B: int, ratio: list[int]) -> float:
    denominator = ratio[0] + ratio[1]
    numerator = A*ratio[1] + B*ratio[0]
    return numerator/denominator

def external_division(A: int, B: int, ratio: list[int]) -> float:
    denominator = ratio[0] - ratio[1] # 2
    numerator = A*ratio[1] - B*ratio[0] # 
    return numerator/denominator

print(f"내분점 좌표 ({internal_division(A_[0], B_[0], ratio)}, {internal_division(A_[1], B_[1], ratio)})")
print(f"외분점 좌표 ({external_division(A_[0], B_[0], ratio)}, {external_division(A_[1], B_[1], ratio)})")
