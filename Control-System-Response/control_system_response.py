import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_step_response(K=1.0, tau=0.5, duration=5.0, num_points=500, save_prefix="control_demo", show=True):
    '''
    Simulate the step response of a first-order system: G(s) = K / (tau*s + 1)
    '''
    num = [K]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    t = np.linspace(0, duration, num_points)
    t_out, y_out = signal.step(system, T=t)
    plt.figure()
    plt.plot(t_out, y_out, label="Step Response")
    plt.xlabel("Time (s)")
    plt.ylabel("Output")
    plt.title("First-Order Control System Step Response")
    plt.grid(True)
    plt.legend()
    if save_prefix:
        plt.savefig(f"{save_prefix}_step_response.png", dpi=200, bbox_inches="tight")
    if show:
        plt.show()
    return t_out, y_out

if __name__ == "__main__":
    simulate_step_response()
