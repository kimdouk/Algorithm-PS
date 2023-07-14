scores = [int(input()) for _ in range(10)]
sum_scores = [0]
mx = 100
result = 0
for score in scores:
    sum_scores.append(sum_scores[-1]+score)
for sum_score in sum_scores:
    if mx>=abs(100-sum_score):
        mx = abs(100-sum_score)
        result = sum_score
print(result)