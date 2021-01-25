Follow the below steps to install and setup Spark for executing Spark Application:

1. Open the Terminal. Type ```python``` and enter, to check whether python is installed. Also, check for ```python3```.

2. Install pip.
    - To do this, we install cURL. cURL is a tool to transfer data from or to a server.
        ```
		sudo apt-get install curl
	    ```
	- Once cURL is installed, install pip for Python3 i.e. pip3.
	   ```
	   curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3'.
	   ```

3. Once we have installed pip3, we install jupyter.
    ```
    sudo pip3 install jupyter
    ```

4. Type ```jupyter notebook``` on the terminal to check whether jupyter is installed properly. 

5. As we are using jupyter notebook for the first time, copy and paste the kernel URL (from the terminal), to check we are able to access it.

6. Install java. Spark is written in Scala, but scala runs on top of the Java virtual machine.
    ```
    sudo apt-get update (This will update apt-get method, that will be used to install/remove the packages).
    sudo apt-get install default-jre
    ```

7. Check the java version by executing ```java -version``` and confirm the version as 1.8.

8. Install scala.
    ```
	sudo apt-get install scala
	```
	(you can run ```sudo-get remove --auto-remove scala```, if you have the wrong version, and then install it again. We require Scala 2.11).

9. Install py4j. Py4J enables Python programs running in a Python interpreter to dynamically access Java objects in a Java Virtual Machine.
    ```
    sudo pip3 install py4j
    ```
	
10. We need to install spark and hadoop. Spark and Hadoop are both big data management systems. Spark is much faster than Hadoop's MapReduce, and hadoop provides the distributed storage system. Spark is often installed on top of hadoop to get the best of both worlds.

11. Go to spark.apache.org. Select the Spark Release as 2.1. Choose the package type as Pre-built for Apache Hadoop 2.7 and later. Download.

12. Copy the file to home folder and uncompress it.
    ```
    sudo tar -zxvf spark-2.1.0-bin-hadoop-2.7.tgz
    ```

13. We need to tell python where to find spark, by setting up the environment variables. This will get python working with spark, and get pyspark working with the jupyter notebook.
    ```
    export SPARK_HOME='home/darshit/spark-2.1.0-bin-hadoop2.7'
    export PATH=$SPARK_HOME:$PATH
    export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
    export PYSPARK_DRIVER_PYTHON="jupyter"
    export PYSPARK_DRIVER_PYTHON=OPTS="notebook"
    export PYSPARK_PYTHON=python3
    ```

14. Fix any possible permission errors using chmod.
    ```
    sudo chmod 777 spark-2.1.0-bin-hadoop2.7
    cd spark-2.1.0-bin-hadoop2.7
    ```

    Also, fix the permission error for python folder.

15. Here, check whether we are able to import pyspark by running ```python3``` and executing the import statement.
    ```
    import pyspark
    ```

16. Now, we will again start jupyter notebook through terminal. Open a new python3 notebook, and try to ```import pyspark```.

Now we have python working with spark

All you need to do is just CD into this directory, and if something doesn't work, chances are it has something to do with the permission errors.
