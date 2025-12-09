# G-MODE

A futuristic, interactive web interface featuring a warp core control system with stunning visual effects.

## Description

G-MODE is a single-page web application that presents a science fiction-inspired interface with an animated energy core, system status panels, and interactive controls. The interface features:

- **Animated Warp Core**: A continuously spinning spiral with glowing energy effects
- **Boot Sequence**: Multi-stage initialization process when activating the system
- **Pulse Animation**: Periodic energy pulses when the system is active
- **Status Display**: Real-time warp status indicator
- **Systems Panel**: Display of various system parameters including:
  - Audio Level
  - Pulse Sync
  - Color Invert
  - Spiral Velocity
  - Warp Stability

## Features

- Pure HTML, CSS, and JavaScript (no dependencies)
- Responsive design optimized for mobile devices
- Smooth animations and transitions
- Interactive button with ripple effects
- Dark theme with cyan/blue color scheme

## Usage

Simply open `index.html` in a web browser to view and interact with the interface.

To test locally with a development server:

```bash
# Using Python 3
python3 -m http.server 8080

# Then open http://localhost:8080 in your browser
```

### Controls

- **G • AKTİF ET Button**: Toggle the warp core between STANDBY and ONLINE states
  - Click once to activate (boot sequence)
  - Click again to deactivate (shutdown sequence)

## Screenshots

### Standby State
![G-MODE Standby](https://github.com/user-attachments/assets/cfbd07c8-7451-4743-9dd1-5fd8d562c42e)

### Active State
![G-MODE Active](https://github.com/user-attachments/assets/0e5fc8c3-ff71-4895-b0fc-37b08798d40a)

## Technical Details

- **Language**: Turkish (tr)
- **Styling**: Modern CSS with gradients, shadows, and animations
- **Animations**: CSS keyframes and JavaScript-controlled state changes
- **Color Palette**: Dark background (#02040a) with cyan/blue accents (#a8d8ff)

## Browser Compatibility

Works on all modern browsers that support:
- CSS Grid and Flexbox
- CSS Custom Properties
- ES6 JavaScript
- CSS Animations

## License

This project is available for use as-is.
