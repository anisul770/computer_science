#gym contest
def main():
    #get valuse form keyboard
    NAMES=[]
    Last_names=[]
    Gender=[]
    Nationality=[]
    Score=[]
    done=True #False
    while not done:
        get_string_from_user(NAMES,'Please, enter a competitor name:')
        get_string_from_user(Last_names,'Please, enter a competitor last name:')
        get_string_from_user(Gender,'Please, enter a competitor gender:')
        get_string_from_user(Nationality,'Please, enter a competitor nationality:')

        new_scores=[]
        for i in range(5):
            value=get_real_value_from_user('Please, enter the score'+str(i+1))
            new_scores.append(value)
        Score.append(new_scores)
        answer= input('are you ok?')
        if answer=='yes':
            done=True
    #precharged data structures to avoid slow user interaction

    NAMES=['Yuri','Veronica','Sabrina','Victoria','Rebecca','Gabbie','Hannah']
    Last_names=['Chechi','Servente','Vega','Komova','Downie','Douglas','Whelan']
    Gender=['M','F','F','F','F','F','F']
    Nationality=['ITA','ITA','USA','RUS','GRB','USA','GRB']
    Score=[[9.3,8.9,9.7,9.7,9.8],
               [9.0,9.0,9.0,9.2,9.5],
               [8.4,8.7,8.5,8.6,9.0],
               [9.3,9.7,9.9,9.9,9.2],
               [8.2,8.9,8.9,8.6,9.3],
               [8.2,8.9,8.9,8.6,9.3],
               [8.0,8.0,8.0,8.0,8.0]]
    Actual_scores=compute_actual_scores(Score)
    #finiding the best female
    first = True
    for i in range(len(Gender)):
        if Gender[i] == 'F':
            if first:
                max_score=Actual_scores[i]
                max_index=i
                first=False
            else:
                if max_score<Actual_scores[i]:
                    max_score=Actual_scores[i]
                    max_index=i
    print('Best female competitor:')
    print(f'{NAMES[max_index]} {Last_names[max_index]}, {Nationality[max_index]} - score:{Actual_scores[max_index]:.1f}')

    #compute countries score
    list_countries=[]
    list_scores=[]
    for i in range(len(Nationality)):
        if Nationality[i] not in  list_countries:
            list_countries.append(Nationality[i])
            list_scores.append(Actual_scores[i])
        else:
            list_scores[list_countries.index(Nationality[i])] += Actual_scores[i]
    new_list_tuples=[]
    for i in range(len(list_countries)):
        new_list_tuples.append((list_scores[i],list_countries[i]))
    new_list_tuples.sort(reverse=True)
    print('Final countries ranking:')
    for i in range(3):
        print(f'{i+1}) {new_list_tuples[i][1]} - score: {new_list_tuples[i][0]:.2f}')
    print(new_list_tuples)
    print(list_countries)
    print(list_scores)

    print(NAMES)
    print(Last_names)
    print(Gender)
    print(Nationality)
    print(Score)
    print(Actual_scores)
def get_string_from_user(list_strings,message):
    input_info=input(message)
    if input_info!='':
        list_strings.append(input_info)
        return True
    else:
        return False
def get_real_value_from_user(message):
    input_info=input(message)
    #check if the input is an real number
    value = float(input_info)
    return value
def compute_actual_scores(Score):
    new_scores=[]
    for i in range(len(Score)):
        tmp_score=sum(Score[i])-max(Score[i])-min(Score[i])
        new_scores.append(tmp_score)
    return new_scores
main()
