# Baseline Experiments
To run a query using I-DLV-sr follow the steps reported next:
1. Download the latest release [here](https://github.com/DeMaCS-UNICAL/I-DLV-sr/releases/tag/v2.0.0)
2. Execute the command: 
```java -jar I-DLV-sr-v2.0.0.jar --program=path/to/query/encoding --py-script=path/to/external.py --mongodb-config=path/to/mongodb/config.yaml --mongodb --t-unit=min --windows-unit=min --now-format=min```

 
For example, to execute the query **q4** reading data from a MongoDB, you can use the following command:
```java -jar I-DLV-sr-v2.0.0.jar --program=EnviroStream/queries/program/q4.idlvsr --py-script=EnviroStream/queries/script/external.py --mongodb-config=EnviroStream/queries/config/q4.yaml --mongodb --t-unit=min --windows-unit=min --now-format=min```
