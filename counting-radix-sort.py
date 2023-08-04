__author__ = "Klarissa Jutivannadevi"
__student_id__ = "32266014"

# counting sort for alphabet (for each team)
def counting_sort_alpha(character, roster):
    """
    source: counting sort pseudocode in notes.pdf and modification from myself
    to allow sorting by alphabet
    This is a counting sort function to sort the group alphabetical name to
    lexicographical order. The approach used is to create a counter and position
    and changing each alphabet to an ASCII value in order to be able to locate
    each alphabet to the counter. The sorted alphabet will be temporarily stored
    in the array and then each letter is concatenated to form back the team name.
    :Input:
        :param character: the string of a single team
        :param roster: the alphabet sets it can contain
    :return: the lexicographical string of the input team
    :Time complexity: O(M) where M is the length of characters within a team and roster
    is considered as a constant
    :Aux space complexity: O(M) where M is the temp array created to temporarily store
    the sorted list for each iteration
    """
    counter = [0] * roster          # ASC: O(1) where roster is the range
    position = [0] * roster         # ASC: O(1) where roster is the range

    # calculating counter
    for i in character:                     # TC: O(M) where M is the len(character)
        counter[ord(i) - 65] += 1

    # calculating position
    for v in range(1, len(counter)):        # O(1) where length of counter is based on the roster
        position[v] = counter[v - 1] + position[v - 1]

    temp = [0] * len(character)

    for j in range(len(character)):        # O(M) where M is the length of the character
        temp[position[ord(character[j]) - 65]] = character[j]
        position[ord(character[j]) - 65] += 1

    character = "".join(temp)         # TC: O(M) where M is the length of temp (the same as the original string length)

    return character

# counting sort for score (descending order)
def counting_sort_score(lst):
    """
    source: counting sort pseudocode in notes.pdf and some modification to allow sorting
    in a decreasing order
    This counting sort method is used to sort each team's score in a decreasing order.
    In this case, instead of inserting value as index, "100-score" is used to store the
    value in the opposite end of the usual counter. This will eventually give a result
    of reversed sorted number, which is what we want.
    :Input:
        :param lst: The list of the results (N)
        :return: The results with the score sorted in a decreasing order
    :Time complexity: O(N) where 2N is the length of the results inserted and the length
    101 is constant.
    :Aux space complexity: O(N) where a temporary list with size 2N is created to store the
    sorted score based on the length of the result
    """
    counter = [0] * 101       # ASC: O(1) where 101 is constant for inclusive 0-100
    position = [0] * 101      # ASC: O(1) where 101 is constant for inclusive 0-100

    # calculating counter
    for i in range(len(lst)):       # TC: O(N) where N is the length of result to be put on counter list
        counter[100-lst[i][2]] += 1

    # calculating position
    for v in range(1, len(counter)):        # TC: O(1) where the length of counter is constant (to be put on position)
        position[v] = counter[v-1] + position[v-1]

    temp = [0] * len(lst)           # ASC: O(N) where N is the len(results) to hold the sorted score temporarily

    for j in range(len(lst)):           # TC: O(N) where N is the len(results) and is iterated to be sorted to position
        temp[position[100-lst[j][2]]] = lst[j]      # set the current value to the allocated temporary list
        position[100-lst[j][2]] += 1

    lst = temp
    return lst

# radix sort for sorting all the groups based on alphabetical order (from the main list)
def radix_pass(arr, digit, team, roster):
    """
    The radix_pass method is a helper function of the radix_sort method where it will
    be called recursively. This method works similarly like a counting sort, but it
    contains more parameter to adapt to the string (since radix sort is used when a
    greater comparison is needed). This method will sort the position of the result list
    to the entire teams' alphabetical order.
    :Input:
        :param arr: The results list where it contains the entire team name
        :param digit: the digit/index at which the team alphabet's is currently being sorted
        :param team: the team that is sorted (team1 or team2)
        :param roster: the sets of alphabet that can be contained in every team's name
    :return: The sorted results list of the alphabet based on the digit it is at
    :Time complexity: O(N) where 2N is the length of results and is iterated once multiple
    times (first is to find the count and second is to put to a sorted list) and the constant
    roster
    :Aux space complexity: O(N) where a temporary list is created to hold the newly sorted
    teams
    """
    counter = [0] * roster              # ASC: O(1) for roster constant
    for i in range(len(arr)):           # TC: O(N) complexity where N is the length of the length of results
        counter[ord(arr[i][team][digit]) - 65] += 1

    position = [0] * roster             # ASC: O(1) for roster constant

    for v in range(1, len(counter)):  # TC: O(1) where it iterates the counter list (which length is a constant roster)
        position[v] = counter[v - 1] + position[v - 1]

    temp = [0] * len(arr)           # ASC: O(N) where N is the length of the results

    for i in range(len(arr)):       # TC: O(N) where it iterates the results to get the position of the sorted alphabet
        location = ord(arr[i][team][digit]) - 65
        temp[position[location]] = arr[i]
        position[location] += 1

    arr = temp
    return arr


