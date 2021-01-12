# Fall 2020 Distributed System Course Lab
This is a simple implementation of client-server file transfer via **Socket API**
To launch the program first run ```server.py``` with
```
$ python3 server.py
```
Then run ```client.py``` with arguments ```filename```, ```ip``` and ```port```. Example:
```
$ python3 client.py file.txt 13.37.13.37 1337
```
As a result, the file in the directory of ```client.py``` file will be transfered to the directory of server with address ```ip```:```port```

> **Update**: filenames are also resolved. E.g. if file **1.jpg** already exists on server storage, it will obtain name **1_copy1.jpg**
