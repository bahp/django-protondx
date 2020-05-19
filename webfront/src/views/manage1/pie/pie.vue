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
			
				return {
				     title: [
				        {
				            text: m2R2Data.title,
				            textStyle: {
				                fontSize: setRem2Px(0.18),
				                color: "#fff"
				            },
				            left: "center",
							top: setRem2Px(0.18)
				        }],
				    tooltip: {
				        trigger: 'item',
				        formatter:function (parms){
				          var str= parms.marker+""+parms.data.legendname+"：  "+ parms.data.value
				          return  str ;
				        }
				    },
				    series: [
						
				        {
				            name:'title',
				            type:'pie',
				            center: ['50%', '55%'],
				            radius: ['10%', '50%'],
				             clockwise: false,
				            avoidLabelOverlap: false,
				            label: {
				                normal: {
				                    show: true,
				                    position: 'outter',
				                     formatter:function (parms){
				                         return parms.data.legendname
				                     }
				                }
				            },
				            labelLine: {
				                normal: {
				                  length:setRem2Px(0.15),
				                  length2:setRem2Px(0.15),
				                }
				            },
				            data:m2R2Data.data
				        }
				    ]
				};
			},
			resize() {
				// initial echart example
				this.myChart = this.$echarts.init(this.$refs.bar);
				// start chart
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
