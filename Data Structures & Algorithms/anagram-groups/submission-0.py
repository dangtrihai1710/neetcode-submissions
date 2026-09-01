

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Tạo bảng băm với giá trị mặc định là một List rỗng []
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sắp xếp các chữ cái của từ rồi ghép lại thành chuỗi (ví dụ: "cat" -> "act")
            sorted_s = "".join(sorted(s))
            
            # Thêm từ gốc vào nhóm có Key là sorted_s
            anagram_map[sorted_s].append(s)
            
        # Lấy tất cả các nhóm (values) ép thành mảng 2 chiều
        return list(anagram_map.values())