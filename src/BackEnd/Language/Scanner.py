errors = []

reserveds = {
    'mkdisk'    : 'RW_mkdisk',
    'rmdisk'    : 'RW_rmdisk',
    'fdisk'     : 'RW_fdisk',
    'mount'     : 'RW_mount',
    'mkfs'      : 'RW_mkfs',
    'login'     : 'RW_login',
    'logout'    : 'RW_logout',
    'mkgrp'     : 'RW_mkgrp',
    'rmgrp'     : 'RW_rmgrp',
    'mkusr'     : 'RW_mkusr',
    'rmusr'     : 'RW_rmusr',
    'mkfile'    : 'RW_mkfile',
    'mkdir'     : 'RW_mkdir',
    'rep'       : 'RW_rep',
    'mbr'       : 'RW_mbr',
    'disk'      : 'RW_disk',
    'bm_inode'  : 'RW_bm_inode',
    'bm_block'  : 'RW_bm_block',
    'tree'      : 'RW_tree',
    'sb'        : 'RW_sb',
    'file'      : 'RW_file',
    'full'      : 'RW_full',
}

tokens = tuple(reserveds.values()) + (
    'RW_size',
    'RW_path',
    'RW_fit',
    'RW_unit',
    'RW_name',
    'RW_type',
    'RW_id',
    'RW_user',
    'RW_pass',
    'RW_grp',
    'RW_r',
    'RW_cont',
    'RW_ruta',
    'TK_number',
    'TK_path',
    'TK_unit',
    'TK_fit',
    'TK_type',
    'TK_id',
    'TK_equ',
)

m = {
    'EXT': r'[a-zA-Z0-9]+',
    'ID1': r'[a-zA-Z0-9_]+',
    'ID2': r'[a-zA-Z0-9_][a-zA-Z0-9_\s]*',
}

t_RW_size     = r'\-\s*(S|s)(I|i)(Z|z)(E|e)'
t_RW_path     = r'\-\s*(P|p)(A|a)(T|t)(H|h)'
t_RW_fit      = r'\-\s*(F|f)(I|i)(T|t)'
t_RW_unit     = r'\-\s*(U|u)(N|n)(I|i)(T|t)'
t_RW_name     = r'\-\s*(N|n)(A|a)(M|m)(E|e)'
t_RW_type     = r'\-\s*(T|t)(Y|y)(P|p)(E|e)'
t_RW_id       = r'\-\s*(I|i)(D|d)'
t_RW_user     = r'\-\s*(U|u)(S|s)(E|e)(R|r)'
t_RW_pass     = r'\-\s*(P|p)(A|a)(S|s)(S|s)'
t_RW_grp      = r'\-\s*(G|g)(R|r)(P|p)'
t_RW_r        = r'\-\s*(R|r)'
t_RW_cont     = r'\-\s*(C|c)(O|o)(N|n)(T|t)'
t_RW_ruta     = r'\-\s*(R|r)(U|u)(T|t)(A|a)'
t_TK_number   = r'\-?[0-9]+'
t_TK_path     = rf'(((\.\.|\.)?\/)*{m["ID1"]})+(\.{m["EXT"]})?|\"(((\.\.|\.)?\/)*{m["ID2"]})+(\.{m["EXT"]})?\"|/'
t_TK_equ      = r'\='

def t_TK_id(t):
    r'[a-zA-Z_0-9]+'
    if t.value.isdigit():
        t.type = 'TK_number'
    elif t.value.upper() in ['B', 'K', 'M']:
        t.type = 'TK_unit'
    elif t.value.upper() in ['BF', 'FF', 'WF']:
        t.type = 'TK_fit'
    elif t.value.upper() in ['P', 'E', 'L']:
        t.type = 'TK_type'
    else:
        t.type = reserveds.get(t.value.lower(), 'TK_id')
    return t

def t_commentary(t):
    r'\#[^\r\n]*'
    t.lexer.skip(1)

t_ignore = " \t"

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    errors.append(t.value[0])
    print(f"\033[31m -> Error: Caracter sin reconocer. «{t.value[0]}» [{t.lexer.lineno}:{t.lexer.lexpos}]\033[0m")
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

import ply.lex as Scanner
scanner = Scanner.lex()