module.exports = {
    // 基本路径
    publicPath:'./',
    //px转rem的配置（postcss-plugin-px2rem插件）
    lintOnSave: true,
    devServer: {
        // // 设置代理
        // proxy: {
        //   "/api": {
        //     target: "https://wish.mynatapp.cc/", // 域名
        //     changeOrigin: true, //开启代理：在本地会创建一个虚拟服务端，然后发送请求的数据，并同时接收请求的数据，这样服务端和服务端进行数据的交互就不会有跨域问题
        //     pathRewrite: {
        //       "^/api": "/"
        //     }
        //   }
        // }
    },
    css: {
        loaderOptions: {
            postcss: {
                plugins: [
                    require('postcss-plugin-px2rem')({
                        selectorBlackList: ['custom-content-marker1'],
                        // ignoreIdentifier: false,  //（boolean/string）忽略单个属性的方法，启用ignoreidentifier后，replace将自动设置为true。
                        // replace: true, // （布尔值）替换包含REM的规则，而不是添加回退。
                        mediaQuery: false,  //（布尔值）允许在媒体查询中转换px。
                        minPixelValue: 0 //设置要替换的最小像素值(3px会被转rem)。 默认 0
                    }),
                ]
            }
        }
    },


}
