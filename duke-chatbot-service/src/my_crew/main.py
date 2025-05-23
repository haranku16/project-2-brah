#!/usr/bin/env python
import sys
import warnings
import time

from datetime import datetime

from my_crew.crew import MyCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'question': 'How much does it cost to finish the AIPI program in 12 months?'
    }
    
    try:
        start_time = time.time()  # Start time measurement
        MyCrew().crew().kickoff(inputs=inputs)
        end_time = time.time()  # End time measurement
        total_time = end_time - start_time  # Calculate total time taken
        print(f"Total Task Completion Time: {total_time:.2f} seconds")  # Print the total time
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        MyCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(n_iterations='2', model='gpt-4o-mini'):
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year),
        "question": "What are the events for the next 50 days?"
    }
    try:
        MyCrew().crew().test(int(n_iterations), model, inputs=inputs)
        
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
