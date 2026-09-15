class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        int[] alphabet = new int[26];
        List<List<String>> result = new ArrayList<>();
        List<String> firstStrings = new ArrayList<>();
        HashMap<String, String> map = new HashMap<>();
        for(int i = 0; i<strs.length;i++){
            for(int j=0; j < strs[i].length();j++){
                alphabet[strs[i].charAt(j)-'a']+=1;
            }
            System.out.println(java.util.Arrays.toString(alphabet));
            if(map.containsKey(java.util.Arrays.toString(alphabet)) == false){
                
                firstStrings.add(strs[i]);
                List<String> temp = new ArrayList<>();
                temp.add(strs[i]);
                result.add(temp);
                map.put(java.util.Arrays.toString(alphabet), strs[i]);
            } else {
                
                int index = firstStrings.indexOf(map.get(java.util.Arrays.toString(alphabet)));
                result.get(index).add(strs[i]);
            }
            alphabet = new int[26];
        }
        return result;
    }
}
