import java.util.Scanner;

public class mattrix_diagonal_and_upperTriangle_and_lowerTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] a = new int[3][3];
        int sumofdiagonalelements=0,sumofuppertriangle=0,sumoflowertriangle=0;
        for(int row = 0; row < 3; row++){
            for(int col = 0; col < 3; col++){
               a[row][col] = sc.nextInt();
            }
        }
        for(int row = 0; row < 3; row++){
            for(int col = 0; col < 3; col++){
                System.out.print("   "+a[row][col]);
            }
            System.out.println();
        }
        for(int row = 0; row < 3; row++){
            for(int col = 0; col < 3; col++){
                if(row==col){
                sumofdiagonalelements = sumofdiagonalelements + a[row][col];
                }
            }
        }
        for(int row = 0; row < 3; row++){
            for(int col = 0; col < 3; col++){
                if(row<col){
                    sumofuppertriangle = sumofuppertriangle + a[row][col];
                }
            }
        }
        for(int row = 0; row < 3; row++){
            for(int col = 0; col < 3; col++){
                if(row>col){
                    sumoflowertriangle = sumoflowertriangle + a[row][col];
                }
            }
        }
        System.out.println("Sum of Diagonal:  "+sumofdiagonalelements);
        System.out.println("Sum of Upper Triangle:  "+sumofuppertriangle);
        System.out.println("Sum of Lower Triangle:  "+sumoflowertriangle);
    }
}
