class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # Lưu dạng {giá_trị_số: vị_trí_index}
        
        for i, num in enumerate(nums):
            complement = target - num  # Số còn thiếu
            
            # Kiểm tra xem số còn thiếu đã xuất hiện trước đó chưa
            if complement in seen:
                return [seen[complement], i]
            
            # Nếu chưa có, lưu số hiện tại vào sổ
            seen[num] = i