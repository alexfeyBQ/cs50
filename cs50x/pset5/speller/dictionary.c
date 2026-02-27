// Implements a dictionary's functionality

#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Word counter
unsigned int counter = 0;

// Hash table
node *table[N];

// Prototype
float frequency(int letter);

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    node *cursor = table[index];

    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int firstlet;
    int letter;
    float weight;
    float sum = 0.0f;
    int len = strlen(word);

    firstlet = toupper(word[0]) - 'A';
    for (int i = 1; i < len; i++)
    {
        letter = toupper(word[i]) - 'A';
        if (letter < 0 || letter > 25)
            continue;
        weight = log(1.0f / frequency(letter));
        sum += weight * (len - i);
    }
    float h = firstlet * frequency(firstlet) * 100 + sum + (sum / len);
    int hash = ((int) (h * 100)) % N;

    return hash;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *source = fopen(dictionary, "r");

    if (source == NULL)
    {
        return false;
    }

    char word[LENGTH + 1];

    while (fscanf(source, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(source);
            unload();
            return false;
        }

        strcpy(n->word, word);
        int index = hash(word);
        n->next = table[index];
        table[index] = n;
        counter++;
    }

    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;    // garder le pointeur pour libérer
            cursor = cursor->next; // avancer dans la liste
            free(tmp);             // libérer la mémoire du node
        }
        table[i] = NULL; // facultatif, bonne pratique
    }

    return true;
}

// Assign english letter frequency to each letter
// source: https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
float frequency(int letter)
{
    switch (letter)
    {
        case 0:
            return 0.0812f; // A
        case 1:
            return 0.0149f; // B
        case 2:
            return 0.0271f; // C
        case 3:
            return 0.0432f; // D
        case 4:
            return 0.1202f; // E
        case 5:
            return 0.0230f; // F
        case 6:
            return 0.0203f; // G
        case 7:
            return 0.0592f; // H
        case 8:
            return 0.0731f; // I
        case 9:
            return 0.0010f; // J
        case 10:
            return 0.0069f; // K
        case 11:
            return 0.0398f; // L
        case 12:
            return 0.0261f; // M
        case 13:
            return 0.0695f; // N
        case 14:
            return 0.0768f; // O
        case 15:
            return 0.0182f; // P
        case 16:
            return 0.0011f; // Q
        case 17:
            return 0.0602f; // R
        case 18:
            return 0.0628f; // S
        case 19:
            return 0.0910f; // T
        case 20:
            return 0.0288f; // U
        case 21:
            return 0.0111f; // V
        case 22:
            return 0.0209f; // W
        case 23:
            return 0.0017f; // X
        case 24:
            return 0.0211f; // Y
        case 25:
            return 0.0007f; // Z
        default:
            return 0.0f;
    }
}
