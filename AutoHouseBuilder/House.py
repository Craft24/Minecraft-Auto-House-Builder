import mcpi.minecraft as minecraft
import random as rn
import mcpi.block as block
import math
import sys
mc = minecraft.Minecraft()
import time


#時間測定
time_sta = time.time()
#領域決定
PP = mc.player.getPos()

end_baseX = PP.x + rn.randint(12, 16)
end_baseY = PP.y - 1
end_baseZ = PP.z + rn.randint(12, 16)


for goldY in range(3):
    for goldX in range(25):
        for goldZ in range(25):
            if mc.getBlockWithData(PP.x + goldX, round(PP.y + goldY - 2), PP.z + goldZ) == block.GOLD_BLOCK:
                end_baseX = PP.x + goldX
                end_baseY = PP.y - 1
                end_baseZ = PP.z + goldZ


first_baseX = (PP.x + 1)
first_baseY = (PP.y - 1)
first_baseZ = (PP.z + 1)


#地面ブロック
regionB1 = rn.randint(1, 10)
if regionB1 <= 6:
    regionB = block.GRASS
elif regionB1 <= 7:
    regionB = block.DIRT_PODZOL
elif regionB1 <= 8:
    regionB = block.GRAVEL
elif regionB1 <= 9:
    regionB = block.STONE
else:
    regionB = block.STONE_ANDESITE

mc.setBlocks(first_baseX, first_baseY, first_baseZ, end_baseX, end_baseY, end_baseZ, regionB)

#柵
wall1 = rn.randint(1, 5)
if wall1 == 1:
    wallB = block.STONE_BRICK
    wallC = block.STONE_BRICK
elif wall1 == 2:
    wallB = block.STONE_BRICK
    wallC = block.IRON_BARS
elif wall1 == 3:
    wallB = block.STONE_SLAB_DOUBLE
    wallC = block.IRON_BARS
elif wall1 == 4:
    wallB = block.CONCRETE_BLOCK_WHITE
    wallC = block.IRON_BARS
elif wall1 == 5:
    wallB = block.CONCRETE_BLOCK_LIGHT_GRAY
    wallC = block.IRON_BARS
else:
    wallB = block.AIR
    wallC = block.AIR
#設置
mc.setBlocks(first_baseX, first_baseY + 1, first_baseZ, end_baseX, end_baseY + 1, end_baseZ, wallB)
mc.setBlocks(first_baseX, first_baseY + 2, first_baseZ, end_baseX, end_baseY + 2, end_baseZ, wallC)
mc.setBlocks(first_baseX + 1, first_baseY + 1, first_baseZ + 1, end_baseX - 1, end_baseY + 2, end_baseZ - 1, block.AIR)

#草
rangeC = rn.randint(40, 90)
rengeD = rn.randint(50, 150)

for i in range(rengeD):
    ranX1 = (first_baseX + 1)
    ranX2 = (end_baseX - 1)
    ranZ1 = (first_baseZ + 1)
    ranZ2 = (end_baseZ - 1)

    ranX = rn.uniform(ranX1, ranX2)
    ranXA = rn.uniform(ranX1, ranX2)
    ranZ = rn.uniform(ranZ1, ranZ2)
    ranZA = rn.uniform(ranZ1, ranZ2)

    if regionB1 <= 7:
        mc.setBlock(ranX, first_baseY + 1, ranZ, 31, 1)

for i in range(rangeC):
    ranX1 = (first_baseX + 1)
    ranX2 = (end_baseX - 1)
    ranZ1 = (first_baseZ + 1)
    ranZ2 = (end_baseZ - 1)

    ranX = rn.uniform(ranX1, ranX2)
    ranXA = rn.uniform(ranX1, ranX2)
    ranZ = rn.uniform(ranZ1, ranZ2)
    ranZA = rn.uniform(ranZ1, ranZ2)

    if regionB1 <= 7:
        mc.setBlock(ranX, first_baseY + 1, ranZ, 18, 12)
        mc.setBlock(ranXA, first_baseY + 2, ranZA, 18, 12)
        mc.setBlock(ranXA, first_baseY + 1, ranZA, block.FENCE)


#家本体
#素材
Hbase1 = rn.randint(1, 12)
if Hbase1 == 1:
    Hmat = block.CONCRETE_BLOCK_WHITE
elif Hbase1 == 2:
    Hmat = block.CONCRETE_POWDER_WHITE
elif Hbase1 == 3:
    Hmat = block.CONCRETE_BLOCK_LIGHT_GRAY
elif Hbase1 == 4:
    Hmat = block.CONCRETE_POWDER_LIGHT_GRAY
elif Hbase1 == 5:
    Hmat = block.WOOD_PLANKS_BIRCH
elif Hbase1 == 6:
    Hmat = block.WOOD_PLANKS_SPRUCE
elif Hbase1 == 7:
    Hmat = block.SAND
elif Hbase1 == 8:
    Hmat = block.HARDENED_CLAY_STAINED_LIGHT_GRAY
elif Hbase1 == 9:
    Hmat = block.HARDENED_CLAY_STAINED_WHITE
elif Hbase1 == 10:
    Hmat = block.STONE_DIORITE
elif Hbase1 == 11:
    Hmat = block.QUARTZ_BLOCK
else:
    Hmat = block.WOOD_PLANKS_OAK

Hmat2B = rn.randint(1, 18)
if Hmat2B == 1:
    Hmat2 = block.CONCRETE_BLOCK_WHITE
elif Hmat2B == 2:
    Hmat2 = block.CONCRETE_POWDER_WHITE
elif Hmat2B == 3:
    Hmat2 = block.CONCRETE_BLOCK_LIGHT_GRAY
elif Hmat2B == 4:
    Hmat2 = block.CONCRETE_POWDER_LIGHT_GRAY
elif Hmat2B == 5:
    Hmat2 = block.WOOD_PLANKS_BIRCH
elif Hmat2B == 6:
    Hmat2 = block.SAND
elif Hmat2B == 7:
    Hmat2 = block.HARDENED_CLAY_STAINED_LIGHT_GRAY
elif Hmat2B == 8:
    Hmat2 = block.HARDENED_CLAY_STAINED_WHITE
elif Hmat2B == 9:
    Hmat2 = block.STONE_DIORITE
elif Hmat2B == 10:
    Hmat2 = block.QUARTZ_BLOCK
else:
    Hmat2 = Hmat

#形
HbaseA = rn.randint(2, 3)
HbaseB = rn.randint(2, 3)
HbaseC = rn.randint(2, 3)
HbaseD = rn.randint(2, 3)
#二階の素材
mc.setBlocks(first_baseX + HbaseA, first_baseY + 1, first_baseZ + HbaseB, end_baseX - HbaseC, end_baseY + 4, end_baseZ - HbaseD, Hmat)
mc.setBlocks(first_baseX + HbaseA, first_baseY + 5, first_baseZ + HbaseB, end_baseX - HbaseC, end_baseY + 7, end_baseZ - HbaseD, Hmat2)

