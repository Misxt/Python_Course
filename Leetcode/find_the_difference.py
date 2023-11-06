class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = {}
        t_dict = {}
        s_letters = list(s)
        t_letters = list(t)
        for i in range(len(s_letters)):
            if s_letters[i] in s_dict:
                s_dict[s_letters[i]] = s_dict[s_letters[i]] + 1
            else:
                s_dict[s_letters[i]] = 1
            if t_letters[i] in t_dict:
                t_dict[t_letters[i]] = t_dict[t_letters[i]] + 1
            else:
                t_dict[t_letters[i]] = 1
        if t_letters[-1] in t_dict:
            t_dict[t_letters[-1]] = t_dict[t_letters[-1]] + 1
        else:
            t_dict[t_letters[-1]] = 1

        for key in t_dict:
            if key in s_dict:
                if t_dict[key] != s_dict[key]:
                    return key
            else:
                return key