#!usr/bin/python3
from lxml import etree as ET

def worldGenerator(grid,w):
    sdf = ET.Element("sdf",version="1.4")

    world = ET.SubElement(sdf,"world",name="road test")

    #setting up the scene
    scene = ET.SubElement(world,"scene")

    ambient = ET.SubElement(scene,"ambient")
    ambient.text = w.ambient

    #Day: 120 120 120 255
    #Night: 20 40 50 255
    #Dawm/Dusk: 120 80 60 255
    #AfterDawn/BeforeDusk: 120 70 80 255

    sky = ET.SubElement(scene,"sky")

    clouds = ET.SubElement(sky,"clouds")

    speed = ET.SubElement(clouds,"speed")
    speed.text = "12"

    time = ET.SubElement(sky,"time")
    time.text  = w.time


    #including models

    init_x = ((grid.totalRows/2)*-10)+5
    init_y = ((grid.totalColumns/2)*-10)+5

    pos = [init_x,init_y,0,0,0,1.57]
    for i in range(grid.totalRows):
        pos[1] = init_y
        for j in range(grid.totalColumns):
            pos[5]=1.57
            if(grid.CompleteGrid[i][j]==1):
                if(i==grid.totalColumns-1):
                    if(grid.CompleteGrid[i-1][j]==2):
                        pos[5]=0
                    elif(grid.CompleteGrid[i-1][j]==1):
                        pos[5]=0
                elif(i==0):
                    if(grid.CompleteGrid[i+1][j]==2):
                        pos[5]=0
                    elif(grid.CompleteGrid[i+1][j]==1):
                        pos[5]=0
                else:
                    if(grid.CompleteGrid[i-1][j]==2 or grid.CompleteGrid[i+1][j]==2):
                        pos[5]=0
                    elif(grid.CompleteGrid[i-1][j]==1 or grid.CompleteGrid[i+1][j]==1):
                        pos[5]=0

                include = ET.SubElement(world,"include")
                uri = ET.SubElement(include,"uri")
                uri.text = "model://road_test"
                pose = ET.SubElement(include,"pose")
                pose.text = " ".join(str(i) for i in pos)

            elif(grid.CompleteGrid[i][j]==2):
                include = ET.SubElement(world,"include")
                uri = ET.SubElement(include,"uri")
                uri.text = "model://road_test2"
                pose = ET.SubElement(include,"pose")
                pose.text = " ".join(str(i) for i in pos)

            pos[1]+=10
        pos[0]+=10

    include = ET.SubElement(world,"include")
    uri = ET.SubElement(include,"uri")
    uri.text = "model://sun"

    #print ET.tostring(sdf,pretty_print=True,xml_declaration=True)
    tree = ET.ElementTree(sdf)
    tree.write('road_test.world', pretty_print=True, xml_declaration=True)
