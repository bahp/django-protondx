<template>
	<div class="bar-echart" ref="bar" :key="mapKey">

	</div>
</template>

<script>
	import $ from 'jquery'
	export default {
		props: ['data'],
		data() {
			return {
				dateStart: '',
				dateEnd: '',
				mapKey: Math.random(),
				zoom: 1
			}
		},
		activated() {
			this.mapKey = Math.random()
			this.zoom = 1
			setTimeout(() => {
				this.resize()
			}, 100)
		},
		mounted () {
			window.addEventListener('resize', () => {
				if (this.myChart) {
					this.myChart.resize();
				}
				
			})
		},
		methods: {
			resize() {
				function getQueryStrings() { //get the country name
				var query = location.href.split("?")
				  var url = query[1]; //get ? and anything after it
				   var theRequest = new Object();
				   var str = url.substr(0);
				   var   strs = str.split("&");
				      for(var i = 0; i < strs.length; i ++) {
				         theRequest[strs[i].split("=")[0]]=unescape(strs[i].split("=")[1]);
				      }
				   return theRequest;
				}

				// initial echarts example
				this.myChart = this.$echarts.init(this.$refs.bar);
				var value0 = []

				for (var i = 0; i < value0.length; i++) {
					value0[i].value = parseInt(Math.random() * 11000) || '0'
				}

				loadMap(`./json/${getQueryStrings()['url']}`, getQueryStrings()['name']); //initial the country map

				var timeFn = null;
				var self = this

				function loadMap(mapCode, name) {
					console.log(mapCode, name)
					$.get(mapCode, function(data) {
						if (data) {
							self.$echarts.registerMap(name, JSON.stringify(data));
							var option = {
								tooltip: {
									show: true,
									formatter: function(params) {
										if (params.data) return params.name + '：' + params.data['value']
									},
								},
								visualMap: {
									min: 0,
									max: 1000,
									left: 26,
									bottom: 40,
									showLabel: !0,
									text: ["", ""],
									pieces: [{
										gt: 10000,
										label: "≥10000",
										color: "#b80909"
									}, {
										gte: 1000,
										lte: 9999,
										label: "1000-9999",
										color: "#e64546"
									}, {
										gte: 100,
										lt: 999,
										label: "100-999",
										color: "#f57567"
									}, {
										gte: 10,
										lt: 99,
										label: "10-99",
										color: "#ff9985"
									}, {
										gte: 1,
										lt: 9,
										label: "1-9",
										color: "#ffe5db"
									}, {
										gte: 0,
										lt: 0,
										label: "0",
										color: "#ffffff"
									}],
									textStyle: {
										color: '#5a6384',
										fontSize: '14px'
									},
									show: !0
								},
								series: [{
									name: 'MAP',
									type: 'map',
									mapType: name,
									top: '9%',
									bottom: '15%',
									left: '5%',
									right: '5%',
									roam: 'move',
									selectedMode: 'false',
									zoom: self.zoom,
									label: {
										normal: {
											show: false
										},
										emphasis: {
											show: true
										}
									},
									data: value0
								}]
							};
							self.myChart.setOption(option);
							self.myChart.resize();
							// curMap = {
							//     mapCode: mapCode,
							//     mapName: name
							// };
						} else {
							alert('Cannot load the map');
						}
					});
				}



				this.myChart.on('click', (params) => {
					clearTimeout(timeFn);

					timeFn = setTimeout(() => {
						var name = params.name; //area name
						


					}, 250);
				});



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
