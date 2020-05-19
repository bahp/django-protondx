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
			<div class="serach">
				<input type="text" placeholder="Please enter a state / Province">
			</div>
			<el-table
			    :data="tableData"
			    :height="tableHeight"
			    border
			    style="width: 100%">
			    <el-table-column
				align="center"
			      prop="date"
			      label="REGION">
				  <template slot-scope="scope">
				         <a style="color: #6178ca;">{{scope.row.date}}</a>
				        </template>
			    </el-table-column>
			    <el-table-column
			      prop="name"
				  align="center"
			      label="CONFIRMED">
			    </el-table-column>
			    <el-table-column
			      prop="address"
				  align="center"
			      label="EXISTING">
			    </el-table-column>
				<el-table-column
				align="center"
				  prop="date1"
				  label="RECOVERY">
				</el-table-column>
				<el-table-column
				align="center"
				  prop="date2"
				  label="DEATH">
				</el-table-column>
			  </el-table>
			  <div class="el-pagination1">
				  <el-pagination
				      layout="prev, pager, next"
				      :total="1000">
				    </el-pagination>
			  </div>
		</div>
    </div>
</template>

<script>
    import {mapActions, mapMutations} from "vuex";
	import mapEchart from './map/map.vue';
    export default {
        name: "login-registered",
        data() {
            return {
				tableHeight: setRem2Px(6.68),
				tableData: [{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }, {
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }, {
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }, {
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        },{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }, {
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        },
						{
						          date: 'A region',
						          name: '288',
						          address: '288',
								  date1: '288',
								  date2: '288'
						        },
								{
								          date: 'A region',
								          name: '288',
								          address: '288',
										  date1: '288',
										  date2: '288'
								        },
										{
										          date: 'A region',
										          name: '288',
										          address: '288',
												  date1: '288',
												  date2: '288'
										        },
												{
												          date: 'A region',
												          name: '288',
												          address: '288',
														  date1: '288',
														  date2: '288'
												        },{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        },
						{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }
						,{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }
						,{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }
						,{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }
						,{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        },
						,{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }
						,{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }
						,{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }
						,{
				          date: 'A region',
				          name: '288',
				          address: '288',
						  date1: '288',
						  date2: '288'
				        }]
            };
        },
        components: {
			mapEchart
        },
        mounted() {
			window.addEventListener('resize', () => {
				this.tableHeight = setRem2Px(6.68)
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
						 	box-shadow: -0.05rem -0.05rem 0.05rem 0rem rgba(75, 75, 83, 0.5), 0.05rem 0.05rem 0.05rem 0rem  rgba(0, 0, 0, 0.5019607843137255);
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
							box-shadow: -0.05rem -0.05rem 0.05rem 0rem rgba(75, 75, 83, 0.5), 0.05rem 0.05rem 0.05rem 0rem  rgba(0, 0, 0, 0.5019607843137255);
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
							box-shadow: -1.4px -1.4px 6px 0px 
								#2fcf87, 
								1.4px 1.4px 6px 0px 
								rgba(28, 29, 50, 0.5);
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
						box-shadow: -0.085rem -0.085rem 0.12rem 0rem rgba(75, 75, 83, 0.5), 0.085rem 0.085rem 0.12rem 0rem  rgba(0, 0, 0, 0.5019607843137255);
						border-radius: 20px;
						margin-right: 40px;
						padding: 0 40px;
						background-image: url(../../assets/images/tp.png);
						    background-size: cover;
						.map-content {
								height: 738px;
								box-shadow: -0.085rem -0.085rem 0.12rem 0rem rgba(75, 75, 83, 0.5), 0.085rem 0.085rem 0.12rem 0rem  rgba(0, 0, 0, 0.5019607843137255);
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
								margin:0 auto;
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
						height:900px;
						background-color: #1c1d32;
						box-shadow: -0.085rem -0.085rem 0.12rem 0rem rgba(75, 75, 83, 0.5), 0.085rem 0.085rem 0.12rem 0rem  rgba(0, 0, 0, 0.5019607843137255);
						border-radius: 20px;
						padding-top: 33px;
						
						.serach {
							width: calc(100% - 114px);
							margin: 0 auto;
								height: 61px;
								background-color: #1c1d32;
								margin-bottom: 20px;
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
								border:none;
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
