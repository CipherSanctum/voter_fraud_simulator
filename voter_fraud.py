from random import randint


def add_skewed_votes(total_voters):
    votes_cast = {'trump': 0, 'biden': 0}
    for vote in range(0, total_voters):
        random_number = randint(1,2)
        if random_number == 1:
            votes_cast['trump'] += .75
        else:
            votes_cast['biden'] += 1.25
    return votes_cast


def fix_votes(total_voters, skewed_votes):
    if (skewed_votes['trump'] + skewed_votes['biden']) > total_voters:
        for i in range(0, round(skewed_votes['biden'])):
            if (skewed_votes['trump'] + skewed_votes['biden']) > total_voters:
                skewed_votes['trump'] = round(skewed_votes['trump']) - 1
                skewed_votes['biden'] = round(skewed_votes['biden']) - 1
    if (skewed_votes['trump'] + skewed_votes['biden']) != total_voters:
        skewed_votes['biden'] = round(skewed_votes['biden'])
        skewed_votes['trump'] = round(skewed_votes['trump'])
        total_voters_difference = total_voters - (skewed_votes['biden'] + skewed_votes['trump'])
        skewed_votes['biden'] += total_voters_difference
    return skewed_votes


def vote_fraud_simulator(total_voters):
    skewed_votes = add_skewed_votes(total_voters)

    print('***** SCAM RESULTS BEFORE MAKING IT LOOK REAL *****')
    print('Total voters: {}'.format(total_voters))
    print('Trump votes: {}'.format(skewed_votes['trump']))
    print('Biden votes: {}'.format(skewed_votes['biden']))
    print('Total skewed votes: {}'.format(skewed_votes['trump'] + skewed_votes['biden']))

    print('\n\n\n***** THE FIX IS IN!!! *****')
    fixed_votes = fix_votes(total_voters, skewed_votes)
    print('Trump fixed votes: {}'.format(fixed_votes['trump']))
    print('Biden fixed votes: {}'.format(fixed_votes['biden']))
    print('Total fixed voters: {}\n\n\n'.format(fixed_votes['trump'] + fixed_votes['biden']))


vote_fraud_simulator(10000)
