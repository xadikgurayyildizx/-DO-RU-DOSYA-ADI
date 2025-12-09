# G-MODE - Warp Control Interface

A futuristic, interactive web interface featuring a dynamic warp core visualization with pulse synchronization and system status monitoring.

## Overview

G-MODE is a single-page web application that presents a science-fiction inspired control panel interface. The application features a rotating spiral animation representing a "warp core" that users can activate and deactivate, along with real-time system status displays.

## Features

- **Interactive Warp Core**: A visually striking central spiral animation that can be toggled between active and standby states
- **Dynamic Status Display**: Real-time status updates showing system initialization, online status, and shutdown sequences
- **Pulse Synchronization**: When active, the core pulses with visual effects including color shifts and scaling animations
- **System Panel**: Displays various system metrics including:
  - Audio Level (MID)
  - Pulse Sync (ACTIVE)
  - Color Invert (PER-PULSE)
  - Spiral Velocity (MEDIUM)
  - Warp Stability (OPTIMAL)
- **Smooth Transitions**: Boot sequences, shutdown animations, and state transitions with visual feedback
- **Responsive Design**: Mobile-friendly interface with a maximum width of 480px

## Visual Effects

- **Rotating Spiral**: Continuous 18-second rotation animation
- **Glow Effects**: Dynamic lighting and shadow effects that respond to system state
- **Pulse Animation**: Periodic pulsing effect every 2.4 seconds when active
- **Color Transitions**: Smooth color shifts between blue and purple tones
- **Background Ambiance**: Subtle radial gradients creating depth

## Usage

1. Open `index.html` in a modern web browser
2. Click the "G • AKTİF ET" button to activate the warp core
3. Watch the initialization sequence:
   - "SYSTEM INITIALIZING..."
   - "WARP CORE ONLINE"
   - "SYNCING MODULES..."
   - "WARP STATUS: ONLINE"
4. Click the button again to shutdown and return to standby mode

## Technical Details

- **Pure HTML/CSS/JavaScript**: No external dependencies required
- **CSS Animations**: Keyframe animations for smooth rotations
- **JavaScript State Management**: Event-driven state transitions
- **Modern CSS**: Uses modern properties like `conic-gradient`, `inset`, and `mix-blend-mode`

## Browser Compatibility

Works best in modern browsers that support:
- CSS Conic Gradients
- CSS Grid/Flexbox
- CSS Custom Properties
- ES6 JavaScript

## Language

The interface uses Turkish text elements:
- "G • AKTİF ET" (G • ACTIVATE)
- "Control the Flow." (Tagline)

## Project History

Initial implementation added complete interface with warp core visualization, system panel, and interactive controls.
