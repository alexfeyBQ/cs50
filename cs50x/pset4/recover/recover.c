#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Constant
const int size = 512;

// Data type
typedef uint8_t BYTE;

// Prototype
int header(BYTE buffer[]);

int main(int argc, char *argv[])
{
    // Single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover filename.jpg\n");
        return 1;
    }

    // Open memory card
    FILE *card = fopen(argv[1], "r");

    if (card == NULL)
    {
        printf("Could not open file %s\n", argv[1]);
        return 1;
    }

    // Variables initialization
    BYTE buffer[size];
    FILE *img = NULL;
    char filename[8];
    int count = 0;

    // Main loop
    // Read the memory card 512 bytes at a time until end of file
    while (fread(buffer, 1, size, card) == size)
    {
        // If block is start of a new JPEG
        if (header(buffer))
        {
            if (img != NULL)
            {
                fclose(img);
            }

            // Generate filename for new JPEG
            sprintf(filename, "%03i.jpg", count);
            img = fopen(filename, "w");

            if (img == NULL)
            {
                printf("Could not create file %s\n", filename);
                fclose(card);
                return 1;
            }

            fwrite(buffer, size, 1, img);
            count++;
        }

        // If inside a JPEG, write the block
        else if (img != NULL)
        {
            fwrite(buffer, size, 1, img);
        }
    }

    // Close files
    if (img != NULL)
    {
        fclose(img);
    }

    fclose(card);
}

// Helper function
int header(BYTE buffer[])
{
    return buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
           (buffer[3] & 0xf0) == 0xe0;
}
