from Structures.SuperBlock import *
from Structures.InodesTable import *
from Structures.BlockFolder import *
from Structures.BlockFile import *
from Structures.User import *
from Structures.Group import *
from io import BufferedRandom
from typing import List, Tuple

class Tree:
    def __init__(self, superBlock: SuperBlock, file: BufferedRandom):
        self.superBlock: SuperBlock = superBlock
        self.file: BufferedRandom = file
        self.blocks = []
        self.fileBlocks = []

# ============================== GRAPH TREE ================================

    def getDot(self, diskname, partName) -> str:
        dot: str = 'digraph Tree{\n\tnode [shape=plaintext];\n\trankdir=LR;\n\t'
        dot += f'label="{diskname}: {partName}";\n\tlabelloc=t;\n\t'
        dot += self.__getDotInode(0)
        dot += '\n}'
        return dot

    def __getDotInode(self, i) -> str:
        self.file.seek(self.superBlock.inode_start + i * InodesTable.sizeOf())
        inode: InodesTable = InodesTable.decode(self.file.read(InodesTable.sizeOf()))
        dot = inode.getDot(i)
        for p in range(len(inode.block)):
            if inode.block[p] != -1:
                if inode.type == '0':
                    dot += '\n\t' + self.__getDotBlockFolder(inode.block[p])
                else:
                    dot += '\n\t' + self.__getDotBlockFile(inode.block[p])
                dot += f'\n\tinode{i}:A{p} -> block{inode.block[p]}:B{inode.block[p]};'
        return dot

    def __getDotBlockFolder(self, i) -> str:
        self.file.seek(self.superBlock.block_start + i * BlockFolder.sizeOf())
        blockFolder: BlockFolder = BlockFolder.decode(self.file.read(BlockFolder.sizeOf()))
        dot = blockFolder.getDot(i)
        for p in range(len(blockFolder.content)):
            if not blockFolder.content[p].name.strip() in ['.', '..'] and blockFolder.content[p].inodo != -1:
                dot += '\n\t' + self.__getDotInode(blockFolder.content[p].inodo)
                dot += f'\n\tblock{i}:A{p} -> inode{blockFolder.content[p].inodo}:I{blockFolder.content[p].inodo};'
        return dot

    def __getDotBlockFile(self, i) -> str:
        self.file.seek(self.superBlock.block_start + i * BlockFile.sizeOf())
        blockFile: BlockFile = BlockFile.decode(self.file.read(BlockFile.sizeOf()))
        return blockFile.getDot(i)

# ================================== READ CONTENT ==================================

    def readFile(self, path: str) -> Tuple[str, bool]:
        dir = [i for i in path.split('/') if i != '']
        return self.__readFileInInodes(0, dir)

    def __readFileInInodes(self, i, path: List[str]) -> Tuple[str, bool]:
        self.file.seek(self.superBlock.inode_start + i * InodesTable.sizeOf())
        inode: InodesTable = InodesTable.decode(self.file.read(InodesTable.sizeOf()))
        content = ''
        founded = False
        for p in range(len(inode.block)):
            if inode.block[p] != -1:
                if inode.type == '0':
                    content, founded = self.__readFileInBlockFolder(inode.block[p], path)
                    if founded:
                        return content, founded
                else:
                    cont, founded = self.__readFileInBlockFile(inode.block[p])
                    content += cont
        return content, founded

    def __readFileInBlockFolder(self, i, path: List[str]) -> Tuple[str, bool]:
        self.file.seek(self.superBlock.block_start + i * BlockFolder.sizeOf())
        blockFolder: BlockFolder = BlockFolder.decode(self.file.read(BlockFolder.sizeOf()))
        for p in range(len(blockFolder.content)):
            if not blockFolder.content[p].name.strip() in ['.', '..'] and blockFolder.content[p].inodo != -1 and blockFolder.content[p].name.strip() == path[0]:
                path.pop(0)
                return self.__readFileInInodes(blockFolder.content[p].inodo, path)
        return '', False

    def __readFileInBlockFile(self, i) -> Tuple[str, bool]:
        self.file.seek(self.superBlock.block_start + i * BlockFile.sizeOf())
        blockFile: BlockFile = BlockFile.decode(self.file.read(BlockFile.sizeOf()))
        return ''.join(blockFile.content), True

