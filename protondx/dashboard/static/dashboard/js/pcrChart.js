let pcrChart;

function createPCRChart() {
    const pcrCanvas = document.getElementById("pcr-chart");
    pcrChart = new Chart(pcrCanvas.getContext("2d"), {
        type: "line",
        data: {
            datasets : [
                {
                    data: [],
                    backgroundColor :'#D4EFFC',
                    borderColor : 'rgba(0,62,116,0.5)',
                    pointBackgroundColor:'#003E74',
                    pointBorderColor : '#003e74',
                    label:"",
                },
            ]
        },
        options: {
            responsive:true,
            scales: {
                xAxes:[{
                    gridLines:{
                        borderDash:[],
                    },
                    scaleLabel:{
                        display:true,
                        labelString:'Time (minutes)',
                        fontColor:'#002147',
                        fontSize:14,
                    },
                }],
                yAxes:[{
                    gridLines:{
                        borderDash:[],
                    },
                    ticks: {
                        beginAtZero: true,
                        max: 1
                    },
                    scaleLabel:{
                        display:true,
                        labelString:'Normalised pH',
                        fontColor:'#002147',
                        fontSize:14,
                    },
                }],
            },
            legend:{
                display:false
            },
            elements: {
                arc: {
                },
                point: {},
                line: {
                    tension:0.4,
                    borderWidth:10,
                },
                rectangle: {
                },
            },
            tooltips: {
                enabled: true,
                intersect:false,
                callbacks: {
                    title: function(tooltipItem, data) {
                        return tooltipItem[0]['label'] + ' minutes';
                    }
                }
            },
        }
    });
}

function updatePCRChart(x, y) {
    pcrChart.data.labels = x;
    pcrChart.data.datasets[0].data = y;
    pcrChart.update();
}
