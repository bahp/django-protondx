let centreChart;

function createCentreChart() {
    const centreCanvas = document.getElementById("centre-chart");
    centreChart = new Chart(centreCanvas.getContext("2d"), {
        type: "doughnut",
        data: {
            labels: ["Home", "Hospital", "GP Clinic", "Drive Through", "Other"],
            datasets: [
                {
                    backgroundColor: [
                        "#FD7F6F",
                        "#7EB0D5",
                        "#B2E061",
                        "#BD7EBE",
                        "#FFB55A"
                    ],
                    borderWidth: 0,
                    data: [0, 0, 0, 0, 0]
                }
            ]
        },
        options: {
            responsive: true,
            cutoutPercentage: 35,
            legend: {
                position: "bottom"
            },
            title: {
                display: true,
                text: "Centre Type"
            }
        }
    });
}

let genderChart;

function createGenderChart() {
    const genderCanvas = document.getElementById("gender-chart");
    genderChart = new Chart(genderCanvas.getContext("2d"), {
        type: "doughnut",
        data: {
            labels: ["Female", "Male", "Other", "Not provided"],
            datasets: [
                {
                    backgroundColor: [
                        "#FD7F6F",
                        "#7EB0D5",
                        "#B2E061",
                        "#BD7EBE",
                    ],
                    borderWidth: 0,
                    data: [0, 0, 0, 0]
                }
            ]
        },
        options: {
            responsive: true,
            cutoutPercentage: 35,
            legend: {
                position: "bottom"
            },
            title: {
                display: true,
                text: "Patient Gender"
            }
        }
    });
}


// used to update charts
function updateChart(chart, dataValues) {
    chart.data.datasets[0].data = dataValues;
    chart.update();
}