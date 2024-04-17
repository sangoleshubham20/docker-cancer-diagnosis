## Preferred IDE & OS: Pycharm & Windows

### Test the streamlit appication on your local machine:

1. Install required dependencies:

```commandline
pip install -r requirements.txt
```


2. Run the streamlit application:

```
streamlit run app.py
```


### Building the docker image

3. Important - Make sure you have installed Docker on your PC:
- Docker Desktop for Windows: https://www.docker.com/products/docker-desktop/

4. Start Docker:
- Start Docker engine from Docker Desktop.

5. Build Docker image from the project directory:

```commandline
docker build -t Image_name:tag .
```

### (Note: Rerun the Docker build command if you want to make any changes to the code files and redeploy.)

### Running the container & removing it

6. Switch to Home Directory:

```
cd %HOMEPATH%
```
List all the Docker images currently present
```
docker images
```

7. Start a container:
```commandline
docker run -p 80:80 Image_ID
```

8. This will display the URL to access the Streamlit app (http://0.0.0.0:80). Note that this URL may not work on Windows. For Windows, go to http://localhost/.

9. In a different terminal window, you can check the running containers with:
```
docker ps
```

10. Stop the container:
```commandline
docker stop Container_ID
```

11. Check all containers:
 ```
 docker ps -a
 ```

12. Delete the container if you are not going to run this again:
 ```
 docker container prune
 ```

### Pushing the docker image to Docker Hub

13. Sign up on Docker Hub.

14. Create a repository on Docker Hub.

15. Log in to Docker Hub from the terminal. You can log in with your password or access token.
```
docker login
```

16. Tag your local Docker image to the Docker Hub repository:
 ```
 docker tag Image_ID username/repo-name:tag
 ```

17. Push the local Docker image to the Docker Hub repository:
 ```
 docker push username/repo-name:tag
 ```

(If you want to delete the image, you can delete the repository in Docker Hub and force delete it locally.)

18. Command to force delete an image:
 ```
 docker rmi -f IMAGE_ID
 ```
