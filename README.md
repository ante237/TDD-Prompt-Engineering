# TDD-Prompt-Engineering

# Bachelor Thesis: [Test-Driven Development: Exploring Prompt Engineering]

## Author
**Cassandra Fluhr**  
Cafl22@student.bth.se, 
[Blekinge Institute of Techonolgy]

**Theodore Reangpusri**  
Thre21@student.bth.se, 
[Blekinge Institute of Techonolgy]

## Supervisor
**Michell Naas**    
Blekinge Institute of Technology

## Experiment Overview

In this experiment, you will implement a Concert Itinerary Builder that creates an optimized concert schedule based on a list of available concerts. You will:

1. Write three unit tests manually
2. Write three unit tests with AI assistance using [ChatGPT 4o model](https://chatgpt.com/?model=gpt-4o&utm_source=chatgpt.com)
3. Implement the code to make all tests pass
4. Refactor your solution as needed


## Test-Driven Development (TDD) Overview

This experiment uses Test-Driven Development (TDD), a software development approach where you:

1. **Red Phase**: Write a failing test that defines a desired function or improvement
2. **Green Phase**: Write the simplest code to make the test pass
3. **Refactor Phase**: Clean up the code while ensuring tests still pass

This "Red-Green-Refactor" cycle is repeated for each feature or requirement. The key principle is to write tests before writing implementation code.

During this experiment, you'll go through this cycle both manually and with AI assistance to explore how these approaches differ in terms of effectiveness, accuracy, and quality.

## System Requirements

The Concert Itinerary Builder must meet the following requirements:

> **As a user, I want to build an itinerary of upcoming concerts of my favorite artists so that I can attend the concerts.**

**Constraints:**
1. The itinerary should return a list of concerts that state the artist, date, and location of each concert.
2. The itinerary should return a list of concerts sorted in chronological order (by date from earliest to latest).
3. An artist has at most one concert in the itinerary. If an artist has more than one concert in the list, the itinerary should only include the one with the earliest start date.
4. Some artists may have no concerts on the list. In that case, that should be indicated in the itinerary.
5. No two concerts may take place on the same day. If two different artists (or the same artist) have a concert on the same day, the itinerary only includes the concert closest to the last one.
6. If an artist only has one concert, it should be prioritized over artists with multiple concerts, regardless if the location is closer or not.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Coverage.py: `pip install coverage`
- Git & GitHub proficiency: cloning repositories, committing changes, pushing updates
- IDE or code editor
- Access to internet

### Setup

1. Fork this repository to your local machine
2. Install the required dependencies   using `pip install -r requirements.txt`
3. Familiarize yourself with the codebase structure

## Project Structure

- `main.py` - Contains the core implementation classes (Concert, ItineraryBuilder)
- `test.py` - Contains the unit test framework where you'll write your tests
- `concerts_data.py` - Contains the dataset of concerts for testing
- `logger.py` - Tracks experiment activity (test runs, file changes, code coverage)
- `run.py` - Script to run tests and track progress
- `experiment_log.json` - Log file that tracks your progress (will be created automatically)

## Experiment Instructions

Run the command `python run.py`(windows) or `python3 run.py`(Linux) to start the experiment. You will be assigned which constraints to implement manually and with AI assistance.

You will need to run [run.py](run.py) to track the tests ran, keep in mind to run the run.py again after changing the [test.py](test.py) file or the [main.py](main.py) file. The file does not track changes in real time.

### Part 1: Manual TDD Cycle

1. Red Phase:
   - Open `test.py` and locate the section for manual tests
   - Write three comprehensive test cases for the assigned constraints, saving the test cases in [TestCase](TestCase.txt) or creating a new folder for them is optional.
   - Run your tests using `python run.py` and select option 1 (tests should fail)
   - Record the time spent on this task using the run.py tool (option 4)

2. Green Phase:
   - Implement the `ItineraryBuilder` class to make your manual tests pass
   - Run your tests using `python run.py` and select option 1 (tests should pass if the implementation is correct)
   - Record the time spent on this task using the run.py tool (option 4)

3. Refactor Phase:
   - Refactor your implementation for code quality and coverage, making sure all tests still pass
   - Check your code coverage using the run.py tool (option 2)
   - Record the time spent on this task using the run.py tool (option 4)

### Part 2: AI-Assisted TDD Cycle

1. Red Phase:
   - Use an AI assistant to help you write three additional test cases, saving the test cases in [TestCase](test.txt) or creating a new map for them is optional.
   - Implement the AI-suggested tests in the designated section of `test.py`
   - Run your tests using `python run.py` and select option 1 (new tests should fail)
   - Record the time spent on this task using the run.py tool (option 4)

2. Green Phase:
   - Extend your implementation to make the AI-assisted tests pass
   - Run your tests using `python run.py` and select option 1 (all tests should pass)
   - Record the time spent on this task using the run.py tool (option 4)

3. Refactor Phase:
   - Refactor your implementation for code quality and coverage, making sure all tests still pass
   - Check your code coverage using the run.py tool (option 2)
   - Record the time spent on this task using the run.py tool (option 4)

## Evaluation Criteria

Your solution will be evaluated based on the following criteria:

1. **Effectiveness**: Measured by the total time spent on test writing and test runs
2. **Accuracy**: Evaluated based on the number of correctly functioning tests (1 point per passing test) and code coverage
3. **Quality**: Assessment of test code readability, structure, and documentation based on established criteria from relevant literature (e.g., "Foundations of Software Testing")

## Using the Run Script

The `run.py` script provides a simple interface for:

- Running tests and viewing results
- Checking code coverage
- Viewing experiment progress
- Recording time spent on tasks

To use the script, run `python run.py`(Windows) or `python3 run.py`(Linux) and follow the on-screen prompts.

## Dataset

The `concerts_data.py` file contains a list of concerts with different artists, dates, and locations. You can use this dataset for testing your implementation.

## Submitting Your Results

When you've completed the experiment:

1. Make sure all your work is committed to your local repository
2. Ensure that the `experiment_log.json` file contains your complete experiment history
3. Push your changes to the remote repository and notify experiment supervisors
