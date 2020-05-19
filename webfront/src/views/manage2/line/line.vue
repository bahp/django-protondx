<template>
	<div class="bar-echart" ref="bar">

	</div>
</template>

<script>
	export default {
		props:['data'],
		data() {
			return {
				dateStart: '',
				dateEnd: ''
			}
		},
		activated() {
			this.$nextTick(() => {
				setTimeout(() => {
					this.resize()
				}, 100)
			})
		},
		mounted () {
			setTimeout(() => {
				this.resize()
			}, 500)
			window.addEventListener('resize', () => {
				if (this.myChart) {
					this.resize()
				}
				
			})
		},
		methods: {
			getOption(m2R2Data) {
				var fontColor = '#fff';
				return {
				    color: ['#c73f43', '#3776d1', '#d16e37'],
				    textStyle: {
				        fontSize: setRem2Px(0.18)
				    },
				    title: {
				        text: 'PCR',
				        left: 'left',
				        textStyle: {
				            color: fontColor,
				            align: 'center',
							fontSize: setRem2Px(0.18)
				        }
				    },
				    grid: {
				        left: '0',
				        right: '10',
				        bottom: '20',
				        top: '50',
				        containLabel: true
				    },
				    tooltip: {
				        trigger: 'axis',
				        axisPointer: {
				            type: 'shadow',
				            label: {
				                show: true,
				                backgroundColor: '#333'
				            }
				        }
				    },
				    legend: {
				        show: true,
				        right: '0%',
				        icon: 'stack',
				        itemWidth:setRem2Px(0.1),
						itemHeight:setRem2Px(0.1),
				        top: '0',
				        textStyle: {
				            color: fontColor
				        },
				        data: ['ADATA', 'BDATA', 'CDATA']
				    },
				    xAxis: [{
				        type: 'category',
				        boundaryGap: false,
				        axisLabel: {
				            color: fontColor
				        },
				        axisLine: {
				            show: true,
				            lineStyle: {
				                color: '#2b2c3c'
				            }
				        },
				        axisTick:{
					            	show:false,
					            },  
				        data: ['1.26', '2.1', '2.7', '2.25', '3.8','3.8', '4.7', '4.25', '5.1', '5.7']
				    }],
				    yAxis: [{
				        type: 'value',
				        axisLine: {
				            show: false,
				            lineStyle: {
				                color: fontColor
				            }
				        },
				        
				        splitLine:{
									show:true,
									lineStyle:{
										color: '#2b2c3c'
									}
								},
				        	axisTick:{
					            	show:false,
					            },  
				    }],
				    series: [{
				            name: 'ADATA',
				            type: 'line',
							 symbolSize: 0,
				             smooth: true, //是否平滑曲线显示
				            data: [30, 52, 71, 54, 40, 30, 40, 62, 91, 34]
				        },
				        {
				            name: 'BDATA',
				            type: 'line',
				            symbol: 'circle',
							 symbolSize: 0,
				            smooth: true, //是否平滑曲线显示
				            data: [20, 32, 51, 64, 50, 40, 70, 42, 61, 24]
				        },
				        {
				            name: 'CDATA',
				            type: 'line',
				            symbol: 'circle',
				            symbolSize: 0,
				            smooth: true, //是否平滑曲线显示
				            data: [10, 42, 51, 64, 30, 40, 30, 62, 71, 39]
				        },
				       
				    ]
				};
			},
			resize() {
				// 基于准备好的dom，初始化echarts实例
				this.myChart = this.$echarts.init(this.$refs.bar);
				// 绘制图表
				this.myChart.setOption(this.getOption(this.data), true);
				this.myChart.resize();
			}
		}
	}
</script>

<style scoped lang="less">
	.bar-echart {
		width: 100%;
		height: 100%;
	}
</style>
