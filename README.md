# 2025-Cloud-Native-HW4
This repo is for Assignment 04 of  2025 Cloud Native in NTU

### Clone the repo and navigate to the project directory:
```bash=
git clone https://github.com/leemng/2025-Cloud-Native-HW4.git
cd 2025-Cloud-Native-HW4
```

### Build the Docker image:
```bash=
docker build -t image_name .
```

### Run the Image Interactively:
Run the container with interactive terminal access (-it) so you can input a number:
```bash=
docker run -it image_name
```

### Pull from Docker Hub
If you don’t want to build the image yourself, just pull it from Docker Hub:
```bash=
docker pull leemng/2025cloud:0.0.2
docker run -it leemng/2025cloud:0.0.2
```

###  Example Output
```
Enter a number: 7
The square of 7.0 is 49.0
```
