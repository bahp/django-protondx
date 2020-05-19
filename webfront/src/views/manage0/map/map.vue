<template>
	<div class="bar-echart" ref="bar">

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
				zoom: 1
			}
		},
		activated() {
			setTimeout(() => {
				this.resize()
			}, 100)
			
			window.addEventListener('resize', () => {
				if (this.myChart) {
					this.myChart.resize();
				}
				
			})
		},
		methods: {
			resize() {
				// initial echarts example
				this.myChart = this.$echarts.init(this.$refs.bar);
				var value0 = [{
						name: "Aruba",
						value: -1.58156e+08
					},
					{
						name: "Afghanistan",
						value: 0
					},
					{
						name: "Angola",
						value: -2.355e+08
					},
					{
						name: "Albania",
						value: -1.183e+08
					},
					{
						name: "Argentina",
						value: 4.552e+09
					},
					{
						name: "Armenia",
						value: 0
					},
					{
						name: "Antigua and Barbuda",
						value: -3.09852e+07
					},
					{
						name: "Australia",
						value: -1.55324e+10
					},
					{
						name: "Austria",
						value: 0
					},
					{
						name: "Azerbaijan",
						value: 0
					},
					{
						name: "Burundi",
						value: -6.94442e+07
					},
					{
						name: "Belgium",
						value: 0
					},
					{
						name: "Benin",
						value: -1.81412e+07
					},
					{
						name: "Burkina Faso",
						value: 0
					},
					{
						name: "Bangladesh",
						value: -3.9791e+08
					},
					{
						name: "Bulgaria",
						value: -1.71e+09
					},
					{
						name: "Bahrain",
						value: 6.96809e+07
					},
					{
						name: "Bahamas",
						value: -3.66e+07
					},
					{
						name: "Bosnia and Herzegovina",
						value: 0
					},
					{
						name: "Belarus",
						value: 0
					},
					{
						name: "Belize",
						value: 1.535e+07
					},
					{
						name: "Bermuda",
						value: 0
					},
					{
						name: "Bolivia",
						value: -1.989e+08
					},
					{
						name: "Brazil",
						value: -3.823e+09
					},
					{
						name: "Barbados",
						value: -7.8e+06
					},
					{
						name: "Brunei",
						value: 0
					},
					{
						name: "Bhutan",
						value: 0
					},
					{
						name: "Botswana",
						value: -1.92962e+07
					},
					{
						name: "Central African Rep.",
						value: -8.9132e+07
					},
					{
						name: "Canada",
						value: -2.02594e+10
					},
					{
						name: "Switzerland",
						value: 6.12364e+09
					},
					{
						name: "Chile",
						value: -4.8461e+08
					},
					{
						name: "China",
						value: 1.1997e+10
					},
					{
						name: "Ivory Coast",
						value: 0
					},
					{
						name: "Cameroon",
						value: -5.51191e+08
					},
					{
						name: "Dem. Rep. Congo",
						value: 0
					},
					{
						name: "Congo",
						value: -2.51226e+08
					},
					{
						name: "Colombia",
						value: 5.42e+08
					},
					{
						name: "Comoros",
						value: -1.04752e+07
					},
					{
						name: "Cape Verde",
						value: -3.83457e+06
					},
					{
						name: "Costa Rica",
						value: -4.24e+08
					},
					{
						name: "Curacao",
						value: 0
					},
					{
						name: "Northern Cyprus",
						value: -1.5434e+08
					},
					{
						name: "Czech Rep.",
						value: 0
					},
					{
						name: "Germany",
						value: 4.6456e+10
					},
					{
						name: "Djibouti",
						value: 0
					},
					{
						name: "Dominican Rep.",
						value: -4.35276e+07
					},
					{
						name: "Denmark",
						value: 1.37155e+09
					},
					{
						name: "Dominican Republic",
						value: -2.796e+08
					},
					{
						name: "Algeria",
						value: 1.42026e+09
					},
					{
						name: "Ecuador",
						value: -3.6e+08
					},
					{
						name: "Egypt",
						value: 2.327e+09
					},
					{
						name: "Euro area",
						value: 0
					},
					{
						name: "Eritrea",
						value: 0
					},
					{
						name: "Spain",
						value: -1.80094e+10
					},
					{
						name: "Estonia",
						value: 0
					},
					{
						name: "Ethiopia",
						value: -2.93768e+08
					},
					{
						name: "Finland",
						value: -6.96227e+09
					},
					{
						name: "Fiji",
						value: -9.39964e+07
					},
					{
						name: "France",
						value: -9.94423e+09
					},
					{
						name: "Faroe Islands",
						value: 0
					},
					{
						name: "Micronesia, Fed. Sts.",
						value: 0
					},
					{
						name: "Gabon",
						value: 1.67704e+08
					},
					{
						name: "United Kingdom",
						value: -3.88109e+10
					},
					{
						name: "Georgia",
						value: 0
					},
					{
						name: "Ghana",
						value: -2.232e+08
					},
					{
						name: "French Guiana",
						value: -2.0298e+08
					},
					{
						name: "Gambia",
						value: 2.41744e+07
					},
					{
						name: "Guinea-Bissau",
						value: -4.5292e+07
					},
					{
						name: "Equatorial Guinea",
						value: -1.89925e+07
					},
					{
						name: "Greece",
						value: -3.537e+09
					},
					{
						name: "Grenada",
						value: -4.6237e+07
					},
					{
						name: "Guatemala",
						value: -2.129e+08
					},
					{
						name: "Guyana",
						value: 0
					},
					{
						name: "Hong Kong SAR, China",
						value: 0
					},
					{
						name: "Honduras",
						value: -5.14e+07
					},
					{
						name: "Croatia",
						value: 0
					},
					{
						name: "Haiti",
						value: -2.19e+07
					},
					{
						name: "Hungary",
						value: 3.78584e+08
					},
					{
						name: "Indonesia",
						value: -2.988e+09
					},
					{
						name: "India",
						value: -7.03565e+09
					},
					{
						name: "Ireland",
						value: 0
					},
					{
						name: "Iran",
						value: 3.27e+08
					},
					{
						name: "Iraq",
						value: 0
					},
					{
						name: "Iceland",
						value: -1.33579e+08
					},
					{
						name: "Israel",
						value: 1.634e+08
					},
					{
						name: "Italy",
						value: -1.64378e+10
					},
					{
						name: "Jamaica",
						value: -3.12099e+08
					},
					{
						name: "Jordan",
						value: -2.27134e+08
					},
					{
						name: "Japan",
						value: 0
					},
					{
						name: "Kazakhstan",
						value: 0
					},
					{
						name: "Kenya",
						value: -5.27084e+08
					},
					{
						name: "Kyrgyz Republic",
						value: 0
					},
					{
						name: "Cambodia",
						value: 0
					},
					{
						name: "Kiribati",
						value: -9.18695e+06
					},
					{
						name: "St. Kitts and Nevis",
						value: -4.69704e+07
					},
					{
						name: "South Korea",
						value: -2.4036e+09
					},
					{
						name: "Kuwait",
						value: 3.88622e+09
					},
					{
						name: "Lao PDR",
						value: -5.49e+07
					},
					{
						name: "Lebanon",
						value: 0
					},
					{
						name: "Liberia",
						value: 0
					},
					{
						name: "Libya",
						value: 2.2011e+09
					},
					{
						name: "St. Lucia",
						value: -5.70444e+07
					},
					{
						name: "Sri Lanka",
						value: -2.98301e+08
					},
					{
						name: "Lesotho",
						value: 1.01687e+08
					},
					{
						name: "Lithuania",
						value: 0
					},
					{
						name: "Luxembourg",
						value: 0
					},
					{
						name: "Latvia",
						value: 0
					},
					{
						name: "Macao SAR, China",
						value: 0
					},
					{
						name: "Morocco",
						value: -1.95575e+08
					},
					{
						name: "Moldova",
						value: 0
					},
					{
						name: "Madagascar",
						value: -2.64981e+08
					},
					{
						name: "Maldives",
						value: 9.85391e+06
					},
					{
						name: "Mexico",
						value: -7.451e+09
					},
					{
						name: "Marshall Islands",
						value: 0
					},
					{
						name: "Macedonia",
						value: 0
					},
					{
						name: "Mali",
						value: -2.21145e+08
					},
					{
						name: "Malta",
						value: -5.57569e+07
					},
					{
						name: "Myanmar",
						value: -4.31312e+08
					},
					{
						name: "Montenegro",
						value: 0
					},
					{
						name: "Mongolia",
						value: -6.1904e+08
					},
					{
						name: "Mozambique",
						value: 0
					},
					{
						name: "Mauritania",
						value: -9.62672e+06
					},
					{
						name: "Mauritius",
						value: -1.19286e+08
					},
					{
						name: "Malawi",
						value: -8.61892e+07
					},
					{
						name: "Malaysia",
						value: -8.69911e+08
					},
					{
						name: "Namibia",
						value: 2.75575e+07
					},
					{
						name: "New Caledonia",
						value: 0
					},
					{
						name: "Niger",
						value: -2.35884e+08
					},
					{
						name: "Nigeria",
						value: 4.98825e+09
					},
					{
						name: "Nicaragua",
						value: -3.052e+08
					},
					{
						name: "Netherlands",
						value: 8.08882e+09
					},
					{
						name: "Norway",
						value: 3.98526e+09
					},
					{
						name: "Nepal",
						value: -2.89196e+08
					},
					{
						name: "New Zealand",
						value: 0
					},
					{
						name: "Oman",
						value: 1.10637e+09
					},
					{
						name: "Pakistan",
						value: -1.66141e+09
					},
					{
						name: "Panama",
						value: 2.091e+08
					},
					{
						name: "Peru",
						value: -1.419e+09
					},
					{
						name: "Philippines",
						value: -2.695e+09
					},
					{
						name: "Palau",
						value: 0
					},
					{
						name: "Papua New Guinea",
						value: -7.56722e+07
					},
					{
						name: "Poland",
						value: 3.067e+09
					},
					{
						name: "Portugal",
						value: -1.81401e+08
					},
					{
						name: "Paraguay",
						value: 3.901e+08
					},
					{
						name: "West Bank",
						value: 0
					},
					{
						name: "French Polynesia",
						value: 0
					},
					{
						name: "Qatar",
						value: 0
					},
					{
						name: "Romania",
						value: -3.254e+09
					},
					{
						name: "Russia",
						value: 0
					},
					{
						name: "Rwanda",
						value: 0
					},
					{
						name: "Saudi Arabia",
						value: -4.14667e+09
					},
					{
						name: "Sudan",
						value: -3.72246e+08
					},
					{
						name: "Senegal",
						value: -3.63286e+08
					},
					{
						name: "Singapore",
						value: 3.12187e+09
					},
					{
						name: "Solomon Is.",
						value: -2.77604e+07
					},
					{
						name: "Sierra Leone",
						value: -6.94069e+07
					},
					{
						name: "El Salvador",
						value: -1.51745e+08
					},
					{
						name: "Serbia",
						value: 0
					},
					{
						name: "South Sudan",
						value: 0
					},
					{
						name: "Sao Tome and Principe",
						value: -1.204e+07
					},
					{
						name: "Suriname",
						value: 0
					},
					{
						name: "Slovak Republic",
						value: 0
					},
					{
						name: "Slovenia",
						value: 0
					},
					{
						name: "Sweden",
						value: -6.33886e+09
					},
					{
						name: "Swaziland",
						value: 5.07475e+07
					},
					{
						name: "Sint Maarten (Dutch part)",
						value: 0
					},
					{
						name: "Seychelles",
						value: -1.29772e+07
					},
					{
						name: "Syria",
						value: 1.7623e+09
					},
					{
						name: "Chad",
						value: -4.56174e+07
					},
					{
						name: "Togo",
						value: -8.42489e+07
					},
					{
						name: "Thailand",
						value: -7.2811e+09
					},
					{
						name: "Tajikistan",
						value: 0
					},
					{
						name: "East Timor",
						value: 0
					},
					{
						name: "Tonga",
						value: 5.79481e+06
					},
					{
						name: "Trinidad and Tobago",
						value: 4.58988e+08
					},
					{
						name: "Tunisia",
						value: -4.63378e+08
					},
					{
						name: "Turkey",
						value: -2.625e+09
					},
					{
						name: "Tuvalu",
						value: 0
					},
					{
						name: "United Republic of Tanzania",
						value: -5.58927e+08
					},
					{
						name: "Uganda",
						value: -2.633e+08
					},
					{
						name: "Ukraine",
						value: 0
					},
					{
						name: "Uruguay",
						value: 1.8589e+08
					},
					{
						name: "United States",
						value: -7.8952e+10
					},
					{
						name: "St. Vincent and the Grenadines",
						value: -2.35556e+07
					},
					{
						name: "Venezuela",
						value: 8.279e+09
					},
					{
						name: "Vietnam",
						value: 0
					},
					{
						name: "Vanuatu",
						value: -6.18187e+06
					},
					{
						name: "Samoa",
						value: 8.6196e+06
					},
					{
						name: "Kosovo",
						value: 0
					},
					{
						name: "Yemen",
						value: 0
					},
					{
						name: "South Africa",
						value: 1.55157e+09
					},
					{
						name: "Zambia",
						value: -5.944e+08
					},
					{
						name: "Zimbabwe",
						value: -1.3968e+08
					},
				];


				var timeFn = null;
				
				function formatterDateTime() {
				  var date=new Date()
				  var month=date.getMonth() + 1
				        var datetime = date.getFullYear()
				                + ""// "年"
				                + (month >= 10 ? month : "0"+ month)
				                + ""// "月"
				                + (date.getDate() < 10 ? "0" + date.getDate() : date
				                        .getDate())
				                + ""
				                + (date.getHours() < 10 ? "0" + date.getHours() : date
				                        .getHours())
				                + ""
				                + (date.getMinutes() < 10 ? "0" + date.getMinutes() : date
				                        .getMinutes())
				                + ""
				                + (date.getSeconds() < 10 ? "0" + date.getSeconds() : date
				                        .getSeconds());
				        return datetime;
				    }

				$.ajax({
					url: 'https://route.showapi.com/2217-5',
					type: 'get',

					dataType: 'json',
					data: {
					        "showapi_timestamp": formatterDateTime(),
					        "showapi_appid": '231965', //appid
					        "showapi_sign": 'eee0c248474046f2a56dc9219d3182c8',  //password
					},
					success: (res) => {

						var data = res.showapi_res_body.foreignList
						value0 = []
						for (var i = 0; i < data.length; i++) {
							let name = data[i].countryFullName
							var keyObj = {
								'Bolivia (Plurinational State of)': 'Bolivia',
								'United States of America': 'United States',
								'Russian Federation': 'Russia',
								"Democratic Republic of the Congo": 'Dem. Rep. Congo',
								"Iran (Islamic Republic of)": 'Iran',
								"South Sudan": 'S. Sudan',
								'The United Kingdom': 'United Kingdom',
								'Syrian ArabRepublic': 'Syria',
								'Uzbekstan': 'Uzbekistan'
							}
							name = keyObj[data[i].countryFullName] || data[i].countryFullName
							
							value0.push({
								name: name,
								value: data[i].confirmedNum
							})
							console.log(value0)
						}
					


					loadMap('./data/starbucks.json', 'china'); //initial map

					
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
										selectedMode: 'false', //multi area selection not allowed
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
							} else {
								alert('Cannot load the map');
							}
						});
					}
				
					}
				})

				//click to next level map
				this.myChart.on('click', (params) => {
					clearTimeout(timeFn);
					//avoid time conflict between single and double click
					timeFn = setTimeout(() => {
						var name = params.name; //area name

						this.$router.push({
							path: '/manage1',
							query: {
								url: `${name.split(" ").join("_")}.json`,
								name: name
							}
						});


					}, 250);
					return false
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