# Method to do Radix Sort
def radix_sort(arr, digit, team, roster):
    """
    source: based on the pseudocode in the notes.pdf + adjustment made by myself for
    simplicity in coding this particular method
    The radix_sort method is a function that simply works to find the digit and the
    rest of the sorting will be done by another method (which is radix_pass). This
    function focuses on the digit of each letter from the team name and will iterate
    it once the previous letter has been sorted. Since it is alphabetical, I
    instead just iterate through the index of the string instead of using base 26,
    since using base 26 will take an extra step on converting to number and converting
    back to string.
    :Input:
        :param arr: The results that was the input from analyze method
        :param digit: The length of the team's name
        :param team: The team number (team1 or team2)
        :param roster: The sets of alphabet that the team name can contain from
    :return: The final sorted array after the all the digits has been sorted
    :Time complexity: O(NM). O(M) complexity comes from the for loop in the radix
    sort method that iterates through the digit (having a length of M) and it is nested
    to a radix_pass function which has a complexity of O(N) where N is the length of the
    results and is sorted.
    :Aux space complexity: O(NM). O(M) comes from the recursive call in the for loop for
    the digits (length of each team) and O(N) comes from the radix_pass function which has
    an auxiliary space complexity of O(N)
    """
    for i in range(digit - 1, -1, -1):          # TC: O(M) where M is the length of each team name and ASC: O(M) for recursive call on radix_pass
        arr = radix_pass(arr, i, team, roster)  # ASC: O(N) since radix_pass has an auxiliary space complexity of O(N)
    return arr

# Method to remove duplicates
def remove_duplicates(lst):
    """
    source: the pseudocode on Tutorial Week 3 Question 6
    The approach of this method is similar to Tutorial 3 Question 6. The element on loop will check
    whether it is the same to the previous one, and if it is, it will skip and counter stays the same.
    At the end of the iteration, the list in front are the ones that has been replaced to the next
    number in case there are duplicates. And the rest of the list are just some unused value that can
    be pop.
    :Input:
        :param lst:  The sorted results list based on the score, team1, and team2
    :return: It will return the results list where the duplicates are now removed
    :Time complexity: O(N) where iteration on results happen to check any duplicate and
    another used to pop
    :Aux space complexity: O(1) since it does not consume any extra space. It simply
    modifies the current list.
    """
    j = 0
    # TC: O(N) where N is length of list and if element is the same as previous element, j count will be added
    # to be removed later on. And also, if
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            lst[j+1] = lst[i]
            j = j + 1
    for k in range(len(lst)-(j+1)):         # TC: O(N) where the lst will be pop until it reaches the value N-(j+1)
        lst.pop()
    return lst

# to search for the closest number based on the score input in analyze
def binary_search(lst, target):
    """
    source: MCD4710 notes on Binary Search + modification on return value
    The binary search is simply used to check whether target exist or not. In
    this binary search, it does not matter whether the target is found or not.
    If it is found, they will return the index where the target is first found.
    If this is not the case, the function will return the last middle where they
    checked before start > end.
    :Input:
        :param lst: The result list where it contains team1, team2, score
        :param target: The score intended to be found
    :return: The mid (an index where it contains target or is the closest value to target)
    :Time complexity: O(logN) where the results are always halved in order to search
    for the target
    :Aux space complexity: O(1) since only new variables containing integer are involved
    """
    start = 0
    end = len(lst)-1
    mid = 0

    while start <= end:
        mid = (end+start)//2
        if target == lst[mid][2]:           # return the mid immediately once target == score
            return mid
        elif target > lst[mid][2]:          # if target > score, the end should be moved forward (since scores are in decreasing order)
            end = mid - 1
        elif target < lst[mid][2]:          # if target < score, the start should be moved to after mid (since scores are in decreasing order)
            start = mid + 1
    return mid

