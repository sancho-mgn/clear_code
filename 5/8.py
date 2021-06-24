"""было"""
def MassVote(N, Votes):
    sum_votes = round(sum(Votes) * 0.5, 3)
    max_votes = max(Votes)
    cnt_max = Votes.count(max_votes)

    if cnt_max == 1:
        if max_votes > sum_votes:
            return 'majority winner ' + str(Votes.index(max_votes) + 1)
        elif max_votes <= sum_votes:
            return 'minority winner ' + str(Votes.index(max_votes) + 1)
    return 'no winner'


Votes = [5, 10, 10, 15, 60]
N = 3
print(MassVote(N, Votes))

"""стало"""
def MassVote(N, votes_sum):
    sum_votes = round(sum(votes_sum) * 0.5, 3)
    max_votes = max(votes_sum)
    votes_max_of_sum = votes_sum.count(max_votes)

    if votes_max_of_sum == 1:
        if max_votes > sum_votes:
            return 'majority winner ' + str(votes_sum.index(max_votes) + 1)
        elif max_votes <= sum_votes:
            return 'minority winner ' + str(votes_sum.index(max_votes) + 1)
    return 'no winner'


Votes = [5, 10, 10, 15, 60]
N = 3
print(MassVote(N, Votes))