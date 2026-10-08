#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_VALUES 400000
#define MIN_VALUE 1
#define MAX_VALUE 500000

int main() {
    FILE *file = fopen("data/data.txt", "w");

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    srand(time(NULL));

    for (int i = 0; i < NUM_VALUES; i++) {
        int value = MIN_VALUE + rand() % (MAX_VALUE - MIN_VALUE + 1);
        fprintf(file, "%d\n", value);
    }

    fclose(file);

    printf("Generated %d random values.\n", NUM_VALUES);
    printf("Value range: %d to %d\n", MIN_VALUE, MAX_VALUE);

    return 0;
}
