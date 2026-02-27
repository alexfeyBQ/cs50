#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Prototype
int calculate_score(string answer);

// Array containing the point values of each letter in the alphabet
int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(void)
{
    // User input
    string answer1 = get_string("Player1: ");
    string answer2 = get_string("Player2: ");

    // Calculate score of both players
    int score1 = calculate_score(answer1);
    int score2 = calculate_score(answer2);

    // Print result
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

// Function to calculate score
int calculate_score(string answer)
{
    int score = 0;
    int length = strlen(answer);

    // Loop to calculate score for each char
    for (int i = 0; i < length; i++)
    {
        if (islower(answer[i])) // Case char is a not capital letter
        {
            score += points[answer[i] - 'a'];
        }
        else if (isupper(answer[i])) // Case char is a not capital letter
        {
            score += points[answer[i] - 'A'];
        }
    }

    return score;
}
