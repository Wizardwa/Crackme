#!/bin/python3

import os
import string


def fun_004015cf(param_1: int, param_2: int, param_3: int) -> int:
    # Initialize local_8 to 1
    local_8 = 1
    
    # Loop from param_2 down to 1
    for _ in range(param_2):
        local_8 = (param_1 * local_8) % param_3


    #print(f"local_8 value: ",local_8)

    return local_8


local_1d = 0xfb
local_1e = 0x81
local_24 = "Th4t's a P455W0rD"
local_28 = "113e5c6eac71358d3a4727639f55f02457565ae57662a2a2727610d84646"
local_8e = bytearray(50)
local_f2 = bytearray(100)
# target = "0f626f57b1"
# decrypted = "ninja"
target_list = ['11','3e','5c','6e','ac','71','35','8d','3a','47','27','63','9f','55','f0','24','57','56','5a','e5','76','62','a2','a2','72','76','10','d8','46','46']
printable = string.printable
printable_list = []
for i in printable:
    printable_list.append(i)

size_of_ascii = len(printable_list)
local_14 = 0
size_of_target_list = len(target_list)
matched = []
while local_14 < size_of_target_list:

    for i in printable_list[:95]:
        local_5c = i
        local_5c = local_5c.encode("ascii")

        local_29 = ord(local_5c)
        iVar6 = fun_004015cf(local_1e,local_29,local_1d)
        local_2a = iVar6
        local_8e[local_14] = local_2a
         

        uVar2 = local_14
        bVar1 = local_8e[local_14]
        sVar7 = len(local_24)
        local_8e[local_14] = bVar1 ^ ord(local_24[uVar2 % sVar7])
        byte_value = local_8e[local_14]
        formatted_value = f"{byte_value:02x}"
        local_f2[local_14 * 2:local_14 * 2 + 2] = bytes.fromhex(formatted_value)
        if formatted_value == target_list[local_14]:
            matched.append(i)
            break
       

    local_14 = local_14 + 1

size = len(matched)
matched[:size] = [''.join(matched[:size])]
print("Password Hash: \t",local_28)
print("Decrypted: \t",matched[0])
