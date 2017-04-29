# -*- UTF-8 -*-
#!/usr/bin/env python3

# License GNU GPL, check out the full notice in LICENSE file
# Copyright (C) 2017 ArenGamerZ

import sys
from . import bin_converter as bconverter


def Count(string, character):
    """ This function counts how many ocurrences of 'character' are in 'string' """
    count = 0
    for cc in string:
        if cc == character:
            count += 1
    return count


def DetClass(ip):
    """ This function determines whether the ip is class A, B, C, D or E
        Name of variables:
            fb_bin means first byte binary"""

    first_byte = str(ip.split('.')[0])
    fb_bin = bconverter.convert(first_byte)

    # We count the successive number of ones in the ip
    count = 0
    for i in range(4):
        if fb_bin[i] == "1":
            count += 1
        else:
            break

    # If the count it's equal to '0', that means it begins with a '0' which means it's an A class
    if count == 0:
        dclass = "A"
        dmask = "255.0.0.0"
    # If the count it's equal to '1', that means that it begins with a '1' but it's followed by a '0' which means it's a B class
    elif count == 1:
        dclass = "B"
        dmask = "255.255.0.0"
    # If the count it's equal to '2' that means there is '2' consecutive ones which means it's a C class.
    elif count == 2:
        dclass = "C"
        dmask = "255.255.255.0"
    # Same as above but with '3' ones which means it's a D class
    elif count == 3:
        dclass = "D"
        dmask = None # D class has no mask
    # If nothing of the above it's accomplished, that means that it has '4' or more ones which means it's an E class.
    else:
        dclass = "E"
        dmask = None # E class has no mask
    return dclass, dmask


def NumOfHosts(mask):
    if bconverter.check(mask):
        NumOfZeroesMask = Count(bconverter.convert(mask), "0")
        result = 2**NumOfZeroesMask-2
    else:
        # We assume the mask was given in number format, eg: 26
        # 32 is the maximum number of ones with 4 bytes (because 8*4 = 32)
        if int(mask) > 31:
            raise ValueError
        else:
            NumOfZeroesMask = 32 - int(mask)
            result = 2**NumOfZeroesMask-2
    return result


def NumOfSubnets(ip, mask):
    dmask = DetClass(ip)[1]
    if bconverter.check(mask):
        diff = Count(bconverter.convert(mask), "1") - Count(bconverter.convert(dmask), "1")
        result = 2**diff
    else:
        # We assume the mask was given in number format, eg: 26
        if int(mask) > 31:
            raise ValueError
        else:
            dmask_ones = Count(bconverter.convert(dmask), "1")
            diff = int(mask) - dmask_ones
            result = 2**diff
    return result


def GetNetAddress(ip, mask):
    ip_list = bconverter.convert(ip).split('.')
    ip_str = ''.join(ip_list)
    if bconverter.check(mask):
        mask_list = bconverter.convert(mask).split('.')
        mask_str = ''.join(mask_list)
    else:
        # We assume the mask was given in number format, eg: 26
        mask = int(mask)
        ZeroesDiffTotalMask = 32 - mask # So we know how much zeroes we must write after the ones.
        mask_str = ""

        for i in range(mask):
            mask_str += "1"
        for i in range(ZeroesDiffTotalMask):
            mask_str += "0"

    # Perform an 'IP AND MASK' operation
    count = 0
    and_operation = []
    for i in range(0, 32):
        if ip_str[i] == "1" and mask_str[i] == "1":
            and_operation.append("1")
        else:
            and_operation.append("0")

    count = 0
    cbyte = []
    result_bin = []
    for i in and_operation:
        if count == 7:
            cbyte.append(i)
            cbyte = ''.join(cbyte)
            result_bin.append(cbyte)
            count = 0
            cbyte = []
        else:
            cbyte.append(i)
            count += 1
    ip_bin = '.'.join(result_bin)

    result = bconverter.convert(ip_bin, "binary")
    return result


def GetBcastAddress(ip, mask):
    ip_list = bconverter.convert(ip).split('.')
    ip_str = ''.join(ip_list)
    if bconverter.check(mask):
        mask_list = bconverter.convert(mask).split('.')
        mask_str = ''.join(mask_list)
    else:
        # We assume the mask was given in number format, eg: 26
        mask = int(mask)
        ZeroesDiffTotalMask = 32 - mask # So we know how much zeroes we must write after the ones.
        mask_str = ""

        for i in range(mask):
            mask_str += "1"
        for i in range(ZeroesDiffTotalMask):
            mask_str += "0"

    # Perform an 'IP OR NOT MASK' operation
    mask_str = mask_str.replace("1", "%temp%").replace("0", "1").replace("%temp%", "0") # NOT MASK
    count = 0
    and_operation = []
    for i in range(0, 32):
        if ip_str[i] == "1" or mask_str[i] == "1":
            and_operation.append("1")
        else:
            and_operation.append("0")

    count = 0
    cbyte = []
    result_bin = []
    for i in and_operation:
        if count == 7:
            cbyte.append(i)
            cbyte = ''.join(cbyte)
            result_bin.append(cbyte)
            count = 0
            cbyte = []
        else:
            cbyte.append(i)
            count += 1
    ip_bin = '.'.join(result_bin)

    result = bconverter.convert(ip_bin, "binary")
    return result