# ================================= WRITE FILE ===================================

    def writeFile(self, path: str, diskpath: str, partstart: int, newContent: str):
        dir = [i for i in path.split('/') if i != '']
        self.__writeFileInInodes(0, dir, diskpath, newContent, partstart)
        self.superBlock.first_blo = self.__findNextFreeBlock(1)[0]
        self.superBlock.first_ino = self.__findNextFreeInode(1)[0]

    def __writeFileInInodes(self, i: int, path: List[str], pathdsk, newContent: str, partstart: int):
        self.file.seek(self.superBlock.inode_start + i * InodesTable.sizeOf())
        inode: InodesTable = InodesTable.decode(self.file.read(InodesTable.sizeOf()))
        if inode.type == '0':
            for p in range(len(inode.block)):
                if inode.block[p] != -1:
                    writed = self.__writeFileInBlockFolder(inode.block[p], path, pathdsk, newContent, partstart)
                    if writed:
                        return
        else:
            blocksFile: Tuple[int, BlockFile] = -1, None
            for p in range(len(inode.block)):
                if inode.block[p] != -1:
                    blocksFile = self.__writeFileInBlockFile(inode.block[p])
            num, block = blocksFile
            if not block:
                block = BlockFile(['' for i in range(64)])
                num = self.__findNextFreeBlock(1)[0]
                self.__writeNewBlock(pathdsk, num, block)
                inode.block[0] = num
                self.__rewriteInode(pathdsk, i, inode)
            contents = [[r for r in block.content if r != '']]
            for z in newContent:
                if len(contents[-1]) < 64:
                    contents[-1].append(z)
                else:
                    contents.append([z])
            block.content = contents.pop(0)
            self.writeInDisk(pathdsk, self.superBlock.block_start + num * BlockFile.sizeOf(), block.encode())
            newSizeInode = (num - 1) * 64 + len(block.content)
            while len(contents) > 0:
                newBlock: BlockFile = BlockFile(['' for i in range(64)])
                contenew = contents.pop(0)
                newSizeInode = (num - 1) * 64 + len(contenew)
                if len(newBlock.content) == len(contenew):
                    newBlock.content = contenew
                else:
                    for z in range(len(contenew)):
                        newBlock.content[z] = contenew[z]
                nextFreeBitBlock = self.__findNextFreeBlock(1)
                for h in range(len(inode.block)):
                    if inode.block[h] == -1:
                        inode.block[h] = nextFreeBitBlock[0]
                        self.writeInDisk(pathdsk, self.superBlock.bm_block_start + nextFreeBitBlock[0], b'1')
                        self.writeInDisk(pathdsk, self.superBlock.block_start + nextFreeBitBlock[0] * BlockFile.sizeOf(), newBlock.encode())
                        self.superBlock.first_blo = self.__findNextFreeBlock(1)[0]
                        self.superBlock.free_blocks_count -= 1
                        self.writeInDisk(pathdsk, partstart, self.superBlock.encode())
                        break
            inode.size = newSizeInode
            self.writeInDisk(pathdsk, self.superBlock.inode_start + i * InodesTable.sizeOf(), inode.encode())

    def __writeFileInBlockFolder(self, i, path: List[str], pathdsk, content: str, partstart: int):
        self.file.seek(self.superBlock.block_start + i * BlockFolder.sizeOf())
        blockFolder: BlockFolder = BlockFolder.decode(self.file.read(BlockFolder.sizeOf()))
        for p in range(len(blockFolder.content)):
            if not blockFolder.content[p].name.strip() in ['.', '..'] and blockFolder.content[p].inodo != -1 and blockFolder.content[p].name.strip() == path[0]:
                path.pop(0)
                self.__writeFileInInodes(blockFolder.content[p].inodo, path, pathdsk, content, partstart)
                return True

    def __writeFileInBlockFile(self, i) -> Tuple[int, BlockFile]:
        self.file.seek(self.superBlock.block_start + i * BlockFile.sizeOf())
        blockFile: BlockFile = BlockFile.decode(self.file.read(BlockFile.sizeOf()))
        return i, blockFile

