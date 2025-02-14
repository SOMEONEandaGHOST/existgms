//functions the button
function addNavigationButton() {
  const button = document.createElement("button");

  // Button styles
  button.textContent = "Panic";
  button.style.position = "fixed";
  button.style.bottom = "20px";
  button.style.right = "20px";
  button.style.padding = "10px 20px";
  button.style.backgroundColor = "#0078d4";
  button.style.color = "#fff";
  button.style.border = "none";
  button.style.borderRadius = "8px";
  button.style.boxShadow = "0px 4px 6px rgba(0, 0, 0, 0.1)";
  button.style.cursor = "pointer";
  button.style.fontSize = "16px";
  button.style.zIndex = "1000";

  // Redirect
  button.addEventListener("click", () => {
    window.location.href = "https://classroom.mcpsmd.org"; // Replace with your target website URL
  });

  // Append button to the body
  document.body.appendChild(button);
}

// Call the function to add the button
addNavigationButton();