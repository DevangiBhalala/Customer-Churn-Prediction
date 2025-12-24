function predict() {

    const data = {
        tenure: Number(document.getElementById("tenure").value),
        MonthlyCharges: Number(document.getElementById("monthly").value),
        TotalCharges: Number(document.getElementById("total").value)
    };

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(res => {

        const prob = Math.round(res.churn_probability * 100);
        const bar = document.getElementById("prob-bar");
        const text = document.getElementById("prob-text");

        bar.style.width = prob + "%";
        text.innerText = prob + "%";

        // Color based on risk
        if (prob < 40) {
            bar.style.background = "green";
        } else if (prob < 60) {
            bar.style.background = "orange";
        } else {
            bar.style.background = "red";
        }

        document.getElementById("result").innerHTML =
            `Risk Level: <b>${res.risk}</b>`;
    })
    .catch(error => {
        console.error(error);
        document.getElementById("result").innerHTML =
            "<b>Prediction failed</b>";
    });
}
