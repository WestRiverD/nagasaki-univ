#!/usr/bin/env python2.7
import mcpi.minecraft as minecraft
import mcpi.block as block
import math

mc = minecraft.Minecraft.create("133.45.131.27")
#mc = minecraft.Minecraft.create("bes-master.cis.nagasaki-u.ac.jp")
#mc = minecraft.Minecraft.create("cv1.progrape.jp")#37 0 64
pos = mc.player.getPos()
x=200
y=-1
z=200

#blocks=mc.getBlocks(-1,-1,-1,1,1,1)
#for block in blocks:
#    print block

# douro
for i in range(0,18):
    for j in range(0,156):
            mc.setBlock(x+i,y,z+j,block.STONE.id)

# seimon 
for i in range(0,1):
    for j in range(0,3):
        mc.setBlock(x+i,y+j,z,block.STONE.id)
        mc.setBlock(x+i-2,y+j,z,block.STONE.id)
        mc.setBlock(x+i+17,y+j,z,block.STONE.id)
        mc.setBlock(x+i+19,y+j,z,block.STONE.id)

#keisatu

#ike renga
for i in range(0,360):
    rad = math.pi*i/180
    mc.setBlock(x+9+6*math.cos(rad),0,z+48+6*math.sin(rad),block.DIRT.id)

#ike water
    for j in range(0,5):
        mc.setBlock(x+9+j*math.cos(rad),0,z+48+j*math.sin(rad),block.WATER.id)

 
print "%d"%(pos.x) 
print "%d"%(pos.y)
print "%d"%(pos.z)
