def minimum_deletions(s: str) -> int:
    """This function will return the minimum of deletions to make the string"""
    """good. """
    # STEP 1: counting the frequency of the characters and store that in a hash.
    # Of course, we can use Counter() in collections, but I prefer do that
    # by my self (I'm learning), at least for the first approach.
    character_counter = {}
    for ch in s:
        if ch in character_counter:
            character_counter[ch] = character_counter[ch] + 1
        else:
            character_counter[ch] = 1
    # Time complexity O(n) withe n the length of the string.
    # We iterate through the string to count the frequency of
    # each character.
    # Space complexity: O(26) = O(1). We are storing in a hash.
    # But that hash has in the worst case 26 the number of
    # character in English.

    # STEP 2: store the frequency of each character in a list.
    frequency = list(character_counter.values())
    # Time complexity and space complexity both are O(26) = O(1).
    # We have only 26 item in the hash character_counter in the
    # worst case.

    # STEP 3: initializing a set that will store the items that will be
    # treated in the step 4 below.
    # We initialize also "res" that will be returned by this function.
    set_frequencies = set()
    res = 0
    # O(1) + O(1) time complexity and space complexity.

    # STEP 4: using a for loop that iterate through the frequency list
    # and see if it's in the set of frequencies or not. If it is, that means
    # a repeated frequency. We must delete a character (subtracting 1 from
    # this frequency and keeping subtracting until we found a value that
    # not exist in the frequency set or we reach 0: deleting all this character
    # in this case).
    for num in frequency:
        while num in set_frequencies:
            num = num - 1
            res = res + 1
        else:
            if num != 0:
                set_frequencies.add(num)
    # Time complexity: looping through the frequency O(26)
    # The nested loop O(26) in the worst case. That means O(26 * 26 * 2)
    # 2 is the maximum number of operation in the while loop.
    # Searching item in the set O(26). That means O(26 * 26 * 2 * 26)
    # in the worst case. In fin O(1)
    # Space complexity O(1), we don't use any extra space in that step.
    return res

    ### Time complexity: O(n) + O(26) + O(1) + O(1) + O(26 * 26 * 2 * 26) = O(n)
    ### Space complexity: O(26) + O(26) + O(1) + O(1) = O(1)

### Testing the code
s1 = "aab"
s2 = "aaabbbc"
s3 = "ceabaacb"
s4 = "abcabc"
s = {s1, s2, s3, s4}
for item in s:
    print(minimum_deletions(item))
    print("----------------------")
