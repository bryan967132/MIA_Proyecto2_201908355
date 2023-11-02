
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'RW_bm_block RW_bm_inode RW_cont RW_disk RW_fdisk RW_file RW_fit RW_full RW_grp RW_id RW_login RW_logout RW_mbr RW_mkdir RW_mkdisk RW_mkfile RW_mkfs RW_mkgrp RW_mkusr RW_mount RW_name RW_pass RW_path RW_r RW_rep RW_rmdisk RW_rmgrp RW_rmusr RW_ruta RW_sb RW_size RW_tree RW_type RW_unit RW_user TK_equ TK_fit TK_id TK_number TK_path TK_type TK_unit commentaryINIT : COMMANDSCOMMANDS : COMMANDS COMMAND\n                | COMMAND COMMAND  : MKDISK\n                | RMDISK\n                | FDISK\n                | MOUNT\n                | MKFS\n                | LOGIN\n                | LOGOUT\n                | MKGRP\n                | RMGRP\n                | MKUSR\n                | RMUSR\n                | MKFILE\n                | MKDIR\n                | REP\n                | COMMENTARYMKDISK   : RW_mkdisk MKDISKPARAMS\n                | RW_mkdiskMKDISKPARAMS : MKDISKPARAMS MKDISKPARAM\n                    | MKDISKPARAMMKDISKPARAM  : RW_size TK_equ TK_number\n                    | RW_path TK_equ TK_path\n                    | RW_fit  TK_equ TK_fit\n                    | RW_unit TK_equ TK_unitRMDISK   : RW_rmdisk RW_path TK_equ TK_path\n                | RW_rmdiskFDISK    : RW_fdisk FDISKPARAMS\n                | RW_fdiskFDISKPARAMS  : FDISKPARAMS FDISKPARAM\n                    | FDISKPARAMFDISKPARAM   : RW_size   TK_equ TK_number\n                    | RW_path   TK_equ TK_path\n                    | RW_name   TK_equ TK_id\n                    | RW_unit   TK_equ TK_unit\n                    | RW_type   TK_equ TK_type\n                    | RW_fit    TK_equ TK_fitMOUNT    : RW_mount MOUNTPARAMS\n                | RW_mountMOUNTPARAMS  : MOUNTPARAMS MOUNTPARAM\n                    | MOUNTPARAMMOUNTPARAM   : RW_path TK_equ TK_path\n                    | RW_name TK_equ TK_idMKFS : RW_mkfs MKFSPARAMS\n            | RW_mkfsMKFSPARAMS   : MKFSPARAMS MKFSPARAM\n                    | MKFSPARAMMKFSPARAM    : RW_id   TK_equ TK_id\n                    | RW_type TK_equ RW_fullLOGIN    : RW_login LOGINPARAMS\n                | RW_loginLOGINPARAMS  : LOGINPARAMS LOGINPARAM\n                    | LOGINPARAMLOGINPARAM   : RW_user TK_equ TK_id\n                    | RW_pass TK_equ TK_id\n                    | RW_pass TK_equ TK_number\n                    | RW_id   TK_equ TK_idLOGOUT : RW_logoutMKGRP    : RW_mkgrp RW_name TK_equ TK_id\n                | RW_mkgrpRMGRP    : RW_rmgrp RW_name TK_equ TK_id\n                | RW_rmgrpMKUSR    : RW_mkusr MKUSERPARAMS\n                | RW_mkusrMKUSERPARAMS : MKUSERPARAMS MKUSERPARAM\n                    | MKUSERPARAMMKUSERPARAM  : RW_user TK_equ TK_id\n                    | RW_pass TK_equ TK_id\n                    | RW_pass TK_equ TK_number\n                    | RW_grp  TK_equ TK_idRMUSR    : RW_rmusr RW_user TK_equ TK_id\n                | RW_rmusrMKFILE   : RW_mkfile MKFILEPARAMS\n                | RW_mkfileMKFILEPARAMS : MKFILEPARAMS MKFILEPARAM\n                    | MKFILEPARAMMKFILEPARAM  : RW_path TK_equ TK_path\n                    | RW_size TK_equ TK_number\n                    | RW_cont TK_equ TK_path\n                    | RW_rMKDIR    : RW_mkdir MKDIRPARAMS\n                | RW_mkdirMKDIRPARAMS  : MKDIRPARAMS MKDIRPARAM\n                    | MKDIRPARAMMKDIRPARAM   : RW_path TK_equ TK_path\n                    | RW_rREP  : RW_rep REPPARAMS\n            | RW_repREPPARAMS    : REPPARAMS REPPARAM\n                    | REPPARAMREPPARAM : RW_name TK_equ NAME\n                | RW_path TK_equ TK_path\n                | RW_id   TK_equ TK_id\n                | RW_ruta TK_equ TK_pathNAME : RW_mbr\n            | RW_disk\n            | RW_bm_inode\n            | RW_bm_block\n            | RW_tree\n            | RW_sb\n            | RW_fileCOMMENTARY : commentary'
    
