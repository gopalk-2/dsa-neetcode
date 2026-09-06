class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target_x, target_y, target_z = target
        found_x = found_y = found_z = False

        for a, b, c in triplets:
            if a > target_x or b > target_y or c > target_z:
                continue
            if a == target_x:
                found_x = True
            if b == target_y:
                found_y = True
            if c == target_z:
                found_z = True
            if found_x and found_y and found_z:
                return True

        return found_x and found_y and found_z


        