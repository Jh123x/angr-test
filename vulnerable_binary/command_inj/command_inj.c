#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void execute_cmd(char *cmd)
{
    // Execute the command.
    system(cmd);
}

void execute_echo(char *word)
{
    // Execute echo command.
    char *cmd_str = "echo %s";
    char cmd[30];
    sprintf(cmd, cmd_str, word);
    printf("Executing command: \"%s\"\n", cmd);
    execute_cmd(cmd);
}

int main()
{
    // Ask the user for 30 characters of input.
    char buf[30];
    scanf_s("%30s", buf);

    // Execute the echo command with the input.
    printf("Input: %s\n", buf);
    execute_echo(buf);
    return 0;
}