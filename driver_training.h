#pragma once
#include <stdlib.h>

#define YOGA    1;
#define FITNESS 2;
#define SPO_PSY 3;
#define PR      4;
#define TECH    5;
#define NINJA   6;
#define SPA     7;

struct driver_data
{
    int concentration;
    int talent;
    int aggressiveness;
    int insight;
    int stamina;
    int charisma;
    int motivation;
};

int manage_driver_data(struct driver_data);