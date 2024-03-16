# Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

## Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

## Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

## Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
## Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

## Solution
Firstly I iterate over the string. Then I check if the character has already been seen in the string and if its index is greater or equal to current start index. If both of these conditions are true, it means, that the character is repeating, and update start index to index after the last occurance of this character. If this condition isn't satisfied I check if the current substring from start to end is longer than previous longest substring. If it is, I update the length of the longest substring and index, where it started. Finally I return the longest substring using slice of the string like [start_index_of_the_longest_substring:start_index_of_the_longest_substring + length_of_the_longest_substring]