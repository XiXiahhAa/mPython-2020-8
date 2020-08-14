from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

for i in range(10):
    x,y,z = mc.player.getTilePos()
    x = x+i
    for j in range(10):
        r = randrange(0,16)
        z = z+1
        mc.setBlock(x,y,z,35,r)
        
ans = random.randrange(0,16)
while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if data == ans:
            mc.postToChat("恭喜你答對了!!")
            mc.setBlock(hit.pos,41)
        else:
            mc.postToChat("找錯了!!")