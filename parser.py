import os
import struct
import InstructionsHelper
from hashlib import sha1
from icecream import ic
from argparse import ArgumentParser
from rich.console import Console
from rich.table import Table

Map_Item_Codes = {
    0x0 : 'TYPE_HEADER_ITEM',
    0x1 : 'TYPE_STRING_ID_ITEM',
    0x2 : 'TYPE_TYPE_ID_ITEM',
    0x3 : 'TYPE_PROTO_ID_ITEM',
    0x4 : 'TYPE_FIELD_ID_ITEM',
    0x5 : 'TYPE_METHOD_ID_ITEM',
    0x6 : 'TYPE_CLASS_DEF_ITEM',
    0x7 : 'TYPE_CALL_SITE_ID_ITEM',
    0x8 : 'TYPE_METHOD_HANDLE_ITEM',
    0x1000 : 'TYPE_MAP_LIST',
    0x1001 : 'TYPE_TYPE_LIST',
    0x1002 : 'TYPE_ANNOTATION_SET_REF_LIST',
    0x1003 : 'TYPE_ANNOTATION_SET_ITEM',
    0x2000 : 'TYPE_CLASS_DATA_ITEM',
    0x2001 : 'TYPE_CODE_ITEM',
    0x2002 : 'TYPE_STRING_DATA_ITEM',
    0x2003 : 'TYPE_DEBUG_INFO_ITEM',
    0x2004 : 'TYPE_ANNOTATION_ITEM',
    0x2005 : 'TYPE_ENCODED_ARRAY_ITEM',
    0x2006 : 'TYPE_ANNOTATIONS_DIRECTORY_ITEM',
    0xF000 : 'TYPE_HIDDENAPI_CLASS_DATA_ITEM'
}

Access_Flags = {
    0x1 : 'ACC_PUBLIC',
    0x2 : 'ACC_PRIVATE',
    0x4 : 'ACC_PROTECTED',
    0x8 : 'ACC_STATIC',
    0x9 : 'PUBLIC_STATIC',
    0xa : 'PRIVATE_STATIC',
    0x10 : 'ACC_FINAL',
    0x20 : 'ACC_SYNCHRONIZED',
    0x40 : 'ACC_VOLATILE',
    0x40 : 'ACC_BRIDGE',
    0x80 : 'ACC_TRANSIENT',
    0x80 : 'ACC_VARARGS',
    0x100 : 'ACC_NATIVE',
    0x200 : 'ACC_INTERFACE',
    0x400 : 'ACC_ABSTRACT',
    0x800 : 'ACC_STRICT',
    0x1000 : 'ACC_SYNTHETIC',
    0x2000 : 'ACC_ANNOTATION',
    0x4000 : 'ACC_ENUM',
    0x8000 : 'NOT DEFINED',
    0x10000 : 'ACC_CONSTRUCTOR',
    0x10001 : 'PUBLIC_CONSTRUCTOR',
    0x20000 : 'ACC_DECLARED_SYNCHRONIZED'
}

