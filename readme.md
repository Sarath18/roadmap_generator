# Road Generator
A wizard written in python that helps in creating realistic city roadmaps for *Gazebo* with appropriate textures and lighting.

Road Grid is generated using the input provided by the user in the grid as shown below. It is then generated into a matrix which is inturn used to find position and place the road blocks.



<img src="https://image.ibb.co/cvtHZT/grid.png"><img src="https://image.ibb.co/gtLmTo/roadmap.png" alt="roadmap" border="0" height=200>



### Working
The wizard basically does the following:
- Asks you a few questions on your roadmap
- Opens a *GUI grid* where you can define the road layout
- Converts that grid into matrix
- Finds the position of each road block
- Creates the required model files and saves it in your `.gazebo/models ` folder
- Creates a `.world` file at the destination path provided by the user

### Requirements
- Python
- Gazebo 7.0 or higher
- lxml
- urllib

### Installation
Install the required files to run on your local system:

- Cloning the repository

      git clone

- lxml

      sudo pip install lxml

- urllib

      sudo pip install urllib