# =========================================== MKDIR AND MKFILE =============================================

    def mkdir(self, path: str, diskpath: str):
        dir = [i for i in path.split('/') if i != '']
        self.current = 0
        self.prev = 0
        self.dir = True
        result = self.__mkdirInInode(0, dir, diskpath)
        self.superBlock.first_blo = self.__findNextFreeBlock(1)[0]
        self.superBlock.first_ino = self.__findNextFreeInode(1)[0]
        return result

    def mkfile(self, path: str, diskpath: str):
        dir = [i for i in path.split('/') if i != '']
        self.current = 0
        self.prev = 0
        self.dir = False
        result = self.__mkdirInInode(0, dir, diskpath)
        self.superBlock.first_blo = self.__findNextFreeBlock(1)[0]
        self.superBlock.first_ino = self.__findNextFreeInode(1)[0]
        return result

    def __mkdirInInode(self, i: int, path: list[str], pathdsk: str):
        self.file.seek(self.superBlock.inode_start + i * InodesTable.sizeOf())
        inode: InodesTable = InodesTable.decode(self.file.read(InodesTable.sizeOf()))
        self.prev = self.current
        self.current = i
        for p in range(len(inode.block)):
            if inode.block[p] != -1:
                mkdirBlockFolder = self.__mkdirInBlockFolder(inode.block[p], path, pathdsk)
                if mkdirBlockFolder:
                    return mkdirBlockFolder
            else:
                inode.block[p] = self.__findNextFreeBlock(1)[0]
                self.__rewriteInode(pathdsk, i, inode)
                newBlockFolder: BlockFolder = BlockFolder([Content() for i in range(4)])
                self.__writeNewBlock(pathdsk, inode.block[p], newBlockFolder)
                return self.__mkdirInBlockFolder(inode.block[p], path, pathdsk)

    def __mkdirInBlockFolder(self, i, path: list[str], pathdsk: str) -> bool:
        self.file.seek(self.superBlock.block_start + i * BlockFolder.sizeOf())
        blockFolder: BlockFolder = BlockFolder.decode(self.file.read(BlockFolder.sizeOf()))
        if len(path) > 1:
            for p in range(len(blockFolder.content)):
                if blockFolder.content[p].inodo != -1 and blockFolder.content[p].name.strip() == path[0]:
                    path.pop(0)
                    return self.__mkdirInInode(blockFolder.content[p].inodo, path, pathdsk)
        else:
            for p in range(len(blockFolder.content)):
                if blockFolder.content[p].inodo == -1:
                    blockFolder.content[p].name = path[0].ljust(12)
                    blockFolder.content[p].inodo = self.__findNextFreeInode(1)[0]
                    self.__rewriteBlock(pathdsk, i, blockFolder)

                    if self.dir:
                        newInode: InodesTable = InodesTable()
                        newInode.block[0] = self.__findNextFreeBlock(1)[0]
                        self.__writeNewInode(pathdsk, blockFolder.content[p].inodo, newInode)

                        self.prev = self.current
                        self.current = blockFolder.content[p].inodo

                        firstBlockFolder: BlockFolder = BlockFolder([Content() for i in range(4)])
                        firstBlockFolder.content[0] = Content('.'.ljust(12), self.current)
                        firstBlockFolder.content[1] = Content('..'.ljust(12), self.prev)
                        self.__writeNewBlock(pathdsk, newInode.block[0], firstBlockFolder)
                    else:
                        newInode: InodesTable = InodesTable(type = '1', block = [-1 for i in range(15)])
                        self.__writeNewInode(pathdsk, blockFolder.content[p].inodo, newInode)
                    return True
        return False

    def __writeNewBlock(self, pathdsk: str, numBlock: int, blockFolder: BlockFolder):
        self.writeInDisk(pathdsk, self.superBlock.block_start + numBlock * BlockFolder.sizeOf(), blockFolder.encode())
        self.writeInDisk(pathdsk, self.superBlock.bm_block_start + numBlock, b'1')
        self.superBlock.free_blocks_count -= 1

    def __writeNewInode(self, pathdsk: str, numInode: int, inode: InodesTable):
        self.writeInDisk(pathdsk, self.superBlock.inode_start + numInode * InodesTable.sizeOf(), inode.encode())
        self.writeInDisk(pathdsk, self.superBlock.bm_inode_start + numInode, b'1')
        self.superBlock.free_inodes_count -= 1

    def __rewriteBlock(self, pathdsk: str, numBlock: int, blockFolder: BlockFolder):
        self.writeInDisk(pathdsk, self.superBlock.block_start + numBlock * BlockFolder.sizeOf(), blockFolder.encode())

    def __rewriteInode(self, pathdsk: str, numInode: int, inode: InodesTable):
        self.writeInDisk(pathdsk, self.superBlock.inode_start + numInode * InodesTable.sizeOf(), inode.encode())

