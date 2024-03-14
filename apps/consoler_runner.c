#include <stdio.h>	
#include <stdlib.h>	
#include <string.h>	
#include <stdint.h>	
#include <sys/types.h>	
#include <unistd.h>	
#include <fcntl.h>	
#include <sys/ioctl.h>	
#include <errno.h>	
#include <omp.h>

extern float max_pts(float a, float b);

#define MAX_THREADS 2

#define CONSOLE_SECTION 0
#define BOOT_SECTION 1

#define MENU_PY "python3 menu.py"
#define BOOT_PY "python3 boot.py"

#define HEX_0 0xFFFFFFC0
#define HEX_1 0xFFFFFFF9
#define HEX_2 0xFFFFFFA4
#define HEX_3 0xFFFFFFB0
#define HEX_4 0xFFFFFF99
#define HEX_5 0xFFFFFF92
#define HEX_6 0xFFFFFF82
#define HEX_7 0xFFFFFFF8
#define HEX_8 0xFFFFFF80
#define HEX_9 0xFFFFFF90
#define HEX_A 0xFFFFFF88
#define HEX_B 0xFFFFFF83
#define HEX_C 0xFFFFFFC6
#define HEX_D 0xFFFFFFA1
#define HEX_E 0xFFFFFF86
#define HEX_F 0xFFFFFF8E

#define RD_SWITCHES   24929
#define RD_PBUTTONS   24930
#define WR_L_DISPLAY  24931
#define WR_R_DISPLAY  24932
#define WR_RED_LEDS   24933
#define WR_GREEN_LEDS 24934

int main(int argc, char** argv){

    int fd, retval;

	if (argc < 2) {
		printf("Syntax: %s <device file path>\n", argv[0]);
		return -EINVAL;
	}

	if ((fd = open(argv[1], O_RDWR)) < 0) {
		fprintf(stderr, "Error opening file %s\n", argv[1]);
		return -EBUSY;
	}

    printf("* INIT CONSOLE *\n");

    #pragma omp parallel num_threads(MAX_THREADS) 
    {   
        switch (omp_get_thread_num()) {
            
            case CONSOLE_SECTION:

                char player[100];
                int pts;
                float ans = -1;

                FILE *file = fopen("score.csv", "r");

                while (!feof(file)) {
                    if (fscanf(file, "%[^;];%d\n", player, &pts) == 2) {
                        ans = max_pts(ans, pts);
                    }
                }

                fclose(file);
                
                unsigned int data = (unsigned int) ans;

                ioctl(fd, WR_R_DISPLAY);
                retval = write(fd, &data, sizeof(data));
                printf("wrote %d bytes\n", retval);

                break;
            
            case BOOT_SECTION:
                
                printf("\n* loading boot...\n");
                system(BOOT_PY);
                
                printf("\n* loading application...\n");
                system(MENU_PY);
                
                break;
        }

        
    }

    return 0;
}