_lr_action_items = {'RW_mkdisk':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_rmdisk':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_fdisk':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_mount':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_mkfs':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_login':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_logout':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_mkgrp':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_rmgrp':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_mkusr':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[28,28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_rmusr':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[29,29,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_mkfile':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[30,30,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_mkdir':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[31,31,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_rep':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[32,32,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'commentary':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[33,33,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,50,51,54,55,58,59,65,66,71,72,76,77,78,80,81,82,87,93,100,103,106,112,117,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-20,-28,-30,-40,-46,-52,-59,-61,-63,-65,-73,-75,-83,-89,-103,-2,-19,-22,-29,-32,-39,-42,-45,-48,-51,-54,-64,-67,-74,-77,-81,-82,-85,-87,-88,-91,-21,-31,-41,-47,-53,-66,-76,-84,-90,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-38,-43,-44,-49,-50,-55,-56,-57,-58,-60,-62,-68,-69,-70,-71,-72,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_size':([19,21,30,35,36,42,43,71,72,76,87,93,117,128,129,130,131,133,134,135,136,137,138,154,155,156,],[37,44,74,37,-22,44,-32,74,-77,-81,-21,-31,-76,-23,-24,-25,-26,-33,-34,-35,-36,-37,-38,-78,-79,-80,]),'RW_path':([19,20,21,22,30,31,32,35,36,42,43,50,51,71,72,76,77,78,80,81,82,87,93,100,117,121,123,128,129,130,131,133,134,135,136,137,138,139,140,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,],[38,41,45,52,73,79,84,38,-22,45,-32,52,-42,73,-77,-81,79,-85,-87,84,-91,-21,-31,-41,-76,-84,-90,-23,-24,-25,-26,-33,-34,-35,-36,-37,-38,-43,-44,-78,-79,-80,-86,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_fit':([19,21,35,36,42,43,87,93,128,129,130,131,133,134,135,136,137,138,],[39,49,39,-22,49,-32,-21,-31,-23,-24,-25,-26,-33,-34,-35,-36,-37,-38,]),'RW_unit':([19,21,35,36,42,43,87,93,128,129,130,131,133,134,135,136,137,138,],[40,47,40,-22,47,-32,-21,-31,-23,-24,-25,-26,-33,-34,-35,-36,-37,-38,]),'RW_name':([21,22,26,27,32,42,43,50,51,81,82,93,100,123,133,134,135,136,137,138,139,140,158,159,160,161,162,163,164,165,166,167,168,],[46,53,63,64,83,46,-32,53,-42,83,-91,-31,-41,-90,-33,-34,-35,-36,-37,-38,-43,-44,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_type':([21,23,42,43,54,55,93,103,133,134,135,136,137,138,141,142,],[48,57,48,-32,57,-48,-31,-47,-33,-34,-35,-36,-37,-38,-49,-50,]),'RW_id':([23,24,32,54,55,58,59,81,82,103,106,123,141,142,143,144,145,146,158,159,160,161,162,163,164,165,166,167,168,],[56,62,85,56,-48,62,-54,85,-91,-47,-53,-90,-49,-50,-55,-56,-57,-58,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'RW_user':([24,28,29,58,59,65,66,106,112,143,144,145,146,149,150,151,152,],[60,67,70,60,-54,67,-67,-53,-66,-55,-56,-57,-58,-68,-69,-70,-71,]),'RW_pass':([24,28,58,59,65,66,106,112,143,144,145,146,149,150,151,152,],[61,68,61,-54,68,-67,-53,-66,-55,-56,-57,-58,-68,-69,-70,-71,]),'RW_grp':([28,65,66,112,149,150,151,152,],[69,69,-67,-66,-68,-69,-70,-71,]),'RW_cont':([30,71,72,76,117,154,155,156,],[75,75,-77,-81,-76,-78,-79,-80,]),'RW_r':([30,31,71,72,76,77,78,80,117,121,154,155,156,157,],[76,80,76,-77,-81,80,-85,-87,-76,-84,-78,-79,-80,-86,]),'RW_ruta':([32,81,82,123,158,159,160,161,162,163,164,165,166,167,168,],[86,86,-91,-90,-92,-96,-97,-98,-99,-100,-101,-102,-93,-94,-95,]),'TK_equ':([37,38,39,40,41,44,45,46,47,48,49,52,53,56,57,60,61,62,63,64,67,68,69,70,73,74,75,79,83,84,85,86,],[88,89,90,91,92,94,95,96,97,98,99,101,102,104,105,107,108,109,110,111,113,114,115,116,118,119,120,122,124,125,126,127,]),'TK_number':([88,94,108,114,119,],[128,133,145,151,155,]),'TK_path':([89,92,95,101,118,120,122,125,127,],[129,132,134,139,154,156,157,166,168,]),'TK_fit':([90,99,],[130,138,]),'TK_unit':([91,97,],[131,136,]),'TK_id':([96,102,104,107,108,109,110,111,113,114,115,116,126,],[135,140,141,143,144,146,147,148,149,150,152,153,167,]),'TK_type':([98,],[137,]),'RW_full':([105,],[142,]),'RW_mbr':([124,],[159,]),'RW_disk':([124,],[160,]),'RW_bm_inode':([124,],[161,]),'RW_bm_block':([124,],[162,]),'RW_tree':([124,],[163,]),'RW_sb':([124,],[164,]),'RW_file':([124,],[165,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INIT':([0,],[1,]),'COMMANDS':([0,],[2,]),'COMMAND':([0,2,],[3,34,]),'MKDISK':([0,2,],[4,4,]),'RMDISK':([0,2,],[5,5,]),'FDISK':([0,2,],[6,6,]),'MOUNT':([0,2,],[7,7,]),'MKFS':([0,2,],[8,8,]),'LOGIN':([0,2,],[9,9,]),'LOGOUT':([0,2,],[10,10,]),'MKGRP':([0,2,],[11,11,]),'RMGRP':([0,2,],[12,12,]),'MKUSR':([0,2,],[13,13,]),'RMUSR':([0,2,],[14,14,]),'MKFILE':([0,2,],[15,15,]),'MKDIR':([0,2,],[16,16,]),'REP':([0,2,],[17,17,]),'COMMENTARY':([0,2,],[18,18,]),'MKDISKPARAMS':([19,],[35,]),'MKDISKPARAM':([19,35,],[36,87,]),'FDISKPARAMS':([21,],[42,]),'FDISKPARAM':([21,42,],[43,93,]),'MOUNTPARAMS':([22,],[50,]),'MOUNTPARAM':([22,50,],[51,100,]),'MKFSPARAMS':([23,],[54,]),'MKFSPARAM':([23,54,],[55,103,]),'LOGINPARAMS':([24,],[58,]),'LOGINPARAM':([24,58,],[59,106,]),'MKUSERPARAMS':([28,],[65,]),'MKUSERPARAM':([28,65,],[66,112,]),'MKFILEPARAMS':([30,],[71,]),'MKFILEPARAM':([30,71,],[72,117,]),'MKDIRPARAMS':([31,],[77,]),'MKDIRPARAM':([31,77,],[78,121,]),'REPPARAMS':([32,],[81,]),'REPPARAM':([32,81,],[82,123,]),'NAME':([124,],[158,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INIT","S'",1,None,None,None),
  ('INIT -> COMMANDS','INIT',1,'p_INIT','Parser.py',20),
  ('COMMANDS -> COMMANDS COMMAND','COMMANDS',2,'p_COMMANDS','Parser.py',24),
  ('COMMANDS -> COMMAND','COMMANDS',1,'p_COMMANDS','Parser.py',25),
  ('COMMAND -> MKDISK','COMMAND',1,'p_COMMAND','Parser.py',33),
  ('COMMAND -> RMDISK','COMMAND',1,'p_COMMAND','Parser.py',34),
  ('COMMAND -> FDISK','COMMAND',1,'p_COMMAND','Parser.py',35),
  ('COMMAND -> MOUNT','COMMAND',1,'p_COMMAND','Parser.py',36),
  ('COMMAND -> MKFS','COMMAND',1,'p_COMMAND','Parser.py',37),
  ('COMMAND -> LOGIN','COMMAND',1,'p_COMMAND','Parser.py',38),
  ('COMMAND -> LOGOUT','COMMAND',1,'p_COMMAND','Parser.py',39),
  ('COMMAND -> MKGRP','COMMAND',1,'p_COMMAND','Parser.py',40),
  ('COMMAND -> RMGRP','COMMAND',1,'p_COMMAND','Parser.py',41),
  ('COMMAND -> MKUSR','COMMAND',1,'p_COMMAND','Parser.py',42),
  ('COMMAND -> RMUSR','COMMAND',1,'p_COMMAND','Parser.py',43),
  ('COMMAND -> MKFILE','COMMAND',1,'p_COMMAND','Parser.py',44),
  ('COMMAND -> MKDIR','COMMAND',1,'p_COMMAND','Parser.py',45),
  ('COMMAND -> REP','COMMAND',1,'p_COMMAND','Parser.py',46),
  ('COMMAND -> COMMENTARY','COMMAND',1,'p_COMMAND','Parser.py',47),
  ('MKDISK -> RW_mkdisk MKDISKPARAMS','MKDISK',2,'p_MKDISK','Parser.py',51),
  ('MKDISK -> RW_mkdisk','MKDISK',1,'p_MKDISK','Parser.py',52),
  ('MKDISKPARAMS -> MKDISKPARAMS MKDISKPARAM','MKDISKPARAMS',2,'p_MKDISKPARAMS','Parser.py',63),
  ('MKDISKPARAMS -> MKDISKPARAM','MKDISKPARAMS',1,'p_MKDISKPARAMS','Parser.py',64),
  ('MKDISKPARAM -> RW_size TK_equ TK_number','MKDISKPARAM',3,'p_MKDISKPARAM','Parser.py',72),
  ('MKDISKPARAM -> RW_path TK_equ TK_path','MKDISKPARAM',3,'p_MKDISKPARAM','Parser.py',73),
  ('MKDISKPARAM -> RW_fit TK_equ TK_fit','MKDISKPARAM',3,'p_MKDISKPARAM','Parser.py',74),
  ('MKDISKPARAM -> RW_unit TK_equ TK_unit','MKDISKPARAM',3,'p_MKDISKPARAM','Parser.py',75),
  ('RMDISK -> RW_rmdisk RW_path TK_equ TK_path','RMDISK',4,'p_RMDISK','Parser.py',79),
  ('RMDISK -> RW_rmdisk','RMDISK',1,'p_RMDISK','Parser.py',80),
  ('FDISK -> RW_fdisk FDISKPARAMS','FDISK',2,'p_FDISK','Parser.py',89),
  ('FDISK -> RW_fdisk','FDISK',1,'p_FDISK','Parser.py',90),
  ('FDISKPARAMS -> FDISKPARAMS FDISKPARAM','FDISKPARAMS',2,'p_FDISKPARAMS','Parser.py',101),
  ('FDISKPARAMS -> FDISKPARAM','FDISKPARAMS',1,'p_FDISKPARAMS','Parser.py',102),
  ('FDISKPARAM -> RW_size TK_equ TK_number','FDISKPARAM',3,'p_FDISKPARAM','Parser.py',110),
  ('FDISKPARAM -> RW_path TK_equ TK_path','FDISKPARAM',3,'p_FDISKPARAM','Parser.py',111),
  ('FDISKPARAM -> RW_name TK_equ TK_id','FDISKPARAM',3,'p_FDISKPARAM','Parser.py',112),
  ('FDISKPARAM -> RW_unit TK_equ TK_unit','FDISKPARAM',3,'p_FDISKPARAM','Parser.py',113),
  ('FDISKPARAM -> RW_type TK_equ TK_type','FDISKPARAM',3,'p_FDISKPARAM','Parser.py',114),
  ('FDISKPARAM -> RW_fit TK_equ TK_fit','FDISKPARAM',3,'p_FDISKPARAM','Parser.py',115),
  ('MOUNT -> RW_mount MOUNTPARAMS','MOUNT',2,'p_MOUNT','Parser.py',119),
  ('MOUNT -> RW_mount','MOUNT',1,'p_MOUNT','Parser.py',120),
  ('MOUNTPARAMS -> MOUNTPARAMS MOUNTPARAM','MOUNTPARAMS',2,'p_MOUNTPARAMS','Parser.py',131),
  ('MOUNTPARAMS -> MOUNTPARAM','MOUNTPARAMS',1,'p_MOUNTPARAMS','Parser.py',132),
  ('MOUNTPARAM -> RW_path TK_equ TK_path','MOUNTPARAM',3,'p_MOUNTPARAM','Parser.py',140),
  ('MOUNTPARAM -> RW_name TK_equ TK_id','MOUNTPARAM',3,'p_MOUNTPARAM','Parser.py',141),
  ('MKFS -> RW_mkfs MKFSPARAMS','MKFS',2,'p_MKFS','Parser.py',145),
  ('MKFS -> RW_mkfs','MKFS',1,'p_MKFS','Parser.py',146),
  ('MKFSPARAMS -> MKFSPARAMS MKFSPARAM','MKFSPARAMS',2,'p_MKFSPARAMS','Parser.py',157),
  ('MKFSPARAMS -> MKFSPARAM','MKFSPARAMS',1,'p_MKFSPARAMS','Parser.py',158),
  ('MKFSPARAM -> RW_id TK_equ TK_id','MKFSPARAM',3,'p_MKFSPARAM','Parser.py',166),
  ('MKFSPARAM -> RW_type TK_equ RW_full','MKFSPARAM',3,'p_MKFSPARAM','Parser.py',167),
  ('LOGIN -> RW_login LOGINPARAMS','LOGIN',2,'p_LOGIN','Parser.py',171),
  ('LOGIN -> RW_login','LOGIN',1,'p_LOGIN','Parser.py',172),
  ('LOGINPARAMS -> LOGINPARAMS LOGINPARAM','LOGINPARAMS',2,'p_LOGINPARAMS','Parser.py',183),
  ('LOGINPARAMS -> LOGINPARAM','LOGINPARAMS',1,'p_LOGINPARAMS','Parser.py',184),
  ('LOGINPARAM -> RW_user TK_equ TK_id','LOGINPARAM',3,'p_LOGINPARAM','Parser.py',192),
  ('LOGINPARAM -> RW_pass TK_equ TK_id','LOGINPARAM',3,'p_LOGINPARAM','Parser.py',193),
  ('LOGINPARAM -> RW_pass TK_equ TK_number','LOGINPARAM',3,'p_LOGINPARAM','Parser.py',194),
  ('LOGINPARAM -> RW_id TK_equ TK_id','LOGINPARAM',3,'p_LOGINPARAM','Parser.py',195),
  ('LOGOUT -> RW_logout','LOGOUT',1,'p_LOGOUT','Parser.py',199),
  ('MKGRP -> RW_mkgrp RW_name TK_equ TK_id','MKGRP',4,'p_MKGRP','Parser.py',204),
  ('MKGRP -> RW_mkgrp','MKGRP',1,'p_MKGRP','Parser.py',205),
  ('RMGRP -> RW_rmgrp RW_name TK_equ TK_id','RMGRP',4,'p_RMGRP','Parser.py',217),
  ('RMGRP -> RW_rmgrp','RMGRP',1,'p_RMGRP','Parser.py',218),
  ('MKUSR -> RW_mkusr MKUSERPARAMS','MKUSR',2,'p_MKUSR','Parser.py',230),
  ('MKUSR -> RW_mkusr','MKUSR',1,'p_MKUSR','Parser.py',231),
  ('MKUSERPARAMS -> MKUSERPARAMS MKUSERPARAM','MKUSERPARAMS',2,'p_MKUSERPARAMS','Parser.py',242),
  ('MKUSERPARAMS -> MKUSERPARAM','MKUSERPARAMS',1,'p_MKUSERPARAMS','Parser.py',243),
  ('MKUSERPARAM -> RW_user TK_equ TK_id','MKUSERPARAM',3,'p_MKUSERPARAM','Parser.py',251),
  ('MKUSERPARAM -> RW_pass TK_equ TK_id','MKUSERPARAM',3,'p_MKUSERPARAM','Parser.py',252),
  ('MKUSERPARAM -> RW_pass TK_equ TK_number','MKUSERPARAM',3,'p_MKUSERPARAM','Parser.py',253),
  ('MKUSERPARAM -> RW_grp TK_equ TK_id','MKUSERPARAM',3,'p_MKUSERPARAM','Parser.py',254),
  ('RMUSR -> RW_rmusr RW_user TK_equ TK_id','RMUSR',4,'p_RMUSR','Parser.py',258),
  ('RMUSR -> RW_rmusr','RMUSR',1,'p_RMUSR','Parser.py',259),
  ('MKFILE -> RW_mkfile MKFILEPARAMS','MKFILE',2,'p_MKFILE','Parser.py',270),
  ('MKFILE -> RW_mkfile','MKFILE',1,'p_MKFILE','Parser.py',271),
  ('MKFILEPARAMS -> MKFILEPARAMS MKFILEPARAM','MKFILEPARAMS',2,'p_MKFILEPARAMS','Parser.py',282),
  ('MKFILEPARAMS -> MKFILEPARAM','MKFILEPARAMS',1,'p_MKFILEPARAMS','Parser.py',283),
  ('MKFILEPARAM -> RW_path TK_equ TK_path','MKFILEPARAM',3,'p_MKFILEPARAM','Parser.py',291),
  ('MKFILEPARAM -> RW_size TK_equ TK_number','MKFILEPARAM',3,'p_MKFILEPARAM','Parser.py',292),
  ('MKFILEPARAM -> RW_cont TK_equ TK_path','MKFILEPARAM',3,'p_MKFILEPARAM','Parser.py',293),
  ('MKFILEPARAM -> RW_r','MKFILEPARAM',1,'p_MKFILEPARAM','Parser.py',294),
  ('MKDIR -> RW_mkdir MKDIRPARAMS','MKDIR',2,'p_MKDIR','Parser.py',301),
  ('MKDIR -> RW_mkdir','MKDIR',1,'p_MKDIR','Parser.py',302),
  ('MKDIRPARAMS -> MKDIRPARAMS MKDIRPARAM','MKDIRPARAMS',2,'p_MKDIRPARAMS','Parser.py',313),
  ('MKDIRPARAMS -> MKDIRPARAM','MKDIRPARAMS',1,'p_MKDIRPARAMS','Parser.py',314),
  ('MKDIRPARAM -> RW_path TK_equ TK_path','MKDIRPARAM',3,'p_MKDIRPARAM','Parser.py',322),
  ('MKDIRPARAM -> RW_r','MKDIRPARAM',1,'p_MKDIRPARAM','Parser.py',323),
  ('REP -> RW_rep REPPARAMS','REP',2,'p_REP','Parser.py',330),
  ('REP -> RW_rep','REP',1,'p_REP','Parser.py',331),
  ('REPPARAMS -> REPPARAMS REPPARAM','REPPARAMS',2,'p_REPPARAMS','Parser.py',342),
  ('REPPARAMS -> REPPARAM','REPPARAMS',1,'p_REPPARAMS','Parser.py',343),
  ('REPPARAM -> RW_name TK_equ NAME','REPPARAM',3,'p_REPPARAM','Parser.py',351),
  ('REPPARAM -> RW_path TK_equ TK_path','REPPARAM',3,'p_REPPARAM','Parser.py',352),
  ('REPPARAM -> RW_id TK_equ TK_id','REPPARAM',3,'p_REPPARAM','Parser.py',353),
  ('REPPARAM -> RW_ruta TK_equ TK_path','REPPARAM',3,'p_REPPARAM','Parser.py',354),
  ('NAME -> RW_mbr','NAME',1,'p_NAME','Parser.py',358),
  ('NAME -> RW_disk','NAME',1,'p_NAME','Parser.py',359),
  ('NAME -> RW_bm_inode','NAME',1,'p_NAME','Parser.py',360),
  ('NAME -> RW_bm_block','NAME',1,'p_NAME','Parser.py',361),
  ('NAME -> RW_tree','NAME',1,'p_NAME','Parser.py',362),
  ('NAME -> RW_sb','NAME',1,'p_NAME','Parser.py',363),
  ('NAME -> RW_file','NAME',1,'p_NAME','Parser.py',364),
  ('COMMENTARY -> commentary','COMMENTARY',1,'p_COMMENTARY','Parser.py',368),
]
