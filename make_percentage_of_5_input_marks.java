import java.util.Scanner;
public class make_percentage_of_5_input_marks
{
    public static void main(String[] args)
    {
        Scanner a = new Scanner(System.in);
        System.out.print("Enter marks 1: ");
        float b = a.nextFloat();
        System.out.print("Enter marks 2: ");
        float c = a.nextFloat();
        System.out.print("Enter marks 3: ");
        float d = a.nextFloat();
        System.out.print("Enter marks 4: ");
        float e= a.nextFloat();
        System.out.print("Enter marks 5: ");
        float f = a.nextFloat();
        float percentage_1 = (b+c+d+e+f)/5;
        float percentage_2 = (percentage_1/500)*100;
        System.out.println("The percentage of marks: "+percentage_2);



    }
}
