class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        shift = np.array(nums)
        array_new = np.roll(shift, k)
        print(array_new)
