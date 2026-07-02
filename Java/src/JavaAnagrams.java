import java.util.Scanner;

/// The Core Concept: The "Counting Bucket"
/// Imagine you have 26 physical buckets, each labeled with a letter from 'a' to 'z'.
/// Every time you see a letter in String a, you add a token to that letter's bucket.
/// Every time you see a letter in String b, you take away a token from that letter's bucket.
/// If String a and String b are perfect anagrams, every single bucket must end up
/// completely empty (0 tokens)
/// because the additions and subtractions will perfectly cancel each other out.

public class JavaAnagrams {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }

    static boolean isAnagram(String a, String b){
        //If length are not the same, they can't be anagrams
        if(a.length() != b.length()){
            return false;
        }

        //Convert both string to lowercase to count
        a = a.toLowerCase();
        b = b.toLowerCase();

        int[] frequencies = new int[26];

        for(int i = 0; i < a.length(); i++){
            frequencies[a.charAt(i) - 'a']++;
            frequencies[b.charAt(i) - 'a']--;
        }

        for(int count : frequencies){
            if(count != 0){
                return false;
            }
        }

        return true;
    }
}
