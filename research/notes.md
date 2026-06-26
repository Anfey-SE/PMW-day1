# 3D Reconstruction Methods — Research Notes

## 1. COLMAP (Structure-from-Motion)
- **Inputs:** Multiple photos of the same object/site from different angles
- **Outputs:** 3D point cloud, camera positions
- **Hardware:** CPU (GPU optional for speed)
- **Difficulty:** Medium
- **PMW use case:** Could reconstruct heritage sites from tourist photos

## 2. NeRF (Neural Radiance Fields)
- **Inputs:** Images with known camera positions
- **Outputs:** Photorealistic 3D scene you can view from any angle
- **Hardware:** GPU required
- **Difficulty:** Hard
- **PMW use case:** Create immersive walkthroughs of Lahore heritage sites

## 3. Gaussian Splatting
- **Inputs:** Images + camera poses (often from COLMAP first)
- **Outputs:** Real-time renderable 3D scene
- **Hardware:** GPU required
- **Difficulty:** Medium-Hard
- **PMW use case:** Fast, high-quality 3D views for the web platform

## 4. Monocular Depth Estimation
- **Inputs:** Single image or video
- **Outputs:** Depth map (how far each pixel is)
- **Hardware:** CPU/GPU
- **Difficulty:** Easy
- **PMW use case:** Quick depth analysis from field videos without special equipment

## 5. Multi-View Stereo (MVS)
- **Inputs:** Multiple calibrated images
- **Outputs:** Dense 3D point cloud
- **Hardware:** CPU/GPU
- **Difficulty:** Medium
- **PMW use case:** Dense reconstruction of building facades

## Summary
For PreserveMy.World, the most practical pipeline would be:
Photos/Video → COLMAP → Gaussian Splatting → Interactive web viewer