<template>
	<div class="manage">
		<div class="left">
			<div class="title">
				<span></span>
				<p>Data update to - 2020.05.17 18:37</p>
			</div>
			<div class="map-content">
				<div class="title-1">NUMBER OF CONFIRMED CASES, EXCLUDING CURE AND DEATH</div>
				<div class="view">
					<div class="more" @click="zoomin"></div>
					<div class="less" @click="zoomout"></div>
				</div>
				<div class="map">
					<mapEchart ref="map"></mapEchart>
				</div>
			</div>
		</div>
		<div class="right">
			<div class="inform">
				<div>
					<h2>CONFIRMED</h2>
					<h3 style="color: #e64546;">288</h3>
					<p>
						YDAY<span style="color: #e64546;">-288</span>
					</p>
				</div>
				<div>
					<h2>EXISTING</h2>
					<h3 style="color: #e64546;">288</h3>
					<p>
						YDAY<span style="color: #e64546;">-288</span>
					</p>
				</div>
				<div>
					<h2>RECOVERY</h2>
					<h3 style="color: #38e093;">288</h3>
					<p>
						YDAY<span style="color: #38e093;">+288</span>
					</p>
				</div>
				<div>
					<h2>DEATH</h2>
					<h3 style="color: #e64546;">288</h3>
					<p>
						YDAY<span style="color: #e64546;">-288</span>
					</p>
				</div>
			</div>
			<div class="pies">
				<div>
					<pieEchart :data="pie1"></pieEchart>
				</div>
				<div>
					<pieEchart :data="pie2"></pieEchart>
				</div>
			</div>
			<div class="line1">
				<lineEchart></lineEchart>
			</div>
			<el-table :data="tableData" :height="tableHeight" border style="width: 100%">
				<el-table-column align="center" prop="date" label="TIME">
					<template slot-scope="scope">
						<a @click="hreftwo" style="color: #6178ca;">{{scope.row.date}}</a>

					</template>
				</el-table-column>
				<el-table-column prop="name" align="center" label="GENDER">
				</el-table-column>
				<el-table-column prop="address" align="center" label="AGE">
				</el-table-column>
				<el-table-column align="center" prop="date1" label="HOSPITAL">
				</el-table-column>
			</el-table>

		</div>
	</div>
</template>

<script>
	import {
		mapActions,
		mapMutations
	} from "vuex";
	import pieEchart from './pie/pie.vue';
	import lineEchart from './line/line.vue';
	import mapEchart from './map/map.vue';
	export default {
		components: {
			pieEchart,
			lineEchart,
			mapEchart
		},
		data() {
			return {
				tableHeight: setRem2Px(1.5),
				pie1: {
					
					title: 'AGE DISTRIBUTION',
					data: [{
							value: 335,
							legendname: '0-12',
							name: "0-12  335",
							itemStyle: {
								color: "#e64546"
							}
						},
						{
							value: 335,
							legendname: '≥71',
							name: "≥71  335",
							itemStyle: {
								color: "#9e38ce"
							}
						},
						{
							value: 335,
							legendname: '50-70',
							name: "50-70  335",
							itemStyle: {
								color: "#3776d1"
							}
						},
						{
							value: 154,
							legendname: '36-49',
							name: "36-49  154",
							itemStyle: {
								color: "#36d38b"
							}
						},
						{
							value: 234,
							legendname: '19-35',
							name: "19-35  234",
							itemStyle: {
								color: "#d1cd37"
							}
						},
						{
							value: 310,
							legendname: '13-18',
							name: "13-18  310",
							itemStyle: {
								color: "#d16e37"
							}
						},




					]
				},
				pie2: {
					title: 'GENDER DISTRIBUTION',
					data: [{
							value: 335,
							legendname: 'FEMALE',
							name: "FEmale  335",
							itemStyle: {
								color: "#e64546"
							}
						},
						{
							value: 310,
							legendname: 'MALE',
							name: "MALE  310",
							itemStyle: {
								color: "#3776d1"
							}
						}
					]
				},
				tableData: [{
						date: '2020.05.07  14:35 ',
						name: 'male',
						address: '31',
						date1: 'Mayo Clinic'
					}, {
						date: '2020.05.07  14:35 ',
						name: 'male',
						address: '31',
						date1: 'Mayo Clinic'
					}, {
						date: '2020.05.07  14:35 ',
						name: 'male',
						address: '31',
						date1: 'Mayo Clinic'
					}, {
						date: '2020.05.07  14:35 ',
						name: 'male',
						address: '31',
						date1: 'Mayo Clinic'
					}, {
						date: '2020.05.07  14:35 ',
						name: 'male',
						address: '31',
						date1: 'Mayo Clinic'
					}, {
						date: '2020.05.07  14:35 ',
						name: 'male',
						address: '31',
						date1: 'Mayo Clinic'
					},
					{
							date: '2020.05.07  14:35 ',
							name: 'male',
							address: '31',
							date1: 'Mayo Clinic'
						},
					{
							date: '2020.05.07  14:35 ',
							name: 'male',
							address: '31',
							date1: 'Mayo Clinic'
						},
					{
							date: '2020.05.07  14:35 ',
							name: 'male',
							address: '31',
							date1: 'Mayo Clinic'
						},
					{
							date: '2020.05.07  14:35 ',
							name: 'male',
							address: '31',
							date1: 'Mayo Clinic'
						}, {
						date: '2020.05.07  14:35 ',
						name: 'male',
						address: '31',
						date1: 'Mayo Clinic'
					},
					{
							date: '2020.05.07  14:35 ',
							name: 'male',
							address: '31',
							date1: 'Mayo Clinic'
						}, {
						date: '2020.05.07  14:35 ',
						name: 'male',
						address: '31',
						date1: 'Mayo Clinic'
					}
				]
			};
		},
		mounted() {
			window.addEventListener('resize', () => {
				this.tableHeight = setRem2Px(1.5)
			})
		},
		methods: {
			zoomin () {
				this.$refs.map.zoom = this.$refs.map.zoom + 0.2
				this.$refs.map.resize()
			},
			zoomout () {
				this.$refs.map.zoom = this.$refs.map.zoom - 0.2
				if (this.$refs.map.zoom <= 0) {
					this.$refs.map.zoom = 0.1
				}
				this.$refs.map.resize()
			},
			hreftwo(){
				this.$router.push({path:'/manage2'})
			}
		}
	};
