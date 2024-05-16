# Network Security Demosntration

## Running the Project
To run the project locally, follow these steps:

1. Change the **docker-compose.yml** file and replace the **<your_path>** with the path of the current directory of the project.

2. Secondly run the **build.sh** bash script.

```bash
sudo chmod +x build.sh
./build.sh
```
3. Then Run the **run.sh** bash script.

```bash
sudo chmod +x run.sh
./run.sh
```

4. Check if the webiste is working at **http://172.20.0.2** or the other adress given by the **build.sh** script.

5. Now you are ready to start! The user is **admin** and the password is **letmein**. You can log in the website and see the new page.

6. To exploit the program you have to run **hearbleed.py** with **python 2.7**. You have to specify the adress and the number of tries:  

```bash
python2.7 heartbleed.py -a 172.20.0.2 -n 5
```

In this case we are attacking 172.20.0.2 and trying 5 times.

7. The Program should return the memory of the server containing the password.

8. Finaly we can log in to the website with this new password we obtained with the exploit.

9. To correct it, you have to go to the **Corrected_Website** and run this tutorial again. Notice that the heartbleed does not work anymore!


