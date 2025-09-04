import numpy as np
import matplotlib.pyplot as plt

def rc_step_response(R=1e3, C=1e-6, V_in=5.0, t_end=0.01, num_points=1000, show=True, save_path=None):
    """Simulate and plot the step response of an RC circuit."""
    t = np.linspace(0, t_end, num_points)
    tau = R * C
    v_out = V_in * (1 - np.exp(-t / tau))
    
    plt.figure()
    plt.plot(t, v_out, label="V_out(t)")
    plt.title("RC Circuit Step Response")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.grid(True)
    plt.legend()
    
    if save_path:
        plt.savefig(save_path, dpi=200, bbox_inches="tight")
    if show:
        plt.show()
    return t, v_out

if __name__ == "__main__":
    rc_step_response(save_path="rc_step_response.png")