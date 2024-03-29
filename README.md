# acqTool
acqTool is a simple tool for self-labeling.

## :books: Usage

![acqTool Interface](./images/acqToolPic.PNG)

The Tool have the main window (left) and setting window (right).

#### :arrow_right: Main Window

In this window it is possible to choose the label to be assigned to the key points during the acquisition.
The start button enables the point saving process.
The process ends with the stop button.
Below a text panel for the output messages.

#### :arrow_right: Setting Window

In the setting window you can:
- change the output path of the files,
- change the output type (pkl or json),
- change the saving sequence. At each stop or when the app closes,
- enable the maximum number of acquisitions for each "start".
To save the changes, press the Save button.

#### :arrow_right: Output format

#### :small_blue_diamond: pkl
  
  - Keypoints vector output: ![](https://latex.codecogs.com/svg.image?[[x_{1},y_{1},...,x_{n},y_{n}]_{1},...,[x_{1},y_{1},...,x_{n},y_{n}]_{k}]) 
  
  - Class vector output: ![](https://latex.codecogs.com/svg.image?[c_{1},...,c_{n}])
  
#### :small_blue_diamond: json
  
  - Non implemented yet.

## :rocket: Launch
```
python acqTool.py -m modelName -t modelType
```
__Note__: The current version support only [_Mediapipe_](https://github.com/google/mediapipe) model ed [_Hand_](https://google.github.io/mediapipe/solutions/hands) type. This limitation is due to my use case. 

To Launch correctly do:
```
python acqTool.py -m Mediapipe -t Hand
```

## :hammer: Technologies
- python 3.8.11
- tkinter 8.6
- opencv 4.5.5
- mediapipe
- threading
- os
- pickle

## :mag: Project status 
#### v0.1.1
- Added interface and a mediapipe support for hand detection.
#### v0.1.12
- Bugfix.
#### v0.2
- Removed bug on keypoint acquisition
- Added recap window after save new settings
___

## :page_facing_up: License

This project is released under the [GNU General Public License v3.0](LICENSE)
