def identifyOpcode(opcode):

    if opcode == 0x0: return '10x', 'nop'
    if opcode == 0x1: return '12x', 'move vA,vB'
    if opcode == 0x2: return '22x', 'move/from16 vAA,vBBBB'
    if opcode == 0x3: return '32x', 'move/16 vAAAA,vBBBB'
    if opcode == 0x4: return '12x', 'move-wide vA,vB'
    if opcode == 0x5: return '22x', 'move-wide/from16 vAA, vBBBB'
    if opcode == 0x6: return '32x', 'move-wide/16 vAAAA, vBBBB'
    if opcode == 0x7: return '12x', 'move-object vA, vB'
    if opcode == 0x8: return '22x', 'move-object/from16 vAA, vBBBB'
    if opcode == 0x9: return '32x', 'move-object/16 vAAAA, vBBBB'
    if opcode == 0xa: return '11x', 'move-result vAA'
    if opcode == 0xb: return '11x', 'move-result-wide vAA'
    if opcode == 0xc: return '11x', 'move-result-object vAA'
    if opcode == 0xd: return '11x', 'move-exception vAA'
    if opcode == 0xe: return '10x', 'return-void'
    if opcode == 0xf: return '11x', 'return vAA'
    if opcode == 0x10: return '11x', 'return-wide vAA'
    if opcode == 0x11: return '11x', 'return-object vAA'
    if opcode == 0x12: return '11n', 'const/4 vA, #+B'
    if opcode == 0x13: return '21s', 'const/16 vAA, #+BBBB'
    if opcode == 0x14: return '31i', 'const vAA, #+BBBBBBBB'
    if opcode == 0x15: return '21h', 'const/high16 vAA, #+BBBB0000'
    if opcode == 0x16: return '21s', 'const-wide/16 vAA, #+BBBB'
    if opcode == 0x17: return '31i', 'const-wide/32 vAA, #+BBBBBBBB'
    if opcode == 0x18: return '51l', 'const-wide vAA, #+BBBBBBBBBBBBBBBB'
    if opcode == 0x19: return '21h', 'const-wide/high16 vAA, #+BBBB000000000000'
    if opcode == 0x1a: return '21c', 'const-string vAA, string@BBBB'
    if opcode == 0x1b: return '31c', 'const-string/jumbo vAA, string@BBBBBBBB'
    if opcode == 0x1c: return '21c', 'const-class vAA, type@BBBB'
    if opcode == 0x1d: return '11x', 'monitor-enter vAA'
    if opcode == 0x1e: return '11x', 'monitor-exit vAA'
    if opcode == 0x1f: return '21c', 'check-cast vAA, type@BBBB'
    if opcode == 0x20: return '22c', 'instance-of vA, vB, type@CCCC'
    if opcode == 0x21: return '12x', 'array-length vA, vB'
    if opcode == 0x22: return '21c', 'new-instance vAA, type@BBBB'
    if opcode == 0x23: return '22c', 'new-array vA, vB, type@CCCC'
    if opcode == 0x24: return '35c', 'filled-new-array '
    if opcode == 0x25: return '3rc', 'filled-new-array/range {vCCCC .. vNNNN}, type@BBBB'
    if opcode == 0x26: return '31t', 'fill-array-data vAA, +BBBBBBBB'
    if opcode == 0x27 : return '11x', 'throw vAA'
    if opcode == 0x28 : return '10t', 'goto +AA'
    if opcode == 0x29 : return '20t', 'goto/16 +AAAA'
    if opcode == 0x2a : return '30t', 'goto/32 +AAAAAAAA'
    if opcode == 0x2b : return '31t', 'packed-switch vAA, +BBBBBBBB'
    if opcode == 0x2c : return '31t', 'sparse-switch vAA, +BBBBBBBB'
    if opcode == 0x2d: return '23x', 'cmpl-float vAA, vBB, vCC'
    if opcode == 0x2e: return '23x', 'cmpg-float vAA, vBB, vCC'
    if opcode == 0x2f: return '23x', 'cmpl-double vAA, vBB, vCC'
    if opcode == 0x30: return '23x', 'cmpg-double vAA, vBB, vCC'
    if opcode == 0x31: return '23x', 'cmp-long vAA, vBB, vCC'
    if opcode == 0x32: return '22t', 'if-eq vA, vB, +CCCC'
    if opcode == 0x33: return '22t', 'if-ne vA, vB, +CCCC'
    if opcode == 0x34: return '22t', 'if-lt vA, vB, +CCCC'
    if opcode == 0x35: return '22t', 'if-ge vA, vB, +CCCC'
    if opcode == 0x36: return '22t', 'if-gt vA, vB, +CCCC'
    if opcode == 0x37: return '22t', 'if-le vA, vB, +CCCC'
    if opcode == 0x38: return '21t', 'if-eqz vAA, +BBBB'
    if opcode == 0x39: return '21t', 'if-nez vAA, +BBBB'
    if opcode == 0x3a: return '21t', 'if-ltz vAA, +BBBB'
    if opcode == 0x3b: return '21t', 'if-gez vAA, +BBBB'
    if opcode == 0x3c: return '21t', 'if-gtz vAA, +BBBB'
    if opcode == 0x3d: return '21t', 'if-lez vAA, +BBBB'
    if opcode == 0x3e: return '10x', 'unused'
    if opcode == 0x40: return '10x', 'unused'
    if opcode == 0x41: return '10x', 'unused'
    if opcode == 0x42: return '10x', 'unused'
    if opcode == 0x43: return '10x', 'unused' 
    if opcode == 0x44: return '23x', 'aget vAA, vBB, vCC'
    if opcode == 0x45: return '23x', 'aget-wide vAA, vBB, vCC'
    if opcode == 0x46: return '23x', 'aget-object vAA, vBB, vCC'
    if opcode == 0x47: return '23x', 'aget-boolean vAA, vBB, vCC'
    if opcode == 0x48: return '23x', 'aget-byte vAA, vBB, vCC'
    if opcode == 0x49: return '23x', 'aget-char vAA, vBB, vCC'
    if opcode == 0x4a: return '23x', 'aget-short vAA, vBB, vCC'
    if opcode == 0x4b: return '23x', 'aput vAA, vBB, vCC'
    if opcode == 0x4c: return '23x', 'aput-wide vAA, vBB, vCC'
    if opcode == 0x4d: return '23x', 'aput-object vAA, vBB, vCC'
    if opcode == 0x4e: return '23x', 'aput-boolean vAA, vBB, vCC'
    if opcode == 0x4f: return '23x', 'aput-byte vAA, vBB, vCC'
    if opcode == 0x50: return '23x', 'aput-char vAA, vBB, vCC'
    if opcode == 0x51: return '23x', 'aput-short vAA, vBB, vCC'
    if opcode == 0x52: return '22c', 'iget vAA, vBB, field@CCCC'
    if opcode == 0x53: return '22c', 'iget-wide vAA, vBB, field@CCCC'
    if opcode == 0x54: return '22c', 'iget-object vAA, vBB, field@CCCC'
    if opcode == 0x55: return '22c', 'iget-boolean vAA, vBB, field@CCCC'
    if opcode == 0x56: return '22c', 'iget-byte vAA, vBB, field@CCCC'
    if opcode == 0x57: return '22c', 'iget-char vAA, vBB, field@CCCC'
    if opcode == 0x58: return '22c', 'iget-short vAA, vBB, field@CCCC'
    if opcode == 0x59: return '22c', 'iput vAA, vBB, field@CCCC'
    if opcode == 0x5a: return '22c', 'iput-wide vAA, vBB, field@CCCC'
    if opcode == 0x5b: return '22c', 'iput-object vAA, vBB, field@CCCC'
    if opcode == 0x5c: return '22c', 'iput-boolean vAA, vBB, field@CCCC'
    if opcode == 0x5d: return '22c', 'iput-byte vAA, vBB, field@CCCC'
    if opcode == 0x5e: return '22c', 'iput-char vAA, vBB, field@CCCC'
    if opcode == 0x5f: return '22c', 'iput-short vAA, vBB, field@CCCC'
    if opcode == 0x60: return '21c', 'sget vAA, field@BBBB'
    if opcode == 0x61: return '21c', 'sget-wide vAA, field@BBBB'
    if opcode == 0x62: return '21c', 'sget-object vAA, field@BBBB'
    if opcode == 0x63: return '21c', 'sget-boolean vAA, field@BBBB'
    if opcode == 0x64: return '21c', 'sget-byte vAA, field@BBBB'
    if opcode == 0x65: return '21c', 'sget-char vAA, field@BBBB'
    if opcode == 0x66: return '21c', 'sget-short vAA, field@BBBB'
    if opcode == 0x67: return '21c', 'sput vAA, field@BBBB'
    if opcode == 0x68: return '21c', 'sput-wide vAA, field@BBBB'
    if opcode == 0x69: return '21c', 'sput-object vAA, field@BBBB'
    if opcode == 0x6a: return '21c', 'sput-boolean vAA, field@BBBB'
    if opcode == 0x6b: return '21c', 'sput-byte vAA, field@BBBB'
    if opcode == 0x6c: return '21c', 'sput-char vAA, field@BBBB'
    if opcode == 0x6d: return '21c', 'sput-short vAA, field@BBBB'
    if opcode == 0x6e: return '35c', 'invoke-virtual '
    if opcode == 0x6f: return '35c', 'invoke-super '
    if opcode == 0x70: return '35c', 'invoke-direct '
    if opcode == 0x71: return '35c', 'invoke-static '
    if opcode == 0x72: return '35c', 'invoke-interface '
    if opcode == 0x73: return '10x', 'unused'
    if opcode == 0x74: return '3rc', 'invoke-virtual/range {vCCCC .. vNNNN}, meth@BBBB'
    if opcode == 0x75: return '3rc', 'invoke-super/range {vCCCC .. vNNNN}, meth@BBBB'
    if opcode == 0x76: return '3rc', 'invoke-direct/range {vCCCC .. vNNNN}, meth@BBBB'
    if opcode == 0x77: return '3rc', 'invoke-static/range {vCCCC .. vNNNN}, meth@BBBB'
    if opcode == 0x78: return '3rc', 'invoke-interface/range {vCCCC .. vNNNN}, meth@BBBB'
    if opcode == 0x79: return '10x', 'unused'
    if opcode == 0x7a: return '10x', 'unused'
    if opcode == 0x7b: return '12x', 'neg-int vA, vB'
    if opcode == 0x7c: return '12x', 'not-int vA, vB'
    if opcode == 0x7d: return '12x', 'neg-long vA, vB'
    if opcode == 0x7e: return '12x', 'not-long vA, vB'
    if opcode == 0x7f: return '12x', 'neg-float vA, vB'
    if opcode == 0x80: return '12x', 'neg-double vA, vB'
    if opcode == 0x81: return '12x', 'int-to-long vA, vB'
    if opcode == 0x82: return '12x', 'int-to-float vA, vB'
    if opcode == 0x83: return '12x', 'int-to-double vA, vB'
    if opcode == 0x84: return '12x', 'long-to-int vA, vB'
    if opcode == 0x85: return '12x', 'long-to-float vA, vB'
    if opcode == 0x86: return '12x', 'long-to-double vA, vB'
    if opcode == 0x87: return '12x', 'float-to-int vA, vB'
    if opcode == 0x88: return '12x', 'float-to-long vA, vB'
    if opcode == 0x89: return '12x', 'float-to-double vA, vB'
    if opcode == 0x8a: return '12x', 'double-to-int vA, vB'
    if opcode == 0x8b: return '12x', 'double-to-long vA, vB'
    if opcode == 0x8c: return '12x', 'double-to-float vA, vB'
    if opcode == 0x8d: return '12x', 'int-to-byte vA, vB'
    if opcode == 0x8e: return '12x', 'int-to-char vA, vB'
    if opcode == 0x8f: return '12x', 'int-to-short vA, vB'
    if opcode == 0x90: return '23x', 'add-int vAA, vBB, vCC'
    if opcode == 0x91: return '23x', 'sub-int vAA, vBB, vCC'
    if opcode == 0x92: return '23x', 'mul-int vAA, vBB, vCC'
    if opcode == 0x93: return '23x', 'div-int vAA, vBB, vCC'
    if opcode == 0x94: return '23x', 'rem-int vAA, vBB, vCC'
    if opcode == 0x95: return '23x', 'and-int vAA, vBB, vCC'
    if opcode == 0x96: return '23x', 'or-int vAA, vBB, vCC'
    if opcode == 0x97: return '23x', 'xor-int vAA, vBB, vCC'
    if opcode == 0x98: return '23x', 'shl-int vAA, vBB, vCC'
    if opcode == 0x99: return '23x', 'shr-int vAA, vBB, vCC'
    if opcode == 0x9a: return '23x', 'ushr-int vAA, vBB, vCC'
    if opcode == 0x9b: return '23x', 'add-long vAA, vBB, vCC'
    if opcode == 0x9c: return '23x', 'sub-long vAA, vBB, vCC'
    if opcode == 0x9d: return '23x', 'mul-long vAA, vBB, vCC'
    if opcode == 0x9e: return '23x', 'div-long vAA, vBB, vCC'
    if opcode == 0x9f: return '23x', 'rem-long vAA, vBB, vCC'
    if opcode == 0xa0: return '23x', 'and-long vAA, vBB, vCC'
    if opcode == 0xa1: return '23x', 'or-long vAA, vBB, vCC'
    if opcode == 0xa2: return '23x', 'xor-long vAA, vBB, vCC'
    if opcode == 0xa3: return '23x', 'shl-long vAA, vBB, vCC'
    if opcode == 0xa4: return '23x', 'shr-long vAA, vBB, vCC'
    if opcode == 0xa5: return '23x', 'ushr-long vAA, vBB, vCC'
    if opcode == 0xa6: return '23x', 'add-float vAA, vBB, vCC'
    if opcode == 0xa7: return '23x', 'sub-float vAA, vBB, vCC'
    if opcode == 0xa8: return '23x', 'mul-float vAA, vBB, vCC'
    if opcode == 0xa9: return '23x', 'div-float vAA, vBB, vCC'
    if opcode == 0xaa: return '23x', 'rem-float vAA, vBB, vCC'
    if opcode == 0xab: return '23x', 'add-double vAA, vBB, vCC'
    if opcode == 0xac: return '23x', 'sub-double vAA, vBB, vCC'
    if opcode == 0xad: return '23x', 'mul-double vAA, vBB, vCC'
    if opcode == 0xae: return '23x', 'div-double vAA, vBB, vCC'
    if opcode == 0xaf: return '23x', 'rem-double vAA, vBB, vCC'
    if opcode == 0xb0: return '12x', 'add-int/2addr vA, vB'
    if opcode == 0xb1: return '12x', 'sub-int/2addr vA, vB'
    if opcode == 0xb2: return '12x', 'mul-int/2addr vA, vB'
    if opcode == 0xb3: return '12x', 'div-int/2addr vA, vB'
    if opcode == 0xb4: return '12x', 'rem-int/2addr vA, vB'
    if opcode == 0xb5: return '12x', 'and-int/2addr vA, vB'
    if opcode == 0xb6: return '12x', 'or-int/2addr vA, vB'
    if opcode == 0xb7: return '12x', 'xor-int/2addr vA, vB'
    if opcode == 0xb8: return '12x', 'shl-int/2addr vA, vB'
    if opcode == 0xb9: return '12x', 'shr-int/2addr vA, vB'
    if opcode == 0xba: return '12x', 'ushr-int/2addr vA, vB'
    if opcode == 0xbb: return '12x', 'add-long/2addr vA, vB'
    if opcode == 0xbc: return '12x', 'sub-long/2addr vA, vB'
    if opcode == 0xbd: return '12x', 'mul-long/2addr vA, vB'
    if opcode == 0xbe: return '12x', 'div-long/2addr vA, vB'
    if opcode == 0xbf: return '12x', 'rem-long/2addr vA, vB'
    if opcode == 0xc0: return '12x', 'and-long/2addr vA, vB'
    if opcode == 0xc1: return '12x', 'or-long/2addr vA, vB'
    if opcode == 0xc2: return '12x', 'xor-long/2addr vA, vB'
    if opcode == 0xc3: return '12x', 'shl-long/2addr vA, vB'
    if opcode == 0xc4: return '12x', 'shr-long/2addr vA, vB'
    if opcode == 0xc5: return '12x', 'ushr-long/2addr vA, vB'
    if opcode == 0xc6: return '12x', 'add-float/2addr vA, vB'
    if opcode == 0xc7: return '12x', 'sub-float/2addr vA, vB'
    if opcode == 0xc8: return '12x', 'mul-float/2addr vA, vB'
    if opcode == 0xc9: return '12x', 'div-float/2addr vA, vB'
    if opcode == 0xca: return '12x', 'rem-float/2addr vA, vB'
    if opcode == 0xcb: return '12x', 'add-double/2addr vA, vB'
    if opcode == 0xcc: return '12x', 'sub-double/2addr vA, vB'
    if opcode == 0xcd: return '12x', 'mul-double/2addr vA, vB'
    if opcode == 0xce: return '12x', 'div-double/2addr vA, vB'
    if opcode == 0xcf: return '12x', 'rem-double/2addr vA, vB'
    if opcode == 0xd0: return '22s', 'add-int/lit16 vA, vB, #+CCCC'
    if opcode == 0xd1: return '22s', 'rsub-int/lit16 vA, vB, #+CCCC'
    if opcode == 0xd2: return '22s', 'mul-int/lit16 vA, vB, #+CCCC'
    if opcode == 0xd3: return '22s', 'div-int/lit16 vA, vB, #+CCCC'
    if opcode == 0xd4: return '22s', 'rem-int/lit16 vA, vB, #+CCCC'
    if opcode == 0xd5: return '22s', 'and-int/lit16 vA, vB, #+CCCC'
    if opcode == 0xd6: return '22s', 'or-int/lit16 vA, vB, #+CCCC'
    if opcode == 0xd7: return '22s', 'xor-int/lit16 vA, vB, #+CCCC'
    if opcode == 0xd8: return '22b', 'add-int/lit8 vA, vB, #+CC'
    if opcode == 0xd9: return '22b', 'rsub-int/lit8 vA, vB, #+CC'
    if opcode == 0xda: return '22b', 'mul-int/lit8 vA, vB, #+CC'
    if opcode == 0xdb: return '22b', 'div-int/lit8 vA, vB, #+CC'
    if opcode == 0xdc: return '22b', 'rem-int/lit8 vA, vB, #+CC'
    if opcode == 0xdd: return '22b', 'and-int/lit8 vA, vB, #+CC'
    if opcode == 0xde: return '22b', 'or-int/lit8 vA, vB, #+CC'
    if opcode == 0xdf: return '22b', 'xor-int/lit8 vA, vB, #+CC'
    if opcode == 0xe0: return '22b', 'shl-int/lit8 vA, vB, #+CC'
    if opcode == 0xe1: return '22b', 'shr-int/lit8 vA, vB, #+CC'
    if opcode == 0xe2: return '22b', 'ushr-int/lit8 vA, vB, #+CC'
    if opcode == 0xe3: return '10x', 'unused'
    if opcode == 0xe4: return '10x', 'unused'
    if opcode == 0xe5: return '10x', 'unused'
    if opcode == 0xe6: return '10x', 'unused'
    if opcode == 0xe7: return '10x', 'unused'
    if opcode == 0xe8: return '10x', 'unused'
    if opcode == 0xe9: return '10x', 'unused'
    if opcode == 0xea: return '10x', 'unused'
    if opcode == 0xeb: return '10x', 'unused'
    if opcode == 0xec: return '10x', 'unused'
    if opcode == 0xed: return '10x', 'unused'
    if opcode == 0xee: return '10x', 'unused'
    if opcode == 0xef: return '10x', 'unused'
    if opcode == 0xf0: return '10x', 'unused'
    if opcode == 0xf1: return '10x', 'unused'
    if opcode == 0xf2: return '10x', 'unused'
    if opcode == 0xf3: return '10x', 'unused'
    if opcode == 0xf4: return '10x', 'unused'
    if opcode == 0xf5: return '10x', 'unused'
    if opcode == 0xf6: return '10x', 'unused'
    if opcode == 0xf7: return '10x', 'unused'
    if opcode == 0xf8: return '10x', 'unused'
    if opcode == 0xf9: return '10x', 'unused'
    if opcode == 0xfa: return '45cc', 'invoke-polymorphic {vC, vD, vE, vF, vG}, meth@BBBB, proto@HHHH'
    if opcode == 0xfb: return '4rcc', 'invoke-polymorphic/range {vCCCC .. vNNNN}, meth@BBBB, proto@HHHH'
    if opcode == 0xfc: return '35c', 'invoke-custom '
    if opcode == 0xfd: return '3rc', 'invoke-custom/range {vCCCC .. vNNNN}, call_site@BBBB'
    if opcode == 0xfe: return '21c', 'const-method-handle vAA, method_handle@BBBB'
    if opcode == 0xff: return '21c', 'const-method-type vAA, proto@BBBB'
    return 'unknown', 'unknown opcode'


