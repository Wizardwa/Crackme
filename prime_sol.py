#!/bin/python3
import os


def fun_004015cf(param_1: int, param_2: int, param_3: int) -> int:
    # Initialize local_8 to 1
    local_8 = 1

    #print(f"param_2 before: {param_2}")
    
    # Loop from param_2 down to 1
    for _ in range(param_2):
        local_8 = (param_1 * local_8) % param_3


    #print(f"local_8 value: ",local_8)

    return local_8


local_1d = 0xfb
local_1e = 0x81
local_24 = "Th4t's a P455W0rD"
local_28 = "113e5c6eac71358d3a4727639f55f02457565ae57662a2a2727610d84646"

local_5c = input("please enter the password: \n")
#local_5c = '\nninja' #testing non printable 
local_5c = local_5c.encode("ascii")


#checking if char is ascii printable
local_14 = 0
sVar5 = len(local_5c)
while local_14 < sVar5:
	if local_5c[local_14] < 0x20 or 0x7e < local_5c[local_14]:
		print(f"Index of local_5c: {local_5c[local_14]}")
		print("ascii please")
		os.system("pause")

	local_14 = local_14 + 1


local_8e = bytearray(50)
local_14 = 0
sVar5 = len(local_5c)
while local_14 < sVar5:
	local_29 = local_5c[local_14]
	iVar6 = fun_004015cf(local_1e,local_29,local_1d)
	local_2a = iVar6
	local_8e[local_14] = local_2a
	local_14 = local_14 + 1

local_f2 = bytearray(100)
local_14 = 0
sVar5 = len(local_5c)
while local_14 < sVar5:
	uVar2 = local_14
	bVar1 = local_8e[local_14]
	sVar7 = len(local_24)
	local_8e[local_14] = bVar1 ^ ord(local_24[uVar2 % sVar7])
	byte_value = local_8e[local_14]
	#print(byte_value)
	formatted_value = f"{byte_value:02x}"
	local_f2[local_14 * 2:local_14 * 2 + 2] = bytes.fromhex(formatted_value)
	print(formatted_value, end='')
	#print(formatted_value)

	local_14 = local_14 + 1
print('\n')
#print(local_28)