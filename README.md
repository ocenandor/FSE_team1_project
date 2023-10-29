# CALCULATOR THAT RECOGNIZES NUMBERS FROM PHOTOS 

## About
Project from Skoltech FSE course.

This calculator can recognize numbers from photos and then add them.


## Run with the aid of Docker:
- First, clone the repository with project to your local machine:
   ```bash
   git clone https://github.com/ocenandor/FSE_team1_project.git
   ```
- Second, build docker image:
   ```bash
   docker build -t fse_3 .
   ```
- Then, copy 2 photos of images to "dataset" directory and run container:
   ```bash
   docker run -v $PWD/src/dataset:/app/src/dataset fse_3
   ```

## Or you can do it by yourself:

- Make following commands 
   ```bash
   apt update
   apt install git
   git clone https://github.com/ocenandor/FSE_team1_project.git project
   cd project
   chmod u+x prereqs.sh
   ./prereqs.sh
   chmod u+x build.sh
   ./build.sh
   cd src/test
   chmod u+x test.sh
   ./test.sh
   cd ../../
   ```
   On local computer:
   ```bash
   docker cp 7.png Kamil:/root/Artem/src/dataset/
   ```

   On docker container:
   ```bash
   python3 digit_predictor.py
   ```

To use docker clone repository and run the following shell scripts:

git clone https://github.com/Pils48/fse-final-project.git to clone repository
./install_docker.sh in case you don't have docker installed
./build_docker.sh
./run_docker.sh


## Docker Container Installation
- To use docker clone repository:
   ```bash
   git clone https://github.com/ocenandor/FSE_team1_project.git
   ```
- Run the following shell scripts:
   ```bash
   ./install_docker.sh in case you don't have docker installed
   ./prereqs.sh
   ./build.sh
   ```



## Developers
- [Kamil Garifullin](https://github.com/kzGarifullin)
- [Victoria Zinkovich](https://github.com/victoriazinkovich)
- [Artem Alekseev](https://github.com/a007mg)
- [Pavel Tikhomirov](https://github.com/ocenandor)
- [Aikun Bexultanova](https://github.com/fokrey)

