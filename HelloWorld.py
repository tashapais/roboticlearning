from ai2thor.controller import Controller

controller = Controller(
    agentMode="default",
    visibilityDistance=1.5,
    scene="FloorPlan212",

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

#controller.start()
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
    
    print (event.metadata["lastActionSuccess"])
    print (event.metadata["errorMessage"])
    controller.step("Done")
