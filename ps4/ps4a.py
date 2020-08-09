# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    sequence_list = list(sequence)
    if len(sequence) == 0:
        print('empty sequence')
        
    if len(sequence) == 1:
        return sequence_list

    if len(sequence_list) > 1:
        sequence0 = ''.join(sequence_list[0])
        sequence_leftover_list = sequence_list[1:len(sequence_list)]
        sequence_leftover = ''.join(sequence_leftover_list)
        last = get_permutations(sequence_leftover)
        final_list = []
        for i in range(len(last)):
            list_new = []
            for j in range(len(sequence)):
                list_new.append (last[i][0:j] + sequence0 + last[i][j:len(last[i])])
            final_list += list_new
        return final_list

    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example = {'a':['a'],'ab':['ab','ba'], 'abc':['abc', 'bac', 'bca', 'acb', 'cab', 'cba']}
    for example_input in example.keys():
        print('Input:', example_input)
        print('Expected Output:', example[example_input])
        print('Actual Output:', get_permutations(example_input))
