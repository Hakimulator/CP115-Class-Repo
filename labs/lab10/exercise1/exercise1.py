num_rounds = int(input())
final_score=0
for rounds_processed in range(1,num_rounds+1):
    round_score=int(input())
    if round_score > 100:
        final_score+=(round_score*1.2)
    else:
        final_score+=round_score
    
print(f"{final_score:.1f}")
print(rounds_processed)
