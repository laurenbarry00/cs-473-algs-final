# CS 473 Final Project: String Matching
By: Lauren Barry and Allysa Sewell

This final project is for CS 473 Advanced Algorithms Design and Analysis. It examines various string matching algorithms.

## Algorithms Implemented:
- Horspool 
- Rabin-Karp 
- Knuth-Morris-Pratt 
- Boyer-Moore

## Example Brute-Force Algorithm

```java
public class BruteForceMatch {

     public static void main (String[] args){
        // We are searching for the pattern "OOD" within the string "HAVE A GOOD BREAK"
        // Should be found at index 8
        String text = "HAVE A GOOD BREAK";
        String pattern = "OOD";

        System.out.println("Searching for pattern '" + pattern + "' in text '" + text + "'...");
        
        int index = bruteForceMatch(text, pattern);
        System.out.println("Found at index: " + index);
     }
     
     // Basic brute-force string matching algorithm
     static int bruteForceMatch(String text, String pattern) {
         // Shift the pattern over by one character each iteration
         for (int i = 0; i < text.length(); i++) {
            char t = text.charAt(i);
            char p = pattern.charAt(0);
            
            // if the first character in the pattern matches text[i]
            if (t == p) {
                int j = 0;
                // compare the rest of the pattern
                while (i + j < pattern.length()) {
                    if (text.charAt(i + j) != pattern.charAt(i + j)) {
                        // if we get a mismatch, stop and shift the pattern
                        break;
                    }
                    j++;
                }
                // if we get to this point, we've compared the whole pattern
                // and didn't get a mismatch. Return the index
                return i + j;
            }
        }
        // No matches found. 
        return -1;
     }
}
```
