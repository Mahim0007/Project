import java.util.Arrays;

public class boro_theke_choto_and_choto_theke_boro {
    public static void main(String[] args) {
        int[]arr={4,-9,3,6,1};
        Arrays.sort(arr);
        System.out.println("Acssending");
        for(int i=0;i<5;i++){
            System.out.println("  "+arr[i]);
        }
        System.out.println("Desceding");
        for(int i=4;i>=0;i--){
            System.out.println("  "+arr[i]);
        }
    }
}
