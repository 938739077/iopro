

class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        number_list = [[], [], [], [], [], [], [], [], [], [], []]
        for i in range(length):
            temp_set = {
                "NO": i,
                "NUM": nums[i],
            }
            flag = nums[i] % 10
            number_list[flag].append(temp_set)
        list_length = len(number_list)
        for i in range(list_length):
            child_length = len(number_list[i])
            for k in range(child_length):
                need_num = target - number_list[i][k]["NUM"]
                find_list_index = need_num % 10
                find_list_length = len(number_list[find_list_index])
                for j in range(find_list_length):
                    if number_list[find_list_index][j]["NO"] != number_list[i][k]["NO"]:
                        if number_list[find_list_index][j]["NUM"] == need_num:
                            if number_list[find_list_index][j]["NO"] > number_list[i][k]["NO"]:
                                return [number_list[i][k]["NO"], number_list[find_list_index][j]["NO"]]
                            else:
                                return [number_list[find_list_index][j]["NO"], number_list[i][k]["NO"]]
        return 0


test_list = [1,2,3,6,5,4,7,8,9,4,5,4,15,145,169,145,7,5,126,54,69,1,25,14,2,4,5,21,4,266,114,199,44,44]
test = Solution()
a = test.twoSum(test_list, 88)
print(a)