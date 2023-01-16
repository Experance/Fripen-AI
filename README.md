# *Fripen* Fruit Ripeness Detector

Built with a handy CV Web Scaffold (but the website almost completely written from scratch), this website holds a model which can detect fruit ripeness for apples (specifically ripe red apples vs green unripe apples), bananas, and blueberries. (Scaffold here: [Github](https://github.com/organization-x/omni/tree/omni_cv))


Made in 3 weeks from ground zero to ground hero 😆 @AICamp 

### How To Use
***

Go to our website [here](https://experance.github.io/Fripen-AI/app/templates/home.html). 
[![Picture of the home page](app/templates/images1/frontpageofwebsite.png)](https://experance.github.io/Fripen-AI/app/templates/home.html)

(Edit) Unfortunately, due to the current environment (github pages) being static, flask does not work, and thus the AI can't run and look through images. Also, there are some resizing issues as well. But normally....
Click on "Click to test fruit" and upload an image of a banana, apple, or blueberry. Our pretrained model will then detect the fruit 
and it's level of ripeness.

### Roles (About Us)
***

**Name** | **Role**
---- | ----
**Hyrum Hansen** | **Leader (instructor)**
Andrew Wood | Product Manager & Web Developer (frontend and backend)
Reign OKeefe | Web Design & Web Developer (frontend)
Dhairya Viramgama | Data Scientist & Web Developer (frontend)
Aviel Wood | Data Scientist & Math/Statistician & Web Developer/Design (frontend)
Nabiha Jawad | Math/Sattistician & Web Developer (frontend and backend)
Rex Ouyang | Data Scientist & Web Developer (frontend)

*The roles mentioned above are the main ones each person did, however, everyone pretty much did a bit of every role.*

### Resources Used
***

**Libraries**

-[Numpy](https://numpy.org)

-[Matplotlib](https://matplotlib.org/)

-[Pandas](https://pandas.pydata.org/)

-[Pytorch](https://pytorch.org/)

**Technical Stack**

-[Python](https://python.org)

-[YOLOv.5](https://github.com/ultralytics/yolov5)

-[Flask](https://flask.palletsprojects.com/en/2.1.x/)

-[Boostrap](https://getbootstrap.com/)

-HTML, CSS, JS

**API's / Tools**

-[SerpAPI](https://serpapi.com/dashboard)

-[Roboflow](https://roboflow.com)

-[GoogleColab](https://colab.research.google.com)

-[WeightsAndBiases](https://wandb.ai)


### Data
***

Data was obtained through a web scraping api (serp api + google)

### Cloning Repo Instructions
***

Start by cloning this repo through the command line: 

`git clone https://github.com/Experance/Fripen-AI.git`

After cloning this, clone ultralytics yolov5 in the `app` folder, by running 

`git clone https://github.com/ultralytics/yolov5.git`
