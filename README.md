# DSAID Data Engineering Technical Test
This submission is for the Data Engineering Technical Test and comprises 5 sections
- Section 1: Data Pipelines
- Section 2: Databases
- Section 3: System Design
- Section 4: Charts and APIs
- Section 5: Machine Learning

## 


## Section 1: Data Pipelines

In this section, dataset1.csv and dataset2.csv were processed and the output files are stored in processed_dataset1.csv and processed_dataset2.csv. The dataprocessing.py file contains the codes to process the input files and scheduling has also been implemented to run at 1am everyday.

## Installation

The dependencies of the program are already documented in requirements.txt. Please install the dependencies by executing pip install requirements.txt.

```sh
pip install -r requirements.txt
```
## Running the program

Please ensure python is installed and just run the program using the command below:

```sh
python dataprocessing.py
```

## Section 2: Databases

For this section, due to some issues with the docker configuration, I was not able to successfully create the database table to store transactions. However, the design of the database tables with the CREATE TABLE commands can be found in the word document. 

## Section 3: System Design

For this section, the design of the system is covered in the Microsoft Powerpoint Slides uploaded. Please do take reference from the file (Section 3 - System Design.pptx).

## Section 4: Charts and APIs

For this section, the chart was successfully implemented showing the trend of increase of COVID-19 cases in Singapore for 2021 (Jan - Present) by month. I used the seaborn library to implement the visualization and plotted it in line plot.

## Installation

The dependencies of the program are already documented in requirements.txt. Please install the dependencies by executing pip install requirements.txt.

```sh
pip install -r requirements.txt
```
## Running the program

Please ensure python is installed and just run the program using the command below:

```sh
python covid19-visualization.py
```

## Section 5: Machine Learning

This part was not attempted due to time constraints. 
