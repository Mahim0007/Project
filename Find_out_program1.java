public class Find_out_program1 {
    public static void main(String[] args) {
        int[][] arr = new int[4][5];
        int k=0;
        for(int row=0;row<4;row++){
            for(int col=0;col<5;col++){
                arr[row][col] = k;
                k++;
            }
        }
        for(int row=0;row<4;row++){
            for(int col=0;col<5;col++){
                System.out.print("   "+arr[row][col]);
            }
            System.out.println();
        }
    }
}
