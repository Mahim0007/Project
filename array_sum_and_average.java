import java.util.Scanner;
public class array_sum_and_average {
    public static void main(String[] args) {
//    int [] arr = new int[5];
//    arr[0]= 20;
//    arr[1]= 40;
//    arr[2]= 60;
//    arr[3]= 80;
//    arr[4]= 100;
//        System.out.println(arr[1]);
//    }
        Scanner ab = new Scanner(System.in);
        int [] arr = new int[5];
        int sum=0;
        System.out.println("Enter 5 numbers: ");
        for(int i=0;i<5;i++){
            arr[i] = ab.nextInt();
        }
        for(int i=0;i<5;i++){
            sum = sum + arr[i];
        }
          double average= sum / 5 ;
        System.out.println("Final result: "+average);
        }






}
