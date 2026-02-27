#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? "); // ask for user's name
    printf("hello, %s\n", answer);                    // print message
}
