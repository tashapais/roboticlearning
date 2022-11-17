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


# for obj in controller.last_event.metadata["objects"]:
#     pprint("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#     pprint(obj["objectType"])
#     pprint(obj["name"])
#     pprint(obj["objectId"])
#     pprint(obj["position"])
#     pprint("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


event= None
while True :
    controller.step("Done")
    choice= input()

    # keys are assigned based on location on keyboard
    if choice == "w":
        event= controller.step("MoveAhead")
    if choice == "s":
        event= controller.step("MoveBack")
    if choice == "a":
        event= controller.step("MoveLeft")
    if choice == "d":
        event= controller.step("MoveRight")

    if choice == "r":
        event= controller.step("RotateRight")
    if choice == "e":
        event= controller.step("RotateLeft")

    if choice == "t":
        event= controller.step(    
            action="LookUp",
            degrees=30
            )
    if choice == "g":
        event= controller.step(    
            action="LookDown",
            degrees=30
            )

    if choice == "o":
        event= controller.step(
            action='SetObjectPoses',
            objectPoses=[
                {
                "objectName": "Bread_665b302c",
                "rotation": {
                    "y": 0,
                    "x": 0,
                    "z": 0
                },
                "position": {
                    "y": 0.97,
                    "x": 1.53,
                    "z": -0.50
                }
                # original bread position: y= 0.97, x=1.53, z=0.49
                # by subtracting 1 from z, the bread object moved to the right 1 meter and rotated somewhat
                }
            ]
)
    # if you're facing the corner by the fridge, #3 is top right, #8 is top left, #9 is middle left, #10 is middle right, 
    if choice == "1":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|+01.40|+01.87|-01.26", 
                                openness=1,
                                forceAction=False)
    if choice == "2":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|-00.20|+01.96|-01.33", 
                                openness=1,
                                forceAction=False)
    if choice == "3":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|+02.82|+01.77|-01.85", 
                                openness=1,
                                forceAction=False)
    if choice == "4":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|+02.85|+00.42|+00.41", 
                                openness=1,
                                forceAction=False)
    if choice == "5":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|+02.85|+00.42|-00.61", 
                                openness=1,
                                forceAction=False)
    if choice == "6":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|+03.07|+01.67|-00.71", 
                                openness=1,
                                forceAction=False)
    if choice == "7":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|+02.82|+01.77|-01.05", 
                                openness=1,
                                forceAction=False)
    if choice == "8":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|+00.62|+01.87|-01.26", 
                                openness=1,
                                forceAction=False)
    if choice == "9":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|+00.14|+01.67|-01.56", 
                                openness=1,
                                forceAction=False)
    if choice == "10":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|-00.19|+01.67|-01.34", 
                                openness=1,
                                forceAction=False)
    if choice == "11":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|-00.71|+01.96|-00.82", 
                                openness=1,
                                forceAction=False)
    if choice == "12":
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|-00.92|+01.67|-00.62", 
                                openness=1,
                                forceAction=False)
    
    print (event.metadata["lastActionSuccess"])
    print (event.metadata["errorMessage"])
   


