# MultiInputTimeSeriesGenerator

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)]()

 Multi Input Timeseries Generator: It works Incase We have multi input, The keras timeseries generator only works for only single input. Keras timeseries generator can only generate sequences for single input.
 
 In this Library we have added functionality of multi input by modifying keras source code to work it for multi input.

- ✨Multi Input Time Series Generator✨


## Problem 

> This was the problem keras wasn't able to handle

![image](https://drive.google.com/uc?export=view&id=1yDxbC3fX3_vrqXH7QXdtLLQzO0Zx3yOz)
> This is what we want as multi input timeseries generator

![image](https://drive.google.com/uc?export=view&id=1wgGnKIQ8BefD7HjlNqw14ri0SX9xkkbG)

> We have given solution to this , We can make generator for equal instances.

## Example working
```sh
gen=MultiInputTimeseriesGenerator(df[["ID","f2","f3"]].values,df[["output"]].values,length=2,batch_size=10,ptotal=3,same=0)
```

| ID | f2 | f3|output
| ------ | ------ |------|----|
| 1 | 2| 3|1
| 1 | 2| 5|2
|1|2|3|5
| 2 | 9 | 7|3
| 2 | 8 | 3|4
| 2| 78 | 24|5

Sequences Generated are : 
input: 
| ID | f2 | f3| 
| ------ | ------ |------|     
| 1 | 2| 3|
| 1 | 2| 5| 
output: 5

input: 
| ID | f2 | f3| 
| ------ | ------ |------|     
| 2 | 9| 7|
| 2 | 8| 3| 
output: 5

```sh
gen=MultiInputTimeseriesGenerator(df[["ID","f2","f3"]].values,df[["output"]].values,length=2,batch_size=10,ptotal=3,same=1)
```
Sequences Generated are : 
input: 
| ID | f2 | f3| 
| ------ | ------ |------|     
| 1 | 2| 3|
| 1 | 2| 5| 
output: 2

| ID | f2 | f3| 
| ------ | ------ |------|     
| 1 | 2| 5|
| 1 | 2| 3| 
output: 5

input: 
| ID | f2 | f3| 
| ------ | ------ |------|     
| 2 | 9| 7|
| 2 | 8| 3| 
output: 4

input: 
| ID | f2 | f3| 
| ------ | ------ |------|     
| 2 | 8| 3|
| 2 | 78| 24| 
output: 5
## Parameters

Parameters required to Pass

| Parameter | To be passed | Format
| ------ | ------ |------|
| data | Independent Vairables (Input)| Numpy Array
| targets | Dependent Vairable (Output)| Numpy Array
| length | Sequence Length or Window Length | a number
| ptotal | Total number of equal instances | a number
| same | Same row output(1) or next row output(0) | 0 or 1

## Calling

```sh
from MultiInputTimeseriesGenerator import MultiInputTimeseriesGenerator

gen=MultiInputTimeseriesGenerator(input,output,length=36,batch_size=1024,ptotal=36,same=0) # training generator
t_gen=MultiInputTimeseriesGenerator(input,output,length=36,batch_size=1024,ptotal=36,same=0) # testing generator
```

Passing to Model

```sh
history=model.fit_generator(gen,validation_data=t_gen,epochs =8 ,use_multiprocessing=False)
```
Can also do
```sh
gen[0]#independent vairable
gen[1]#dependent Vairable
gen[0][0]#single instance gen input
gen[0][1]#single instance gen output
gen[0][0][0] #single row
gen[0][0][0][0]#single value
1 can be used inplace of 0 to get output
```