# main
def analyze(results, roster, score):
    """
    The analyze method is the main method where it will compute the input to give the desired
    output (By order of score, then team1, then team2, removing the duplicates, displaying
    the top 10 results, and finding searched results where score <= to the result in the
    results array). This method has not much logic since the rest of the logic has been
    implemented in different methods. Hence, this method is used to call the other
    functions. For sorting, since it is stable, we can start from team2, then team1, and
    lastly score.
    :Input:
        :param results: The results list that is given
        :param roster: The sets of an alphabet that the team name should be within
        :param score: The "target" to find an equal score or nearest higher score
    :return: The [top10searches, searchedmatches] based on the output shown on the
    assignment pdf
    :Time complexity: O(NM). Highest complexity from radix_sort method and the looping
    of counting_sort_alpha to sort each team's name
    :Aux space complexity: O(NM). Highest complexity taken from the radix_sort method
    and the for loop of counting_sort_alpha
    """
    # Collect all possible results (including team2, team1 as the new "team1, team2")
    for i in range(len(results)):           # TC: O(N) where the (results list x 2) to find all possible team and score
        results.append([results[i][1], results[i][0], (100 - results[i][2])])

# Next step is to arrange the alphabet of each group
    # the entire time complexity is O(NM) and space complexity is O(NM)
    for i in range(len(results)):           # TC: O(N) for iteration in results to find every team1 and team2
        results[i][0] = counting_sort_alpha(results[i][0], roster)  # complexity is based on the counting_sort_alpha method
        results[i][1] = counting_sort_alpha(results[i][1], roster)  # complexity is based on the counting_sort_alpha method

# Next step is to use radix sort to sort the team alphabetical
    # auxiliary space and time complexity is the same as the method radix_sort. ASC: O(NM), TC: O(NM)
    # no extra auxiliary space in this case since in this part, no new list is created and instead
    # the returned results is overwritten to the previous results array
    results = radix_sort(results, len(results[0][1]), 1, roster)
    results = radix_sort(results, len(results[0][0]), 0, roster)

# Next step is to sort every team in lexicographical order (this only require counting sort)
    # auxiliary space and time complexity is the same as the method counting_sort_score where both is O(N)
    results = counting_sort_score(results)

# Next step is to check any duplicates (use swapping method)
    # ASC: O(1) and TC: O(N), same as the method called
    remove_duplicates(results)

# Next step is to select 10
    # Finding top10matches has an overall complexity of O(1) since top10matches are constant
    top10matches = []               # ASC: O(1) since the top10matches will always top on 10 results, which is constant
    if len(results) > 10:
        for i in range(10):         # TC: O(1) iteration only goes 10 times every time, hence it is constant
            top10matches.append(results[i])
    else:
        top10matches = results

# Next step is to find the closest score
    # Overall time complexity is O(N) where N is results. This is done since the input with same score needs to be
    # searched and appended to the searchedmatches, to be displayed.
    # Aux space complexity will also be O(N) since searchedmatches array can contain as many list depending to the
    # matches
    searchedmatches = []        # ASC: O(N) where score matches will be appended

    current_match = results[binary_search(results, score)][2]       # get the current match score from binary search

    # since score might not exist in result, binary_search might return the closest index to target score (this can be
    # lower or higher). Hence, the condition checks for lower score, then index-1 will guarantee a higher score.
    # if score is higher than the highest result available, it will definitely return an empty list of searchedmatches
    if score > results[0][2]:       # condition in which score target is greater than the highest score available in results
        return [top10matches, searchedmatches]      # return [top10matches, []]
    elif current_match < score:         # when current_match is lower, go back 1 index and it will definitely be higher
        current_match = results[binary_search(results, score) - 1][2]


    # TC: O(N) where it iterates to results and append value if is the same as the current_match that hold value.
    # iteration will stop once the results[score] < current_match (which is the score closest to target score)
    for i in range(len(results)):
        if results[i][2] > current_match:
            continue
        elif results[i][2] == current_match:
            searchedmatches.append(results[i])
        elif results[i][2] < current_match:
            break
    return [top10matches, searchedmatches]


# if __name__ == '__main__':
#     list_b = [['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42], ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
# ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
# ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
# ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
# ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
# ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]
#
#     list_c = [['ACABE', 'AAEAB', 20], ['AADEE', 'BBABC', 74], ['ABCDE', 'ACCEC', 90], ['BCDBC', 'CCCCC', 62], ['BCCBA', 'ABCDB', 53],
#               ['BABEC', 'CABEA', 10],
#               ['CECEE', 'ABDBC', 23], ['BDEDD', 'DEABD', 42]]
#
#     list_d = [['A', 'A', 50]]
#
#     list_e = [['ABCD', 'ABCE', 50]]
#
#     list_f = [['ABAABBA', 'BBBBBBA', 49]]
#
#     list_g = [['A', 'B', 49], ['J', 'B', 51]]
#
#
#
#     print(analyze(list_b, 2, 64))
#     print("\n")
#     print(analyze(list_c, 5, 30))
#     print("\n")
#     print(analyze(list_d, 7, 100))
#     print("\n")
#     print(analyze(list_e, 5, 10))
#     print("\n")
#     print(analyze(list_f, 2, 52))
#     print("\n")
#     print(analyze(list_g, 10, 51))
