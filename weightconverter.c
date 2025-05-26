/* This is written in C. So it needs to be compiled and run */
#include <stdio.h>
#include <stdlib.h>
int main() {
    int convert;
    float weight;
    while (1) {
        printf("\n _____________________________________________________________\n");
        printf("|                                                             |\n");
        printf("|                     Weight Converter                        |\n");
        printf("|_____________________________________________________________|\n");
        printf("\nOptions:\n");
        printf("1) Kilogram to gram\n");
        printf("2) Gram to kilogram\n");
        printf("3) Pound to kilogram\n");
        printf("4) Kilogram to pound\n");
        printf("5) Gram to pound\n");
        printf("6) Pound to gram\n");
        printf("7) Exit\n");
        printf("Enter an option: ");
        if (scanf("%d", &convert) != 1 || convert < 1 || convert > 7) {
            printf("Invalid option selected. Please try again.\n");
            while (getchar() != '\n'); 
            continue;
        }
        break;
    }
    while (1) {
        if (convert == 7) {
            printf("Exiting the program...\n");
            break;
        }
        printf("Enter weight: ");
        if (scanf("%f", &weight) != 1 || weight < 0) {
            printf("Please enter a valid positive number.\n");
            while (getchar() != '\n');
            continue;
        }
        switch (convert) {
            case 1:
                printf("%.2f kilogram(s) in gram(s) is: %.2f\n", weight, weight * 1000);
                break;
            case 2:
                printf("%.2f gram(s) in kilogram(s) is: %.2f\n", weight, weight / 1000);
                break;
            case 3:
                printf("%.2f pound(s) in kilogram(s) is: %.2f\n", weight, weight * 0.45359237);
                break;
            case 4:
                printf("%.2f kilogram(s) in pound(s) is: %.2f\n", weight, weight * 2.204623);
                break;
            case 5:
                printf("%.2f gram(s) in pound(s) is: %.2f\n", weight, weight * 0.00220462);
                break;
            case 6:
                printf("%.2f pound(s) in gram(s) is: %.2f\n", weight, weight * 453.59237);
                break;
        }
        break;
    }
    return 0;
}
