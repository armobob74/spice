let percentiles = [
  0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95,100
];
let lead_values = [
  0.0, 24.38, 38.62, 54.5, 68.1, 86.2, 107.0, 127.0, 148.0, 179.4, 212.0, 246.0,
  288.0, 336.0, 404.4, 505.0, 631.0, 773.0, 1130.0, 2270.0,146000.0
];
function determinePercentile(lead_level) {
  for (let i = 0; i < lead_values.length; i++) {
    if (lead_level <= lead_values[i]) {
      if (i === 0) {
        return percentiles[i];
      } else {
        const lowerValue = lead_values[i - 1];
        const upperValue = lead_values[i];
        const lowerPercentile = percentiles[i - 1];
        const upperPercentile = percentiles[i];

        // Calculate the percentile using linear interpolation
        const percentile =
          lowerPercentile +
          ((upperPercentile - lowerPercentile) * (lead_level - lowerValue)) /
            (upperValue - lowerValue);

        return percentile;
      }
    }
  }
}
function determineLead(percentile) {
  if (percentile < 0 || percentile > 100) {
    throw new Error("Percentile must be between 0 and 100");
  }

  for (let i = 0; i < percentiles.length; i++) {
    if (percentile <= percentiles[i]) {
      if (i === 0) {
        return lead_values[i];
      } else {
        const lowerPercentile = percentiles[i - 1];
        const upperPercentile = percentiles[i];
        const lowerValue = lead_values[i - 1];
        const upperValue = lead_values[i];

        // Calculate the lead value using linear interpolation
        const lead_value =
          lowerValue +
          ((upperValue - lowerValue) * (percentile - lowerPercentile)) /
            (upperPercentile - lowerPercentile);

        return lead_value;
      }
    }
  }
}


let danger_colors = [
  "#a8e6cf" /* Soft Green */,
  "#a8e6cf" /* Soft Green */,
  "#ffd3b6" /* Soft Yellow */,
  "#ffaaa5" /* Soft Orange */,
  "#d32f2f" /* Deep Red */,
  "#690000" /* Dark Red */,
];
function pickColor(percent) {
  // Ensure the percentage is within the range [0, 100]
  percent = Math.min(Math.max(percent, 0), 100);

  // Calculate which two colors to interpolate between
  const numColors = danger_colors.length;
  const scale = ((numColors - 1) * percent) / 100;
  const firstColorIndex = Math.floor(scale);
  const secondColorIndex = Math.min(firstColorIndex + 1, numColors - 1);

  // Find the relative position between the two colors
  const fraction = scale - firstColorIndex;

  // Interpolate between the two colors
  const color1 = hexToRGB(danger_colors[firstColorIndex]);
  const color2 = hexToRGB(danger_colors[secondColorIndex]);

  const r = Math.round(lerp(color1.r, color2.r, fraction));
  const g = Math.round(lerp(color1.g, color2.g, fraction));
  const b = Math.round(lerp(color1.b, color2.b, fraction));

  return rgbToHex(r, g, b);
}

function hexToRGB(hex) {
  let r = 0,
    g = 0,
    b = 0;

  // 3 digits
  if (hex.length === 4) {
    r = parseInt(hex[1] + hex[1], 16);
    g = parseInt(hex[2] + hex[2], 16);
    b = parseInt(hex[3] + hex[3], 16);
  }
  // 6 digits
  else if (hex.length === 7) {
    r = parseInt(hex.substring(1, 3), 16);
    g = parseInt(hex.substring(3, 5), 16);
    b = parseInt(hex.substring(5, 7), 16);
  }

  return { r, g, b };
}

function lerp(start, end, fraction) {
  return start + (end - start) * fraction;
}

function rgbToHex(r, g, b) {
  return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}

function pickTextColor(bgColor) {
  // Convert the background color to RGB
  const bgColorRGB = hexToRGB(bgColor);

  // Calculate the brightness of the background color
  const brightness =
    (bgColorRGB.r * 299 + bgColorRGB.g * 587 + bgColorRGB.b * 114) / 1000;

  // Determine whether the text color should be light or dark based on brightness
  if (brightness > 128) {
    // Background is light, so use a dark text color
    return "#000000"; // Black
  } else {
    // Background is dark, so use a light text color
    return "#FFFFFF"; // White
  }
}
