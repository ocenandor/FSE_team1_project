# A calculator that recognizes numbers from photos. 
Project from Skoltech FSE course.

### Run with the aid of Docker:

First of all clone the repo with project to your local machine:

git clone https://github.com/ocenandor/FSE_team1_project.git

Then build docker image:

docker build -t fse_3 .

Then copy 2 photos of images to "dataset" directory and run container:

docker run -v $PWD/src/dataset:/app/src/dataset fse_3




### Or you can do it by yourself:

apt update

apt install git

git clone https://github.com/ocenandor/FSE_team1_project.git project

cd project

chmod u+x prereqs.sh

cd src/test

chmod u+x test.sh

./test.sh

cd ../../

python3 digit_predictor.py