class DexParser:

    def __init__(self,filepath):
        self.filepath = filepath
        self.console = Console()
        self.f = open(self.filepath,'rb')

    def clean(self,s):
        return s.replace('\n',' ')

    def header_parse(self):
        self.f.seek(0,0)
        self.DEX_MAGIC = self.clean(struct.unpack('8s',self.f.read(8))[0].decode('utf-8'))
        # ic(self.DEX_MAGIC)
        self.f.seek(8,0)
        self.Checksum = struct.unpack('<I',self.f.read(4))[0]
        #ic(self.Checksum)
        self.f.seek(12,0)
        self.Signature = sha1(struct.unpack('20s',self.f.read(20))[0]).hexdigest()
        #ic(self.Signature)
        self.f.seek(32,0)
        self.FileSize = struct.unpack('I',self.f.read(4))[0]
        # ic(self.FileSize)
        self.f.seek(36,0)
        self.HeaderSize = struct.unpack('I',self.f.read(4))[0]
        #ic(self.HeaderSize)
        self.f.seek(40,0)
        self.EndianConstant = hex(struct.unpack('I',self.f.read(4))[0])
        #ic(self.EndianConstant)
        self.f.seek(44,0)
        self.LinkSize = struct.unpack('I',self.f.read(4))[0]
        # ic(self.LinkSize)
        self.f.seek(48,0)
        self.LinkOffset = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(52,0)
        self.MapOffset =  struct.unpack('I',self.f.read(4))[0]

        self.f.seek(56,0)
        self.String_Ids_Size = struct.unpack('I',self.f.read(4))[0]
        #ic(self.String_Ids_Size)

        self.f.seek(60,0)
        self.String_Ids_Offset = struct.unpack('I',self.f.read(4))[0]
        #ic(self.String_Ids_Offset)

        self.f.seek(64,0)
        self.Type_Ids_Size = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(68,0)
        self.Type_Ids_Offset = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(72,0)
        self.Proto_Ids_Size = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(76,0)
        self.Proto_Ids_Offset = struct.unpack('I',self.f.read(4))[0]
        
        self.f.seek(80,0)
        self.Field_Ids_Size = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(84,0)
        self.Field_Ids_Offset = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(88,0)
        self.Method_Ids_Size = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(92,0)
        self.Method_Ids_Offset  = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(96,0)
        self.Class_Def_Size = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(100,0)
        self.Class_Def_Offset = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(104,0)
        self.Data_size = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(108,0)
        self.Data_offset = struct.unpack('I',self.f.read(4))[0]
    
    def print_headers(self):
        table = Table(title="DEX Headers")
        table.add_column("Headers",justify="center",style="cyan")
        table.add_column("Values",justify="center",style="magenta")

        table.add_row("Version",self.DEX_MAGIC)
        table.add_row("Checksum",str(self.Checksum))
        table.add_row("Signature",self.Signature)
        table.add_row("File Size",str(self.FileSize))
        table.add_row("Header Size",str(self.HeaderSize))
        table.add_row("Endian Tag",str(self.EndianConstant))
        table.add_row("Link Size",str(self.LinkSize))
        table.add_row("Link Offset",str(self.LinkOffset))
        table.add_row("Map Offset",str(self.MapOffset))
        table.add_row("String Ids Size",str(self.String_Ids_Size))
        table.add_row("String Ids Offset",str(self.String_Ids_Offset))
        table.add_row("Type Ids Size",str(self.Type_Ids_Size))
        table.add_row("Type Ids Offset",str(self.Type_Ids_Offset))
        table.add_row("Proto Ids Size",str(self.Proto_Ids_Size))
        table.add_row("Proto Ids Offset",str(self.Proto_Ids_Offset))
        table.add_row("Field Ids Size",str(self.Field_Ids_Size))
        table.add_row("Field Ids Offset",str(self.Field_Ids_Offset))
        table.add_row("Method Ids Size",str(self.Method_Ids_Size))
        table.add_row("Method Ids Offset",str(self.Method_Ids_Offset))
        table.add_row("Class Def Size",str(self.Class_Def_Size))
        table.add_row("Class Def Offset",str(self.Class_Def_Offset))
        table.add_row("Data Size",str(self.Data_size))
        table.add_row("Data Offset",str(self.Data_offset))

        self.console.print(table)

    def parseMapItems(self,loc,ind):
        
        self.f.seek(loc + ind * 12,0)

        self.Map_Item_Type = struct.unpack('H',self.f.read(2))[0]

        self.f.seek(loc+(ind * 12) + 2,0)
        self.Map_Item_Unused = struct.unpack('H',self.f.read(2))[0]

        self.f.seek(loc+(ind*12)+4,0)
        self.Map_Item_Size = struct.unpack('I',self.f.read(4))[0]

        self.f.seek(loc+(ind+12)+8,0)
        self.Map_Item_Offset = struct.unpack('I',self.f.read(4))[0]

        self.console.print(f"Type [yellow]{Map_Item_Codes[self.Map_Item_Type]}")
        self.console.print(f"Unused {self.Map_Item_Unused}")
        self.console.print(f"Size {self.Map_Item_Size}")
        self.console.print(f"Offset {self.Map_Item_Offset}")

    def MapList(self):

        self.f.seek(self.MapOffset,0)

        self.Map_List_size  = struct.unpack('I',self.f.read(4))[0]

        for i in range(self.Map_List_size):
            self.console.print("=====================")
            self.console.print(f'[bold red]Map List Item {i+1}')
            self.parseMapItems(self.MapOffset+4,i)
    
    def DexStrings(self):
        
        table1 = Table(title="Strings")
        table1.add_column("String Data", justify="left", style="cyan")
        self.strArr = []


        for j in range(self.String_Ids_Size):
            self.f.seek(self.String_Ids_Offset+j*4,0)

            self.String_Data_Offset = struct.unpack('I',self.f.read(4))[0]

            self.f.seek(self.String_Data_Offset,0)

            length = struct.unpack('B',self.f.read(1))[0]

            self.f.seek(self.String_Data_Offset+1)

            strData = struct.unpack(f'{length}s',self.f.read(length))[0].decode('utf-8')

            self.strArr.append(strData)

            table1.add_row(strData)

        self.console.print(table1)

    def DexTypes(self):

        table2 = Table(title='Types')
        table2.add_column("Descriptor Index",justify="left")
        table2.add_column("Descriptor")
        self.TypeArr = []

        for k in range(self.Type_Ids_Size):
            self.f.seek(self.Type_Ids_Offset+k*4,0)

            TypeIdx = struct.unpack('I',self.f.read(4))[0]

            table2.add_row(str(TypeIdx),self.strArr[TypeIdx])

            self.TypeArr.append(self.strArr[TypeIdx])
        
        self.console.print(table2)

    def DexProtoItem(self):

        table3 = Table(title='Method Prototypes')
        table3.add_column('Prototype Descriptor',justify='left')
        table3.add_column('Return Type',style='magenta')
        table3.add_column('Parameters',style='yellow')

        self.ProtoDesc = []

        for i in range(self.Proto_Ids_Size):

            self.f.seek(self.Proto_Ids_Offset+i*12,0)

            shortyIdx = struct.unpack('I',self.f.read(4))[0]
            returnTypeIdx = struct.unpack('I',self.f.read(4))[0]
            parameterOffset = struct.unpack('I',self.f.read(4))[0]
            # ic(shortyIdx,returnTypeIdx,parameterOffset)

            protoDescriptor = self.strArr[shortyIdx]
            self.ProtoDesc.append(protoDescriptor)
            returnTypeDescriptor = self.TypeArr[returnTypeIdx]

            parameterDescriptor = None

            if parameterOffset != 0:
                self.f.seek(parameterOffset,0)
                type_list_size = struct.unpack('I',self.f.read(4))[0]
                tmp = []
                for j in range(type_list_size):
                    typeIdx = struct.unpack('H',self.f.read(2))[0]
                    tmp.append(typeIdx)
                parameterDescriptor = ''.join(self.TypeArr[i] for i in tmp)
            else:
                parameterDescriptor = 'No Parameters'

            table3.add_row(protoDescriptor,returnTypeDescriptor,parameterDescriptor)
        
        self.console.print(table3)
    
    def DexFieldItem(self):

        self.f.seek(self.Field_Ids_Offset,0)

        table4 = Table(title='Fields')
        table4.add_column('Class',justify='left',style='red')
        table4.add_column('Type',style="#d2601a")
        table4.add_column('Field Name',style="#ffc13b")

        self.FieldName = []

        for k in range(self.Field_Ids_Size):
            
            classIdx = struct.unpack('H',self.f.read(2))[0]
            typeIdx = struct.unpack('H',self.f.read(2))[0]
            nameIdx = struct.unpack('I',self.f.read(4))[0]

            field_class = self.TypeArr[classIdx]
            field_type = self.TypeArr[typeIdx]
            field_name = self.strArr[nameIdx]

            self.FieldName.append(field_name)

            table4.add_row(field_class,field_type,field_name)
        
        self.console.print(table4)

    def DexMethods(self):

        self.f.seek(self.Method_Ids_Offset,0)
        table = Table(title='Methods')
        table.add_column('Class',style='#7fe7dc')
        table.add_column('Prototype',style='#d902ee')
        table.add_column('Method Name',style='#edca82')

        self.MethodName = []

        for i in range(self.Method_Ids_Size):

            classIdx = struct.unpack('H',self.f.read(2))[0]
            protoIdx = struct.unpack('H',self.f.read(2))[0]
            nameIdx = struct.unpack('I',self.f.read(4))[0]

            method_class = self.TypeArr[classIdx]
            method_prototype = self.ProtoDesc[protoIdx]
            method_name =  self.strArr[nameIdx]

            self.MethodName.append(method_name)

            table.add_row(method_class,method_prototype,method_name)
        
        self.console.print(table)

    
    def read_unsigned_leb128(self,file):
        result = 0
        shift = 0

        while True:
            byte = struct.unpack('B', file.read(1))[0]
            result |= (byte & 0x7F) << shift
            if byte & 0x80 == 0:
                break
            shift += 7

        return result

    def DumpDexCode(self, method_name, access_specifier, code_offset):
        file = open(self.filepath, 'rb')
        file.seek(code_offset, 0)

        register_size = struct.unpack('H', file.read(2))[0]
        ins_size = struct.unpack('H', file.read(2))[0]
        outs_size = struct.unpack('H', file.read(2))[0]
        tries_size = struct.unpack('H', file.read(2))[0]
        debug_info_off = struct.unpack('I', file.read(4))[0]
        insns_size = struct.unpack('I', file.read(4))[0]

        header_table = Table(show_header=True, header_style="bold magenta", title="Method Information")
        header_table.add_column("Property")
        header_table.add_column("Value")

        header_table.add_row("Method Name", method_name)
        header_table.add_row("Access Flags", access_specifier)
        header_table.add_row("Registers", str(register_size))
        header_table.add_row("Ins Size", str(ins_size))
        header_table.add_row("Outs Size", str(outs_size))
        header_table.add_row("Tries Size", str(tries_size))
        header_table.add_row("Debug Offset", hex(debug_info_off))

        if insns_size == 0:
            insns = []
        else:
            i = insns_size * 2
            insn = file.read(i).hex()
            insns = InstructionsHelper.parseInstructions(insn, insns_size, self.TypeArr, 
                                                    self.FieldName, self.MethodName, 
                                                    self.strArr, self.ProtoDesc)

        inst_table = Table(show_header=True, header_style="bold cyan", title=f"Instructions ({insns_size} units)")
        inst_table.add_column("Offset", justify="right", style="#f9caa7")
        inst_table.add_column("Hex", style="#f37736")
        inst_table.add_column("Assembly", style="#88d8b0")

        offset = 0
        for instruction, bytes_consumed in insns:
            inst_table.add_row(hex(offset)[2:].zfill(4),insn[offset:offset + bytes_consumed],instruction)
            offset += bytes_consumed

        self.console.print(header_table)
        self.console.print(inst_table)
        self.console.print("") 
        file.close()

    def DexClass(self):
        self.f.seek(self.Class_Def_Offset, 0)

        for i in range(self.Class_Def_Size):
            class_idx = struct.unpack('I', self.f.read(4))[0]
            access_flags = struct.unpack('I', self.f.read(4))[0]
            superclass_idx = struct.unpack('I', self.f.read(4))[0]
            interfaces_off = struct.unpack('I', self.f.read(4))[0]
            source_file_idx = struct.unpack('I', self.f.read(4))[0]
            annotations_off = struct.unpack('I', self.f.read(4))[0]
            class_data_off = struct.unpack('I', self.f.read(4))[0]
            static_values_off = struct.unpack('I', self.f.read(4))[0]

            self.console.print(f"\n[#ffcc5c]Class #{i + 1}")
            class_table = Table(show_header=True, header_style="bold magenta")
            class_table.add_column("Property",style="#7bc043")
            class_table.add_column("Value",style="#ff8b94")

            class_table.add_row("Class Name", self.TypeArr[class_idx])
            class_table.add_row("Access Flags", Access_Flags[access_flags])
            class_table.add_row("Superclass", self.TypeArr[superclass_idx])
            class_table.add_row("Source File", self.strArr[source_file_idx])
            
            self.console.print(class_table)

            if class_data_off == 0:
                self.console.print("[yellow]No class data")
                continue

            self.f.seek(class_data_off, 0)

            static_fields_size = self.read_unsigned_leb128(self.f)
            instance_fields_size = self.read_unsigned_leb128(self.f)
            direct_methods_size = self.read_unsigned_leb128(self.f)
            virtual_methods_size = self.read_unsigned_leb128(self.f)

            if static_fields_size > 0:
                self.console.print("\n[#ffffff]Static Fields")
                fields_table = Table(show_header=True, header_style="bold magenta")
                fields_table.add_column("Name")
                fields_table.add_column("Access Flags")

                for _ in range(static_fields_size):
                    field_idx = self.read_unsigned_leb128(self.f)
                    access_flags = self.read_unsigned_leb128(self.f)
                    fields_table.add_row(self.FieldName[field_idx],Access_Flags[access_flags])

                self.console.print(fields_table)

            if instance_fields_size > 0:
                self.console.print("\n[#ffffff]Instance Fields")
                fields_table = Table(show_header=True, header_style="bold magenta")
                fields_table.add_column("Name")
                fields_table.add_column("Access Flags")

                for _ in range(instance_fields_size):
                    field_idx = self.read_unsigned_leb128(self.f)
                    access_flags = self.read_unsigned_leb128(self.f)
                    fields_table.add_row(self.FieldName[field_idx],Access_Flags[access_flags])
                self.console.print(fields_table)

            if direct_methods_size > 0:
                self.console.print("\n[#ffffff]Direct Methods")
                previous_idx = 0
                for _ in range(direct_methods_size):
                    method_idx_diff = self.read_unsigned_leb128(self.f)
                    access_flags = self.read_unsigned_leb128(self.f)
                    code_off = self.read_unsigned_leb128(self.f)
                    
                    method_idx = previous_idx + method_idx_diff
                    previous_idx = method_idx
                    
                    self.DumpDexCode(self.MethodName[method_idx],Access_Flags[access_flags],code_off)

            if virtual_methods_size > 0:
                self.console.print("\n[#ffffff]Virtual Methods")
                previous_idx = 0
                for _ in range(virtual_methods_size):
                    method_idx_diff = self.read_unsigned_leb128(self.f)
                    access_flags = self.read_unsigned_leb128(self.f)
                    code_off = self.read_unsigned_leb128(self.f)
                    
                    method_idx = previous_idx + method_idx_diff
                    previous_idx = method_idx
                    self.DumpDexCode(self.MethodName[method_idx],Access_Flags[access_flags],code_off)
   
def dexParser(filepath):
    dex = DexParser(filepath)
    dex.header_parse()
    dex.print_headers()
    dex.MapList()
    dex.DexStrings()
    dex.DexTypes()
    dex.DexProtoItem()
    dex.DexFieldItem()
    dex.DexMethods()
    dex.DexClass()

if __name__ == '__main__':
    argparse = ArgumentParser(__doc__)
    argparse.add_argument("dex",metavar="DEX File")
    args = argparse.parse_args()
    filename = args.dex
    filepath = os.path.join(os.getcwd(),filename)
    
    if os.path.exists(filepath):
        ic('File exists')
        status = dexParser(filepath)
    else:
        ic('File doesnt exist')
        exit(-1)