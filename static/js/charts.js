function renderClinicChart(canvasId, chartData) {

    const ctx = document.getElementById(canvasId);

    new Chart(ctx, {

        type: "line",

        data: {

            labels: chartData.labels,

            datasets: [

                {
                    label: "Clinic 1",
                    data: chartData.clinic1,
                    borderWidth: 2
                },

                {
                    label: "Clinic 2",
                    data: chartData.clinic2,
                    borderWidth: 2
                }

            ]
        },

        options: {

            responsive: true,

            maintainAspectRatio: false
        }
    });
}


function renderMonthlyChart(canvasId, chartData) {

    const ctx = document.getElementById(canvasId);

    new Chart(ctx, {

        type: "bar",

        data: {

            labels: chartData.labels,

            datasets: [

                {
                    label: "Death Proportion",
                    data: chartData.deaths,
                    borderWidth: 2
                }

            ]
        },

        options: {

            responsive: true,

            maintainAspectRatio: false
        }
    });
}