# =========================================== SEARCH DIRECTORY =============================================

    def searchdir(self, path: str):
        dir = [i for i in path.split('/') if i != '']
        return self.__searchdirInInode(0, dir)

    def __searchdirInInode(self, i: int, path: list[str]):
        self.file.seek(self.superBlock.inode_start + i * InodesTable.sizeOf())
        inode: InodesTable = InodesTable.decode(self.file.read(InodesTable.sizeOf()))
        result = False
        for p in range(len(inode.block)):
            if inode.block[p] != -1:
                searchdirBlockFolder = self.__searchdirInBlockFolder(inode.block[p], path)
                if searchdirBlockFolder:
                    return searchdirBlockFolder
        return result

    def __searchdirInBlockFolder(self, i, path: list[str]) -> bool:
        self.file.seek(self.superBlock.block_start + i * BlockFolder.sizeOf())
        blockFolder: BlockFolder = BlockFolder.decode(self.file.read(BlockFolder.sizeOf()))
        if len(path) > 1:
            for p in range(len(blockFolder.content)):
                if blockFolder.content[p].inodo != -1 and blockFolder.content[p].name.strip() == path[0]:
                    path.pop(0)
                    return self.__searchdirInInode(blockFolder.content[p].inodo, path)
        else:
            for p in range(len(blockFolder.content)):
                if blockFolder.content[p].inodo != -1 and blockFolder.content[p].name.strip() == path[0]:
                    path.pop(0)
                    return True
        return False

# ========================================= FIND NEXT BIT =============================================

    def __findNextFreeInode(self, count: int):
        self.file.seek(self.superBlock.bm_inode_start)
        bm_inode = self.file.read(self.superBlock.inodes_count).decode('utf-8')
        freeBlocks = []
        for i in range(len(bm_inode)):
            if len(freeBlocks) == count:
                break
            if bm_inode[i] == '0':
                freeBlocks.append(i)
        return freeBlocks

    def __findNextFreeBlock(self, count: int):
        self.file.seek(self.superBlock.bm_block_start)
        bm_block = self.file.read(self.superBlock.blocks_count).decode('utf-8')
        freeBlocks = []
        for i in range(len(bm_block)):
            if len(freeBlocks) == count:
                break
            if bm_block[i] == '0':
                freeBlocks.append(i)
        return freeBlocks

# ========================================= USERS AND GROUPS ===============================================

    def getUsers(self, content) -> List[User]:
        users: list[User] = []
        registers = [[j.strip() for j in i.split(',')] for i in content.split('\n') if i.strip() != '']
        for reg in registers:
            if reg[1] == 'U' and reg[0] != '0':
                users.append(User(reg[0], reg[2], reg[3], reg[4]))
        return users

    def getGroups(self, content) -> List[Group]:
        users: list[Group] = []
        registers = [[j.strip() for j in i.split(',')] for i in content.split('\n') if i.strip() != '']
        for reg in registers:
            if reg[1] == 'G' and reg[0] != '0':
                users.append(Group(reg[0], reg[2]))
        return users

# ========================================== WRITE IN DISK =================================================

    def writeInDisk(self, path: str, seek: int, content: bytes):
        with open(path, 'r+b') as file:
            file.seek(seek)
            file.write(content)