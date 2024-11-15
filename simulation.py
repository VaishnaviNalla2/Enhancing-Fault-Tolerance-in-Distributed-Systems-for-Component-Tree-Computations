import pickle
import os

# Simulated component tree computation state
computation_state = {"step": 0, "results": []}

def create_checkpoint(state, filename="latest_checkpoint.pkl"):
    """Save the current state to a file."""
    with open(filename, "wb") as f:
        pickle.dump(state, f)
    print(f"Checkpoint created at step {state['step']}.")

def restart_from_checkpoint(filename="latest_checkpoint.pkl"):
    """Load the last saved state if exists."""
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    return None

def simulate_computation():
    """Simulate the computation process with checkpointing."""
    state = restart_from_checkpoint()
    if not state:
        state = computation_state

    for _ in range(10):  # Simulate 10 computation steps
        state["step"] += 1
        state["results"].append(state["step"] * 2)
        
        if state["step"] % 3 == 0:  # Create a checkpoint every 3 steps
            create_checkpoint(state)

        print(f"Processing step {state['step']}, results: {state['results']}")

simulate_computation()
