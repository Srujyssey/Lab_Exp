#include <stdio.h>
#include <omp.h>

#define MAX_SIZE 400000

int main() {
    int data[MAX_SIZE];
    int n = 0;

    FILE *file = fopen("data/data.txt", "r");

    if (file == NULL) {
        printf("Error opening data file.\n");
        return 1;
    }

    while (n < MAX_SIZE && fscanf(file, "%d", &data[n]) == 1) {
        n++;
    }

    fclose(file);

    int max = data[0];
    int min = data[0];
 
    double start = omp_get_wtime();
    for (int i = 1; i < n; i++) {
        if (data[i] > max)
            max = data[i];

        if (data[i] < min)
            min = data[i];
    }

    
double end = omp_get_wtime();
    printf("Number of values: %d\n", n);
    printf("Maximum: %d\n", max);
    printf("Minimum: %d\n", min);
    printf("Execution time: %.6f seconds\n", end - start);
    return 0;
}
