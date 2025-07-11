// thermal_processing.c
#include <stdint.h>

int process_thermal(uint16_t* data, int rows, int cols) {
    // fake detection logic
    int sum = 0;
    for (int i = 0; i < rows * cols; i++) {
        sum += data[i];
    }

    if (sum > 1000000) {
        return 1; // detected
    }
    return 0; // not detected
}
