from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    hit = hits[0]
    x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
    block = mc.setBlock(x,y,z,41)