import java.util.Scanner;

public class arrary_maximum_and_minimum {
    public static void main(String[] args) {
        Scanner ab = new Scanner(System.in);
        int [] arr = new int[5];
        System.out.println("Enter the number: ");
        for(int i=0;i<5;i++){
            arr[i] = ab.nextInt();
        }
        double max=0; 
        for(int i=0;i<5;i++){
            if(max < arr[i]){
                max=arr[i];
            }
        }
        System.out.println("Maximum number: "+max);
        double min=1;
        for(int i=0;i<5;i++){
            if(min > arr[i]){
                min=arr[i];
            }
        }
        System.out.println("Minimum number: "+min);
    }
}
