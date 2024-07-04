# python-termui

## Table of Contents

- [python-termui](#python-termui)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
    - [Example YAML File](#example-yaml-file)
    - [Explanation](#explanation)

## Installation

To install the project, follow these steps:

```sh
git clone https://github.com/yourusername/yourproject.git
cd yourproject
pip install -r requirements.txt
```

## Usage

After installing the necessary dependencies, you can run the project using:

```sh
python main.py
```

## Configuration

The project can be optionally configured using a YAML file. This file allows you to specify name of your fleets and its ip ranges

### Example YAML File

Here is an example of how the YAML configuration file should look:

```yaml
miners:
  - name: Container 1
    ip_start: 192.168.0.10  
    ip_end: 192.168.0.100
  - name: Container 2
    ip_start: 192.168.1.10  
    ip_end: 192.168.1.100
  - name: Container 3
    ip_start: 192.168.2.10  
    ip_end: 192.168.2.100

credentials:
  username: root
  password: root
```

### Explanation

- `miners`: A list of miner configurations.
  - `name`: The name of the container/rack/fleet.
  - `ip_start`: The starting IP address of the range for the container.
  - `ip_end`: The ending IP address of the range for the container.


---
