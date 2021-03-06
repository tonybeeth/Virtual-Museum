import bpy
import math

f = open("modular.dat", "w")

baseObj = None
objBaseNames = ["brick_wall", "brick_door", "lamp_holder", "Bench", "nFrame", "sphere_bulb", "Cone_bulb"]#,"bulb", "Cone"]
f.write(str(len(objBaseNames))+'\n')
#primary location of objects assumed to be the origin(0,0,0)

#print info for brick walls
for baseName in objBaseNames:
    f.write(baseName+'\n')
    
    for obj in bpy.data.objects:    
        
        if baseName in obj.name:
            #Assign first object in this group
            if baseObj == None:
                baseObj = obj
            
            baseScale = baseObj.scale            
            loc = obj.location
            rot = obj.rotation_euler
            scale = obj.scale
            
            f.write(obj.name+'\n')
            f.write(str(loc[0])+" "+str(loc[2])+" "+str(-loc[1])+'\n')
            if "Bench" in obj.name or "nFrame" in obj.name:
                f.write(str((rot[0]*180/math.pi) - 90.0))
            else:
                f.write(str(rot[0]*180/math.pi))
            if "frame_plane" in obj.name:
                f.write(" "+str(rot[1]*180/math.pi)+" "+str(rot[2]*180/math.pi)+'\n')
            else:               
                f.write(" "+str(rot[2]*180/math.pi)+" "+str(rot[1]*180/math.pi)+'\n')
            f.write(str(scale[0]/baseScale[0])+" "+str(scale[1]/baseScale[1])+" "+str(scale[2]/baseScale[2])+"\n")
    
    baseObj = None            
    f.write('\n')
        
f.close()