def parseAddress1(val):

    binary = bin(val)[2:].zfill(8)

    if binary[0:1] == "0":
        return val
    
    b = ""

    for i in range(7):
        if binary[i+1:i+2] == "1":
            b += '0'
        else:
            b += '1'
    return -(int(b,2)+1)

def parseAddress2(val):

    binary = bin(val).zfill(16)

    if binary[0:1] == "0":
        return val
    
    b = ""
    for i in range(15):
        if binary[i+1:i+2] == "1":
            b += '0'
        else:
            b += '1'
    return -(int(b,2)+1)

def parseAddress3(val):

    binary = bin(val).zfill(32)

    if binary[0] == "0":
        return val
    
    b = ""

    for i in range(31):
        if binary[i+1:i+2] == "1":
            b += "0"
        else:
            b+= "1"
    return b

def instructionUtil(ins,offset,TypeArr,FieldArr,MethodArr,StrArr,ProtoArr):
    
    opcode = int(ins[offset:offset+2],16)
    format, syntax = identifyOpcode(opcode)

    if format == '10x':
        # op
        return syntax , 4
    
    elif format == '12x':
        # op vA, vB
        B = int(ins[offset+2:offset+3],16)
        A = int(ins[offset+3:offset+4],16)
        return syntax.replace('vA',f'v{A}').replace('vB',f'v{B}'), 4
    
    elif format == '11n':
        # op vA , #+B
        B = int(ins[offset+2:offset+3],16)
        A = int(ins[offset+3:offset+4],16)
        return syntax.replace('vA',f'v{A}').replace('#+B',f'#+{B}'),4
    
    elif format == '11x':
        # op vAA
        AA = int(ins[offset+2:offset+4],16)
        return syntax.replace('vAA',f'v{AA}') ,4
    
    elif format == '10t':
        # op +AA
        AA = int(ins[offset+2:offset+4],16)
        branch_offset = parseAddress1(AA)
        return syntax.replace("+AA",str(branch_offset)), 4
    
    elif format == '20t':
        # op +AAAA
        AAAA = int(ins[offset+2:offset+8],16)
        branch_offset = parseAddress2(AAAA)
        return syntax.replace("+AAAA",str(branch_offset)) , 8
    
    elif format == "20bc":
        # op AA, kind@BBBB
        pass

    elif format == "22x":
        # op AA| op BBBB
        AA = int(ins[offset+2:offset+4],16)
        BBBB = int(ins[offset+6:offset+8]+ins[offset+4:offset+6],16)
        return syntax.replace('vAA',f'v{AA}').replace('vBBBB',f'v{BBBB}') , 8

    elif format == "21t":
        
        AA = int(ins[offset+2:offset+4],16)
        BBBB = int(ins[offset+6:offset+8]+ins[offset+4:offset+6],16)
        return syntax.replace('vAA',f'v{AA}').replace('+BBBB',f'+{BBBB}') , 8

    elif format == '21s':
        AA = int(ins[offset+2:offset+4],16)
        BBBB = int(ins[offset+6:offset+8]+ins[offset+4:offset+6],16)
        return syntax.replace('vAA',f'v{AA}').replace('#+BBBB',f'#+{BBBB}') , 8    

    elif format == '21h':
        AA = int(ins[offset+2:offset+4],16)
        BBBB = ins[offset+6:offset+8]+ins[offset+4:offset+6]
        if 'const/high16' in syntax:
            BBBB = int(BBBB+'0000',16)
            syntax = syntax.replace('BBBB0000',str(BBBB))
        else:
            BBBB = int(BBBB+'00000000',16)
            syntax = syntax.replace('BBBB00000000',str(BBBB))
        return syntax.replace('vAA',f'v{AA}'), 8
        
    elif format == '21c':
        AA = int(ins[offset+2:offset+4],16)
        BBBB = int(ins[offset+6:offset+8]+ins[offset+4:offset+6],16)
        
        if 'type' in syntax:
            syntax = syntax.replace('vAA',f'v{AA}').replace('type@BBBB',f'type@{BBBB} // {TypeArr[BBBB]}')
        elif 'field' in syntax:
            syntax = syntax.replace('vAA',f'v{AA}').replace('field@BBBB',f'field@{BBBB} // {FieldArr[BBBB]}')
        elif 'method_handle' in syntax:
            syntax = syntax.replace('vAA',f'v{AA}').replace('method_handle@BBBB',f'method_handle@{BBBB}')
        elif 'proto' in syntax:
            syntax = syntax.replace('vAA',f'v{AA}').replace('proto@BBBB',f'proto@{BBBB} // {ProtoArr[BBBB]}')
        elif 'string' in syntax:
            syntax = syntax.replace('vAA',f'v{AA}').replace('string@BBBB',f'string@{BBBB} // {StrArr[BBBB]}')

        return syntax,8

    elif format == '23x':
        AA = int(ins[offset+2:offset+4],16)
        BB = int(ins[offset+4:offset+6],16)
        CC = int(ins[offset+6:offset+8],16)
        return syntax.replace('vAA',f'v{AA}').replace('vBB',f'v{BB}').replace('vCC',f'v{CC}') , 8

    elif format == '22b':
        AA = int(ins[offset+2:offset+4],16)
        BB = int(ins[offset+4:offset+6],16)
        CC = int(ins[offset+6:offset+8],16)
        return syntax.replace('vAA',f'v{AA}').replace('vBB',f'v{BB}').replace('#+CC',f'#={CC}') , 8

    elif format == '22t':
        B = int(ins[offset+2:offset+3],16)
        A = int(ins[offset+3:offset+4],16)
        CCCC = int(ins[offset+6:offset+8]+ins[offset+4:offset+6],16)
        return syntax.replace('vA',f'v{A}').replace('vB',f'v{B}').replace('+CCCC',f'+{CCCC}') , 8
    
    elif format == '22s':
        B = int(ins[offset+2:offset+3],16)
        A = int(ins[offset+3:offset+4],16)
        CCCC = int(ins[offset+6:offset+8]+ins[offset+4:offset+6],16)
        return syntax.replace('vA',f'v{A}').replace('vB',f'v{B}').replace('#+CCCC',f'#+{CCCC}') , 8

    elif format == '22c':
        B = int(ins[offset+2:offset+3],16)
        A = int(ins[offset+3:offset+4],16)
        CCCC = int(ins[offset+6:offset+8]+ins[offset+4:offset+6],16)
        
        if ('instance-of' or 'new-array') in syntax:
            val = TypeArr[CCCC]
            syntax = syntax.replace('type@CCCC',f'type@{CCCC}')
        else:
            val = FieldArr[CCCC]
            syntax = syntax.replace('field@CCCC',f'field@{CCCC}')
        syntax = syntax.replace('vA',f'v{A}').replace('vB',f'v{B}')
        syntax = f'{syntax} //{val}'
        return syntax , 8

    elif format == '22cs':
        pass 

    elif format == '30t':
        AAAAlo = int(ins[offset+4:offset+8],16)
        AAAAhi = int(ins[offset+8:offset+12],16)
        AAAA = (AAAAhi << 16) | AAAAlo
        AAAA = parseAddress3(AAAA)
        current_offset = offset // 4  
        target_offset = current_offset + AAAA

        return syntax.replace("+AAAAAAAA",f"{hex(target_offset) // hex(AAAA)}") , 12
    
    elif format == '32x':
        AAAA = int(ins[offset+6:offset+8]+ins[offset+4:offset+6],16)
        BBBB = int(ins[offset+10:offset+12]+ins[offset+8:offset+10],16)
        return syntax.replace('vAAAA',f'v{AAAA}').replace('vBBBB',f'v{BBBB}') , 12
    
    elif format == '31i':
        AA = int(ins[offset+2:offset+4],16)
        BBBBlo = int(ins[offset+4:offset+8],16)
        BBBBhi = int(ins[offset+8:offset+12],16)
        BBBB = (BBBBhi << 16) | BBBBlo
        return syntax.replace('vAA',f'v{AA}').replace('#+BBBBBBBB',f'#+{BBBB}') , 12
    
    elif format == '31t':
        AA = int(ins[offset+2:offset+4],16)
        BBBBlo = int(ins[offset+4:offset+8],16)
        BBBBhi = int(ins[offset+8:offset+12],16)
        BBBB = (BBBBhi << 16) | BBBBlo
        BBBB = parseAddress3(BBBB)

        current_offset = offset // 4
        target_offset = current_offset + BBBB
        return syntax.replace('vAA',f'v{AA}').replace('+BBBBBBBB',f"{hex(target_offset) // hex(BBBB)}") , 12

    elif format == '31c':
        AA = int(ins[offset+2:offset+4],16)
        BBBBlo = int(ins[offset+4:offset+8],16)
        BBBBhi = int(ins[offset+8:offset+12],16)
        BBBB = (BBBBhi << 16) | BBBBlo
        syntax = syntax.replace('vAA',f'v{AA}').replace('string@BBBBBBBB',f"string@{BBBB}")
        syntax = f'{syntax} // {StrArr[BBBB]}'
        return syntax , 12
    
    elif format == '35c':

        A = int(ins[offset+2:offset+3],16)
        G = int(ins[offset+3:offset+4],16)
        BBBB = int(ins[offset+6:offset+8]+ins[offset+4:offset+6],16)
        F = int(ins[offset+8:offset+9],16)
        E = int(ins[offset+9:offset+10],16)
        D = int(ins[offset+10:offset+11],16)
        C = int(ins[offset+11:offset+12],16)

        if opcode == 0x24:
            type = 'type'
            val = TypeArr[BBBB]
        elif 0x6e <= opcode <= 0x72:
            type = 'method'
            val = MethodArr[BBBB]
        elif format == 0xfc:
            type = 'call_site'
            val = ''

        if A == 0:
            s = f'(), {type}@{BBBB} // {val}'
        elif A == 1:
            s = f'(v{C}), {type}@{BBBB} // {val}'
        elif A == 2:
            s = f'(v{C},v{D}), {type}@{BBBB} // {val}'
        elif A == 3:
            s = f'(v{C},v{D},v{E}), {type}@{BBBB} // {val}'
        elif A == 4:
            s = f'(v{C},v{D},v{E},v{F}), {type}@{BBBB} // {val}'
        elif A == 5:
            s = f'(v{C},v{D},v{E},v{F},v{G}), {type}@{BBBB} // {val}'

        return syntax+s , 12
    
    elif format in ('35ms', '35mi','3rc','3rms','3rmi'):
        return syntax , 12
    
    elif format in ('45cc','4rcc'):
        return syntax , 16
    
    return syntax , 20

def parseInstructions(instructions,insns_size,TypeArr,FieldArr,MethodArr,StrArr,ProtoArr):
    
    i = insns_size * 4
    offset = 0
    insns = []
    
    while offset < i:
        instruction , bytes_consumed = instructionUtil(instructions,offset,TypeArr,FieldArr,MethodArr,StrArr,ProtoArr)
        insns.append([instruction,bytes_consumed])
        offset += bytes_consumed
    
    return insns