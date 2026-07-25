const analyzeBtn = document.getElementById("analyzeBtn");
const urlInput = document.getElementById("urlInput");

const loading = document.getElementById("loading");
const results = document.getElementById("results");
const errorMessage = document.getElementById("errorMessage");
analyzeBtn.addEventListener("click", async () => {

    const url = urlInput.value.trim();

    errorMessage.classList.add("hidden");
    results.classList.add("hidden");

    if (url === "") {
        errorMessage.textContent = "Please enter a website URL.";
        errorMessage.classList.remove("hidden");
        return;
    }

    loading.classList.remove("hidden");
        try {

        const response = await fetch("https://page-pulse-21ig.onrender.com/audit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        const data = await response.json();

        loading.classList.add("hidden");

        if (!response.ok) {
            throw new Error(data.detail);
        }

        document.getElementById("status").textContent = data.status;
        document.getElementById("responseTime").textContent =
            data.response_time_ms + " ms";

        document.getElementById("title").textContent =
            data.title;

        document.getElementById("meta").textContent =
            data.meta_description;

        document.getElementById("h1").textContent =
            data.h1_count;

        document.getElementById("alt").textContent =
            data.images_missing_alt;

        document.getElementById("words").textContent =
            data.word_count;

        results.classList.remove("hidden");

    }

    catch (error) {

        loading.classList.add("hidden");

        errorMessage.textContent = error.message;

        errorMessage.classList.remove("hidden");

    }

});