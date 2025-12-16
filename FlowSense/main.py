import time
from flowsense import FlowSenseSystem

def main():
    system = FlowSenseSystem()
    
    # How many 'steps' the simulation will run
    simulation_steps = 30
    
    try:
        for i in range(simulation_steps):
            print(f"\n===== Step {i+1}/{simulation_steps} =====")
            system.run_simulation_step()
            
            # Wait 2 seconds between steps (to simulate real-time)
            time.sleep(2)
            
        print("\n===== Simulation Complete =====")
        
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

# This makes the file runnable
if __name__ == "__main__":
    main()