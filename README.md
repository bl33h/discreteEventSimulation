# discreteEventSimulation
A code that simulates a CPU scheduling process using the SimPy library in Python. It models the execution of multiple processes with different memory and instruction requirements. The program initializes a simulation environment and defines the necessary resources such as memory (RAM) and the CPU. Each process is represented as a separate entity and follows a series of steps: arrival, memory allocation, instruction execution, and termination. The program tracks the total time taken for all processes and calculates the average time and standard deviation. This simulation provides insights into the CPU scheduling behavior and resource utilization in a simulated environment.

<p align="center">
  <br>
  <img src="https://media0.giphy.com/media/970Sr8vpwEbXG/giphy.gif" alt="pic" width="500">
  <br>
</p>
<p align="center" >
  <a href="#Files">Files</a> •
  <a href="#Features">Features</a> •
  <a href="#how-to-use">How To Use</a> 
</p>

## Files
- src: the file that implements de solution.
- others: excel with graphs, process management analysis and the zip file.

## Features
The main features of the application include:
- Simulation Environment: The code sets up a simulation environment using the SimPy library, allowing the modeling and simulation of CPU scheduling processes.
- Process Modeling: Each process is represented as a separate entity with specific characteristics such as arrival time, memory requirements, and instruction queue size. The code simulates the execution of these processes in a simulated environment.
- Resource Management: The code manages system resources, specifically memory (RAM) and the CPU. It handles the allocation and release of memory for each process and ensures that the CPU is appropriately utilized by scheduling process execution.
- Randomized Parameters: The code incorporates randomness by generating random values for process parameters such as arrival time, instruction queue size, and memory requirements. This adds variability to the simulation and allows for more realistic modeling.
- Performance Metrics: The code tracks and calculates performance metrics such as total time taken for all processes, average time per process, and the standard deviation. These metrics provide insights into the efficiency and variability of the CPU scheduling process.
- Console Output: The code displays informative messages during the simulation, indicating the state of each process (e.g., arrival, ready, running, terminated) and the allocation of system resources. This output helps in understanding the simulation progress and behavior.

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/bl33h/discreteEventSimulation

# Open the folder
$ cd src

# Run de app
$ python CPU.py
```
