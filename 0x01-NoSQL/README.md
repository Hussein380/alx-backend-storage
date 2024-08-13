# Nginx Log Stats with MongoDB

This project contains Python scripts that interact with MongoDB to provide statistics about Nginx request logs. The scripts are designed to help analyze log data stored in a MongoDB collection, specifically focusing on HTTP methods and IP addresses.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Scripts Explanation](#scripts-explanation)
  - [Script 1: `12-log_stats.py`](#script-1-12-log_statspy)
  - [Script 2: `15-log_stats.py`](#script-2-15-log_statspy)
- [Example Output](#example-output)
- [License](#license)

## Project Overview

This project consists of Python scripts that analyze and provide statistics on Nginx logs stored in a MongoDB database. The scripts can:

1. Count the total number of logs.
2. Count the number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE).
3. Count the number of GET requests to the `/status` path.
4. Display the top 10 IP addresses with the highest number of requests.

## Features

- **Efficient Log Analysis**: The scripts efficiently process large volumes of Nginx logs.
- **MongoDB Integration**: Uses the `pymongo` library to interact with MongoDB.
- **Data Aggregation**: Aggregates log data to provide meaningful statistics.

## Installation

To run this project, you'll need Python 3 and MongoDB installed on your system.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/alx-backend-storage.git
   cd alx-backend-storage/0x01-NoSQL
   ```

2. **Install the required Python packages**:
   ```bash
   pip install pymongo
   ```

3. **Restore the provided MongoDB dump (optional)**:
   ```bash
   curl -o dump.zip -s "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-webstack/411/dump.zip"
   unzip dump.zip
   mongorestore dump
   ```

## Usage

To use the scripts, simply run them using Python:

```bash
python3 12-log_stats.py
python3 15-log_stats.py
```

Make sure your MongoDB server is running and accessible at `mongodb://127.0.0.1:27017`.

## Scripts Explanation

### Script 1: `12-log_stats.py`

This script prints basic statistics about Nginx logs stored in the MongoDB collection `logs.nginx`.

- **Total Logs**: Displays the total number of log entries.
- **HTTP Methods**: Shows the count of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE).
- **Status Checks**: Counts the number of GET requests with the path `/status`.

### Script 2: `15-log_stats.py`

This script extends the functionality of `12-log_stats.py` by additionally displaying statistics about the top 10 IP addresses that made the most requests.

- **Top IPs**: Aggregates and prints the top 10 IPs by request count.

## Example Output

When running `15-log_stats.py`, the output might look like this:

```
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
IPs:
    192.168.0.1: 1200
    10.0.0.1: 1150
    172.16.0.1: 1120
    ...
```

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code.

---

