<template>
	<div class="manage">
		<div class="left">
			<div class="title">
				<span></span>
				<p>Data update to - 2020.05.17 18:37</p>
			</div>
			<div class="map-content">
				<div class="title-12">THE CASE HAS BEEN TRACKED IN THE PAST THREE DAYS</div>
				
				<div id="container">
					
				</div>
			</div>
		</div>
		<div class="right">

			<div class="serach">
				<input type="text" value="The patient" >
			</div>
			<div class="line">
				<lineEchart></lineEchart>
			</div>
			<div class="inform">
				<div style="width:34%;margin-right: 58px;">
					<h2>TIME OF DIAGNOSIS</h2>
					<h3 style="color: #e64546;">2020.05.07</h3>
				</div>
				<div style="margin-right: 58px;">
					<h2>AGE</h2>
					<h3 style="color: #3776d1;">31</h3>
				</div>
				<div>
					<h2>GENDER</h2>
					<h3 style="color: #3776d1;">Male</h3>
				</div>
			</div>
			
			<div>
				<h4 class="h4">Doctor's comments on the patient</h4>
				<p class="p">Good Good Good.</p>
			</div>

		</div>
	</div>
</template>

<script>
	import {
		mapActions,
		mapMutations
	} from "vuex"
	import lineEchart from './line/line.vue';
	export default {
		components: {
			//pieEchart,
			lineEchart
		},
		data() {
			return {
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
							legendname: 'WOMAN',
							name: "WOMAN  335",
							itemStyle: {
								color: "#e64546"
							}
						},
						{
							value: 310,
							legendname: 'MAN',
							name: "MAN  310",
							itemStyle: {
								color: "#3776d1"
							}
						}
					]
				},
			};
		},
		mounted() {
			this.$nextTick(() => {
				var map = new AMap.Map('container', {
					resizeEnable: true, //size change
					zoom: 11,
					center: [116.397428, 39.90923] ,//initial center
					  lang: "en" //language
				});
				
				var toolBar = new AMap.ToolBar({
				     visible: false
				 })
				 map.addControl(toolBar);
				 
				 toolBar.show();
				 toolBar.hideDirection()
				 toolBar.hideRuler();
		
				// location1
				var markerContent = '' +
					'<div class="custom-content-marker1 showText" style="width:90px;height:90px">' +
					' 	<div class="num" style="background-color: rgba(107, 110, 172, 0.5)"><span style="background-color: #6b6eac;"></span></div>' +
					' 	<div class="address" style="background-color: #6b6eac;">2020.05.07  14:35 - 2020.05.08  14:35</div>' +
					'</div>';
		
		
				var position = new AMap.LngLat(116.326028, 39.88423);
				var marker = new AMap.Marker({
					position: position,

					content: markerContent,

					offset: new AMap.Pixel(-13, -30)
				});
		
				// add to map
				map.add(marker);
				

				var markerContent = '' +
					'<div class="custom-content-marker1" style="width:90px;height:90px">' +
					' 	<div class="num" style="background-color: rgba(107, 110, 172, 0.5)"><span style="background-color: #6b6eac;"></span></div>' +
					' 	<div class="address" style="background-color: #6b6eac;">2020.05.07  14:35 - 2020.05.08  14:35</div>' +
					'</div>';
						
						
				var position = new AMap.LngLat(116.325028, 39.85423);
				var marker = new AMap.Marker({
					position: position,

					content: markerContent,

					offset: new AMap.Pixel(-13, -30)
				});
						

				map.add(marker);
				

				var markerContent = '' +
					'<div class="custom-content-marker1" style="width:180px;height:180px">' +
					' 	<div class="num" style="background-color: rgba(253, 62, 111, 0.5)"><span style="background-color: #fd3e6f;"></span></div>' +
					' 	<div class="address" style="background-color: #fd3e6f;">2020.05.07  14:35 - 2020.05.08  14:35</div>' +
					'</div>';
						
						
				var position = new AMap.LngLat(116.223028, 39.84423);
				var marker = new AMap.Marker({
					position: position,

					content: markerContent,

					offset: new AMap.Pixel(-13, -30)
				});
						

				map.add(marker);
				

				var markerContent = '' +
					'<div class="custom-content-marker1 showText" style="width:70px;height:70px">' +
					' 	<div class="num" style="background-color: rgba(253, 62, 111, 0.5)"><span style="background-color: #fd3e6f;"></span></div>' +
					' 	<div class="address" style="background-color: #fd3e6f;">2020.05.07  14:35 - 2020.05.08  14:35</div>' +
					'</div>';
						
						
				var position = new AMap.LngLat(116.213028, 39.94423);
				var marker = new AMap.Marker({
					position: position,

					content: markerContent,

					offset: new AMap.Pixel(-13, -30)
				});
						

				map.add(marker);
				   
			})
		},
		methods: {

		}
	};
</script>