NW_x = first_baseX + HbaseA
NW_z = first_baseZ + HbaseB
NE_x = end_baseX - HbaseC
NE_z = first_baseZ + HbaseB
SW_x = first_baseX + HbaseA
SW_z = end_baseZ - HbaseD
SE_x = end_baseX - HbaseC
SE_z = end_baseZ - HbaseD

NW_xa = round(first_baseX + HbaseA - 1)
NW_za = round(first_baseZ + HbaseB - 1)
NE_xa = round(end_baseX - HbaseC)
NE_za = round(first_baseZ + HbaseB)
SW_xa = round(first_baseX + HbaseA)
SW_za = round(end_baseZ - HbaseD)
SE_xa = round(end_baseX - HbaseC)
SE_za = round(end_baseZ - HbaseD)

#角の消去
CC3 = 10
CC3a = 10
F2S = 1

Hs1 = rn.randint(1, 10)  #屋根の形抽選1~10
if Hs1 <= 6:
    CC1 = rn.randint(1, 7)
    CC1a = rn.randint(0, 1)
    if CC1 <= 4:
        mc.setBlocks(NW_x, first_baseY + 1, NW_z, NW_x + CC1, first_baseY + 7, NW_z + CC1a, block.AIR)
    CC2 = rn.randint(1, 7)
    CC2a = 0
    if CC2 <= 4:
        mc.setBlocks(NE_x, first_baseY + 1, NE_z, NE_x - CC2a, first_baseY + 7, NE_z + CC2, block.AIR)

    # 南
    CC3 = rn.randint(2, 7)
    CC3a = rn.randint(0, 1)
    if CC3 <= 5:
        mc.setBlocks(SW_x, first_baseY + 1, SW_z, SW_x + CC3, first_baseY + 7, SW_z - CC3a, block.AIR)

    CC4 = rn.randint(1, 7)
    CC4a = 0
    if CC4 <= 4:
        mc.setBlocks(SE_x, first_baseY + 1, SE_z, SE_x - CC4a, first_baseY + 7, SE_z - CC4, block.AIR)
    # 二階
    F2E = rn.randint(0, 2)
    F2W = rn.randint(0, 2)
    F2S = rn.randint(0, 0)
    F2N = rn.randint(0, 1)

    if F2E <= 0:
        mc.setBlocks(NE_x, first_baseY + 5, NE_z, SE_x - F2E, first_baseY + 7, SE_z, block.AIR)
    if F2W <= 0:
        mc.setBlocks(NW_x, first_baseY + 5, NW_z, SW_x + F2W, first_baseY + 7, SW_z, block.AIR)
    if F2N <= 0:
        mc.setBlocks(NW_x, first_baseY + 5, NW_z, NE_x, first_baseY + 7, NE_z + F2N, block.AIR)
    if F2S <= 0:
        mc.setBlocks(SW_x, first_baseY + 5, SW_z, SE_x, first_baseY + 7, SE_z - F2S, block.AIR)

#家の中心検出
House_center_x = round((NE_x + NW_x)/2)
House_center_z = round((NE_z + NW_z)/2)

#屋根
roofB1 = rn.randint(1, 8)
if roofB1 <= 2:#ネザーレンガ
    roofB = 44, 6
    roofT = 44, 14
    roofFull = 112
    roofSE = 114, 5
    roofSW = 114, 4
elif roofB1 == 3:#丸石
    roofB = 44, 3
    roofT = 44, 11
    roofFull = 4
    roofSE = 67, 5
    roofSW = 67, 4
elif roofB1 <= 5:#ダークオーク
    roofB = 126, 5
    roofT = 126, 13
    roofFull = 5, 5
    roofSE = 164, 5
    roofSW = 164, 4
elif roofB1 == 6:#マツ
    roofB = 126, 1
    roofT = 126, 9
    roofFull = 5, 1
    roofSE = 134, 5
    roofSW = 134, 4
elif roofB1 == 7:#石レンガ
    roofB = 44, 5
    roofT = 44, 13
    roofFull = 98
    roofSE = 109, 5
    roofSW = 109, 4
elif roofB1 == 8:#レンガ
    roofB = 44, 4
    roofT = 44, 12
    roofFull = 45
    roofSE = 108, 5
    roofSW = 108, 4

#縁
if Hs1 <= 6:
    for roofEdgeZ in range(25):
        for roofEdgeX in range(25):
            if mc.getBlockWithData(first_baseX + roofEdgeX, first_baseY + 7, first_baseZ + roofEdgeZ) == Hmat2:
                if mc.getBlockWithData(first_baseX + roofEdgeX + 1, first_baseY + 7, first_baseZ + roofEdgeZ + 1) == block.AIR:
                    mc.setBlock(first_baseX + roofEdgeX + 1, first_baseY + 7, first_baseZ + roofEdgeZ + 1, roofT)
                if mc.getBlockWithData(first_baseX + roofEdgeX - 1, first_baseY + 7, first_baseZ + roofEdgeZ + 1) == block.AIR:
                    mc.setBlock(first_baseX + roofEdgeX - 1, first_baseY + 7, first_baseZ + roofEdgeZ + 1, roofT)
                if mc.getBlockWithData(first_baseX + roofEdgeX + 1, first_baseY + 7, first_baseZ + roofEdgeZ - 1) == block.AIR:
                    mc.setBlock(first_baseX + roofEdgeX + 1, first_baseY + 7, first_baseZ + roofEdgeZ - 1, roofT)
                if mc.getBlockWithData(first_baseX + roofEdgeX - 1, first_baseY + 7, first_baseZ + roofEdgeZ - 1) == block.AIR:
                    mc.setBlock(first_baseX + roofEdgeX - 1, first_baseY + 7, first_baseZ + roofEdgeZ - 1, roofT)


if Hs1 == 7:
    for roofEdge in range(1500):
        randomX = rn.randint(NW_xa - 1, NE_xa + 1)
        randomZ = rn.randint(NW_za - 1, SW_za + 1)
        roofN1 = mc.getBlockWithData(randomX + 1, first_baseY + 7, randomZ)
        roofN2 = mc.getBlockWithData(randomX - 1, first_baseY + 7, randomZ)

        if roofN1 == Hmat2 or roofN2 == Hmat2:
            if mc.getBlock(randomX, first_baseY + 7, randomZ) == block.AIR:
                mc.setBlock(randomX, first_baseY + 7, randomZ, roofT)
if Hs1 == 8:
    for roofEdge in range(1500):
        randomX = rn.randint(NW_xa - 1, NE_xa + 1)
        randomZ = rn.randint(NW_za - 1, SW_za + 1)
        roofN1 = mc.getBlockWithData(randomX, first_baseY + 7, randomZ + 1)
        roofN2 = mc.getBlockWithData(randomX, first_baseY + 7, randomZ - 1)

        if roofN1 == Hmat2 or roofN2 == Hmat2:
            if mc.getBlock(randomX, first_baseY + 7, randomZ) == block.AIR:
                mc.setBlock(randomX, first_baseY + 7, randomZ, roofT)

