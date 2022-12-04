from ai2thor.controller import Controller
from pprint import pprint
from PIL import Image 
import numpy as np
import pickle
from transforms3d import euler, affines

controller = Controller(
    agentMode="default",
    visibilityDistance=1.5,
    scene="FloorPlan30",

    # step sizes
    gridSize=0.25,
    snapToGrid=True,
    rotateStepDegrees=90,

    # image modalities
    renderDepthImage=True,
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
                "objectName": "Potato_8a72b89b",
                "rotation": {
                    "x": 0,
                    "y": 0,
                    "z": 0
                },
                "position": {
                    "x": 1.2,
                    "y": 1.87,
                    "z": -1.4
                }
                # original bread position: y= 0.97, x=1.53, z=0.49
                # cabinet 1 position: x= 1.4, y= 1.87, z=-1.26
                # by subtracting 1 from z, the bread object moved to the right 1 meter and rotated somewhat
                # Potato_8a72b89b (cabinet 1), Apple_5ad013bf (cabinet 8), DishSponge_a3f8f753 (cabinet 9), "Bread_665b302c"
            },
            {
                "objectName": "Apple_5ad013bf",
                "rotation": {
                    "x": 0,
                    "y": 0,
                    "z": 0
                },
                "position": {
                    "x": 0.8,
                    "y": 1.87,
                    "z": -1.4
                }
            },
            {
                "objectName": "DishSponge_a3f8f753",
                "rotation": {
                    "y": 0,
                    "x": 0,
                    "z": 0
                },
                "position": {
                    "x": 0.3,
                    "y": 1.67,
                    "z": -1.7
                }
            }
            ]
        )

        # event= controller.step(
        #     action="GetSpawnCoordinatesAboveReceptacle",
        #     objectId="Cabinet|+01.40|+01.87|-01.26",
        #     anywhere=False
        # )

        # print (event.metadata["actionReturn"])
        # event= controller.step(
        # action="PlaceObjectAtPoint",
        # objectId="Bread|+01.53|+00.97|+00.49",
        # position={
        #     "x": spawnCoordinates[0],
        #     "y": spawnCoordinates[1],
        #     "z": spawnCoordinates[2]
        # }
        # )


    if choice == "camera":
        event1 = controller.step(
        action="AddThirdPartyCamera",
        position=dict(x=-1.25, y=1, z=-1),
        rotation=dict(x=90, y=0, z=0),
        fieldOfView=90,
        )

        # we just need cam_intr and cam_pose 
        height = controller.height
        width = controller.width
        fov_w = 90

        focal_length = (width / 2) / np.tan((np.pi * fov_w / 180) / 2)
        
        cam_intr = np.array(
            [[focal_length, 0, height / 2], [0, focal_length, width / 2], [0, 0, 1]]
        )
        
        #position = event1.position 
        #rotation = event1.rotation

        cam_pose = affines.compose(
            T=list(event1.metadata["agent"]["position"].values()),
            R=euler.euler2mat(
                list(event1.metadata["agent"]["rotation"].values())[2] * np.pi / 180,
                list(event1.metadata["agent"]["rotation"].values())[1] * np.pi / 180,
                list(event1.metadata["agent"]["rotation"].values())[0] * np.pi / 180,
            ),
            Z=np.ones(3),
        )

        
        img1 = Image.fromarray(event1.frame)    


        data = {"depth": event1.depth_frame,
                "cam_intr":cam_intr,
                "cam_pose":cam_pose,
                "image":img1}
        
        output = open('assets/data.pkl','wb')
        pickle.dump(data,output)
        output.close()


        # print(cam_intr)
        # print(cam_pose)
        #to get depth matrix
        # event = controller.step(dict(action='Initialize', renderDepthImage=True, gridSize=0.25))
        # print(event.depth_frame.shape)

        #to print an image:
        #print(np.array(event1.third_party_camera_frames).shape)
        #img1 = Image.fromarray(event1.frame)
        #img1.show()

    if choice == "close cabinets":
        #cabinet 1
        controller.step(action="CloseObject",
                                objectId="Cabinet|+01.40|+01.87|-01.26", 
                                forceAction=False)
        
        #cabinet 8
        event = controller.step(action="CloseObject",
                                objectId="Cabinet|+00.62|+01.87|-01.26", 
                                forceAction=False)
        #cabinet 9
        event = controller.step(action="CloseObject",
                                objectId="Cabinet|+00.14|+01.67|-01.56", 
                                forceAction=False)
    if choice == "open cabinets":
        #cabinet 1
        controller.step(action="OpenObject",
                                objectId="Cabinet|+01.40|+01.87|-01.26", 
                                openness=1,
                                forceAction=False)
        
        #cabinet 8
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|+00.62|+01.87|-01.26", 
                                openness=1,
                                forceAction=False)
        #cabinet 9
        event = controller.step(action="OpenObject",
                                objectId="Cabinet|+00.14|+01.67|-01.56", 
                                openness=1,
                                forceAction=False)


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
    
    # print (event.metadata["lastActionSuccess"])
    # print (event.metadata["errorMessage"])
