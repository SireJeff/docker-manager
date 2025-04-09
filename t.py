import matplotlib.pyplot as plt
import numpy as np

# Parameters
tc = 105  # Critical time (just after the plot ends)
omega = 15  # Log-frequency (controls density of wiggles)
A = 1.0  # Amplitude
t = np.linspace(1, 100, 500) # Time points (avoid t=tc)

# Log-periodic function (oscillating around zero)
# Use tc - t for oscillations accelerating towards tc
dSdt = A * np.cos(omega * np.log(tc - t))

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(t, dSdt, label='Hypothetical dS/dt')

# Add labels and title
plt.xlabel("Time (Arbitrary Units)")
plt.ylabel("Rate of Inventory Change (dS/dt)\n(Surplus / Shortage)")
plt.title("Hypothetical Inventory Change (dS/dt) with Log-Periodic Oscillations")
plt.axhline(0, color='grey', linestyle='--', linewidth=0.7, label='Balance (dS/dt = 0)')
plt.ylim(-A * 1.5, A * 1.5) # Adjust ylim for better visibility
plt.grid(True, linestyle=':', alpha=0.6)

# Add annotation for oscillations
plt.annotate('Oscillations Accelerate\n(Log-Periodicity)',
             xy=(85, dSdt[np.where(t>85)[0][0]]), # Point to a wiggle near the end
             xytext=(50, -1.2), # Text position
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.3"))

# Add the caution box
plt.text(0.98, 0.02, 'Caution: Simplified Model\nIllustrates Concept Only',
         fontsize=9,
         ha='right', va='bottom',
         transform=plt.gca().transAxes, # Position relative to axes
         bbox=dict(boxstyle='round,pad=0.3', fc='wheat', alpha=0.7))

plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

