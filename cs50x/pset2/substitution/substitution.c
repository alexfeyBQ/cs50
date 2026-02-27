#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Helper Functions Prototypes
string encrypt(string plaintext, string key);
void args_validity(int argc, string argv[]);
int check_error(string key);
string error_message(int ErrorCode);

// Main Function
int main(int argc, string argv[])
{
    args_validity(argc, argv);
    string plaintext = get_string("plaintext: ");
    string ciphertext = encrypt(plaintext, argv[1]);
    printf("ciphertext: %s\n", ciphertext);
}

// Helper Functions
// Encrypt Function using a substitution key
string encrypt(string plaintext, string key)
{
    // Get the length of the plaintext
    int length = strlen(plaintext);

    // Allocate memory for ciphertext depending on plaintext's length
    string ciphertext = malloc(length + 1);

    // Loop over each character of plaintext
    for (int i = 0; i < length; i++)
    {
        if (isupper(plaintext[i])) // Check if character is uppercase
        {
            int letter = plaintext[i] - 'A';
            ciphertext[i] = toupper(key[letter]); // Substitute with uppercase key letter
        }
        else if (islower(plaintext[i])) // Check if character is lowercase
        {
            int letter = plaintext[i] - 'a';
            ciphertext[i] = tolower(key[letter]); // Substitute with lowercase key letter
        }
        else
        {
            ciphertext[i] = plaintext[i]; // Otherwise, keep unchanged for non-alphanbetic
        }
    }
    ciphertext[length] = '\0'; // String end

    return ciphertext;
}

// Check Validity
void args_validity(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        exit(1); // Exit if not 2 argument (file, key)
    }

    int error = check_error(argv[1]); // Assign ErrorCode with check_error()
    if (error != 0)
    {
        printf("%s\n", error_message(error));
        exit(1); // Print Message related to ErrorCode and Exit
    }
}

// Check errors in the key and return an int we will call error_code
int check_error(string key)
{
    int length = strlen(key);

    if (length != 26)
        return 1; // ErrorCode = 1: key length must be 26

    for (int i = 0; i < length; i++)
    {
        if (!isalpha(key[i]))
        {
            return 2; // ErrorCode = 2: key must be alphanumeric only
        }

        for (int j = i + 1; j < length; j++)
        {
            if (toupper(key[i]) == toupper(key[j])) // Normalize letters in the key
            {
                return 3; // ErrorCode = 3: key must not contain any repetition of char
            }
        }
    }

    return 0; // No Error
}

// Assign int error_code from CheckError() function to a string Message
string error_message(int error_code)
{
    switch (error_code)
    {
        case 1:
            return "Key must contain 26 characters.";
        case 2:
            return "Key must only contain alphabetic characters.";
        case 3:
            return "Key must not contain repeated characters.";
        default:
            return "Unknown error.";
    }
}
