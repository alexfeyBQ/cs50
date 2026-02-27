#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

void grade(string text);

int main(void)
{
    string text = get_string("Text: ");
    grade(text);
}

void grade(string text)
{
    int words = 0;
    int letters = 0;
    int sentences = 0;

    if (strlen(text) > 0) words++;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }

        if (text[i] == ' ')
        {
            words++;
        }

        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }

    float L = (float)letters / words * 100; // Average number of letters per 100 words
    float S = (float)sentences / words * 100; // Average number of sentences per 100 words

    float index = 0.0588 * L - 0.296 * S - 15.8; // Coleman-Liau index
    int grade_level = (int)round(index);

    if (grade_level < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade_level > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        switch (grade_level)
        {
            case 1: printf("Grade 1\n"); break;
            case 2: printf("Grade 2\n"); break;
            case 3: printf("Grade 3\n"); break;
            case 4: printf("Grade 4\n"); break;
            case 5: printf("Grade 5\n"); break;
            case 6: printf("Grade 6\n"); break;
            case 7: printf("Grade 7\n"); break;
            case 8: printf("Grade 8\n"); break;
            case 9: printf("Grade 9\n"); break;
            case 10: printf("Grade 10\n"); break;
            case 11: printf("Grade 11\n"); break;
            case 12: printf("Grade 12\n"); break;
            case 13: printf("Grade 13\n"); break;
            case 14: printf("Grade 14\n"); break;
            case 15: printf("Grade 15\n"); break;
            case 16: printf("Grade 16\n"); break;
        }
    }
}
