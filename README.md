# CALCULATOR THAT RECOGNIZES NUMBERS FROM PHOTOS 

## About
Project from Skoltech FSE course.

This calculator can recognize numbers from photos and then add them.


## Get started. Building a docker image from the provided Dockerfile
- First, clone the repository with project to your local machine:
   ```bash
   git clone https://github.com/ocenandor/FSE_team1_project.git -b master
   ```
- Second, build docker image:
   ```bash
   docker build -t fse_project .
   ```
- Then, copy 2 photos of images to "dataset" directory and run container:
   ```bash
   docker run -v $PWD/src/dataset:/app/src/dataset fse_project
   ```

## Docker Container Installation
- Create an empty ubuntu:23.04 docker container:
   ```bash
   docker pull ubuntu:23.04
   docker run -ti --name fse_project ubuntu:23.04
   git clone https://github.com/ocenandor/FSE_team1_project.git -b master
   ```
- Clone repository with project:
   ```bash
   git clone https://github.com/ocenandor/FSE_team1_project.git -b master
   ```   
- Run the following shell scripts:
   ```bash
   ./build.sh 
   ./prereqs.sh
   ./test.sh
   ```
- To use the code, you need to copy 2 photos of numbers from your local computer to a docker container:
   ```bash
   docker cp 7.png Kamil:/root/Artem/src/dataset/
   docker cp 2.png Kamil:/root/Artem/src/dataset/
   ```
- Then run python script in the docker container:
   ```bash
   python3 digit_predictor.py
   ```



## Developers
- [Kamil Garifullin](https://github.com/kzGarifullin)
- [Victoria Zinkovich](https://github.com/victoriazinkovich)
- [Artem Alekseev](https://github.com/a007mg)
- [Pavel Tikhomirov](https://github.com/ocenandor)
- [Aikun Bexultanova](https://github.com/fokrey)

