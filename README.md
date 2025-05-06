# 2025-Cloud-Native-HW4
This repo is for Assignment 04 of  2025 Cloud Native in NTU
Docker hub repo: [link](https://hub.docker.com/r/leemng/2025cloud/)
## Build and Run the image
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
---
## Github Action: Auto Build, Test & Push Docker Image
GitHub Action workflow is triggered when either the Dockerfile or setup.txt file is modified in the repository. Based on the setup.txt configuration, it will:
- Check if Docker image should be pushed (using the push=true flag).
- Read the Docker tag from setup.txt.
- Build the Docker image with the specified tag.
- Run a test to ensure the image runs properly.
- Push the Docker image to Docker Hub (leemng/2025cloud).
```
┌────────────────────────────┐
│  Push to GitHub (Dockerfile│
│     or setup.txt changed)  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│  Read setup.txt values     │
│  - push flag               │
│  - tag version             │
└────────────┬───────────────┘
             │
     Is push=true?
             │
     ┌───────▼────────┐
     │                │
     ▼                ▼
  Continue         Skip Action
             (exit with message)
     │
     ▼
┌────────────────────────────┐
│ Log in to Docker Hub       │
│ (via GitHub Secrets)       │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Build Docker image         │
│ using tag from setup.txt   │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Test image (e.g. run echo) │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Push image to Docker Hub   │
│ leemng/2025cloud:<tag>     │
└────────────────────────────┘
```
### setup.txt Example
```
push=true
tag=v1.2.3
username=leemng
```

