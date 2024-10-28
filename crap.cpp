#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstring>

using namespace std;

int FUN_004015cf(unsigned char param_1, char param_2, unsigned char param_3) {
    char local_1c;
    int local_8 = 1;

    // Loop until local_1c is '\0'
    for (local_1c = param_2; local_1c != '\0'; local_1c--) {
        local_8 = (static_cast<int>(param_1) * local_8) % static_cast<int>(param_3);
    }

    return local_8;
}

void FUN_004015a5(void) {
    puts("fail");
    //system("pause");
    exit(0);
}

int main() {
    std::byte local_5c[50]; // Password input
    std::byte local_8e[50]; // Encrypted output
    char local_f2[100];     // Hexadecimal representation
    uint32_t local_14;
    uint uVar2;
    size_t sVar5;
    int iVar6;
    std::byte local_2a;
    std::byte local_29;
    std::byte local_1d;
    std::byte local_1e;
    unsigned char bVar1;

    local_1d = static_cast<std::byte>(0xfb);
    local_1e = static_cast<std::byte>(0x81);
    const char *local_24 = "Th4t's a P455W0rD"; // Key for XOR
    const char *local_28 = "113e5c6eac71358d3a4727639f55f02457565ae57662a2a2727610d84646"; // Expected hash

    puts("Please enter the password:");
    fgets(reinterpret_cast<char *>(local_5c), sizeof(local_5c), stdin);
    printf("Value of local_5c: %s", local_5c);

    local_14 = 0;

    while (true) {
        sVar5 = strlen(reinterpret_cast<char *>(local_5c));
        if (sVar5 - 1 <= local_14) break;

        // Check for non-printable ASCII characters
        if ((static_cast<unsigned char>(local_5c[local_14]) < 0x20) || 
            (0x7e < static_cast<unsigned char>(local_5c[local_14]))) {
            printf("Value of local_5c array: %d\n", static_cast<unsigned char>(local_5c[local_14]));
            puts("ASCII please");
            //system("pause");
            exit(1);
        }
        
        local_14++;
    }

    local_14 = 0;    
    while (true) {
        sVar5 = strlen(reinterpret_cast<char *>(local_5c));
        if (sVar5 - 1 <= local_14) break;

        local_29 = local_5c[local_14];
        iVar6 = FUN_004015cf(static_cast<unsigned char>(local_1e), 
                              static_cast<char>(local_29), 
                              static_cast<unsigned char>(local_1d));
        local_2a = static_cast<std::byte>(iVar6);
        local_8e[local_14] = local_2a;

        local_14++;
    }

    local_14 = 0;
    while (true) {
        sVar5 = strlen(reinterpret_cast<char *>(local_5c));
        uVar2 = local_14;
        if (sVar5 - 1 <= local_14) break;
        bVar1 = static_cast<unsigned char>(local_8e[local_14]);
        sVar5 = strlen(local_24);
        local_8e[local_14] = static_cast<std::byte>(bVar1 ^ static_cast<unsigned char>(local_24[uVar2 % sVar5]));
        sprintf(local_f2 + local_14 * 2, "%02x", static_cast<unsigned int>(local_8e[local_14]));
        local_14++;
    }

    iVar6 = strcmp(local_f2, local_28);
    printf("%s\n", local_f2);
    if (iVar6 != 0) {
        FUN_004015a5();
    }
    puts("well done");
    //system("pause");

    return 0;
}