if Hs1 >= 9:
    os1 = rn.randint(1, 4)#1~4
else:
    os1 = 0


#端の探索
for Edge1 in range(1000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    mc.getBlockWithData(randomX, first_baseY + 7, randomZ)
    if mc.getBlockWithData(randomX, first_baseY + 7, randomZ) == Hmat2:
        if mc.getBlockWithData(randomX + 1, first_baseY + 7, randomZ) == Hmat2:
            if mc.getBlockWithData(randomX, first_baseY + 7, randomZ + 1) == Hmat2:
                if mc.getBlockWithData(randomX, first_baseY + 7, randomZ - 1) != Hmat2:
                    if mc.getBlockWithData(randomX - 1, first_baseY + 7, randomZ) != Hmat2:
                        NWe_x = randomX
                        NWe_z = randomZ
for Edge2 in range(1000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    mc.getBlockWithData(randomX, first_baseY + 7, randomZ)
    if mc.getBlockWithData(randomX, first_baseY + 7, randomZ) == Hmat2:
        if mc.getBlockWithData(randomX + 1, first_baseY + 7, randomZ) == Hmat2:
            if mc.getBlockWithData(randomX, first_baseY + 7, randomZ + 1) != Hmat2:
                if mc.getBlockWithData(randomX, first_baseY + 7, randomZ - 1) == Hmat2:
                    if mc.getBlockWithData(randomX - 1, first_baseY + 7, randomZ) != Hmat2:
                        SWe_x = randomX
                        SWe_z = randomZ
for Edge3 in range(1000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    mc.getBlockWithData(randomX, first_baseY + 7, randomZ)
    if mc.getBlockWithData(randomX, first_baseY + 7, randomZ) == Hmat2:
        if mc.getBlockWithData(randomX + 1, first_baseY + 7, randomZ) != Hmat2:
            if mc.getBlockWithData(randomX, first_baseY + 7, randomZ + 1) != Hmat2:
                if mc.getBlockWithData(randomX, first_baseY + 7, randomZ - 1) == Hmat2:
                    if mc.getBlockWithData(randomX - 1, first_baseY + 7, randomZ) == Hmat2:
                        SEe_x = randomX
                        SEe_z = randomZ
for Edge4 in range(1000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    mc.getBlockWithData(randomX, first_baseY + 7, randomZ)
    if mc.getBlockWithData(randomX, first_baseY + 7, randomZ) == Hmat2:
        if mc.getBlockWithData(randomX + 1, first_baseY + 7, randomZ) != Hmat2:
            if mc.getBlockWithData(randomX, first_baseY + 7, randomZ + 1) == Hmat2:
                if mc.getBlockWithData(randomX, first_baseY + 7, randomZ - 1) != Hmat2:
                    if mc.getBlockWithData(randomX - 1, first_baseY + 7, randomZ) == Hmat2:
                        NEe_x = randomX
                        NEe_z = randomZ
#屋根
if Hs1 <= 6:
    for roofJ_1 in range(1000):
        randomX = rn.randint(NW_xa, NE_xa)
        randomZ = rn.randint(NW_za, SW_za)
        roofN = mc.getBlockWithData(randomX, first_baseY + 7, randomZ)
        if roofN == Hmat2:
            mc.setBlock(randomX, first_baseY + 8, randomZ, roofB)

    for roofJ_2 in range(1000):
        randomX = rn.randint(NW_xa, NE_xa)
        randomZ = rn.randint(NW_za, SW_za)
        roofN1 = mc.getBlockWithData(randomX + 1, first_baseY + 8, randomZ)
        roofN2 = mc.getBlockWithData(randomX - 1, first_baseY + 8, randomZ)
        roofN3 = mc.getBlockWithData(randomX, first_baseY + 8, randomZ + 1)
        roofN4 = mc.getBlockWithData(randomX, first_baseY + 8, randomZ - 1)
        if roofN1 == roofB or roofN1 == roofFull:
            if roofN2 == roofB or roofN2 == roofFull:
                if roofN3 == roofB or roofN3 == roofFull:
                    if roofN4 == roofB or roofN4 == roofFull:
                        mc.setBlock(randomX, first_baseY + 8, randomZ, roofFull)

    for roofJ_3 in range(1000):
        randomX = rn.randint(NW_xa, NE_xa)
        randomZ = rn.randint(NW_za, SW_za)
        roofN1 = mc.getBlockWithData(randomX + 1, first_baseY + 8, randomZ)
        roofN2 = mc.getBlockWithData(randomX - 1, first_baseY + 8, randomZ)
        roofN3 = mc.getBlockWithData(randomX, first_baseY + 8, randomZ + 1)
        roofN4 = mc.getBlockWithData(randomX, first_baseY + 8, randomZ - 1)
        if roofN1 == roofFull:
            if roofN2 == roofFull:
                if roofN3 == roofFull:
                    if roofN4 == roofFull:
                        mc.setBlock(randomX, first_baseY + 9, randomZ, roofB)

    for roofJ_4 in range(1000):
        randomX = rn.randint(NW_xa, NE_xa)
        randomZ = rn.randint(NW_za, SW_za)
        roofN1 = mc.getBlockWithData(randomX + 1, first_baseY + 9, randomZ)
        roofN2 = mc.getBlockWithData(randomX - 1, first_baseY + 9, randomZ)
        roofN3 = mc.getBlockWithData(randomX, first_baseY + 9, randomZ + 1)
        roofN4 = mc.getBlockWithData(randomX, first_baseY + 9, randomZ - 1)
        if roofN1 == roofB or roofN1 == roofFull:
            if roofN2 == roofB or roofN2 == roofFull:
                if roofN3 == roofB or roofN3 == roofFull:
                    if roofN4 == roofB or roofN4 == roofFull:
                        mc.setBlock(randomX, first_baseY + 9, randomZ, roofFull)

    for roofJ_5 in range(1000):
        randomX = rn.randint(NW_xa, NE_xa)
        randomZ = rn.randint(NW_za, SW_za)
        roofN1 = mc.getBlockWithData(randomX + 1, first_baseY + 9, randomZ)
        roofN2 = mc.getBlockWithData(randomX - 1, first_baseY + 9, randomZ)
        roofN3 = mc.getBlockWithData(randomX, first_baseY + 9, randomZ + 1)
        roofN4 = mc.getBlockWithData(randomX, first_baseY + 9, randomZ - 1)
        if roofN1 == roofFull:
            if roofN2 == roofFull:
                if roofN3 == roofFull:
                    if roofN4 == roofFull:
                        mc.setBlock(randomX, first_baseY + 10, randomZ, roofB)

if Hs1 == 7: #東西流れ切妻
    mc.setBlocks(NEe_x, first_baseY + 8, NEe_z, SWe_x, first_baseY + 8, SWe_z, roofB)

    if NEe_x - NWe_x + 1 > 2:
        mc.setBlocks(NEe_x - 1, first_baseY + 8, NEe_z, SWe_x + 1, first_baseY + 8, SWe_z, roofFull)
    if NEe_x - NWe_x + 1 > 4:
        mc.setBlocks(NEe_x - 2, first_baseY + 9, NEe_z, SWe_x + 2, first_baseY + 9, SWe_z, roofB)
    if NEe_x - NWe_x + 1 > 6:
        mc.setBlocks(NEe_x - 3, first_baseY + 9, NEe_z, SWe_x + 3, first_baseY + 9, SWe_z, roofFull)
    if NEe_x - NWe_x + 1 > 8:
        mc.setBlocks(NEe_x - 4, first_baseY + 10, NEe_z, SWe_x + 4, first_baseY + 10, SWe_z, roofB)
    if NEe_x - NWe_x + 1 > 10:
        mc.setBlocks(NEe_x - 5, first_baseY + 10, NEe_z, SWe_x + 5, first_baseY + 10, SWe_z, roofFull)

    for roofJ_5 in range(2000):
        randomX = rn.randint(NW_xa, NE_xa)
        randomZ = rn.randint(NW_za, SW_za)
        randomY1 = round(first_baseY + 8)
        randomY2 = round(first_baseY + 10)
        randomY = rn.randint(randomY1, randomY2)
        if mc.getBlockWithData(randomX, randomY, randomZ) == roofFull:
            if mc.getBlockWithData(randomX, randomY, randomZ - 1) == block.AIR or mc.getBlockWithData(randomX, randomY, randomZ + 1) == block.AIR:
                if mc.getBlockWithData(randomX, randomY + 1, randomZ) != block.AIR:
                    mc.setBlock(randomX, randomY, randomZ, Hmat2)

if Hs1 == 8: #南北流れ切妻
    mc.setBlocks(NEe_x, first_baseY + 8, NEe_z, SWe_x, first_baseY + 8, SWe_z, roofB)
    if SEe_z - NWe_z + 1 > 2:
        mc.setBlocks(NEe_x, first_baseY + 8, NEe_z + 1, SWe_x, first_baseY + 8, SWe_z - 1, roofFull)
    if SEe_z - NWe_z + 1 > 4:
        mc.setBlocks(NEe_x, first_baseY + 9, NEe_z + 2, SWe_x, first_baseY + 9, SWe_z - 2, roofB)
    if SEe_z - NWe_z + 1 > 6:
        mc.setBlocks(NEe_x, first_baseY + 9, NEe_z + 3, SWe_x, first_baseY + 9, SWe_z - 3, roofFull)
    if SEe_z - NWe_z + 1 > 8:
        mc.setBlocks(NEe_x, first_baseY + 10, NEe_z + 4, SWe_x, first_baseY + 10, SWe_z - 4, roofB)
    if SEe_z - NWe_z + 1 > 10:
        mc.setBlocks(NEe_x, first_baseY + 10, NEe_z + 5, SWe_x, first_baseY + 10, SWe_z - 5, roofFull)

    for roofJ_5 in range(2000):
        randomX = rn.randint(NWe_x, NEe_x)
        randomZ = rn.randint(NWe_z, SWe_z)
        randomY1 = round(first_baseY + 8)
        randomY2 = round(first_baseY + 10)
        randomY = rn.randint(randomY1, randomY2)
        if mc.getBlockWithData(randomX, randomY, randomZ) == roofFull:
            if mc.getBlockWithData(randomX - 1, randomY, randomZ) == block.AIR or mc.getBlockWithData(randomX + 1, randomY, randomZ) == block.AIR:
                if mc.getBlockWithData(randomX, randomY + 1, randomZ) != block.AIR:
                    mc.setBlock(randomX, randomY, randomZ, Hmat2)

if os1 == 1:
    mc.setBlocks(NEe_x + 1, first_baseY + 7, NEe_z, SEe_x + 1, first_baseY + 7, SEe_z, roofT)
    for osE in range(20):
        if NEe_x - osE >= NWe_x:
            if osE % 2 == 0 or osE == 0:
                mc.setBlocks(NEe_x - osE, first_baseY + 8 + (osE / 2), NEe_z, SEe_x - osE, first_baseY + 8 + (osE / 2), SEe_z, roofB)
                mc.setBlocks(NEe_x - osE, first_baseY + 7 + (osE / 2), NEe_z, SEe_x - osE, first_baseY + 7, NEe_z, Hmat2)
                mc.setBlocks(NEe_x - osE, first_baseY + 7 + (osE / 2), SEe_z, SEe_x - osE, first_baseY + 7, SEe_z, Hmat2)
                if NEe_x - osE == NWe_x:
                    mc.setBlocks(NEe_x - osE, first_baseY + 7 + (osE / 2), SEe_z, SEe_x - osE, first_baseY + 7, NEe_z, Hmat2)
            else:
                mc.setBlocks(NEe_x - osE, first_baseY + 8 + (osE / 2 - 0.5), NEe_z, SEe_x - osE, first_baseY + 8 + (osE / 2 - 0.5), SEe_z, roofFull)
                mc.setBlocks(NEe_x - osE, first_baseY + 7 + (osE / 2 - 0.5), NEe_z, SEe_x - osE, first_baseY + 7, NEe_z, Hmat2)
                mc.setBlocks(NEe_x - osE, first_baseY + 7 + (osE / 2 - 0.5), SEe_z, SEe_x - osE, first_baseY + 7, SEe_z, Hmat2)
                if NEe_x - osE == NWe_x:
                    mc.setBlocks(NEe_x - osE, first_baseY + 7 + (osE / 2 - 0.5), SEe_z, SEe_x - osE, first_baseY + 7, NEe_z, Hmat2)

if os1 == 2:
    mc.setBlocks(NWe_x - 1, first_baseY + 7, NWe_z, SWe_x - 1, first_baseY + 7, SWe_z, roofT)
    for osW in range(20):
        if NWe_x + osW <= NEe_x:
            if osW % 2 == 0 or osW == 0:
                mc.setBlocks(NWe_x + osW, first_baseY + 8 + (osW / 2), NWe_z, SWe_x + osW, first_baseY + 8 + (osW / 2), SWe_z, roofB)
                mc.setBlocks(NWe_x + osW, first_baseY + 7 + (osW / 2), NWe_z, SWe_x + osW, first_baseY + 7, NWe_z, Hmat2)
                mc.setBlocks(SWe_x + osW, first_baseY + 7 + (osW / 2), SWe_z, SWe_x + osW, first_baseY + 7, SWe_z, Hmat2)
                if NWe_x + osW == NEe_x:
                    mc.setBlocks(NWe_x + osW, first_baseY + 7 + (osW / 2), NWe_z, SWe_x + osW, first_baseY + 7, SWe_z, Hmat2)
            else:
                mc.setBlocks(NWe_x + osW, first_baseY + 8 + (osW / 2 - 0.5), NWe_z, SWe_x + osW, first_baseY + 8 + (osW / 2 - 0.5), SWe_z, roofFull)
                mc.setBlocks(NWe_x + osW, first_baseY + 7 + (osW / 2 - 0.5), NWe_z, SWe_x + osW, first_baseY + 7, NWe_z, Hmat2)
                mc.setBlocks(SWe_x + osW, first_baseY + 7 + (osW / 2 - 0.5), SWe_z, SWe_x + osW, first_baseY + 7, SWe_z, Hmat2)
                if NWe_x + osW == NEe_x:
                    mc.setBlocks(NWe_x + osW, first_baseY + 7 + (osW / 2 - 0.5), NWe_z, SWe_x + osW, first_baseY + 7, SWe_z, Hmat2)
Solar = rn.randint(1, 2)
if os1 == 3:
    mc.setBlocks(SEe_x, first_baseY + 7, SEe_z + 1, SWe_x, first_baseY + 7, SWe_z + 1, roofT)
    for osS in range(20):
        if SW_z - osS >= NW_z:
            if osS % 2 == 0 or osS == 0:
                mc.setBlocks(SEe_x, first_baseY + 8 + (osS / 2), SEe_z - osS, SWe_x, first_baseY + 8 + (osS / 2), SEe_z - osS, roofB)
                mc.setBlocks(SEe_x, first_baseY + 7, SEe_z - osS, SEe_x, first_baseY + 7 + (osS / 2), SEe_z - osS, Hmat2)
                mc.setBlocks(SWe_x, first_baseY + 7, SEe_z - osS, SWe_x, first_baseY + 7 + (osS / 2), SEe_z - osS, Hmat2)
                if SW_z - osS == NW_z:
                    mc.setBlocks(SEe_x, first_baseY + 7, SEe_z - osS, SWe_x, first_baseY + 7 + (osS / 2), SEe_z - osS, Hmat2)
            else:
                mc.setBlocks(SEe_x, first_baseY + 8 + (osS / 2 - 0.5), SEe_z - osS, SWe_x, first_baseY + 8 + (osS / 2 - 0.5), SEe_z - osS, roofFull)
                mc.setBlocks(SEe_x, first_baseY + 7, SEe_z - osS, SEe_x, first_baseY + 7 + (osS / 2 - 0.5), SEe_z - osS, Hmat2)
                mc.setBlocks(SWe_x, first_baseY + 7, SEe_z - osS, SWe_x, first_baseY + 7 + (osS / 2 - 0.5), SEe_z - osS, Hmat2)
                if SW_z - osS == NW_z:
                    mc.setBlocks(SEe_x, first_baseY + 7, SEe_z - osS, SWe_x, first_baseY + 7 + (osS / 2 - 0.5), SEe_z - osS, Hmat2)

    if Solar == 1:
        for Solar1 in range(3000):
            randomX = rn.randint(NWe_x + 1, NEe_x - 1)
            randomY = rn.randint(round(first_baseY + 8), round(first_baseY + 15))
            randomZ = rn.randint(NEe_z + 1, SWe_z)
            if mc.getBlockWithData(randomX, randomY, randomZ) == roofFull:
                mc.setBlock(randomX, randomY, randomZ, block.OBSIDIAN)
            elif mc.getBlockWithData(randomX, randomY, randomZ) == roofB:
                mc.setBlock(randomX, randomY, randomZ, 178)



if os1 == 4:
    mc.setBlocks(NEe_x, first_baseY + 7, NEe_z - 1, NWe_x, first_baseY + 7, NEe_z - 1, roofT)
    for osN in range(20):
        if NWe_z + osN <= SWe_z:
            if osN % 2 == 0 or osN == 0:
                mc.setBlocks(NWe_x, first_baseY + 8 + (osN / 2), NEe_z + osN, NEe_x, first_baseY + 8 + (osN / 2), NEe_z + osN, roofB)
                mc.setBlocks(NWe_x, first_baseY + 7 + (osN / 2), NEe_z + osN, NWe_x, first_baseY + 7, NEe_z + osN, Hmat2)
                mc.setBlocks(NEe_x, first_baseY + 7 + (osN / 2), NEe_z + osN, NEe_x, first_baseY + 7, NEe_z + osN, Hmat2)
                if NWe_z + osN == SWe_z:
                    mc.setBlocks(NEe_x, first_baseY + 7 + (osN / 2), NEe_z + osN, NWe_x, first_baseY + 7, NEe_z + osN, Hmat2)
            else:
                mc.setBlocks(NWe_x, first_baseY + 8 + (osN / 2 - 0.5), NEe_z + osN, NEe_x, first_baseY + 8 + (osN / 2 - 0.5), NEe_z + osN, roofFull)
                mc.setBlocks(NWe_x, first_baseY + 7 + (osN / 2 - 0.5), NEe_z + osN, NWe_x, first_baseY + 7, NEe_z + osN, Hmat2)
                mc.setBlocks(NEe_x, first_baseY + 7 + (osN / 2 - 0.5), NEe_z + osN, NEe_x, first_baseY + 7, NEe_z + osN, Hmat2)
                if NWe_z + osN == SWe_z:
                    mc.setBlocks(NEe_x, first_baseY + 7 + (osN / 2 - 0.5), NEe_z + osN, NWe_x, first_baseY + 7, NEe_z + osN, Hmat2)


#一階屋根
for roofJ_6 in range(2000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    roofN = mc.getBlockWithData(randomX, first_baseY + 4, randomZ)
    if roofN == Hmat:
        if mc.getBlockWithData(randomX, first_baseY + 5, randomZ) == block.AIR:
            mc.setBlock(randomX, first_baseY + 5, randomZ, roofB)

for roofJ_7 in range(1000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    roofN = mc.getBlockWithData(randomX, first_baseY + 5, randomZ)
    if roofN == roofB:
        if mc.getBlockWithData(randomX - 1, first_baseY + 4, randomZ) == block.AIR:
            mc.setBlock(randomX - 1, first_baseY + 4, randomZ, roofT)
        elif mc.getBlockWithData(randomX + 1, first_baseY + 4, randomZ) == block.AIR:
            mc.setBlock(randomX + 1, first_baseY + 4, randomZ, roofT)
        elif mc.getBlockWithData(randomX, first_baseY + 4, randomZ + 1) == block.AIR:
            mc.setBlock(randomX, first_baseY + 4, randomZ + 1, roofT)
        elif mc.getBlockWithData(randomX, first_baseY + 4, randomZ - 1) == block.AIR:
            mc.setBlock(randomX, first_baseY + 4, randomZ - 1, roofT)

#アンテナ
for roofJ_7 in range(150):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    Height = mc.getHeight(randomX, randomZ)
    HeightB = mc.getBlockWithData(randomX, Height - 1, randomZ)
    if Height >= first_baseY + 7:
        if HeightB == roofFull:
            mc.setBlocks(randomX, Height, randomZ, randomX, Height + 1, randomZ, block.IRON_BARS)
            antenna1 = rn.randint(1, 5)
            antenna2 = rn.randint(1, 5)
            antenna3 = rn.randint(1, 5)
            antenna4 = rn.randint(1, 5)
            if antenna1 <= 3:
                mc.setBlock(randomX - 1, Height + 1, randomZ, block.IRON_BARS)
                if antenna1 == 1:
                    mc.setBlock(randomX - 1, Height + 2, randomZ, block.IRON_TRAPDOOR)
            if antenna2 <= 3:
                mc.setBlock(randomX + 1, Height + 1, randomZ, block.IRON_BARS)
                if antenna2 == 1:
                    mc.setBlock(randomX + 1, Height + 2, randomZ, block.IRON_TRAPDOOR)
            if antenna3 <= 3:
                mc.setBlock(randomX, Height + 1, randomZ - 1, block.IRON_BARS)
                if antenna3 == 1:
                    mc.setBlock(randomX, Height + 2, randomZ - 1, block.IRON_TRAPDOOR)
            if antenna4 <= 3:
                mc.setBlock(randomX, Height + 1, randomZ + 1, block.IRON_BARS)
                if antenna1 == 4:
                    mc.setBlock(randomX, Height + 2, randomZ + 1, block.IRON_TRAPDOOR)
            if antenna1 >= 4 and antenna2 >= 4 and antenna3 >= 4 and antenna4 >= 4:
                mc.setBlock(randomX, Height + 1, randomZ - 1, block.IRON_BARS)
            break
#床
floorBG = rn.randint(1,5)
if floorBG == 1:
    floorB = block.STONE_ANDESITE
if floorBG == 2:
    floorB = block.STONE_ANDESITE_SMOOTH
if floorBG == 3:
    floorB = block.CONCRETE_BLOCK_WHITE
if floorBG == 4:
    floorB = block.HARDENED_CLAY_STAINED_BLACK
if floorBG == 5:
    floorB = block.IRON_BLOCK
for floor in range(1000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    floor1B = mc.getBlockWithData(randomX, first_baseY + 4, randomZ)
    floor2B = mc.getBlockWithData(randomX -1, first_baseY + 4, randomZ)
    floor3B = mc.getBlockWithData(randomX + 1, first_baseY + 4, randomZ)
    floor4B = mc.getBlockWithData(randomX, first_baseY + 4, randomZ - 1)
    floor5B = mc.getBlockWithData(randomX, first_baseY + 4, randomZ + 1)
    if floor1B == Hmat and floor2B != block.AIR and floor3B != block.AIR and floor4B != block.AIR and floor5B != block.AIR:
        mc.setBlock(randomX, first_baseY + 4, randomZ, floorB)

#くり抜き
for contents in range(4000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    randomY = rn.randint(int(PP.y - 1), int(PP.y + 6))
    contents1 = mc.getBlockWithData(randomX + 1, randomY, randomZ)
    contents2 = mc.getBlockWithData(randomX - 1, randomY, randomZ)
    contents3 = mc.getBlockWithData(randomX, randomY, randomZ + 1)
    contents4 = mc.getBlockWithData(randomX, randomY, randomZ - 1)
    if contents1 == Hmat or contents1 == Hmat2 or contents1 == block.STONE_BRICK_MOSSY:
        if contents2 == Hmat or contents2 == Hmat2 or contents2 == block.STONE_BRICK_MOSSY:
            if contents3 == Hmat or contents3 == Hmat2 or contents3 == block.STONE_BRICK_MOSSY:
                if contents4 == Hmat or contents4 == Hmat2 or contents4 == block.STONE_BRICK_MOSSY:
                    mc.setBlock(randomX, randomY, randomZ, block.STONE_BRICK_MOSSY)
for contents_3 in range(5000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    randomY = rn.randint(int(PP.y - 1), int(PP.y + 6))
    contents_2A = mc.getBlockWithData(randomX, randomY, randomZ)
    if contents_2A == block.STONE_BRICK_MOSSY:
        mc.setBlock(randomX, randomY, randomZ, block.AIR)

for contents in range(2000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    randomY = first_baseY + 6
    contents1 = mc.getBlockWithData(randomX + 1, randomY, randomZ)
    contents2 = mc.getBlockWithData(randomX - 1, randomY, randomZ)
    contents3 = mc.getBlockWithData(randomX, randomY, randomZ + 1)
    contents4 = mc.getBlockWithData(randomX, randomY, randomZ - 1)
    if contents1 == Hmat or contents1 == Hmat2 or contents1 == block.STONE_BRICK_MOSSY:
        if contents2 == Hmat or contents2 == Hmat2 or contents2 == block.STONE_BRICK_MOSSY:
            if contents3 == Hmat or contents3 == Hmat2 or contents3 == block.STONE_BRICK_MOSSY:
                if contents4 == Hmat or contents4 == Hmat2 or contents4 == block.STONE_BRICK_MOSSY:
                    mc.setBlock(randomX, randomY, randomZ, block.STONE_BRICK_MOSSY)
for contents_2 in range(2000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    randomY = rn.randint(int(PP.y - 1), int(PP.y + 6))
    contents_2A = mc.getBlockWithData(randomX, randomY, randomZ)
    if contents_2A == block.STONE_BRICK_MOSSY:
        mc.setBlock(randomX, randomY, randomZ, block.AIR)
#雨樋
for rainG in range(1000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    rainBR = rn.randint(1, 5)
    rainPX = rn.randint(0, 1)

    #rainPX = 0

    if rainPX == 0:
        rainPZ = 1
    else:
        rainPZ = 0

        if rainBR == 1:
            rainB = 189
        if rainBR == 2:
            rainB = 188
        if rainBR == 3:
            rainB = 191
        if rainBR == 4:
            rainB = 113
        if rainBR == 5:
            rainB = 101
        rainG = mc.getBlockWithData(randomX, first_baseY + 6, randomZ)
        rainG1 = mc.getBlockWithData(randomX - 1, first_baseY + 6, randomZ)
        rainG2 = mc.getBlockWithData(randomX + 1, first_baseY + 6, randomZ)
        rainG3 = mc.getBlockWithData(randomX, first_baseY + 6, randomZ - 1)
        rainG4 = mc.getBlockWithData(randomX, first_baseY + 6, randomZ + 1)
        #下のブロック探索
        if rainG1 == Hmat2 and rainG3 == Hmat2 and rainG == Hmat2:
            if mc.getBlock(randomX + rainPX, first_baseY + 3, randomZ + rainPZ) == block.AIR:
                mc.setBlocks(randomX + rainPX, first_baseY + 1, randomZ + rainPZ, randomX + rainPX, first_baseY + 6, randomZ + rainPZ, rainB)
                if mc.getBlockWithData(randomX + rainPX, first_baseY + 7, randomZ + rainPZ) == roofT:
                    mc.setBlock(randomX + rainPX, first_baseY + 7, randomZ + rainPZ, roofSE)
                else:
                    mc.setBlock(randomX + rainPX, first_baseY + 7, randomZ + rainPZ, 69,  9)
        if rainG1 == Hmat2 and rainG4 == Hmat2 and rainG == Hmat2:
            if mc.getBlock(randomX + rainPX, first_baseY + 3, randomZ - rainPZ) == block.AIR:
                mc.setBlocks(randomX + rainPX, first_baseY + 1, randomZ - rainPZ, randomX + rainPX, first_baseY + 6, randomZ - rainPZ, rainB)
                if mc.getBlockWithData(randomX + rainPX, first_baseY + 7, randomZ - rainPZ) == roofT:
                    mc.setBlock(randomX + rainPX, first_baseY + 7, randomZ - rainPZ, roofSE)
                else:
                    mc.setBlock(randomX + rainPX, first_baseY + 7, randomZ - rainPZ, 69, 9)
        if rainG2 == Hmat2 and rainG3 == Hmat2 and rainG == Hmat2:
            if mc.getBlock(randomX - rainPX, first_baseY + 3, randomZ + rainPZ) == block.AIR:
                mc.setBlocks(randomX - rainPX, first_baseY + 1, randomZ + rainPZ, randomX - rainPX, first_baseY + 6, randomZ + rainPZ, rainB)
                if mc.getBlockWithData(randomX - rainPX, first_baseY + 7, randomZ + rainPZ) == roofT:
                    mc.setBlock(randomX - rainPX, first_baseY + 7, randomZ + rainPZ, roofSW)
                else:
                    mc.setBlock(randomX - rainPX, first_baseY + 7, randomZ + rainPZ, 69, 10)
        if rainG2 == Hmat2 and rainG4 == Hmat2 and rainG == Hmat2:
            if mc.getBlock(randomX - rainPX, first_baseY + 3, randomZ - rainPZ) == block.AIR:
                mc.setBlocks(randomX - rainPX, first_baseY + 1, randomZ - rainPZ, randomX - rainPX, first_baseY + 6, randomZ - rainPZ, rainB)
                if mc.getBlockWithData(randomX - rainPX, first_baseY + 7, randomZ - rainPZ) == roofT:
                    mc.setBlock(randomX - rainPX, first_baseY + 7, randomZ - rainPZ, roofSW)
                else:
                    mc.setBlock(randomX - rainPX, first_baseY + 7, randomZ - rainPZ, 69, 10)

#照明
for ligting in range(10):

    lightingB = rn.randint(1, 4)
    if lightingB == 1:
        lightB = block.SEA_LANTERN
    if lightingB == 2:
        lightB = block.GLOWSTONE_BLOCK
    if lightingB == 3:
        lightB = block.GLAZED_TERRACOTTA_YELLOW
    if lightingB == 4:
        lightB = block.END_ROD

    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    randomY = rn.randint(int(PP.y - 1), int(PP.y + 6))
    lightP = mc.getBlockWithData(randomX, randomY, randomZ)
    if lightP == block.AIR:
        if mc.getBlockWithData(randomX, randomY - 1, randomZ) == floorB or mc.getBlockWithData(randomX, randomY + 1, randomZ) == floorB:
            mc.setBlock(randomX, randomY, randomZ, lightB)
#ベランダ
veranda1 = rn.randint(1, 6)
if veranda1 == 1:
    verandaB = 44, 8
elif veranda1 == 2:
    verandaB = 44, 13
elif veranda1 == 3:
    verandaB = 44, 12
elif veranda1 == 4:
    verandaB = 44, 14
elif veranda1 == 5:
    verandaB = 44, 15
elif veranda1 == 6:
    verandaB = 167, 8
veranda2 = rn.randint(1, 7)
if veranda2 == 1:
    verandaC = Hmat
elif veranda2 == 2:
    verandaC = Hmat2
elif veranda2 == 3:
    verandaC = block.STONE_ANDESITE_SMOOTH
elif veranda2 == 4:
    verandaC = block.STONE_GRANITE_SMOOTH
elif veranda2 == 5:
    verandaC = 155, 2
elif veranda2 == 6:
    verandaC = 162, 0
elif veranda2 == 7:
    verandaC = block.BRICK_BLOCK

veranda3 = rn.randint(1, 5)
if veranda3 == 1:
    verandaD = block.CARPET_LIGHT_GRAY
elif veranda3 == 2:
    verandaD = block.CARPET_WHITE
elif veranda3 == 3:
    verandaD = block.CARPET_BROWN
elif veranda3 == 4:
    verandaD = block.CARPET_GRAY
elif veranda3 == 5:
    verandaD = block.CARPET_BLACK

if CC3 <= 5:
    if CC3a >= 0:
        mc.setBlocks(SW_x, first_baseY + 4, SW_z, SW_x + CC3, first_baseY + 4, SW_z - CC3a, verandaB)
        mc.setBlocks(SW_x, first_baseY + 5, SW_z, SW_x + CC3, first_baseY + 5, SW_z - CC3a, verandaC)
        mc.setBlocks(SW_x, first_baseY + 6, SW_z, SW_x + CC3, first_baseY + 6, SW_z - CC3a, verandaD)
else:
    if F2S <= 0:
        veranda6 = 0
    else:
        veranda6 = 1

    verandaP1 = SW_x + rn.randint(1, 2)
    verandaP2 = SE_x - rn.randint(1, 2)
    if F2S > 0:
        mc.setBlocks(verandaP1, first_baseY + 4, SW_z + veranda6, verandaP2, first_baseY + 4, SW_z + veranda6, verandaB)
    mc.setBlocks(verandaP1, first_baseY + 5, SW_z + veranda6, verandaP2, first_baseY + 5, SW_z + veranda6, verandaC)
    mc.setBlocks(verandaP1, first_baseY + 6, SW_z + veranda6, verandaP2, first_baseY + 6, SW_z + veranda6, verandaD)
for berandaW in range(4000):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(SW_za - 2, SW_za)
    randomY = rn.randint(int(PP.y + 4), int(PP.y + 5))
    if mc.getBlockWithData(randomX, randomY, randomZ) == verandaC or mc.getBlockWithData(randomX, randomY, randomZ) == verandaD:
        if mc.getBlockWithData(randomX, randomY, randomZ - 1) == Hmat2:
            if mc.getBlockWithData(randomX - 1, randomY, randomZ - 1) == Hmat2:
                mc.setBlock(randomX, randomY, randomZ - 1, 160, 15)
                if mc.getBlockWithData(randomX + 1, randomY, randomZ - 1) == block.AIR:
                    mc.setBlock(randomX, randomY, randomZ - 1, 95, 15)

#窓
for win1 in range(170):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    wnG1 = mc.getBlockWithData(randomX, first_baseY + 3, randomZ)
    if wnG1 == Hmat:
        if mc.getBlockWithData(randomX - 1, first_baseY + 3, randomZ) == Hmat and mc.getBlockWithData(randomX + 1, first_baseY + 3, randomZ) == Hmat:
            winB1 = rn.randint(1, 6)
            if winB1 <= 3:
                winB = 160, 15
            elif winB1 == 4:
                winB = 160, 7
            elif winB1 == 5:
                winB = 101
            elif winB1 == 6:
                winB = 5, 1
            mc.setBlock(randomX, first_baseY + 3, randomZ, winB)
            winGU = rn.randint(0, 2)
            if winGU >= 1:
                mc.setBlock(randomX, first_baseY + 2, randomZ, winB)
            winGS1 = rn.randint(0, 1)
            if winGS1 == 0 and mc.getBlockWithData(randomX - 2, first_baseY + 3, randomZ) == Hmat:
                if winGU >= 1:
                    mc.setBlocks(randomX, first_baseY + 2, randomZ, randomX - 1, first_baseY + 3, randomZ, winB)
                else:
                    mc.setBlock(randomX - 1, first_baseY + 3, randomZ, winB)
        elif mc.getBlockWithData(randomX, first_baseY + 3, randomZ - 1) == Hmat and mc.getBlockWithData(randomX, first_baseY + 3, randomZ + 1) == Hmat:
            winB1 = rn.randint(1, 6)
            if winB1 <= 3:
                winB = 160, 15
            elif winB1 == 4:
                winB = 160, 7
            elif winB1 == 5:
                winB = 101
            elif winB1 == 6:
                winB = 5, 1
            mc.setBlock(randomX, first_baseY + 3, randomZ, winB)
            winGU = rn.randint(0, 2)
            if winGU >= 1:
                mc.setBlock(randomX, first_baseY + 2, randomZ, winB)
            winGS1 = rn.randint(0, 1)
            if winGS1 == 0 and mc.getBlockWithData(randomX, first_baseY + 3, randomZ - 2) == Hmat:
                if winGU >= 1:
                    mc.setBlocks(randomX, first_baseY + 2, randomZ, randomX, first_baseY + 3, randomZ - 1, winB)
                else:
                    mc.setBlock(randomX, first_baseY + 3, randomZ - 1, winB)

for win2 in range(250):
    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    wnG1 = mc.getBlockWithData(randomX, first_baseY + 6, randomZ)
    if wnG1 == Hmat2:
        if mc.getBlockWithData(randomX - 1, first_baseY + 6, randomZ) == Hmat2 and mc.getBlockWithData(randomX + 1, first_baseY + 6, randomZ) == Hmat2:
            winB1 = rn.randint(1, 5)
            if winB1 <= 3:
                winB = 160, 15
            elif winB1 == 4:
                winB = 160, 7
            elif winB1 == 5:
                winB = 5, 1
            mc.setBlock(randomX, first_baseY + 6, randomZ, winB)
            winGU = rn.randint(0, 2)
            if winGU >= 1:
                mc.setBlock(randomX, first_baseY + 5, randomZ, winB)
            winGS1 = rn.randint(0, 1)
            if winGS1 == 0 and mc.getBlockWithData(randomX - 2, first_baseY + 6, randomZ) == Hmat2:
                if winGU >= 1:
                    mc.setBlocks(randomX, first_baseY + 5, randomZ, randomX - 1, first_baseY + 6, randomZ, winB)
                else:
                    mc.setBlock(randomX - 1, first_baseY + 6, randomZ, winB)
        elif mc.getBlockWithData(randomX, first_baseY + 6, randomZ - 1) == Hmat2 and mc.getBlockWithData(randomX, first_baseY + 6, randomZ + 1) == Hmat2:
            winB1 = rn.randint(1, 5)
            if winB1 <= 3:
                winB = 160, 15
            elif winB1 == 4:
                winB = 160, 7
            elif winB1 == 5:
                winB = 5, 1
            mc.setBlock(randomX, first_baseY + 6, randomZ, winB)
            winGU = rn.randint(0, 2)
            if winGU >= 1:
                mc.setBlock(randomX, first_baseY + 5, randomZ, winB)
            winGS1 = rn.randint(0, 1)
            if winGS1 == 0 and mc.getBlockWithData(randomX, first_baseY + 6, randomZ - 2) == Hmat2:
                if winGU >= 1:
                    mc.setBlocks(randomX, first_baseY + 5, randomZ, randomX, first_baseY + 6, randomZ - 1, winB)
                else:
                    mc.setBlock(randomX, first_baseY + 6, randomZ - 1, winB)

#換気口など
for airvent in range(60):
    airvBE1 = rn.randint(1, 3)
    if airvBE1 == 1:
        airvBE = 77, 1
    if airvBE1 == 2:
        airvBE = 143, 1
    if airvBE1 == 3:
        airvBE = 131, 3
    airvBW1 = rn.randint(1, 3)
    if airvBW1 == 1:
        airvBW = 77, 2
    if airvBW1 == 2:
        airvBW = 143, 2
    if airvBW1 == 3:
        airvBW = 131, 1
    airvBS1 = rn.randint(1, 3)
    if airvBS1 == 1:
        airvBS = 77, 3
    if airvBS1 == 2:
        airvBS = 143, 3
    if airvBS1 == 3:
        airvBS = 131, 0
    airvBN1 = rn.randint(1, 3)
    if airvBN1 == 1:
        airvBN = 77, 4
    if airvBN1 == 2:
        airvBN = 143, 4
    if airvBN1 == 3:
        airvBN = 131, 2

    randomX = rn.randint(NW_xa, NE_xa)
    randomZ = rn.randint(NW_za, SW_za)
    randomY1 = rn.randint(3, 6)
    randomY = first_baseY + randomY1
    if mc.getBlockWithData(randomX, randomY, randomZ) == Hmat or mc.getBlockWithData(randomX, randomY, randomZ) == Hmat2:
        if mc.getBlockWithData(randomX + 1, randomY, randomZ) == block.AIR:
            mc.setBlock(randomX + 1, randomY, randomZ, airvBE)
        if mc.getBlockWithData(randomX - 1, randomY, randomZ) == block.AIR:
            mc.setBlock(randomX - 1, randomY, randomZ, airvBW)
        if mc.getBlockWithData(randomX, randomY, randomZ + 1) == block.AIR:
            mc.setBlock(randomX, randomY, randomZ + 1, airvBS)
        if mc.getBlockWithData(randomX, randomY, randomZ - 1) == block.AIR:
            mc.setBlock(randomX, randomY, randomZ - 1, airvBN)


#チャット
mc.postToChat("House built on " + "  x" + str(House_center_x) + "  z" + str(House_center_z))
time_end = time.time()
tim = time_end - time_sta
tim2 = round(tim, 2)
mc.postToChat("Time: " + str(tim2) + "s")
