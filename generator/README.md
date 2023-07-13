# Data Generator
The script `data_generator.py` implements a customizable data source simulator. 
It allows to read an event log in JSON format and send events to a MongoDB database, a TCP socket, or to print them in standard output.
Moreover, it is possible to set the frequency at which events must be sent, and the timeframe of the log to consider.
All the settings must be contained in a YAML configuration file ( [see YAML Configuration files](#yaml-configuration-files))

To run the script, execute the following command:

`data_generator.py -o <output> -c <path/to/your/config/file.yaml>`

where `<output>` can be one out:` mongodb`, `socket` or `stdout`, while` <path/to/your/config/file.yaml>` is the path to the file YAML containing the configuration of the generator.

# YAML Configuration files
Details on the required configuration files follow.
## MongoDB
In order to send events to a MongoDB database, the following configuration details are necessary:
* **connection_string**: _(required)_ the connection string to your database
* **database_name**: _(required)_ the name of the MongoDB database
* **collection_name**: _(required)_ the name of the collection where to insert the events
* **log_path**:  _(required)_ the path to the JSON file containing the events
* **from**: _(optional)_ a datetime string indicating the start of the timeframe to consider
* **to**:  _(optional)_ a datetime string indicating the end of the timeframe to consider
* **frequency**:  _(required)_  the frequency at which events must be sent. It can be the string **"original"** or an integer number. The former indicates that events must be sent according to the timestamps stated by the considered log, the latter indicates the frequency to use in seconds.

An example of configuration file is `source_mongodb.yaml`

**NOTE: each time the script is executed, events already present into the indicated collection will be deleted. If you don't want to lose your data, be sure to have a backup before executing this script.** 
## Socket TCP
In order to send events on a TCP socket, the following configuration details are necessary:
* **host**: _(required)_ the ip address of the host
* **port**: _(required)_ the port number
* **log_path**:  _(required)_ the path to the JSON file containing the events
* **from**: _(optional)_ a datetime string indicating the start of the timeframe to consider
* **to**:  _(optional)_ a datetime string indicating the end of the timeframe to consider
* **frequency**:  _(required)_  the frequency at which events must be sent. It can be the string **"original"** or an integer number. The former indicates that events must be sent according to the timestamps stated by the considered log, the latter indicates the frequency to use in seconds.

An example of configuration file is `source_socket.yaml`
## Standard Output
In order to extract events falling within a timeframe and print them to standard output, the following configuration details are necessary:
* **log_path**:  _(required)_ the path to the JSON file containing the events
* **from**: _(optional)_ a datetime string indicating the start of the timeframe to consider
* **to**:  _(optional)_ a datetime string indicating the end of the timeframe to consider

An example of configuration file is `source_stdout.yaml`

# Requirements
To install the script requirements, use the command `pip install -r requirements.txt`