from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()

def plantTree(x,y,z):
    mc.setBlocks(x+1,y+5,z+1,x-1,y+5,z-1,18)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
for h in range(0,50,4):
    for i in range(0,50,4):
        plantTree(x+i,y,z+h)