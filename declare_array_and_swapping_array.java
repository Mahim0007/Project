import java.util.Scanner;
public class declare_array_and_swapping_array {
    public static void main(String[] args) {
// printing array and swapping array
        Scanner ab = new Scanner(System.in);
        int [] arr = new int[10];
        int n;
        System.out.print("Enter n: ");
        n = ab.nextInt();
        for(int i=0;i<n;i++){
            System.out.println("arr[" + i +"]: ");
            arr[i] = ab.nextInt();
        }
        for(int i=0;i<n;i++){
            System.out.println(arr[i]);
        }
        System.out.println("Sapping 3 and 4 index: ");
        int temp;
        temp = arr[3];
        arr[3] = arr[4];
        arr[4] = temp;
        for(int i=0;i<n;i++){
            System.out.println("Final swap: "+arr[i]);
        }









    }
}
