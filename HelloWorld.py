from ai2thor.controller import Controller
from pprint import pprint 

controller = Controller(
    agentMode="default",
    visibilityDistance=1.5,
    scene="FloorPlan30",

    # step sizes
    gridSize=0.25,
    snapToGrid=True,
    rotateStepDegrees=90,

    # image modalities
    renderDepthImage=False,
    renderInstanceSegmentation=False,

    # camera properties
    width=1000,
    height=1000,
    fieldOfView=90
)
'''
controller.step(
    action='SetObjectPoses',
    objectPoses=[{
        "objectName":"Mug_843dabdf",
        "rotation": {
            "y": 0,
            "x": 0,
            "z": 0
        },
        "position":{
            "x":"1.401",
            "y":"1.872",
            "z":"-1.26"
        }
    }
    ]
)
'''

''',
    {
        "objectName":"Ladle_7069fa47",
        "rotation": {
            "y": 0,
            "x": 0,
            "z": 0
        },
        "position":{
            "y":"1.404",
            "x":"1.878",
            "z":"-1.26"
        }
    },
    {
        "objectName":"Kettle_9509bd9c",
        "rotation": {
            "y": 0,
            "x": 0,
            "z": 0
        },
        "position":{
            "y":"1.407",
            "x":"1.870",
            "z":"-1.26"
        }
    }'''


for obj in controller.last_event.metadata["objects"]:
    pprint("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    pprint(obj["objectType"])
    pprint(obj["name"])
    pprint(obj["objectId"])
    pprint(obj["position"])
    pprint("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

event= None
while True :
    choice= input()
    if choice == "w":
        event= controller.step("MoveAhead")
    if choice == "s":
        event= controller.step("MoveBack")
    if choice == "a":
        event= controller.step("MoveLeft")
    if choice == "d":
        event= controller.step("MoveRight")
    if choice == "o":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|+01.40|+01.87|-01.26", 
                                openness=1,
                                forceAction=False)
    
    print (event.metadata["lastActionSuccess"])
    print (event.metadata["errorMessage"])
    controller.step("Done")