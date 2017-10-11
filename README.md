# Logs-Analysis

### Introduction

The database includes three databases.

* The `authors` table includes information about the authors of articles.
* The `articles` table includes the articles themselves.
* The `log` table includes one entry for each time a user has accessed the site.

### Requirements

This project includes a [Vagrant](https://www.vagrantup.com/) virtual environment and [VirtualBox](https://www.virtualbox.org/). To use it, install VirtualBox and (Vagrant), and follow the project installation steps bellow.

### Installation

1. Clone the project repository and connect to the virtual machine
```
$ git clone https://github.com/Adr23ian/Logs-Analysis.git
$ cd Logs-Analysis-master
$ vagrant up
$ vagrant ssh
$ cd /vagrant
```
2. Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip this file after downloading it. The file inside is called *newsdata.sql*. Put this file into the vagrant directory, which is shared with the virtual machine. Setup and load the data.
```
vagrant@vagrant:~$ cd /vagrant
vagrant@vagrant:/vagrant$ psql -d news -f newsdata.sql
```
3. Connect to the database. 
```sh
vagrant@vagrant:/vagrant$ psql -d news
```
4. Run the code print results
```sh
vagrant@vagrant:/vagrant$ python news.py
