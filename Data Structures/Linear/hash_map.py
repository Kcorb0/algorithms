# Leet Code Two Sum Example


def twoSum(nums, target):

    # Init the hashmap, use this to store a past occurance of a number

    hashmap = {}

    # Loop through the given array
    # If the target number - current number = a number that already exists in the hashtable
    # Then we return the stored indexs

    for idx, n in enumerate(nums):
        check = target - n

        if check in hashmap.keys():
            return [hashmap[check], idx]

        # Store value and location in array in the hashmap
        else:
            hashmap[n] = idx

    return "There is an error"
