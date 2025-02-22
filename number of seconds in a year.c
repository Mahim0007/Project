#include <stdio.h>

int main()
{

    long long int min, hour_1, hour_2, day_input, hour_3, total_1, total_2;
    printf("Enter the day: ");
    scanf("%lld", &day_input);
    min = 60;
    hour_1 = 60;
    hour_2 = 24;
    hour_3 = 24;
    // total_1=min*hour_1*hour_2;
    total_1 = day_input * hour_3;
    total_2 = total_1 * min * hour_1 * hour_2;
    printf("The second is: %lld", total_2);
    return 0;
}