from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()

pos = mc.player.getPos()

while True:
    x = pos.x+random.uniform(-20,20)
    z = pos.z+random.uniform(-20,20)
    y = pos.y+5
    mc.spawnEntity(x,y,z, 101)
    time.sleep(0.1)