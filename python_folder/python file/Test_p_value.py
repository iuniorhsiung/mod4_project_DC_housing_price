# Create a function to detect the hypothesis testing results. 1: reject null, 0: fail to reject null
def test_p_value(p = .05, name = 'ttest'):
    name_list = []
    for i in range(len(test_matrix)):
        if test_matrix["p_" + name][i] < p:
            name_list.append(1) 
        else:
            name_list.append(0)   
    test_matrix['index_' + name] = name_list
