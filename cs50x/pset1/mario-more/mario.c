#include <cs50.h>
#include <stdio.h>

void print_blank(int n);
void print_hash(int n);

int main(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);

    for (int i = 1; i <= h; i++)
    {
        print_blank(h - i); // print (h - i) of blank
        print_hash(i);      // print i of #
        printf("  ");       // blank space
        print_hash(i);      // print i of #
        printf("\n");
    }
}

void print_blank(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf(" ");
    }
}

void print_hash(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
}
