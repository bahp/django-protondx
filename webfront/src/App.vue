<template>
    <div id="app">
        <keep-alive>
            <router-view/>
        </keep-alive>
    </div>
</template>

<style lang="less">
	.el-table__body-wrapper a {
		cursor: pointer;
	}
   

    body,
    html {
        padding: 0px;
        margin: 0px;
    }

    * {
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
    }

    body::-webkit-scrollbar {

        width: 3px;

        height: 1px;
    }

    body::-webkit-scrollbar-thumb {

        border-radius: 3px;
        -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
        background: #3a6bef;
    }

    body::-webkit-scrollbar-track {

        -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
        border-radius: 3px;
        background: #3a5584;
    }


    .custom-content-marker {
        position: relative;

        .my-wz {
            width: 110px;
            height: 42px;
            font-size: 18px;
            font-weight: normal;
            font-stretch: normal;
            letter-spacing: 0px;
            color: #ffffff;
            text-align: center;
            line-height: 35px;
            position: absolute;
            top: 20px;
            left: -45px;
            background-image: url(http://94.191.115.121:8080/i2.svg);
            background-repeat: no-repeat;
        }

        img {
            width: 24px;
            height: 45px;
        }
    }


    .custom-content-marker1 {
        position: relative;
		
		&:hover {
			.address {
				display: block;
			}
		}
		
		&.showText {
			.address {
				display: block;
			}
		}
		

        .num {
            width:100%;
			height: 100%;
			border-radius: 100px;
			&:before {
				content: "";
				width: 14px;
					height: 14px;
					border: solid 2px #ffffff;
					position: absolute;
					top: 50%;
					left: 50%;
					transform: translate(-50%, -50%);
					border-radius: 100px;
			}
			span {
				width: 12px;
					height: 12px;
					position: absolute;
					top: 50%;
					border-radius: 100px;
					left: 50%;
					transform: translate(-50%, -50%);
			}
        }


        .address {
			display: none;
            font-size: 0.16rem;
                font-weight: normal;
                font-stretch: normal;
                line-height: 0.16rem;
                letter-spacing: 0rem;
                color: #93b4e6;
                position: absolute;
                top: 50%;
                left: 50%;
                font-weight: 700;
                width: 316px;
                height: 50px;
                width: 316px;
                height: 50px;
                
                box-shadow: -7.1px -7.1px 10px 0px rgba(33, 33, 49, 0.5), 7.1px 7.1px 10px 0px rgba(33, 33, 49, 0.5);
                border-radius: 0px 10px 10px 10px;
                font-size: 16px;
                font-weight: normal;
                font-stretch: normal;
                line-height: 20px;
                letter-spacing: 0px;
                color: #ffffff;
                line-height: 50px;
                text-align: center;
        }
    }


    // 122444


    @font-face {
        font-family: 'iconfont';  /* project id 1748805 */
        src: url('assets/fonts/iconfont.eot');
        src: url('assets/fonts/iconfont.eot?#iefix') format('embedded-opentype'),
        url('assets/fonts/iconfont.woff2') format('woff2'),
        url('assets/fonts/iconfont.woff') format('woff'),
        url('assets/fonts/iconfont.ttf') format('truetype'),
        url('assets/fonts/iconfont.svg#iconfont') format('svg');
    }


    // 以下是公共css

    .table-box-w100 {
        
    }

    

    input::-webkit-input-placeholder {
        color: #6899e3 !important;
    }

    input::-moz-placeholder {
        color: #6899e3 !important;
    }

    input:-moz-placeholder {
        color: #6899e3 !important;
    }

    input:-ms-input-placeholder {
        color: #6899e3 !important;
    }

    textarea::-webkit-input-placeholder {
        color: #6899e3 !important;
    }

    textarea::-moz-placeholder {
        color: #6899e3 !important;
    }

    textarea:-moz-placeholder {
        color: #6899e3 !important;
    }

    textarea:-ms-input-placeholder {
        color: #6899e3 !important;
    }

    .table-pagination {
        margin-top: 13px;
        display: flex;
        justify-content: flex-end;

        .el-pagination.is-background .btn-next, .el-pagination.is-background .btn-prev, .el-pagination.is-background .el-pager li {
            background-color: transparent;
            color: #40d5f5;
            min-width: 0.18rem;
            min-height: 0.2rem;
            height: 0.2rem;
            line-height: 0.2rem;
        }

        .el-pagination.is-background .el-pager li:not(.disabled).active {
            background-color: rgba(64, 214, 246, 0.2);
            border-radius: 3px;
            color: #40d5f5;
        }

        .el-pagination {
            padding: 0px !important;
            height: 20px !important;
        }

        .el-pager .more::before {
            line-height: 0.2rem;
        }

        .el-pagination .btn-prev {
            margin-left: 0px !important;
        }

        .el-pagination .btn-next {
            margin-right: 0px !important;
        }

        .el-pagination .btn-next, .el-pagination .btn-prev {
            background-color: rgba(64, 214, 246, 0.2) !important;
            border-radius: 3px !important;
            min-width: 20px !important;
        }
    }

    .workorderTable {
        .status-button {
            min-width: 55px;
            width: 55px;
            max-width: 55px;
            min-height: 18px;
            background-color: #48d6a9;
            border-radius: 4px;
            margin: 0 auto;

            button {
                width: 100%;
                height: 100%;
                height: 18px;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 0px !important;
                font-size: 12px;

                &.el-button--warning {
                    background-color: #cf6e39 !important;
                    border-color: #cf6e39 !important;
                }

                &.el-button--success {
                    background-color: #48d6a9 !important;
                    border-color: #48d6a9 !important;
                }

                &.el-button--primary {
                    background-color: #2e5efa !important;
                    border-color: #2e5efa !important;
                }

                span {
                    line-height: 18px;
                    font-size: 12px;
                }
            }
        }

        .el-table__row {
            padding: 0px !important;

            .is-center:nth-child(9) {
                padding: 0px !important;

                .cell {
                    height: 100%;
                    padding: 0px !important;
                }
            }

        }
    }


    .mTable {
        .el-table__row {
            padding: 0px !important;

            .is-center:nth-child(6) {
                padding: 0px !important;

                .cell {
                    height: 100%;
                    padding: 0px !important;
                }
            }

        }
    }

  
	.el-pagination1 {
		display: flex;
		justify-content: center;
		height: 40px;
		margin-top: 32px;
	}
	
	
	.el-pagination1 .el-pagination {
		display: flex;
		    align-items: center;
	}
	
	
	.el-pagination1 .el-pager li {
		background-color: transparent;
	}
	
	.el-pagination1 .el-pagination button {
		background-color: transparent;
	}
	
	.el-pagination1 .el-pager li.active  {
		color: #fff !important;
	}
	.el-pagination1 .el-pager li {
		color: #5a6384  !important;
	}
	
	.el-pagination1 .btn-prev {
		    display: flex;
		    justify-content: center;
		    padding: 0px !important;
		width: 40px;
			height: 40px;
			background-color: #1c1d32 !important;
			box-shadow: -7.1px -7.1px 10px 0px 
				rgba(34, 34, 51, 0.5), 
				7.1px 7.1px 10px 0px 
				rgba(33, 33, 49, 0.5);
			border-radius: 12px;
			color: #3a6bef !important;
			margin-right: 25px !important;
			box-shadow: -0.03rem -0.03rem 0.03rem 0rem rgba(75, 75, 83, 0.5), 0.03rem 0.03rem 0.03rem 0rem  rgba(0, 0, 0, 0.5019607843137255);
			
	}
	.el-pagination1 .btn-next {
		    display: flex;
		    justify-content: center;
		    padding: 0px !important;
		width: 40px;
		margin-left: 25px !important;
			height: 40px;
			background-color: #1c1d32 !important;
			box-shadow: -7.1px -7.1px 10px 0px 
				rgba(34, 34, 51, 0.5), 
				7.1px 7.1px 10px 0px 
				rgba(33, 33, 49, 0.5);
				box-shadow: -0.03rem -0.03rem 0.03rem 0rem rgba(75, 75, 83, 0.5), 0.03rem 0.03rem 0.03rem 0rem  rgba(0, 0, 0, 0.5019607843137255);
				
			border-radius: 12px;
			color: #3a6bef !important;
	}
	
   
	.el-table {
		background-color: transparent !important;
		border:none !important;
		margin-left: 20px;
		margin-right: 10px;
		width: calc(100% - 30px) !important;
	}
	.el-table th, .el-table tr {
		background-color: transparent !important;
		border:none !important;
	}
	.el-table th {
		color: #fff;
		position: relative;
	}
	.el-table th::after {
		content: "";
		background-image: url(./assets/images/t.png);
		background-size: cover;
		content: "";
		position: absolute;
		bottom: 0px;
		left: 0px;
		width: 100%;
		height: 8px;
	}
	.el-table--enable-row-transition .el-table__body td {
		background-color: transparent !important;
		border:none !important;
		color: #5a6384;
		position: relative;
	}
	.el-table--enable-row-transition .el-table__body td:after {
		content: "";
		background-image: url(./assets/images/t.png);
		background-size: cover;
		content: "";
		position: absolute;
		bottom: 0px;
		left: 0px;
		width: 100%;
		height: 8px;
	}
	.el-table::after {
		display: none;
	}
	.el-table::before {
		display: none;
	}
   

    .el-select {
        height: 100%;
    }

    .el-input.el-input--suffix {
        height: 100%;
    }

    .el-select .el-input.el-input--suffix input {
        height: 100%;
        background: transparent;
        border: none;
        color: #fff;
        &::placeholder{
            color: #fff;
        }
    }

    .el-select .el-input__icon {
        line-height: 0.3rem;
    }


    
   

    .el-table--scrollable-y .el-table__body-wrapper {
        &::-webkit-scrollbar {
           width: 10px;
           	
           
          
        }

        &::-webkit-scrollbar-thumb {
            -webkit-box-shadow: -2.1px -2.1px 6px 0px
				rgba(58, 107, 239, 0.5), 
				2.1px 2.1px 6px 0px 
				rgba(27, 28, 49, 0.5);
            background-color: #3a6bef;
			 	border-radius: 4px;
				margin:0 auto;

        }

        &::-webkit-scrollbar-track {
            -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
            background: #1c1d32;

        }

    }

    
</style>

<script>
    export default {
        data() {
            return {
            };
        },
        mounted() {

        },
        created() {
        },
        computed: {
        },
        methods: {
        },
    };
</script>
