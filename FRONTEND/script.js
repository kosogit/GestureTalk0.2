async function uploadVideo() {
    let file = document.getElementById("fileInput").files[0];
    if (!file) {
        alert("Please select a video first!");
        return;
    }

    let formData = new FormData();
    formData.append("video", file);

    const resultBox = document.getElementById("resultBox");
    const resultText = document.getElementById("predictionText");

    // Show result box & show loading text
    resultBox.classList.remove("hidden");
    resultText.innerText = "Processing...";

    try {
        console.log("📤 Sending request to Flask backend...");

        let res = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            body: formData
        });

        console.log("📥 Response status:", res.status);

        let raw = await res.text();
        console.log("📄 Raw response:", raw);

        let data;
        try {
            data = JSON.parse(raw);
        } catch (err) {
            console.error("❌ JSON parse error:", err);
            resultText.innerText = "Error: Invalid server response.";
            return;
        }

        console.log("✅ Final Prediction:", data.prediction);
        resultText.innerText = "Prediction: " + data.prediction;

    } catch (err) {
        console.error("🔥 Fetch error:", err);
        resultText.innerText = "Error connecting to backend.";
    }
}

