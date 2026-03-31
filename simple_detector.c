/*
 * Phoenix Core - Simple C Detector
 * Manual verification with no Python dependencies
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char command[512];
    char photo_path[256] = "capture.jpg";
    int block_count = 0;
    int frame_count = 0;
    char input[10];

    printf("========================================\n");
    printf("Phoenix Core - Simple C Detector\n");
    printf("========================================\n");
    printf("Press ENTER to capture, 'q' to quit\n\n");

    while (1) {
        printf("Capture? ");
        if (!fgets(input, sizeof(input), stdin)) {
            break;
        }

        if (input[0] == 'q' || input[0] == 'Q') {
            break;
        }

        snprintf(command, sizeof(command), "termux-camera-photo %s 2>/dev/null", photo_path);
        system(command);

        snprintf(command, sizeof(command), "test -f %s", photo_path);
        if (system(command) == 0) {
            frame_count++;

            snprintf(command, sizeof(command), "stat -c %%s %s", photo_path);
            FILE *fp = popen(command, "r");
            long size = 0;
            if (fp) {
                fscanf(fp, "%ld", &size);
                pclose(fp);
            }

            printf("  Photo captured (size: %ld bytes)\n", size);
            printf("  Is this explicit? (y/n): ");
            if (!fgets(input, sizeof(input), stdin)) {
                break;
            }

            if (input[0] == 'y' || input[0] == 'Y') {
                block_count++;
                printf("  🔴 BLOCKED\n");
                remove(photo_path);
            } else {
                printf("  🟢 ALLOWED\n");
                remove(photo_path);
            }

            printf("\n  Statistics: %d blocks / %d captures (%.1f%%)\n\n",
                   block_count, frame_count,
                   frame_count > 0 ? ((float)block_count * 100 / frame_count) : 0.0f);
        } else {
            printf("  ERROR: Camera capture failed\n\n");
        }
    }

    printf("\nFinal Statistics:\n");
    printf("  Total captures: %d\n", frame_count);
    printf("  Blocks: %d\n", block_count);
    if (frame_count > 0) {
        printf("  Block rate: %.1f%%\n", (float)block_count * 100 / frame_count);
    }

    return 0;
}
