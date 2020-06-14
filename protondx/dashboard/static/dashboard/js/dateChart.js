let dateChart;

function createDateChart() {
    const dateCanvas = document.getElementById("date-chart");
    dateChart = new Chart(dateCanvas.getContext("2d"), {
        type: "line",
        data: {
            datasets: [{
                label: 'Daily Tests',
                backgroundColor: "#FD7F6F",
                borderColor: "#B2E061",
                fill: false,
                data: [],
            }, {
                label: 'Daily positive tests',
                backgroundColor: "#7EB0D5",
                borderColor: "#BD7EBE",
                fill: false,
                data: [],
            }]
        },
        options: {
            responsive: true,

            legend: {
                position: "bottom",
                labels: {
                    "fontSize": 16,
                }
            },
            title: {
                display: true,
                text: "Testing trends"
            },
            scales: {
                xAxes: [{
                    type: 'time',
                    time: {
                        unit: 'month'
                    },
                    ticks: {
                        fontSize: 14
                    },
                }],
                yAxes: [{
                    ticks: {
                        fontSize: 14
                    },
                    scaleLabel: {
                        display: true,
                        fontSize: 16,
                        labelString: "Number of tests"
                    }
                }]
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            }
        }
    });
}

function updateDateChart(data0, data1) {
    dateChart.data.datasets[0].data = data0;
    dateChart.data.datasets[1].data = data1;
    dateChart.update();
}