<style lang="less" scope>
	
	.amap-zoom-plus {
		width: 0.4rem;
		    height: 0.4rem;
		    background-color: #1c1d32;
		    box-shadow: -0.05rem -0.05rem 0.05rem 0rem rgba(75, 75, 83, 0.5), 0.05rem 0.05rem 0.05rem 0rem rgba(0, 0, 0, 0.50196078);
		    border-radius: 0.12rem;
		    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaAQMAAACThN6NAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAZQTFRFAAAAOWvvOGEqVQAAAAJ0Uk5TAP9bkSK1AAAAF0lEQVR4nGNgAAM+soj6//8PIBHkmQIAqnUK7BvF6LcAAAAASUVORK5CYII=);
		    background-position: center;
		    background-repeat: no-repeat;
		    cursor: pointer;
	}
	.amap-zoom-plus:hover {
	   background-position: center;
	}
	.amap-zoom-minus:hover {
	   background-position: center;
	}
	.amap-zoom-minus {
		    width: 0.4rem;
		    height: 0.4rem;
		    background-color: #1c1d32;
		    box-shadow: -0.05rem -0.05rem 0.05rem 0rem rgba(75, 75, 83, 0.5), 0.05rem 0.05rem 0.05rem 0rem rgba(0, 0, 0, 0.50196078);
		    border-radius: 0.12rem;
		    margin-left: 0.22rem;
		    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAEAQMAAACqWL1mAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAZQTFRFAAAAOWvvOGEqVQAAAAJ0Uk5TAP9bkSK1AAAAEUlEQVR4nGNgAIH6//8PIAgAR8wJuHmwHh0AAAAASUVORK5CYII=);
		    background-position: center;
		    background-repeat: no-repeat;
		    cursor: pointer;
	}
	.amap-toolbar {
		position: initial;
	}
	.amap-locate {
		display: none !important;
	}
	.amap-zoomcontrol {
		    position: absolute !important;
		    display: flex;
		    left: 8rem !important;
		    bottom: 0.44rem;
		    z-index: 99;
		    width: 100px;
	}
	
	#container {
		width: 100%;
		height: 100%;
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
		
		.h4 {
			font-size: 20px;
				font-weight: normal;
				font-stretch: normal;
				line-height: 20px;
				
				
				letter-spacing: 0px;
				color: #ffffff;
				width: 5.95rem;
				    margin: 0 auto;
					margin-bottom: 23px;
					margin-top: 60px;
				
		}
		
		.p {
			font-size: 16px;
				font-weight: normal;
				font-stretch: normal;
				line-height: 16px;
				letter-spacing: 0px;
				color: #5a6384;
				width: 5.95rem;
				    margin: 0 auto;
		}

		.pins {
			height: 309px;
			display: flex;
			width: 100%;
		}

		.pins>div {
			width: 50%;
			height: 100%;
			position: relative;

			&>div {
				z-index: 99;
			}

			&:after {
				content: "";
				width: 180px;
				height: 180px;
				background-color: #1c1d32;
				box-shadow: -0.08rem -0.08rem 0.08rem 0rem rgba(75, 75, 83, 0.5), 0.08rem 0.08rem 0.08rem 0rem rgba(0, 0, 0, 0.5019607843137255);
				border-radius: 100px;
				position: absolute;
				top: 50%;
				left: 50%;
				transform: translate(-50%, -50%);
			}
		}

		.line {
			height: 300px;
			width: 100%;
			margin-left: 65px;
			margin-right: 43px;
			width: calc(100% - 108px);
			margin-bottom: 20px;
		}

		.inform {
			display: flex;
			width: 595px;
			margin: 0 auto;
			position: relative;
			padding-top: 16px;
			box-sizing: border-box;
			justify-content: center;
			padding-top: 46px;

			&:after {
				content: "";

				position: absolute;

				top: 0px;

				left: 0px;

				width: 100%;

				height: 8px;

				background-image: url(../../assets/images/t.png);

				background-size: cover;

			}

			&>div {


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

				.title-12 {
					height: 112px;

					font-size: 16px;
					font-weight: normal;
					font-stretch: normal;
					line-height: 50px;
					letter-spacing: 0px;
					color: #ffffff;
					text-align: center;
					position: relative;
					width: 800px;
					margin: 0 auto;
					position: absolute;
					z-index: 99;
						width: 590px;
						height: 50px;
						background-color: #1c1d32;
						box-shadow: -0.085rem -0.085rem 0.12rem 0rem rgba(75, 75, 83, 0.5), 0.085rem 0.085rem 0.12rem 0rem rgba(0, 0, 0, 0.5019607843137255);
						left: 50%;
						border-radius: 10px;
						transform: translate(-50%);
						top: 19px;
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
				background-size: cover;
				background-size: 100%;
				background-position: center;
				
					height: 61px;
					background-color: #1c1d32;
					box-shadow: -0.085rem -0.085rem 0.12rem 0rem rgba(75, 75, 83, 0.5), 0.085rem 0.085rem 0.12rem 0rem rgba(0, 0, 0, 0.5019607843137255);
					
					border-radius: 10px;

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
					color: #ffffff;
					font-weight: 700;

				}
			}
		}
	}
</style>
