class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in group:
                group[sorted_str].append(str)
            else:
                group[sorted_str] = [str]
        return list(group.values())

        