</script>

<style lang="less" scope>
	.map {
		position: relative;
		width: 100%;
		height: calc(100% - 112px);
	}
	.manage {
		width: 1920px;
		height: 100vh;
		display: flex;
		justify-content: center;
		align-items: center;

		box-sizing: border-box;
		background-image: url(../../assets/images/jb.png);
		background-size: 100%;

		.pies {
			height: 259px;
			display: flex;
			width: 100%;
		}

		.pies>div {
			width: 50%;
			height: 100%;
			position: relative;

			&>div {
				z-index: 99;
			}

			&:after { //line
				content: "";
				width: 160px;
				height: 160px;
				background-color: #1c1d32;
				box-shadow: -0.08rem -0.08rem 0.08rem 0rem rgba(75, 75, 83, 0.5), 0.08rem 0.08rem 0.08rem 0rem rgba(0, 0, 0, 0.5019607843137255);
				border-radius: 100px;
				position: absolute;
				top: 55%;
				left: 50%;
				transform: translate(-50%, -50%);
			}
		}

		.line1 {
			height: 250px;
			width: 100%;
			margin-left: 65px;
			margin-right: 43px;
			width: calc(100% - 108px);
			margin-bottom: 20px;
		}

		.inform {
			display: flex;
			height: 160px;
			width: 595px;
			margin: 0 auto;
			position: relative;
			padding-top: 16px;
			box-sizing: border-box;

			&:after {
				content: "";

				position: absolute;

				bottom: 0px;

				left: 0px;

				width: 100%;

				height: 8px;

				background-image: url(../../assets/images/t.png);

				background-size: cover;

			}

			&>div {

				width: 25%;

				h2 {
					font-size: 20px;
					font-weight: normal;
					font-stretch: normal;
					letter-spacing: 0px;
					color: #ffffff;
					text-align: center;
					line-height: 20px;
					margin-bottom: 15px;
				}

				h3 {
					font-size: 36px;
					font-weight: normal;
					font-stretch: normal;
					letter-spacing: 0px;
					color: #e64546;
					text-align: center;
					font-weight: 700;
					line-height: 36px;
					margin-bottom: 17px;
				}

				p {
					font-size: 16px;
					font-weight: normal;
					font-stretch: normal;
					letter-spacing: 0px;
					color: #5a6384;
					text-align: center;
					line-height: 16px;

					span {}
				}
			}
		}


		.view {
			position: absolute;
			display: flex;
			right: 100px;
			bottom: 44px;
			z-index: 99;

			.more {
				width: 40px;
				height: 40px;
				background-color: #1c1d32;
				box-shadow: -0.05rem -0.05rem 0.05rem 0rem rgba(75, 75, 83, 0.5), 0.05rem 0.05rem 0.05rem 0rem rgba(0, 0, 0, 0.5019607843137255);
				border-radius: 12px;
				background-image: url(../../assets/images/p.png);
				background-position: center;
				background-repeat: no-repeat;
				cursor: pointer;
			}

			.less {
				width: 40px;
				height: 40px;
				background-color: #1c1d32;
				box-shadow: -0.05rem -0.05rem 0.05rem 0rem rgba(75, 75, 83, 0.5), 0.05rem 0.05rem 0.05rem 0rem rgba(0, 0, 0, 0.5019607843137255);
				border-radius: 12px;
				margin-left: 22px;
				background-image: url(../../assets/images/l.png);
				background-position: center;
				background-repeat: no-repeat;
				cursor: pointer;
			}
		}

		.title {
			height: 82px;
			display: flex;
			align-items: center;
			margin-bottom: 40px;
			position: relative;

			&:after {
				content: "";
				position: absolute;
				bottom: 0px;
				width: 100%;
				height: 8px;
				background-image: url(../../assets/images/t.png);
				background-size: cover;
				left: 0px;
			}

			span {
				width: 14px;
				height: 14px;
				background-image: linear-gradient(0deg,
					#19b98e 0%,
					#5bfe79 100%);
				box-shadow: -1.4px -1.4px 6px 0px #2fcf87,
					1.4px 1.4px 6px 0px rgba(28, 29, 50, 0.5);
				margin-right: 15px;
				border-radius: 100px;
			}

			p {
				font-size: 20px;
				font-weight: normal;
				font-stretch: normal;
				line-height: 4.68px;
				letter-spacing: 0px;
				color: #ffffff;
			}
		}

		.left {
			width: 1082px;
			height: 900px;
			background-color: #1c1d32;
			box-shadow: -0.085rem -0.085rem 0.12rem 0rem rgba(75, 75, 83, 0.5), 0.085rem 0.085rem 0.12rem 0rem rgba(0, 0, 0, 0.5019607843137255);
			border-radius: 20px;
			margin-right: 40px;
			padding: 0 40px;
			background-image: url(../../assets/images/tp.png);
			background-size: cover;

			.map-content {
				height: 738px;
				box-shadow: -0.085rem -0.085rem 0.12rem 0rem rgba(75, 75, 83, 0.5), 0.085rem 0.085rem 0.12rem 0rem rgba(0, 0, 0, 0.5019607843137255);
				overflow: hidden;
				border-radius: 20px;
				background-color: #1c1d32;
				position: relative;

				.title-1 {
					height: 112px;

					font-size: 16px;
					font-weight: normal;
					font-stretch: normal;
					line-height: 112px;
					letter-spacing: 0px;
					color: #ffffff;
					text-align: center;
					position: relative;
					width: 800px;
					margin: 0 auto;

					&:after {
						content: "";
						position: absolute;
						bottom: 0px;
						left: 0px;
						width: 100%;
						height: 8px;
						background-image: url(../../assets/images/t.png);
						background-size: cover;
					}
				}
			}
		}

		.right {
			width: 718px;
			height: 900px;
			background-color: #1c1d32;
			box-shadow: -0.085rem -0.085rem 0.12rem 0rem rgba(75, 75, 83, 0.5), 0.085rem 0.085rem 0.12rem 0rem rgba(0, 0, 0, 0.5019607843137255);
			border-radius: 20px;
			padding-top: 33px;

			.serach {
				width: calc(100% - 114px);
				margin: 0 auto;
				height: 61px;
				background-color: #1c1d32;
				margin-bottom: 60px;
				display: flex;
				background-image: url(../../assets/images/k.png);
				background-size: cover;
				background-size: 100%;
				background-position: center;

				&>input::-webkit-input-placeholder {
					/* Chrome/Opera/Safari */
					color: #5a6384 !important;
				}

				&>input::-moz-placeholder {
					/* Firefox 19+ */
					color: #5a6384 !important;
				}

				&>input:-ms-input-placeholder {
					/* IE 10+ */
					color: #5a6384 !important;
				}

				&>input:-moz-placeholder {
					/* Firefox 18- */
					color: #5a6384 !important;
				}

				&>input {
					width: 100%;
					height: 100%;
					background-color: transparent;
					border: none;
					font-family: SourceHanSansCN-Regular;
					font-size: 16px;
					font-weight: normal;
					font-stretch: normal;
					line-height: 4.68px;
					letter-spacing: 0px;
					color: #5a6384;
					padding: 0 40px;
					box-sizing: border-box;
					outline: none;

				}
			}
		}
	}
</style>
