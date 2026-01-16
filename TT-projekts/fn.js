document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector(".top-section button");
    const newsletter = document.getElementById("newsletter");

    button.addEventListener("click", () => {
        newsletter.style.display =
            newsletter.style.display === "block" ? "none" : "block";
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const emailInput = document.querySelector("#newsletter input");
    const errorText = document.getElementById("email-error");

    emailInput.addEventListener("input", () => {
        const value = emailInput.value.trim();
        const isValid = value.includes("@") && value.includes(".com");

        if (isValid) {
            errorText.style.display = "none";
        } else {
            errorText.style.display = "block";
        }
    });
});