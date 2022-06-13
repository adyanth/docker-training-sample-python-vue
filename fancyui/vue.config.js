const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
    publicPath: '/ui/',

    devServer: {
        proxy: {
            '^/api': {
                target: 'http://localhost:8080',
                ws: true,
                changeOrigin: true
            },
        },
    },
    transpileDependencies: [
        'vuetify'
    ]
})
