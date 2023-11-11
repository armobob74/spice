function parseDate(dateString) {
  const dateParts = dateString.split("/");
  if (dateParts.length !== 3) {
    return null;
  }
  const month = parseInt(dateParts[0], 10);
  const day = parseInt(dateParts[1], 10);
  const year = parseInt(dateParts[2], 10);

  // Check if day, month, and year are valid
  if (
    !isNaN(day) &&
    !isNaN(month) &&
    !isNaN(year) &&
    day >= 1 &&
    day <= 31 &&
    month >= 1 &&
    month <= 12
  ) {
    // Create a JavaScript Date object (months are 0-based, so subtract 1 from month)
    let date = new Date(year, month - 1, day);
    return date.getTime();
  }

  // If the input doesn't match the expected format, return null or handle the error as needed
  return null;
}
