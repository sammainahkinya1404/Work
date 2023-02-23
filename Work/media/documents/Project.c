#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>

void listFilesRecursively(char *basePath, int depth)
{
    char path[1000];
    struct dirent *dp;
    DIR *dir = opendir(basePath);

    if (!dir)
        return;

    while ((dp = readdir(dir)) != NULL)
    {
        if (strcmp(dp->d_name, ".") != 0 && strcmp(dp->d_name, "..") != 0)
        {
            printf("%*s%s\n", depth, "", dp->d_name);

            // Construct new path from our base path
            strcpy(path, basePath);
            strcat(path, "/");
            strcat(path, dp->d_name);

            listFilesRecursively(path, depth + 1);
        }
    }

    closedir(dir);
}

int main(int argc, char* argv[])
{
    char* path;

    if (argc > 1) {
        path = argv[1];
    } else {
        path = ".";
    }

    printf("Directory listing of %s:\n", path);
    listFilesRecursively(path, 0);

    return 0;
}
