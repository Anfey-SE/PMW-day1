# Monocular Depth Estimation Experiment
# Amna Hafeez | PMW x TechRealm 2026 | AI-assisted with Gemini CLI

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Save to file instead of displaying
import matplotlib.pyplot as plt

print("=== PMW Depth Estimation Experiment ===")
print("Method: Monocular Depth Estimation (simulated)")
print("Why: Works with single images — ideal for heritage site photos")
print("")

# Simulate a depth map (what a real model would output)
np.random.seed(42)
depth_map = np.random.rand(100, 100)

# Make it look like a real depth map with gradients
for i in range(100):
    for j in range(100):
        depth_map[i][j] = (i + j) / 200.0 + np.random.rand() * 0.1

print("Generating simulated depth map...")
plt.figure(figsize=(8, 6))
plt.imshow(depth_map, cmap='plasma')
plt.colorbar(label='Depth (simulated)')
plt.title('Simulated Depth Map — Heritage Site\nPMW x TechRealm 2026')
plt.savefig('research/depth_map_output.png')
print("Saved output to: research/depth_map_output.png")
print("")
print("=== Experiment Complete ===")